#!/usr/bin/env python3
"""Reproducible simulation for the edge-offloading research note.

The model is intentionally small: devices generate compute-heavy tasks, each
task can run locally or be sent to a shared edge server. The simulator compares
three policies: local-only, always-offload, and a deadline/energy-aware
heuristic. It is a training model, not a production digital twin.

Run:
    uv run --with numpy --with matplotlib python scripts/research/offloading_sim.py
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Config:
    n_devices: int = 20
    sim_time_s: float = 600.0
    deadline_s: float = 0.75

    local_cpu_ghz: float = 1.2
    edge_cpu_ghz: float = 8.0
    uplink_mbps: float = 8.0

    local_power_w: float = 1.2
    tx_power_w: float = 0.8
    radio_overhead_j: float = 0.05

    # Adaptive policy margins: keep the edge below its deadline, and only
    # offload for latency when local execution is close to missing.
    edge_deadline_margin: float = 0.85
    local_deadline_margin: float = 0.90

    workload_mean_gcycles: float = 0.6
    workload_sigma: float = 0.50
    workload_min_gcycles: float = 0.10
    workload_max_gcycles: float = 2.5

    data_mean_mbits: float = 0.35
    data_sigma: float = 0.45
    data_min_mbits: float = 0.03
    data_max_mbits: float = 2.0

    seed: int = 20261027


@dataclass(frozen=True)
class Task:
    device: int
    arrival_s: float
    workload_gcycles: float
    data_mbits: float


POLICIES = ("local", "edge", "adaptive")
POLICY_LABELS = {
    "local": "Local only",
    "edge": "Always offload",
    "adaptive": "Adaptive",
}
POLICY_COLORS = {
    "local": "#8a8a8a",
    "edge": "#eaeaea",
    "adaptive": "#ff2a2a",
}


# ---------------------------------------------------------------------------
# Workload and simulator
# ---------------------------------------------------------------------------


def generate_tasks(cfg: Config, arrival_rate: float, rng: np.random.Generator) -> list[Task]:
    """Generate a Poisson task stream for every device."""
    tasks: list[Task] = []
    for device in range(cfg.n_devices):
        t = 0.0
        while True:
            t += float(rng.exponential(1.0 / arrival_rate))
            if t >= cfg.sim_time_s:
                break

            workload = float(
                np.clip(
                    rng.lognormal(math.log(cfg.workload_mean_gcycles), cfg.workload_sigma),
                    cfg.workload_min_gcycles,
                    cfg.workload_max_gcycles,
                )
            )
            data = float(
                np.clip(
                    rng.lognormal(math.log(cfg.data_mean_mbits), cfg.data_sigma),
                    cfg.data_min_mbits,
                    cfg.data_max_mbits,
                )
            )
            tasks.append(Task(device, t, workload, data))

    tasks.sort(key=lambda task: task.arrival_s)
    return tasks


def simulate(tasks: list[Task], policy: str, cfg: Config) -> dict[str, float]:
    """Run one policy over a task trace.

    Tasks are served in arrival order. Local queues are per device; the edge
    server has one shared FIFO queue. Transmission time is charged before the
    edge task enters the queue.
    """
    local_free = np.zeros(cfg.n_devices, dtype=float)
    radio_free = np.zeros(cfg.n_devices, dtype=float)
    edge_free = 0.0

    latencies = []
    energies = []
    offloaded = 0

    for task in tasks:
        local_start = max(task.arrival_s, local_free[task.device])
        local_finish = local_start + task.workload_gcycles / cfg.local_cpu_ghz
        local_latency = local_finish - task.arrival_s
        local_energy = cfg.local_power_w * (task.workload_gcycles / cfg.local_cpu_ghz)

        tx_start = max(task.arrival_s, radio_free[task.device])
        tx_finish = tx_start + task.data_mbits / cfg.uplink_mbps
        edge_start = max(tx_finish, edge_free)
        edge_finish = edge_start + task.workload_gcycles / cfg.edge_cpu_ghz
        edge_latency = edge_finish - task.arrival_s
        edge_energy = cfg.radio_overhead_j + cfg.tx_power_w * (task.data_mbits / cfg.uplink_mbps)

        if policy == "local":
            use_edge = False
        elif policy == "edge":
            use_edge = True
        elif policy == "adaptive":
            # Offload only when the edge can meet the deadline and the move is
            # either necessary for latency or better for energy.
            use_edge = (edge_latency <= cfg.deadline_s * cfg.edge_deadline_margin) and (
                (local_latency > cfg.deadline_s * cfg.local_deadline_margin)
                or (local_energy > edge_energy)
            )
        else:
            raise ValueError(f"unknown policy: {policy}")

        if use_edge:
            local_latency = edge_latency
            local_energy = edge_energy
            radio_free[task.device] = tx_finish
            edge_free = edge_finish
            offloaded += 1
        else:
            local_free[task.device] = local_finish

        latencies.append(local_latency)
        energies.append(local_energy)

    latencies_arr = np.asarray(latencies, dtype=float)
    energies_arr = np.asarray(energies, dtype=float)
    missed = latencies_arr > cfg.deadline_s

    return {
        "n_tasks": float(len(tasks)),
        "mean_latency_ms": float(np.mean(latencies_arr) * 1000.0),
        "p95_latency_ms": float(np.percentile(latencies_arr, 95) * 1000.0),
        "deadline_miss_rate": float(np.mean(missed)),
        "mean_energy_mj": float(np.mean(energies_arr) * 1000.0),
        "total_energy_j": float(np.sum(energies_arr)),
        "offload_fraction": float(offloaded / len(tasks)) if tasks else 0.0,
    }


# ---------------------------------------------------------------------------
# Sweep and output
# ---------------------------------------------------------------------------


def mean_ci(values: list[float]) -> tuple[float, float]:
    arr = np.asarray(values, dtype=float)
    if arr.size <= 1:
        return float(arr.mean()), 0.0
    return float(arr.mean()), float(1.96 * arr.std(ddof=1) / math.sqrt(arr.size))


def run_sweep(
    cfg: Config,
    arrivals: list[float],
    reps: int,
    out_dir: Path,
    plot_dir: Path,
) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    plot_dir.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, float | str]] = []
    raw: dict[str, dict[str, dict[str, list[float]]]] = {}

    for arrival_rate in arrivals:
        for policy in POLICIES:
            raw.setdefault(str(arrival_rate), {}).setdefault(policy, {})
            for key in (
                "mean_latency_ms",
                "p95_latency_ms",
                "deadline_miss_rate",
                "mean_energy_mj",
                "total_energy_j",
                "offload_fraction",
            ):
                raw[str(arrival_rate)][policy].setdefault(key, [])

        for rep in range(reps):
            rep_seed = cfg.seed + int(arrival_rate * 1000) + rep * 97
            rng = np.random.default_rng(rep_seed)
            tasks = generate_tasks(cfg, arrival_rate, rng)
            for policy in POLICIES:
                metrics = simulate(tasks, policy, cfg)
                for key in (
                    "mean_latency_ms",
                    "p95_latency_ms",
                    "deadline_miss_rate",
                    "mean_energy_mj",
                    "total_energy_j",
                    "offload_fraction",
                ):
                    raw[str(arrival_rate)][policy][key].append(metrics[key])

    for arrival_rate in arrivals:
        for policy in POLICIES:
            values = raw[str(arrival_rate)][policy]
            row: dict[str, float | str] = {"arrival_rate": arrival_rate, "policy": policy}
            for key in (
                "mean_latency_ms",
                "p95_latency_ms",
                "deadline_miss_rate",
                "mean_energy_mj",
                "total_energy_j",
                "offload_fraction",
            ):
                mean, ci = mean_ci(values[key])
                row[key] = mean
                row[f"{key}_ci"] = ci
            rows.append(row)

    csv_path = out_dir / "offloading_sweep.csv"
    with csv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "config": asdict(cfg),
        "arrival_rates": arrivals,
        "replications": reps,
        "rows": rows,
    }
    (out_dir / "offloading_summary.json").write_text(json.dumps(summary, indent=2))

    make_plots(rows, plot_dir)
    return summary


def _style_axis(ax: plt.Axes) -> None:
    ax.set_facecolor("#0f0f0f")
    ax.tick_params(colors="#b8b8b8", labelsize=8)
    ax.xaxis.label.set_color("#b8b8b8")
    ax.yaxis.label.set_color("#b8b8b8")
    ax.title.set_color("#eaeaea")
    for spine in ax.spines.values():
        spine.set_color("#333333")
    ax.grid(True, color="#262626", linewidth=0.7, alpha=0.9)
    ax.set_axisbelow(True)


def _plot_metric(
    rows: list[dict[str, float | str]],
    metric: str,
    ylabel: str,
    out_path: Path,
    percent: bool = False,
    log_y: bool = False,
) -> None:
    fig, ax = plt.subplots(figsize=(7.2, 4.1), dpi=200)
    fig.patch.set_facecolor("#0f0f0f")
    _style_axis(ax)

    for policy in POLICIES:
        selected = [row for row in rows if row["policy"] == policy]
        x = [float(row["arrival_rate"]) for row in selected]
        y = [float(row[metric]) for row in selected]
        yerr = [float(row.get(f"{metric}_ci", 0.0)) for row in selected]
        if percent:
            y = [value * 100.0 for value in y]
            yerr = [value * 100.0 for value in yerr]
        ax.errorbar(
            x,
            y,
            yerr=yerr,
            label=POLICY_LABELS[policy],
            color=POLICY_COLORS[policy],
            marker="o",
            markersize=4.5,
            linewidth=1.8,
            capsize=2.5,
            ecolor=POLICY_COLORS[policy],
            alpha=0.95,
        )

    if log_y:
        ax.set_yscale("log")
        ax.set_ylim(50, 300_000)
    ax.set_xlabel("Task arrival rate per device (tasks/s)")
    ax.set_ylabel(ylabel)
    ax.legend(frameon=False, labelcolor="#d8d8d8", fontsize=8, loc="best")
    fig.tight_layout()
    fig.savefig(out_path, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close(fig)


def make_plots(rows: list[dict[str, float | str]], plot_dir: Path) -> None:
    _plot_metric(
        rows,
        "deadline_miss_rate",
        "Deadline miss rate (%)",
        plot_dir / "fig1-deadline-miss.png",
        percent=True,
    )
    _plot_metric(
        rows,
        "mean_latency_ms",
        "Mean end-to-end latency (ms, log scale)",
        plot_dir / "fig2-latency.png",
        log_y=True,
    )
    _plot_metric(
        rows,
        "mean_energy_mj",
        "Energy per task (mJ)",
        plot_dir / "fig3-energy.png",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reps", type=int, default=20)
    parser.add_argument("--quick", action="store_true", help="small sweep for a smoke test")
    parser.add_argument("--seed", type=int, default=20261027)
    parser.add_argument("--out", type=Path, default=Path("static/data/research"))
    parser.add_argument("--plots", type=Path, default=Path("static/images/research"))
    args = parser.parse_args()

    cfg = Config(seed=args.seed)
    arrivals = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0]
    reps = args.reps
    if args.quick:
        arrivals = [0.2, 0.8, 1.5]
        reps = min(reps, 3)

    summary = run_sweep(cfg, arrivals, reps, args.out, args.plots)

    print("Simulation complete.")
    print(f"Rows: {len(summary['rows'])}")
    for row in summary["rows"]:
        print(
            f"lambda={row['arrival_rate']:.1f} {row['policy']:>8} "
            f"miss={row['deadline_miss_rate']*100:5.1f}% "
            f"latency={row['mean_latency_ms']:7.1f}ms "
            f"energy={row['mean_energy_mj']:7.2f}mJ "
            f"offload={row['offload_fraction']*100:5.1f}%"
        )


if __name__ == "__main__":
    main()
