---
date: '2026-09-20T00:00:00+08:00'
title: 'PrayerTime Calculator'
description: 'Offline terminal prayer time calculator for Malaysia.'
---

Open source: [github.com/hexrogue/PrayerTime](https://github.com/hexrogue/PrayerTime).

Terminal-based prayer time calculator for Malaysia. Computes every time from scratch using spherical trigonometry. Offline-first. No APIs, no network calls.

## How it works

Three pieces. A SQLite database of Malaysian district coordinates. The math that turns coordinates into times. A terminal interface to make it usable.

The math follows a 2017 research paper on spherical trigonometry: solar declination from a full Fourier series (the simplified formula looked almost right, which was worse than wrong), the equation of time to stop Zuhr drifting, solar noon as the anchor every other prayer offsets from, and an hour angle function that converts sun angles into hours. Asr is computed from shadow length, not a fixed offset. Fajr and Isha use -18 degrees.

The interface is Charmbracelet's Bubble Tea. A `Model` struct tracks where you are: pick a state, pick a city, see the times. Everything compiles to a single binary.

Results were cross-checked against official times. Standard disclaimers apply: elevation and local sighting conventions can shift edge cases by a minute or two, so for worship use e-solat.gov.my.

## Write-ups

- [From Research Paper to Working Code: A Go Prayer Time Calculator](/blog/my-go-prayer-time-calculator-from-pdf-formulas-to-terminal-tui/)
- [Building an Offline Prayer Time Calculator in Go](/blog/my-go-prayer-time-caltulator/)

## Stack

Go, Bubble Tea, SQLite.
