---
date: '2026-10-27T00:00:00+08:00'
title: 'Thesis Plan: Adaptive Offloading Under Uncertainty at the Edge'
description: 'A four-year thesis outline that extends the first simulation study into a trace-driven, multi-edge, testbed-validated investigation of computation offloading.'
weight: 2
status: 'THESIS PLAN / DRAFT 01'
paper_type: 'Proposal outline'
keywords: ['Edge computing', 'Computation offloading', 'IoT', 'Uncertainty', 'Testbed', 'PhD']
related: ['/research/offloading-paper/']
abstract: >-
  This plan turns a small simulation study into a PhD-sized question. The working title is
  “Adaptive Offloading Under Uncertainty at the Edge.” The central problem is not how to make a
  single device offload faster. It is how a group of devices should decide when the channel, the
  edge load, and the task mix are all changing. The plan has four phases: trace collection,
  multi-edge simulation, policy design, and testbed validation. Each phase has a concrete artifact
  and a failure condition. The first paper is a baseline; the thesis is the attempt to find out
  which parts of that baseline survive contact with real hardware.
---

## Working title

**Adaptive Offloading Under Uncertainty at the Edge: From Trace-Driven Simulation to a Multi-Device Testbed**

The title may change. The question should not.

## The problem

Edge offloading is usually framed as a per-task choice: run locally or send the task to a nearby server. That framing hides the difficult part. In a real deployment, the device does not know the next task, the channel changes, the edge server is shared, and other devices are making the same decision at the same time. A policy that is optimal for one device can be bad for the system. A policy that is optimal at low load can fail at high load. A policy that works in simulation can fail on hardware because the radio consumes more energy than the datasheet suggests.

The first working paper models this tension with synthetic tasks and a single edge server. It shows that a deadline/energy-aware heuristic can avoid the queue collapse of always-offload, but the evidence is only as good as the assumptions. The thesis asks which of those assumptions matter, and what a policy should do when they are violated.

## Research questions

**RQ1.** How do real IoT workloads and Wi-Fi transfer costs differ from the synthetic distributions used in edge-offloading simulations?

**RQ2.** How does the optimal offloading decision change when there are multiple edge servers, variable channel quality, and competing devices?

**RQ3.** Can an online policy learn the current operating point from local observations, without a central controller or a full model of the network?

**RQ4.** Under what conditions does a simulation-trained policy transfer to a real ESP32 testbed, and where does it fail?

The questions are ordered by risk. RQ1 is mostly measurement and can produce a useful dataset even if the policy part fails. RQ2 and RQ3 are simulation and algorithm work. RQ4 is the validation step, and it is the one that decides whether the thesis is about a real system or only about a model.

## Preliminary work

The first working paper, [Offload or Not?](/research/offloading-paper/), provides the baseline. It compares local-only, always-offload, and an adaptive heuristic across a load sweep. The main finding is that the best static policy depends on the operating point, and that the adaptive policy avoids the edge queue collapse at high load while giving up some of the edge's energy advantage.

That paper is useful because it is small. The simulator is a few hundred lines of Python, the data is published, and the figures can be regenerated. The thesis can use it as a reference point: every new policy has to beat the baseline, and every new assumption has to be justified by a measurement.

## Method

### Phase 1: Trace collection

Collect a small, open trace from an ESP32 and a local edge server. The workload should be fixed and repeatable: for example, a matrix operation, a small image classifier, and a compression task. For each task, record:

- CPU time and energy on the device.
- Input size and output size.
- Wi-Fi transfer time, retries, and signal strength.
- Edge execution time and queue wait.
- Device power draw during local execution, transmission, and idle.

The artifact is a dataset and a measurement note. The failure condition is a workload that is too small or too noisy to distinguish the policies. If that happens, the workload should be made heavier, not the statistics more elaborate.

### Phase 2: Multi-edge simulation

Extend the simulator from one edge server to several. Add:

- A channel model with time-varying rate and packet loss.
- Multiple devices competing for each edge server.
- A choice of which edge server to use, not only whether to offload.
- A battery model with capacity, voltage sag, and a realistic power trace.
- Task dependencies for at least one pipeline workload.

The artifact is a simulator and a sensitivity study. The question is not which policy wins in one configuration. It is which assumptions change the ranking of policies. A result that is stable across a wide range of assumptions is more interesting than a result that is optimal in one narrow setting.

### Phase 3: Policy design

Compare three families:

1. **Heuristic**: the deadline/energy rule from the first paper, with margins tuned on the trace.
2. **Model-based**: a queueing or Markov decision process model that uses the measured distributions.
3. **Learning-based**: a contextual bandit or a small reinforcement-learning policy that observes local state and learns online.

