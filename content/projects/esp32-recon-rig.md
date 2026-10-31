---
date: '2026-09-20T00:00:00+08:00'
title: 'ESP32 Recon Rig'
description: 'A five-dollar board turned into a wifi and BLE recon dashboard, including the driver fight.'
weight: 11
status: 'LAB PROJECT'
period: '2026'
stack: ['ESP32', 'ESP-IDF', 'C', '802.11', 'BLE']
cover: 'images/shots/esp32-board.webp'
coverAlt: 'ESP32 development board wired for wifi and BLE capture'
---

The long version lives in the blog series: [the driver fight](/blog/esp32-recon-rig-driver-said-no/) and [the build guide](/blog/esp32-recon-rig-build-guide/). This page is the project summary.

## The Problem

Wifi and Bluetooth analysis usually starts with a laptop, a compatible adapter, and a stack of tools that assume you already know what you are looking at. I wanted to understand the layers from the radio up, on hardware cheap enough to keep on the desk and small enough to carry.

## What I Built

An ESP32 recon rig with a web dashboard and a serial console:

- Promiscuous-mode 802.11 capture: beacons, probes, deauth frames, and EAPOL counts.
- A station table with MAC addresses, signal strength, and the access point each station belongs to.
- Channel hopping across 1 to 13, with the single-radio trade-offs made explicit.
- PMKID extraction for my own lab network, because the best way to understand the attack is to collect your own ticket.
- Passive BLE scanning into the same dashboard: MACs, names, and signal strength.
- A deauth detector that notices the attack it can also transmit, on lab gear only.
- A web flow that turns a scanned access point into a target without asking the user to type forty hex characters.

## The Hard Part

The closed wifi driver has an allowlist. Deauth frames are not on it. The project turned into a lesson in linker tricks, symbol overrides, SDK downgrades, and reading Xtensa assembly by hand. The ending is better than the detour: the frame goes out, the detector catches it, and the lab stays a lab.

## Scope

The transmitting side is for my own access point or gear I have written permission to test. The [lab rules](/lab-rules/) are part of the project, not a disclaimer bolted on at the end. The receiving side is where most of the learning happens, and it is safe almost everywhere.

## Stack

ESP32, ESP-IDF, C, 802.11, BLE, a handwritten web dashboard, and a serial console.

## Write-ups

- [I Taught a $5 Board to Sniff WiFi, Then Fought Its Driver](/blog/esp32-recon-rig-driver-said-no/)
- [Building the ESP32 recon rig for real](/blog/esp32-recon-rig-build-guide/)
- [Wifi from zero](/wifi-from-zero/)
