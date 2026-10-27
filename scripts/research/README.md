# Research training scripts

This directory holds the code behind the public research notebook at
`/research/`. The first study compares local execution, always-offload, and a
deadline/energy-aware offloading heuristic for edge-assisted IoT devices.

## Reproduce the working paper

```sh
uv run --with numpy --with matplotlib python scripts/research/offloading_sim.py --reps 20
```

The default run writes:

- `static/data/research/offloading_sweep.csv`
- `static/data/research/offloading_summary.json`
- `static/images/research/fig1-deadline-miss.png`
- `static/images/research/fig2-latency.png`
- `static/images/research/fig3-energy.png`

Use `--quick` for a short smoke test, or `--reps` to change the number of
Monte Carlo replications. The seed is fixed by default so the published figures
can be regenerated.

## Model notes

- 20 devices, Poisson arrivals, 600 simulated seconds per replication.
- Task workload is lognormal in Gcycles; input size is lognormal in Mbits.
- Local execution uses a 1.2 GHz CPU and 1.2 W active power.
- The shared edge server uses an 8 GHz CPU and a FIFO queue.
- Uplink is 8 Mbps with 0.8 W transmit power and a 0.05 J radio wake-up cost.
- Deadline is 750 ms. The adaptive policy keeps a 15% safety margin below the
  deadline and only offloads for latency when local execution is close to
  missing.

The numbers are illustrative. This is a training model, not a measurement of a
specific deployment.
