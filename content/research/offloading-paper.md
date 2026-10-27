---
date: '2026-10-27T00:00:00+08:00'
title: 'Offload or Not? A Simulation Study of Latency- and Energy-Aware Computation Offloading for IoT Devices'
description: 'A working paper on when battery-powered IoT devices should compute locally or send work to a shared edge server. Includes a reproducible Python simulator, a load sweep, and the limits of the model.'
weight: 1
status: 'WORKING PAPER / DRAFT 01'
paper_type: 'Simulation study'
keywords: ['Edge computing', 'Computation offloading', 'IoT', 'Latency', 'Energy', 'Simulation']
related: ['/research/thesis-plan/']
abstract: >-
  Edge computing promises lower latency and lower device energy by moving computation away from
  battery-powered devices. That promise is conditional. A shared edge server has finite capacity,
  wireless transmission is not free, and a policy that is optimal at low load can collapse when
  many devices decide to offload at once. This paper compares three policies in a reproducible
  simulation: local-only execution, always-offload, and a deadline/energy-aware heuristic that
  decides per task. The model uses 20 devices, Poisson task arrivals, lognormal workloads, a
  shared FIFO edge queue, and a 750 ms deadline. Across a sweep from 0.1 to 1.0 tasks per device
  per second, the adaptive policy matches always-offload at low load and avoids the edge queue
  collapse that appears at higher load. At 0.8 tasks per device per second, adaptive execution
  misses 10.3% of deadlines, compared with 45.1% for local-only and 99.7% for always-offload.
  It also uses 62.5% less energy per task than local-only. The result is a baseline, not a
  deployment claim: the workload and channel are synthetic, and the next step is a trace-driven
  model calibrated with real ESP32 and Wi-Fi measurements.
---

## 1. Introduction

A small device with a battery, a radio, and a processor has three ways to handle a compute-heavy task. It can run the task locally, send it to a nearby edge server, or defer it. Local execution avoids the radio but spends time and energy on the device. Offloading can finish sooner and drain less battery, but it adds transmission time, a shared queue, and a dependency on the network.

The interesting question is not whether an edge server is faster than a microcontroller. It usually is. The interesting question is when offloading stops helping. A single device sees a fast server. A thousand devices see a queue. The same decision that is rational for one device can be irrational for the system.

This paper studies that tension with a deliberately small model. The model has one shared edge server, many devices, and tasks that arrive as a Poisson process. Each task has a computational workload and an input size. The simulator compares three policies:

1. **Local-only**: every task runs on the device.
2. **Always-offload**: every task is sent to the edge server.
3. **Adaptive**: a task is offloaded only when the estimated edge latency is below a safety margin of the deadline and the move is justified by either latency or energy.

The research question is: *under a synthetic but plausible workload, when does a deadline/energy-aware offloading policy outperform static local-only and always-offload policies on deadline misses, mean latency, and energy per task?*

The contribution is not a new algorithm. It is a transparent baseline: a simulator small enough to inspect, a sweep that shows where each policy breaks, and a public record of the assumptions. The paper is a training exercise for PhD-level work, and it is written so that the next version can replace the synthetic assumptions with measurements.

## 2. Background and Related Work

Mobile edge computing (MEC) places compute and storage at the edge of the network, close to the devices that generate data. Surveys by Mao et al. [1], Satyanarayanan [2], and Mach and Becvar [3] describe the architecture, the motivating applications, and the main research problems. The common claim is that edge execution can reduce end-to-end latency and extend battery life. The common caveat is that the benefit depends on the channel, the workload, and the load on the edge.

Computation offloading has been studied from several angles. Some work formulates the decision as an optimization problem and solves it with convex optimization or Lyapunov control [4]. Some work models the interaction between users as a game and looks for an equilibrium [5]. More recent work uses reinforcement learning to learn a policy when the workload or channel is unknown. The shared theme is that the decision is a trade-off: local execution spends device energy, while offloading spends transmission energy and adds queueing delay.

The model in this paper is closer to the early measurement-driven and queueing studies than to a new learning method. Zhang et al. [6] show that the energy-optimal offloading decision depends on the stochastic wireless channel. Chen et al. [7] study multi-user offloading and show that the interaction between users matters. Those results motivate the central design choice here: the edge server is shared, and the policy sees the current queue estimate.

