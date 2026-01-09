---
date: '2026-01-08T21:36:08+08:00'
title: 'My Go Prayer Time Calculator: From Reasearch Paper Formulas to Terminal TUI'
description: 'How I translated a dense academic research on spherical trigonometry into a working Golang prayer time calculator. Real problems, wrong assumptions, debugging moments, and how I validated my math using AI and human friends.'
---

# Introduction


Prayer time calculation looks simple on the surface.
But once you stop relying on tables, APIs, or existing libraries, reality hits different.

This project started with one question in my head:

> If prayer times are fixed by the Sun, why do most implementations feel like black boxes?

So I went straight to the source.
An academic paper titled "**Tracing the Shadow: Mathematical Calculation of Prayer Times Using Spherical Trigonometry**" published in Middle-East Journal of Scientific Research.

This post is not about re-explaining the research paper.
This is about **how I translated theory into Go code**, step by step, including the mistakes I made along the way.

Deep work only. No vibes coding.

## Starting Point: The Holy PDF

I began with ["Prayer Times Calculation" by Mohamoud (2017)](https://astronomycenter.net/pdf/mohamoud_2017.pdf). Solid paper. Clear sections. But it reads like an astronomy final exam 😅.

The core idea:

> Prayer time = function of latitude, longitude, date, and sun angle (e.g., -18° for Fajr).

Key equations I needed:

- **Solar Declination** (Eq. 7, p.5)
- **Equation of Time (EoT)** (Eq. 8–9, p.6)
- **Hour Angle** (Eq. 12, p.7)
- **Solar Noon (Istiwa)** (derived from EoT + longitude)

So I opened Neovim and started typing… with full confidence and zero understanding.


## The Reference Paper (Why This One)

The paper does three important things that most blog posts skip:

1. It defines prayer times **based on geometry**, not tradition alone
2. It models **Asr using shadow length**, not fixed offsets
3. It connects **Julian Day, solar declination, hour angle, and Equation of Time** cleanly

That’s rare.

This line basically sets the tone:

> *Prayer indeed has been enjoined on the believers at fixed times.*
**Surah An-Nisaa, 4:103**

Fixed times means calculable times.

## Research Breakdown & Context

Before we hit Go code, let's unpack the research a bit. This is boring, you can skip this part if you want to.

The original paper dives deep into spherical trig & shadow lengths, so here's how I digested it:

### 1. Solar Declination & Elevation

The research shows how the Sun’s angle with the equator changes daily (declination), which affects **all prayers**.
- Concept: Max elevation at noon, min at sunrise/sunset.
- My code: `w.declination` in `calculate()`.

![](/images/Screenshot_20260109_004413.png)

### 2. Hour Angle & Equation of Time

They explain **hour angle H**: basically how far the Sun is from zenith in hours, plus **Equation of Time (EoT)** which fixes solar noon vs clock noon.
- Concept: Zuhr isn’t exactly 12:00 PM, small offset daily.
- My code: `hourAngle(w, angle)` & `equationOfTime()`

![](/images/Screenshot_20260109_004719.png)

### 3. Shadow Length & Asr

Asr time depends on shadow length, which is the trickiest part.
- The research paper uses: `l = h[1 + tan(|latitude - declination|)]`
- My code: `Asr()` uses a ratio of shadow length + zenith shadow adjustment

![](/images/Screenshot_20260109_005518.png)

### 4. Fajr & Isha Angles

Fajr/Isha angles set at -18° below horizon.
- The research paper explains why different angles produce slightly different times in different regions.
- My code: `Fajr()` & `Isha()` just plug in -18°

![](/images/Screenshot_20260109_005743.png)

## High Level Idea 

Before touching Go, I wrote this mental model:
- Everything depends on Sun position
- Sun position depends on
  - Latitude
  - Declination
  - Hour angle
- Time is just angle converted to hours
- Zuhr is the anchor
- Everything else is offset from Zuhr

Once you get this, the research paper stops looking scary.

## Step 1: Shared Astronomical State

### Research Paper Concept

The paper repeatedly reuses:
- Sun declination
- Local solar noon

So instead of recalculating per prayer, I centralized it.

### Go Translation

```go
type PrayerTime struct {
	Latitude  float64
	Longitude float64
	Year      int
	Month     int
	Day       int
	Zone      int

	declination float64
	istiwa      float64
}
```

This struct is not just data.
It's **cached astronomy**.

![](/images/Screenshot_20260109_003008.png)
![](/images/Screenshot_20260109_003033.png)

## Step 2: Solar Declination

### The Research Paper Says

Declination varies sinusoidally with Julian Day.

### My First Mistake

I initially trusted a simplified formula.
Results looked "almost correct" which is dangerous.

Close is worse than wrong.

### Final implementation

```go
n := daySinceJan1(w.Year, w.Month, w.Day)
t := 2 * math.Pi * float64(n-1) / 365

w.declination =
	0.006918 -
	0.399912*math.Cos(t) +
	0.070257*math.Sin(t) -
	0.006758*math.Cos(2*t) +
	0.000907*math.Sin(2*t)
```

This maps directly to the paper's declination curve.

Lesson here
If math looks ugly, it's probably correct.

## Step 3: Equation of Time

This part humbled me.

### The Problem

My Zuhr was drifting.
Some days correct, some days off by minutes.

That's not rounding error.
That's physics screaming.

### PDF Insight

The Earth:
- Moves elliptically
- Tilts its axis

So clock time \(\neq\) solar time.

### Go Implementation

```go
E := L - alpha
if E > 50 {
	E -= 360
}
return -E * 4
```

This one function fixed:
- Zuhr accuracy
- All downstream prayer times

![](/images/Screenshot_20260109_012930.png)

## Step 4: Zuhr Is the Anchor

From the paper:

> All prayer times are offsets from solar noon.

So Zuhr is not "12:00 PM".
It's **when the Sun crosses the local meridian**.

```go
w.istiwa = (12 + eot/60) + ((120 - w.Longitude) / 15)
```

This line alone explains why tables differ by region.

Longitude matters. Always.

## Step 5: Hour Angle Is Everything

This is the core translation from PDF to code.

### PDF Formula (simplified)

\(\cos(H) = \frac{\sin(a) - \sin(\delta) \sin(\phi)}{\cos(\delta) \cos(\phi)}\)

### Go Version

```go
func hourAngle(w *PrayerTime, angle float64) float64 {
	return rad2deg(math.Acos(
		(math.Sin(deg2rad(angle)) -
			math.Sin(w.declination)*math.Sin(deg2rad(w.Latitude))) /
			(math.Cos(w.declination)*math.Cos(deg2rad(w.Latitude)),
	)) / 15
}
```

Angle goes in
Time comes out

No magic.

## Step 6: Asr Nearly Broke Me

Asr is not based on elevation directly.
It's based on shadow ratio.

From the paper:

> Asr begins when shadow length equals object height plus zenith shadow.

### Translation Logic

```go
r := math.Atan(1 / (1 + math.Tan(math.Abs(deg2rad(w.Latitude)-w.declination))))
```

This line took me the longest.

Why
Because if you misunderstand shadow geometry, everything collapses silently.

```go
func (w *PrayerTime) Asr() string {
	// Asr uses shadow length ratio of 1
	r := math.Atan(1 / (1 + math.Tan(math.Abs(deg2rad(w.Latitude)-w.declination))))
	return formatTime(w.istiwa + hourAngle(w, rad2deg(r)))
}
```
![](/images/Screenshot_20260109_013658.png)

## Step 7: Fajr & Isha (Why I Chose -18°)

The paper lists multiple standards.

I explicitly chose:

- Fajr: -18°
- Isha: -18°

Not because it's "best"
But because it's **widely accepted** and mathematically clean.

```go
func (w *PrayerTime) Fajr() string {
	return formatTime(w.istiwa - hourAngle(w, -18))
}
```

Clarity > debates.

## Verification

I did't trust myself.

So I did three things:

1. Cross-checked outputs with official prayer times
2. Asked AI to independently re-derive the formulas
3. Had a friend sanity-check edge cases

When all three agree, ego steps aside.

Truth wins.


## Final Thought

This project taught me one thing:

> If your implementation can't be explained from first principles, you don't understand it yet.

Prayer times are not mystical.
They are celestial mechanics rendered human.

{{< callout type="warning" >}}
This project is intended for **portfolio and educational purposes only**. For official prayer times, always refer to [e-solat.gov.my](https://www.e-solat.gov.my).
{{< /callout >}}
