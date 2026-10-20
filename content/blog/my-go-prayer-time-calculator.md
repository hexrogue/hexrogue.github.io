---
date: '2021-04-12T00:00:00+08:00'
title: 'The Sun Does Not Need an API'
description: "How I built a prayer time app that works with zero internet. Just your location, the Sun, and math."
aliases: ['/blog/my-go-prayer-time-caltulator/']
tags: ['go', 'cli', 'astronomy', 'bubbletea', 'malaysia']
author: nuh
---

I have stood in a basement carpark, holding my phone at the angle where hope lives, waiting for a prayer app to admit it needed the internet. No signal, no answer. For a prayer timetable. The Sun was directly above the building, no signal required.

That was the moment I decided to compute the times myself.

The result is one Go file you can run anywhere Go runs. Open the terminal, pick a state, pick a city, get the times. No API, no network call, no account. The only inputs are coordinates and the date. The Sun does the rest.

<figure>
<img src="/images/memes/meme-prayer-offline.png" alt="Doge meme about offline prayer times">
<figcaption>No bars. No problem.</figcaption>
</figure>

## What the program actually does

Three pieces:

- A list of Malaysian cities and their coordinates.
- The Sun math that turns a coordinate and a date into prayer times.
- A terminal screen that remembers which step you are on.

That is the whole app. No database, no cloud, no "sign in with Google" button. Pick your city and the math runs locally. I checked the output against official times. It holds up.

## The hard part was the sky

Prayer times are Sun positions with names. The Sun's position comes from four ideas that sound worse than they are:

- **Solar declination**: how tilted the Sun is today. Changes daily.
- **Equation of time**: the few minutes by which Sun time and clock time disagree.
- **Hour angle**: how far the Sun is from its daily peak, measured as an angle.
- **Solar noon**: the peak itself. Every other prayer is counted from here.

I followed a 2017 research paper by Mohamoud that lays all this out with geometry instead of magic.

The equation of time nearly ruined the project. Get it slightly wrong and every prayer drifts by minutes. My Zohor kept showing up fifteen minutes early. I stared at the code long enough to question my life choices, then found it: a longitude correction was off. One wrong correction, fifteen minutes. Astronomy does not forgive sloppiness.

To debug it, I split every formula into its own small function, printed the middle numbers, and compared them against a scientific calculator until they matched. The heart of it:

```go
func (w *PrayerTime) calculate() {
    n := daySinceJan1(w.Year, w.Month, w.Day)
    t := 2 * math.Pi * float64(n-1) / 365

    w.declination =
        0.006918 -
        0.399912*math.Cos(t) +
        0.070257*math.Sin(t) -
        0.006758*math.Cos(2*t) +
        0.000907*math.Sin(2*t) -
        0.002696*math.Cos(3*t) +
        0.00148*math.Sin(3*t)

    eot := equationOfTime(w.Year, w.Month, w.Day, w.Zone)
    w.istiwa = (12 + eot/60) + ((120 - w.Longitude) / 15)
}
```

In plain words: figure out which day of the year it is, compute the Sun's tilt, correct for the clock-versus-Sun gap, and find your local noon. Everything else hangs off that noon.

The screen uses Bubble Tea, a Go toolkit for terminal apps. It remembers which step you are on: pick a state, pick a city, see the times. Arrow keys do the rest.

## What it cannot do

Sky math has limits. Hills, air pressure, and local moon-sighting rules can move times by a minute or two. I used a standard darkness angle for Fajr and Isha that most sources accept, but it will not match everyone.

If you need the official number for worship, use e-solat.gov.my. This project is a learning exercise that happens to give the right answers.

## What I got out of it

I learned Go, terminal screens, and one humbling fact: ancient astronomers worked all of this out with sticks, shadows, and patience. No computers.

The Sun has been doing this for a while. I just wrote it down. The code is on GitHub if you want to poke at it.