This study does not claim to advance that literature. It is a reproducible baseline and a writing exercise. The value is in the comparison: a static policy can look good at one operating point and fail at another, and the failure is visible when the load sweep is plotted rather than hidden behind a single average.

## 3. System Model

### 3.1 Tasks and arrivals

There are \(N = 20\) devices. Tasks arrive at each device as a Poisson process with rate \(\lambda\) tasks per second. Each task \(i\) has a computational workload \(C_i\) measured in gigacycles and an input size \(D_i\) measured in megabits. The workload and input size are drawn independently from lognormal distributions, clipped to a plausible range. The lognormal shape is intentional: it produces a small number of heavy tasks that stress the deadline, which is closer to real workloads than a uniform distribution.

A task has a relative deadline \(D = 750\) ms. A task misses its deadline if its end-to-end completion time is greater than \(D\). The simulator records the completion time for every task, including tasks that finish after the nominal simulation window.

### 3.2 Local execution

The device CPU runs at \(f_\ell = 1.2\) GHz. The local execution time is:

\[
t_i^{\text{loc}} = \frac{C_i}{f_\ell}.
\]

The local energy is modeled with a constant active power \(P_\ell = 1.2\) W:

\[
e_i^{\text{loc}} = P_\ell \, t_i^{\text{loc}}.
\]

Each device has its own FIFO local queue. A task that chooses local execution waits for the previous local task on that device, then runs. This matters because a policy that keeps too much work local can create a local queue even when the edge is idle.

### 3.3 Edge execution

The shared edge server runs at \(f_e = 8\) GHz. The uplink rate is \(R = 8\) Mbps. The transmission time for task \(i\) is:

\[
t_i^{\text{tx}} = \frac{D_i}{R}.
\]

The edge server serves tasks in arrival order. If the server is busy until time \(F_e\), the completion time is:

\[
t_i^{\text{edge}} = \max\left(t_i + t_i^{\text{tx}}, F_e\right) + \frac{C_i}{f_e}.
\]

The model ignores downlink time because the result payload is assumed to be small. It also assumes a perfect channel at a fixed rate. Both assumptions are optimistic; Section 7 discusses what they hide.

The device energy for offloading is:

\[
e_i^{\text{off}} = E_0 + P_{\text{tx}} \, t_i^{\text{tx}},
\]

where \(E_0 = 0.05\) J is a fixed radio wake-up cost and \(P_{\text{tx}} = 0.8\) W is the transmit power. The fixed cost is important: for very small tasks, the radio overhead can make local execution cheaper even when the edge is faster.

### 3.4 Metrics

The simulator reports four metrics:

- **Deadline miss rate**: the fraction of tasks with completion time greater than \(D\).
- **Mean end-to-end latency**: the mean completion time from arrival to finish.
- **Energy per task**: the mean device energy consumed per task, in millijoules.
- **Offload fraction**: the fraction of tasks sent to the edge.

The first three are the outcome metrics. The offload fraction explains the policy's behavior.

## 4. Policies

### 4.1 Local-only

Every task runs on its device. The policy has no coordination, no radio cost, and no dependence on the edge. It is the safest baseline when the network is unavailable, but it pays for every cycle on the device.

### 4.2 Always-offload

Every task is sent to the edge. This policy minimizes local computation and, in this model, usually minimizes device energy. It is also the most fragile: all devices share one queue, and the queue is stable only while the offered load stays below the server capacity.

### 4.3 Adaptive

The adaptive policy estimates both options at the moment the task arrives. It uses the current local queue and the current edge queue, not future knowledge. The decision rule is:

\[
\text{offload}_i =
\left(t_i^{\text{edge}} \le 0.85D\right)
\land
\left[
\left(t_i^{\text{loc}} > 0.90D\right)
\lor
\left(e_i^{\text{loc}} > e_i^{\text{off}}\right)
\right].
\]

The first condition keeps a 15% safety margin below the deadline. The second condition says: offload if local execution is close to missing the deadline, or if offloading is cheaper in energy. If the edge is already congested, the first condition fails and the task stays local even when the edge would eventually finish it faster.

