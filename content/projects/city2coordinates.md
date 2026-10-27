---
date: '2026-09-20T00:00:00+08:00'
title: 'City2Coordinates'
description: 'Lightweight geocoding tool that turns Malaysian cities into latitude and longitude data.'
weight: 10
status: 'OPEN SOURCE'
period: '2026'
stack: ['Go', 'SQLite', 'OpenStreetMap']
---

Open source: [github.com/hexrogue/city2coordinates](https://github.com/hexrogue/city2coordinates).

A small geocoding tool that converts Malaysian cities and districts into latitude and longitude data. It was built as a data preparation pipeline for location-aware projects, including the [PrayerTime calculator](/projects/prayertime/).

## The Problem

The prayer time calculator needs coordinates for every city and district it supports. Typing them by hand is boring, error-prone, and exactly the kind of task that should be a script. The data also needs to be cached, because rate limits are real and network calls are not a personality.

## What I Built

- A Go CLI that resolves Malaysian place names through the OpenStreetMap Nominatim API.
- Rate limiting and local SQLite caching for repeatable, offline-friendly runs.
- A data pipeline that produces coordinates in a format the prayer time calculator can consume.
- A small enough tool to read in one sitting, which is the correct size for a data-prep utility.

## The Result

The prayer time project gets a repeatable coordinate source instead of a hand-maintained list. The tool is also a useful example of how to treat an external API politely: cache, rate-limit, and do not re-fetch what you already know.

## Stack

Go, SQLite, OpenStreetMap Nominatim.