The learned policy should be evaluated on its ability to adapt, not only on its average reward. The important metrics are regret, convergence time, and behavior under distribution shift. A policy that needs a long training period is not useful for a device that runs for a day.

The artifact is a policy comparison with a clear baseline. The failure condition is a learned policy that only wins when it is trained on the test distribution. That is not a result; it is leakage.

### Phase 4: Testbed validation

Build a testbed with:

- Several ESP32 devices running the same workload.
- A local edge server on a small single-board computer.
- A Wi-Fi access point with controllable channel conditions.
- A logging pipeline that records latency, energy, and offload decisions.

Run the policies from Phase 3 on the testbed. Compare the measured ranking with the simulated ranking. The interesting result is not a perfect match. It is a systematic difference that can be explained by a measured cost the simulator ignored.

The artifact is a testbed, a reproducibility guide, and a paper. The failure condition is a testbed that is too small to support the claims. In that case, the thesis should narrow the claims rather than inflate the testbed.

## Expected contributions

- An open trace of ESP32 workload, Wi-Fi transfer, and energy measurements.
- A multi-edge simulator with channel variability and realistic device energy.
- A policy comparison that separates the value of adaptation from the value of a better model.
- Evidence about when simulation-trained policies transfer to hardware, and when they do not.
- A reproducible research record: code, data, figures, and the negative results.

The contribution is not “a new offloading algorithm.” There are many. The contribution is a careful account of which assumptions matter, with enough code and data for someone else to check.

## Scope and non-goals

**In scope:** computation offloading for small IoT devices, edge queueing, channel variability, energy measurement, and online policy adaptation.

**Out of scope:** data-center scheduling, wide-area network routing, federated learning, privacy-preserving computation, and custom silicon. These are important, but they are different theses.

The testbed will not be a production deployment. It will be a controlled instrument for testing causal claims. The simulation will not be a digital twin. It will be a place to generate hypotheses before spending weeks on hardware.

## Timeline

<div class="table-wrap">

| Period | Focus | Artifact | Checkpoint |
|---|---|---|---|
| Year 1, Q1–Q2 | Literature review and trace collection | Measurement dataset and reading notes | Can I explain the gap without overclaiming? |
| Year 1, Q3–Q4 | Multi-edge simulator | Simulator and sensitivity study | Does the baseline reproduce? |
| Year 2, Q1–Q2 | Policy design | Heuristic, model-based, and learned policies | Is the comparison fair? |
| Year 2, Q3–Q4 | First paper | Conference or workshop submission | Does an outside reader believe the result? |
| Year 3, Q1–Q2 | Testbed | ESP32 testbed and validation | Does the ranking transfer? |
| Year 3, Q3–Q4 | Second paper and thesis chapters | Draft chapters | Are the claims bounded by the evidence? |
| Year 4, Q1–Q2 | Thesis writing | Full draft | Can someone reproduce the work? |
| Year 4, Q3–Q4 | Revision and defense | Final thesis | What would I do differently? |

</div>

<p class="table-caption">Table 1. A four-year plan. The quarters are a planning device, not a promise.</p>

## Risks and mitigations

- **The trace is too small.** Mitigation: choose workloads with measurable CPU and radio cost, and publish the raw logs. A small trace with good metadata is more useful than a large trace with no context.
- **The simulator becomes the thesis.** Mitigation: set a hard date for the first testbed experiment. If the simulator is not ready by then, narrow the simulation scope.
- **The learned policy does not beat the heuristic.** Mitigation: treat that as a result. The thesis can argue that the heuristic is sufficient under the measured conditions, which is useful for practitioners.
- **The testbed does not reproduce the simulation.** Mitigation: measure the gap, identify the missing cost, and update the model. A failed transfer is evidence, not a failed project.
- **The scope grows.** Mitigation: keep the out-of-scope list visible and say no to interesting detours. A PhD is a bounded argument, not a complete map of edge computing.

## What I need to learn

- Queueing theory well enough to know when a simulation is stable and when it is only surviving because the run is short.
- Measurement methodology: power profiling, clock alignment, confidence intervals, and the difference between a repeatable experiment and a demo.
- The edge-computing literature beyond the survey level, especially papers that report negative or mixed results.
- How to write a thesis chapter that states a claim, presents the evidence, and then explains the strongest objection to the claim.

## Next action

The next concrete step is Phase 1: build the ESP32 workload harness and measure one task end to end. The first measurement note will be published here, including the parts that do not work. The simulation can wait until there is a real number to put into it.