The margins are heuristic. A tighter margin protects the edge but sends more work to the local queues. A looser margin uses the edge more aggressively but risks a queue build-up. The sensitivity of the result to that choice is a natural next experiment.

## 5. Simulation Method

The simulator is a discrete-event model written in Python with NumPy. For each replication, it generates a task trace for all devices, sorts the tasks by arrival time, and processes them in order. Each device has a local free-time variable; the edge has a shared free-time variable. Transmission time is charged before a task enters the edge queue.

The same trace is replayed for all three policies. This paired design reduces variance: the difference between policies comes from the decisions, not from different random workloads. The reported values are means over 20 replications, with 95% confidence intervals computed from the replication-level means.

The default sweep uses \(\lambda \in \{0.1, 0.2, \ldots, 1.0\}\) tasks per device per second. Each replication simulates 600 seconds of arrivals. The main parameters are listed in Table 1.

<div class="table-wrap">

| Parameter | Value |
|---|---:|
| Devices | 20 |
| Simulation window | 600 s |
| Task deadline | 750 ms |
| Local CPU | 1.2 GHz |
| Edge CPU | 8 GHz |
| Uplink rate | 8 Mbps |
| Local active power | 1.2 W |
| Transmit power | 0.8 W |
| Radio wake-up cost | 0.05 J |
| Workload distribution | Lognormal, mean 0.6 Gcycles, \(\sigma = 0.50\) |
| Input distribution | Lognormal, mean 0.35 Mbits, \(\sigma = 0.45\) |
| Replications per point | 20 |

</div>

<p class="table-caption">Table 1. Default simulation parameters. The workload and channel values are illustrative, not measured.</p>

The simulator and the published data are reproducible with:

```sh
uv run --with numpy --with matplotlib python scripts/research/offloading_sim.py --reps 20
```

The script writes the sweep to `static/data/research/offloading_sweep.csv` and regenerates the three figures in `static/images/research/`. The random seed is fixed by default.

## 6. Results

### 6.1 Deadline misses

Figure 1 shows the deadline miss rate as the arrival rate increases. Local-only starts at 23.2% misses at 0.1 tasks per device per second and rises to 53.5% at 1.0. The high starting point is not a queueing failure; it is the heavy tail of the workload distribution. Even with an idle local CPU, some tasks exceed the 750 ms deadline because their workload is large.

Always-offload is the best policy at low load. It reaches 0% misses at 0.1 and 0.2 tasks per device per second, and 0.1% at 0.3. The edge queue is stable. Then the queue crosses its stability region. At 0.5 tasks per device per second the miss rate is already 14.9%; at 0.6 it is 95.2%; at 0.8 it is 99.7%. The average latency in Figure 2 rises from 438 ms at 0.5 to 105.8 seconds at 0.8. The policy is not slow because the server is slow. It is slow because every device is waiting behind every other device.

The adaptive policy tracks always-offload until the edge starts to saturate. At 0.5 tasks per device per second it misses 1.6% of deadlines, compared with 14.9% for always-offload. At 0.6 it misses 3.8%, compared with 37.7% for local-only and 95.2% for always-offload. At 0.8 it misses 10.3%, compared with 45.1% and 99.7%. The adaptive policy does not eliminate misses at high load. It keeps the system from collapsing.

<figure>
  <img src="/images/research/fig1-deadline-miss.png" alt="Line chart of deadline miss rate against task arrival rate for local-only, always-offload, and adaptive policies.">
  <figcaption>Figure 1. Deadline miss rate versus arrival rate. Always-offload is best at low load and collapses once the shared edge queue saturates. Adaptive tracks the edge at low load and degrades gradually at high load.</figcaption>
</figure>

<div class="table-wrap results-table">

