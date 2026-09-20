---
date: '2026-01-12T00:00:00+08:00'
title: 'Offline Prayer Times in Go'
description: "How I built a prayer time app that works with zero internet. Just your location, the Sun, and math."
tags: ['go', 'cli', 'astronomy', 'bubbletea', 'malaysia']
---

## The problem

Muslims check prayer times every day. Almost every app answers by asking a server on the internet. No signal in the basement carpark? Server down? No answer for you.

That always bothered me. "What time is Zuhr" should not need the cloud. The Sun is right there. So I built a calculator that works with zero internet. Open the terminal, pick your city, get your times.

## The solution

A small app with three ingredients. A list of Malaysian cities and their map coordinates. The Sun math that turns coordinates into prayer times. And a friendly terminal screen to tie it together. No APIs or network calls, just math.

## Result

One file you can run anywhere Go runs. Pick your state, pick your city, get accurate times for today. The math checks out against official sources.

<figure>
<img src="/images/memes/meme-prayer-offline.png" alt="Doge meme about offline prayer times">
<figcaption>No bars. No problem.</figcaption>
</figure>

## The hard part was the sky

Prayer times are Sun positions, and the Sun's position comes from four ideas that sound scary and are not:

- **Solar declination**: how tilted the Sun is today. Changes daily.
- **Equation of time**: the few minutes by which Sun time and clock time disagree.
- **Hour angle**: how far the Sun is from its daily peak, measured as an angle.
- **Solar noon**: the peak itself. Every other prayer is counted from here.

I followed a 2017 research paper by Mohamoud that lays all this out with geometry instead of magic.

The trickiest bit was the equation of time. Get it slightly wrong and every single prayer drifts by minutes. My Zohor kept showing up 15 minutes early and I stared at the code for a while before finding it: a longitude correction was off. Fifteen minutes, one wrong correction. Astronomy does not forgive sloppiness.

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

## Reality check

Sky math has limits. Hills, air pressure, and local moon-sighting rules can move times by a minute or two. I used a standard darkness angle for Fajr and Isha that most sources accept, but it will not match everyone.

So: for actual worship, check e-solat.gov.my, which has an official API for real products. This project is a learning exercise that happens to give the right answers.

## Wrap up

I learned Go, terminal screens, and one humbling fact: ancient astronomers worked all of this out with sticks, shadows, and patience. No computers. The code is on GitHub if you want to poke at it.
