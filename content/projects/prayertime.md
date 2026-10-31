---
date: '2026-09-20T00:00:00+08:00'
title: 'PrayerTime Calculator'
description: 'Offline terminal prayer time calculator for Malaysia, built from spherical trigonometry.'
weight: 8
status: 'OPEN SOURCE'
period: '2026'
stack: ['Go', 'Bubble Tea', 'SQLite']
cover: 'images/shots/prayertime-code.webp'
coverAlt: 'PrayerTime Go source in nvim with the prayer time calculation functions open'
gallery:
  - src: 'images/shots/prayertime-demo.webp'
    alt: 'PrayerTime terminal interface showing the day prayer times'
    caption: 'The terminal app running offline, with no network call and no API key.'
---

Open source: [github.com/hexrogue/PrayerTime](https://github.com/hexrogue/PrayerTime).

A terminal-based prayer time calculator for Malaysia. It computes every time from scratch using spherical trigonometry. No APIs, no network calls, no account, no "please enable location services" popup.

## The Problem

Prayer apps that need the internet are useless in a basement car park, a rural area, or a flight with no wifi. The Sun does not need an API. The calculation is deterministic, and the data is small enough to ship with the binary.

## How It Works

Three pieces:

- A SQLite database of Malaysian district coordinates.
- The math that turns coordinates and a date into prayer times.
- A Bubble Tea terminal interface that makes it usable.

The math follows a 2017 research paper on spherical trigonometry: solar declination from a full Fourier series, the equation of time to stop Zuhr drifting, solar noon as the anchor for every other prayer, and an hour angle function that converts sun angles into hours. Asr is computed from shadow length, not a fixed offset. Fajr and Isha use -18 degrees.

The interface is a `Model` struct that tracks where you are: pick a state, pick a city, see the times. Everything compiles to a single binary. The user can run it offline, which is the entire point.

## The Result

The calculator was cross-checked against official Malaysian prayer times. Standard disclaimers apply: elevation and local sighting conventions can shift edge cases by a minute or two, so for worship use [e-solat.gov.my](https://www.e-solat.gov.my/).

## Stack

Go, Bubble Tea, SQLite.

## Write-ups

- [From Research Paper to Working Code: A Go Prayer Time Calculator](/blog/my-go-prayer-time-calculator-from-pdf-formulas-to-terminal-tui/)
- [Building an Offline Prayer Time Calculator in Go](/blog/my-go-prayer-time-calculator/)