| Arrival rate | Policy | Deadline misses | Mean latency | Energy per task | Offload fraction |
|---:|---|---:|---:|---:|---:|
| 0.2 | Local-only | 26.0% | 613 ms | 679.6 mJ | 0% |
| 0.2 | Always-offload | 0.0% | 164 ms | 88.9 mJ | 100% |
| 0.2 | Adaptive | 0.0% | 164 ms | 89.2 mJ | 100% |
| 0.5 | Local-only | 34.5% | 707 ms | 679.3 mJ | 0% |
| 0.5 | Always-offload | 14.9% | 438 ms | 88.8 mJ | 100% |
| 0.5 | Adaptive | 1.6% | 311 ms | 115.7 mJ | 97.2% |
| 0.8 | Local-only | 45.1% | 858 ms | 678.0 mJ | 0% |
| 0.8 | Always-offload | 99.7% | 105,771 ms | 88.7 mJ | 100% |
| 0.8 | Adaptive | 10.3% | 560 ms | 254.3 mJ | 80.9% |
| 1.0 | Local-only | 53.5% | 1,031 ms | 677.6 mJ | 0% |
| 1.0 | Always-offload | 99.8% | 206,809 ms | 88.8 mJ | 100% |
| 1.0 | Adaptive | 16.5% | 655 ms | 339.0 mJ | 69.7% |

</div>

<p class="table-caption">Table 2. Selected results from the 27-point sweep. Values are means over 20 replications. The full table is in <a href="/data/research/offloading_sweep.csv">the published CSV</a>.</p>

### 6.2 Latency

Figure 2 uses a logarithmic scale because the always-offload latency spans five orders of magnitude. The shape is the important part. Local-only latency grows slowly with load because each device has its own queue. Always-offload latency is almost flat until the edge saturates, then grows without bound. Adaptive latency sits between them: it is lower than local-only at every load and far below always-offload once the edge is congested.

The adaptive policy is not the lowest-latency policy at low load. It is effectively the same as always-offload there, because the edge is fast and the policy offloads almost every task. The difference appears at high load, where the adaptive policy refuses work that would miss the deadline. That refusal is the whole point. The edge server is a shared resource, and the policy treats it that way.

<figure>
  <img src="/images/research/fig2-latency.png" alt="Line chart of mean end-to-end latency on a logarithmic scale against task arrival rate for three offloading policies.">
  <figcaption>Figure 2. Mean end-to-end latency versus arrival rate, log scale. Always-offload collapses once the shared queue is unstable. Adaptive keeps latency bounded by moving work back to the devices.</figcaption>
</figure>

### 6.3 Energy

Figure 3 shows the energy trade-off. Local-only uses about 678 mJ per task across the whole sweep because the energy depends on the workload, not on the arrival rate. Always-offload uses about 88.7 mJ per task because the radio and the edge CPU are more efficient than the local CPU for this workload. Adaptive starts at the same 89 mJ at low load and rises to 254 mJ at 0.8 and 339 mJ at 1.0 as it sends more work back to the devices.

That increase is not a bug. It is the cost of protecting the deadline. At 0.8 tasks per device per second, adaptive uses 62.5% less energy per task than local-only while missing 77.2% fewer deadlines than local-only. It uses 2.9 times more energy than always-offload, but always-offload misses 99.7% of deadlines at that load. A policy that saves energy by missing every deadline is not a useful policy.

<figure>
  <img src="/images/research/fig3-energy.png" alt="Line chart of energy per task against task arrival rate for local-only, always-offload, and adaptive policies.">
  <figcaption>Figure 3. Energy per task versus arrival rate. Adaptive gives up some of the edge's energy advantage as it moves work back to the devices to protect the deadline.</figcaption>
</figure>

### 6.4 Interpretation

The results support a simple claim: the best static policy depends on the operating point, and the operating point is not known in advance. Local-only is robust to network failures but wastes device energy and misses deadlines even at low load. Always-offload is excellent at low load and unacceptable at high load. The adaptive policy is a compromise, and the compromise is visible in the energy curve.

The result also shows why a single average is not enough. If the evaluation only used 0.2 tasks per device per second, always-offload would look dominant. If it only used 0.8, always-offload would look broken. A load sweep makes the transition visible, and the transition is the interesting part.

## 7. Threats to Validity

The model is intentionally small, and the threats are correspondingly large.

