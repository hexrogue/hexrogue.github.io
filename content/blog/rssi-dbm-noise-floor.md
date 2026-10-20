---
date: '2026-10-05T09:45:00+08:00'
title: 'RSSI is a liar'
description: 'dBm is a log scale, RSSI has no standard unit, and the same signal number can mean a working link or a buried one. Noise floor and SNR are the numbers that matter.'
tags: ['wifi', 'networking', 'explainer']
author: nuh
---

Your laptop reports -67 dBm and streams video. Your phone reports -67 dBm and stutters. Neither number is lying about the signal. Both are lying about the quality, because the signal alone does not contain the noise.

## dBm is a log scale

0 dBm is one milliwatt. Every 3 dB doubles or halves the power, and every 10 dB is a factor of ten. So -60 dBm is ten times the power of -70 dBm, and -70 is ten times -80. The gap between "fine" and "dead" is smaller than the numbers suggest: -67 to -80 is 13 dB, roughly a factor of twenty in power.

Wifi lives between about -30 next to the access point and -90 in the background. Below roughly -80, most clients start dropping or refuse to associate, and the exact cut-off depends on the client.

## RSSI is not a unit

RSSI means received signal strength indicator, and the standard does not define the scale. Some chips report dBm. Some report a vendor specific number that happens to look like dBm. Some clamp at both ends. Apple hides it entirely and shows bars. Two devices showing -67 may be measuring different things with different antennas and different calibration.

This is why comparing your phone to your laptop is meaningless. Compare one device to itself, over time, at the places you actually sit.

## The number that matters: SNR

The noise floor is the background energy on the channel. In a quiet house it sits near -90 dBm. In an apartment with ten networks it can be -80 or worse. Signal to noise ratio is signal minus noise.

-67 signal with -90 noise is 23 dB SNR. Comfortable.
-67 signal with -60 noise is -7 dB SNR. The signal is buried.

Same bars, different worlds. This is how "the signal is strong" and "the wifi is unusable" are both true at once, and it is the answer to most arguments about routers.

```mermaid {alt="The same -67 dBm signal with two different noise floors: against -90 dBm it gives 23 dB SNR and works, against -60 dBm it gives minus 7 dB and is unusable"}
flowchart LR
  S["signal -67 dBm"] --> N{"minus noise floor"}
  N -->|"-90 dBm"| G["SNR 23 dB, fine"]
  N -->|"-60 dBm"| B["SNR -7 dB, unusable"]
  G --> R["check retries before blaming the app"]
  B --> F["find the interferer first"]
```

## Link rate lies too

The number in the wifi menu is a negotiated rate, not throughput. It depends on channel width, spatial streams, guard interval and the modulation scheme, and it can stay high while retries eat the airtime. A 2.4 GHz link claiming 144 Mbps can deliver less than a 5 GHz link claiming 400, because the first one is sharing a lane and the second one is not.

## Measure the right things

- SNR, not bars.
- Retry and error counters, not the signal icon.
- Latency and jitter during the task that fails, not a speed test in an empty room.
- Airtime, if your access point exposes it.

On Linux, `iw dev wlan0 station dump` gives signal, noise, retries and rate. On Windows, `netsh wlan show interfaces` gives a signal percentage and a rate, both approximations. The pattern over time matters more than any single reading.

<figure>
<img src="/images/memes/meme-wifi-rssi-drake.jpg" alt="Drake meme: refusing to check the signal bars once, approving logging signal, noise and retries for an hour">
<figcaption>One reading is a rumour. An hour of readings is a diagnosis.</figcaption>
</figure>

## The human body is an obstacle

2.4 GHz is absorbed by water, and you are mostly water. Holding the phone changes the antenna's environment. Standing between the router and the laptop changes the link. Measure where you actually sit, not where the router is, and measure with the device in the position you use it.

## What to do with the number

If the SNR is good and the application is slow, the problem is upstream and wifi is not it. If the SNR is bad, move the access point or the client before buying a repeater, because a repeater with a bad backhaul just repeats the problem louder.

If the noise floor is the bad half, the interferer is the target, and [the 2.4 GHz post](/blog/24ghz-interference-channel-planning/) is where to look. If the SNR is fine but the retries climb, you are sharing airtime with too many neighbours.

One signal reading is a rumour. An hour of SNR and retries is a diagnosis.
