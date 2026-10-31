---
date: '2026-10-27T00:00:00+08:00'
title: 'Research Training'
description: 'A public research notebook: one topic at a time, reproducible simulations, journal-style drafts, and a thesis plan.'
---

I am using this section to practise the parts of research that a job does not usually teach: framing a question, building a model small enough to understand, reading the literature without pretending I have read everything, and writing a paper that states its own limits.

The rule is one topic at a time. Right now that topic is computation offloading at the edge.

<div class="research-current">
  <div>
    <p class="telemetry">/// CURRENT PROJECT / WORKING PAPER 01</p>
    <h2>Offload or Not?</h2>
    <p class="research-lede">A simulation study of latency- and energy-aware computation offloading for IoT devices. The question is not whether the edge is faster. It is when moving work to the edge stops helping and starts building a queue.</p>
    <p>The model compares three policies: run everything locally, send everything to a shared edge server, and a deadline/energy-aware heuristic that decides per task. The simulator, the data, and the figures are in the repository.</p>
    <div class="tech-tags"><span>Python</span> <span>NumPy</span> <span>Matplotlib</span> <span>Monte Carlo</span> <span>Queueing</span> <span>Edge computing</span></div>
    <div class="paper-links">
      <a href="/research/offloading-paper/">Read the working paper &gt;&gt;&gt;</a>
      <a href="/research/thesis-plan/">Thesis plan &gt;&gt;&gt;</a>
      <a href="/data/research/offloading_sweep.csv">Download the data</a>
    </div>
  </div>
  <div class="research-stats">
    <div><strong>27</strong><span>simulation points</span></div>
    <div><strong>20</strong><span>replications each</span></div>
    <div><strong>3</strong><span>policies compared</span></div>
    <div><strong>0.75 s</strong><span>task deadline</span></div>
  </div>
</div>

## Why this exists

I am preparing for a PhD after my degree. A PhD is not a longer version of a software project. It is a habit of asking a question that can survive being wrong, building evidence that someone else can reproduce, and writing down what the evidence does not show.

This notebook is where I practise that habit in public. The work here is early. It is not peer reviewed, and it is not a claim of novelty. It is a record of the method I am learning: choose a narrow question, build a transparent model, run the experiment, report the result, then attack the result before someone else does.

## The rules

- **One topic at a time.** The current question gets the attention. Old notes stay online so the mistakes remain visible.
- **Code has to run.** Every figure comes from a script in `scripts/research/`. The seed is fixed. The data is published.
- **No invented citations.** If a reference is listed, it should be a real paper I have opened. The reading list will grow slowly.
- **State the limitation before the conclusion.** A simulation is an argument about assumptions, not a measurement of the world.
- **Write for a reader who is not me.** The paper should explain the model without requiring the reader to run the code first.

## Writing log

<div class="timeline">
  <article class="timeline-item">
    <div class="timeline-date">2026-10-27</div>
    <div class="timeline-body">
      <h3>Draft 01: edge offloading paper and thesis plan</h3>
      <ul>
        <li>Built the first Python simulator: 20 devices, shared edge queue, three offloading policies.</li>
        <li>Ran a 27-point sweep with 20 replications per point and generated three figures.</li>
        <li>Wrote the first journal-style draft and a four-year thesis outline for the same topic.</li>
        <li>Next: replace the synthetic workload with a trace from a real ESP32 and a local edge server.</li>
      </ul>
    </div>
  </article>
</div>

## Reading list

These are the papers I am using to orient the topic, not a complete survey.

- Mao et al., “A Survey on Mobile Edge Computing: The Communication Perspective,” *IEEE Communications Surveys & Tutorials*, 2017.
- Satyanarayanan, “The Emergence of Edge Computing,” *Computer*, 2017.
- Mach and Becvar, “Mobile Edge Computing: A Survey on Architecture and Computation Offloading,” *IEEE Communications Surveys & Tutorials*, 2017.
- Mao, Zhang, and Letaief, “Dynamic Computation Offloading for Mobile-Edge Computing with Energy Harvesting Devices,” *IEEE JSAC*, 2016.
- Chen et al., “Efficient Multi-User Computation Offloading for Mobile-Edge Cloud Computing,” *IEEE/ACM Transactions on Networking*, 2016.
- Zhang et al., “Energy-Optimal Mobile Cloud Computing under Stochastic Wireless Channel,” *IEEE Transactions on Wireless Communications*, 2013.

## What comes next

The next version should be less synthetic. I want to collect a small trace from an ESP32 running a fixed workload, measure the Wi-Fi transfer time and energy for that workload, and replace the lognormal assumptions with the measured distribution. If the conclusion changes, that is the useful result.

The longer thesis direction is in [the thesis plan](/research/thesis-plan/). It extends the same question to multiple edge servers, variable channels, and a testbed, with the simulation used to choose which policies are worth testing on real hardware.
