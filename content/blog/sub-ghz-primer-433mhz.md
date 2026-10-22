---
date: '2026-05-31T15:20:00+08:00'
title: 'Sub-GHz primer: 433 MHz, weather stations and remote controls'
description: 'Everything cheap and wireless below 1 GHz. On-off keying, why a garage remote replays, and what the CC1101 in my mail bag is actually for.'
tags: ['radio', 'security', 'explainer']
author: nuh
---

Wifi and Bluetooth both live at 2.4 GHz. The rest of the cheap wireless world lives below 1 GHz, and the ESP32 cannot hear any of it. That is the entire reason the second half of this project exists, and the reason your cheap remote control can reach the garage while your phone gives up at the kitchen door. The setup deserves a primer before the hardware arrives.

## Why below 1 GHz

Lower frequencies go further and through more walls at the same power. A 433 MHz signal from a coin cell crosses a house; a 2.4 GHz signal from the same cell struggles with two walls. The trade is bandwidth, and these devices do not need bandwidth. A weather sensor sends twelve bytes every minute. A doorbell sends one bit when pressed. A lower frequency with a wide open band is the correct engineering choice, and it has been for thirty years.

The bands, roughly: 433 MHz is the common one across much of the world, 315 MHz turns up in North America, 868 MHz in Europe, 915 MHz in much of the Americas. Devices are cheap, unlicensed within power limits, and consequently everywhere: remotes, sensors, doorbells, tyre pressure monitors, utility meters, thermostats.

## On-off keying, which is Morse with silicon

<figure>
<img src="/images/diagrams/ook-waveform.svg" alt="A carrier switched on and off to encode bits">
<figcaption>The carrier is on, off, on, on, off, on. The receiver only has to measure the gaps between them.</figcaption>
</figure>

The simplest modulation is OOK, on-off keying. A carrier at 433.92 MHz is switched on and off to send ones and zeros. Switch fast enough and you are sending a frame; switch in a pattern and you are sending a remote's button code. It is Morse code with a microcontroller holding the key, and a receiver can record the pattern exactly as it was transmitted.

More robust devices use FSK, which shifts the frequency instead of switching the carrier, and survives noise better. Either way, the frame that comes out is short, often carries no encryption, and almost never has a handshake. Nothing associates, nothing exchanges keys, and nothing admits anyone. Somebody transmits, and whoever has a compatible receiver decodes.

## Why a remote replays

Recording a signal and playing it back is a replay, and it is the whole reason sub-GHz got a reputation. A cheap remote transmits the same pattern every press. Capture it once with a receiver, transmit it once with a transmitter, and the door, gate or socket does the same thing it does when you press the real button. No cracking involved. The signal is not secret and the device does not ask who is sending it.

Modern car keys and anything that takes security seriously use rolling codes: each press increments a counter, so the same capture does not work twice, and a replay of an old capture is either ignored or noticed. That closed the easy path and pushed the interesting work into the code-generation algorithms, which is a different hobby with a higher price of entry.

## Weather stations, the gentle target

Weather sensors are the friendliest study subjects in radio. A sensor broadcasts temperature, humidity and often pressure every thirty to sixty seconds, with an ID so the indoor display knows which sensor is which. There is no pairing, so anyone with a decoder can read a neighbour's sensor. The frames are unencrypted, the data is not personal, and nobody is harmed by decoding numbers that the air is already carrying.

The interesting part is that every vendor uses a different bit layout, and most of them never published it. So the work is: record the frame, find where it repeats, then find the field that moves. Change the temperature in the room and see which byte changes. When you find the one that tracks the thermometer, you have decoded a protocol that was never documented, which is a very satisfying afternoon.

<figure>
<img src="/images/hardware/weather-sensor.jpg" alt="A wireless remote sensor showing temperature on its display, with 433 MHz printed on the case">
<figcaption>A wireless remote sensor, band printed on the case for anyone who cares to read it. Photo by Hedwig Storch, CC BY-SA 3.0, via Wikimedia Commons.</figcaption>
</figure>

## The hardware I am waiting on

The ESP32 speaks 2.4 GHz and nothing lower, so sub-GHz needs a second radio. The CC1101 is the cheap standard choice: a small SPI module, tuned from about 300 to 928 MHz, well documented, a few dollars. Wire it to the board's SPI pins, write a driver, and the same dashboard grows a second radio. That is the plan for part two, and it starts when the jumper wires arrive, which is, as always, the least glamorous bottleneck.

One note before the fun: transmitting on these bands has power limits, duty-cycle limits and type approval in every country, and the rules change band to band. Receiving is the safe half and the half that teaches you the protocol. Transmitting to your own hardware, within the limits, is the rest of it. The rules for that are the same as everywhere on this site, on [the lab rules](/lab-rules/) page.

<figure>
<img src="/images/memes/meme-subghz-boromir.jpg" alt="One does not simply meme about decoding a weather station with no datasheet">
<figcaption>The datasheet exists. It is someone's blog post from 2009 with three dead images.</figcaption>
</figure>

<figure>
<img src="/images/memes/meme-subghz-drake-replay.jpg" alt="Drake meme preferring recording one signal and replaying it over pressing a button hundreds of times">
<figcaption>One capture, one replay. The door does not check who is holding the transmitter.</figcaption>
</figure>

> "If you can hear it, you can decode it.", me, at 3 AM, staring at a repeating bit pattern and calling it progress.

## Try this

If you have an RTL-SDR or a CC1101, record a weather sensor. Look at the same signal as bits and find the frame that repeats every minute. Then find the temperature field the slow way: change the room temperature, record again, and look for the byte that moved. The sensor is yours and the air was already carrying it, so you need nothing else.

The 2.4 GHz half of this board is written up in [the recon rig story](/blog/esp32-recon-rig-driver-said-no/).