- **Synthetic workload.** The lognormal workload and input distributions are plausible but not measured. A real ESP32 workload may be more bursty, more correlated, or much smaller. The conclusion could change.
- **Synthetic channel.** The uplink is a fixed 8 Mbps with no fading, retries, contention, or handover. A real Wi-Fi link can vary by an order of magnitude within a few seconds.
- **No downlink.** The model assumes the result payload is negligible. That is reasonable for some inference tasks and wrong for others.
- **No failures.** The edge server does not fail, restart, or lose a task. The network does not drop a packet. The device does not run out of battery.
- **Single edge server.** The model has one shared queue. A multi-edge deployment would change the decision space and the failure modes.
- **No task dependencies.** Every task is independent. Real applications often have pipelines, which makes the offloading decision a graph problem rather than a per-task choice.
- **Heuristic policy.** The adaptive rule is not optimal. It is a transparent baseline with two margins. A learned or optimization-based policy could do better, especially if it can predict arrivals.
- **Baseline choice.** Local-only uses FIFO scheduling, not a deadline-aware scheduler. The comparison is between offloading policies, not between the best possible local scheduler and the best possible edge scheduler.
- **No security or privacy model.** Offloading sends data to another machine. The model ignores confidentiality, authentication, and trust.

These limitations do not invalidate the comparison. They define its scope. The result is a statement about this model, not a claim about every edge deployment.

## 8. Conclusion and Next Steps

This paper asked when an IoT device should offload computation to a shared edge server. In the model, the answer depends on load. Always-offload is best while the edge queue is stable and collapses when it is not. Local-only is stable but expensive and misses deadlines even at low load. A deadline/energy-aware heuristic tracks the edge at low load and avoids the collapse at high load, at the cost of higher device energy.

The next step is to make the model less synthetic. I want to collect a trace from an ESP32 running a fixed workload, measure the Wi-Fi transfer time and energy for that workload, and replace the lognormal assumptions with the measured distribution. If the adaptive policy still helps with the measured trace, the result is stronger. If it does not, that is also useful: it would show which assumption was doing the work.

The longer thesis direction extends the same question to multiple edge servers, variable channels, and a real testbed. The simulation is not the thesis. It is the instrument for choosing which policies are worth testing on hardware.

## References

1. Y. Mao, C. You, J. Zhang, K. Huang, and K. B. Letaief, “A Survey on Mobile Edge Computing: The Communication Perspective,” *IEEE Communications Surveys & Tutorials*, vol. 19, no. 4, pp. 2322–2358, 2017.
2. M. Satyanarayanan, “The Emergence of Edge Computing,” *Computer*, vol. 50, no. 1, pp. 30–39, 2017.
3. P. Mach and Z. Becvar, “Mobile Edge Computing: A Survey on Architecture and Computation Offloading,” *IEEE Communications Surveys & Tutorials*, vol. 19, no. 3, pp. 1628–1656, 2017.
4. Y. Mao, J. Zhang, and K. B. Letaief, “Dynamic Computation Offloading for Mobile-Edge Computing with Energy Harvesting Devices,” *IEEE Journal on Selected Areas in Communications*, vol. 34, no. 12, pp. 3590–3605, 2016.
5. X. Chen, L. Jiao, W. Li, and X. Fu, “Efficient Multi-User Computation Offloading for Mobile-Edge Cloud Computing,” *IEEE/ACM Transactions on Networking*, vol. 24, no. 5, pp. 2795–2808, 2016.
6. W. Zhang, Y. Wen, K. Guan, D. Kilper, H. Luo, and D. O. Wu, “Energy-Optimal Mobile Cloud Computing under Stochastic Wireless Channel,” *IEEE Transactions on Wireless Communications*, vol. 12, no. 9, pp. 4569–4581, 2013.
7. S. Wang, X. Zhang, Y. Zhang, L. Wang, J. Yang, and W. Wang, “A Survey on Mobile Edge Networks: Convergence of Computing, Caching and Communications,” *IEEE Access*, vol. 5, pp. 6757–6779, 2017.

## Appendix: Reproducibility

The simulator is at `scripts/research/offloading_sim.py`. The published sweep is at `static/data/research/offloading_sweep.csv`, and the full summary, including confidence intervals, is at `static/data/research/offloading_summary.json`. The figures are generated by the same script.

The default command is:

```sh
uv run --with numpy --with matplotlib python scripts/research/offloading_sim.py --reps 20
```

The default seed is `20261027`. The script uses 20 replications per arrival rate and 600 simulated seconds per replication. The results in this draft were produced with those defaults.

<p class="paper-note">Status: working paper, draft 01. Not peer reviewed. The code and data are public so the result can be checked, extended, or disproved.</p>
