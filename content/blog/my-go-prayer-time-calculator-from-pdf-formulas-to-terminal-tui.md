---
date: '2026-02-03T00:00:00+08:00'
title: 'Sun Math: Prayer Times from a Research Paper'
description: 'How I turned a math paper about the Sun into a working prayer time calculator. No APIs, just the Sun and some code.'
---

## The problem

Your phone knows when to pray. But have you ever asked how? Most apps just download the answer from the internet. No internet, no answer. And nobody shows their work.

I wanted to know for real. Prayer times come from where the Sun sits in the sky. That is it. That is the whole secret. So I asked: can I compute them myself, from scratch, with nothing but math?

## The solution

I found a research paper with a great title: "Tracing the Shadow: Mathematical Calculation of Prayer Times Using Spherical Trigonometry" from the Middle-East Journal of Scientific Research. Big words. Simple idea. The Sun moves in ways we can predict, and prayer times are just Sun positions with names.

My goal: turn that paper into Go code, step by step, and check every number against official prayer times.

## Result

A Go library that computes prayer times from first principles. Every number traces back to the paper. The output matches official JAKIM times and survived cross-checks from independent re-derivations.

<figure>
<img src="/images/memes/meme-prayer-paper.png" alt="A meme about trusting the Sun with math">
<figcaption>Roll Safe contemplating celestial mechanics.</figcaption>
</figure>

## How the Sun becomes a schedule

Think of it like this. The Sun is a lamp moving across your ceiling. Where the lamp is tells you the time. Zuhr is when the lamp is at its highest. Everything else is measured from there.

Before any code, that is the whole mental model. Sun position depends on three things: your latitude (how far north or south you are), the Sun's tilt that day (called declination), and the hour angle (a fancy word for how far the Sun is from its peak). Time is just that angle converted into hours.

### Solar declination: the Sun's daily mood

The Sun does not sit in the same place every day. It drifts north and south through the year, which is why days get longer and shorter. That drift is called declination, and every prayer time depends on it.

I started with a simplified formula. The answers looked almost right. Almost right is the most dangerous kind of wrong, because you stop looking. So I switched to the full formula from the paper:

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

The `calculate()` method works out the day's tilt:

```go
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
```

Scary looking. It is just a recipe: take the day of the year, mix sines and cosines, get the tilt.

### Equation of time: why noon is rarely noon

My Zuhr kept drifting. Right some days, minutes off on others. That is not a rounding error. The Earth does not orbit in a perfect circle and it sits tilted, so clock time and Sun time disagree by a few minutes depending on the date. The fix is a small correction called the equation of time:

```go
E := L - alpha
if E > 50 {
	E -= 360
}
return -E * 4
```

One tiny function. It fixed Zuhr, and every prayer after it.

### Zuhr is the anchor

The paper's key sentence: every prayer time is an offset from solar noon. Zuhr is not 12:00 PM on your watch. It is the moment the Sun crosses your local middle line, the meridian:

```go
w.istiwa = (12 + eot/60) + ((120 - w.Longitude) / 15)
```

Your longitude shifts this. Two cities in the same timezone can have different Zuhrs. Longitude always matters.

<figure>
<img src="/images/memes/meme-badluck.png" alt="Shocked audience meme about longitude">
<figcaption>Computes everything. Forgets longitude.</figcaption>
</figure>

### Hour angle: angles in, hours out

This is the heart of the whole project. Give the formula a Sun angle, get back hours. Morning prayers subtract hours from Zuhr. Evening prayers add them:

```go
func hourAngle(w *PrayerTime, angle float64) float64 {
	return rad2deg(math.Acos(
		(math.Sin(deg2rad(angle)) -
			math.Sin(w.declination)*math.Sin(deg2rad(w.Latitude))) /
			(math.Cos(w.declination)*math.Cos(deg2rad(w.Latitude))),
	)) / 15
}
```

One function, used by every prayer. Learn this one and you understand the project.

### Asr: follow the shadow

Asr does not use a Sun height. It uses shadows. When your shadow grows to a certain length compared to your height, it is Asr. The paper gives the exact ratio from your latitude and the day's tilt. This part took me the longest, because getting shadow geometry slightly wrong breaks everything without any error message:

```go
func (w *PrayerTime) Asr() string {
	r := math.Atan(1 / (1 + math.Tan(math.Abs(deg2rad(w.Latitude)-w.declination))))
	return formatTime(w.istiwa + hourAngle(w, rad2deg(r)))
}
```

### Fajr and Isha: how dark is dark enough

Fajr and Isha happen when the Sun sits a certain depth below the horizon. How deep? Scholars differ. The paper lists several standards. I picked -18 degrees because it is widely used and keeps the math clean:

```go
func (w *PrayerTime) Fajr() string {
	return formatTime(w.istiwa - hourAngle(w, -18))
}
```

### Verification: trust nothing, check everything

I did not trust my own code. I checked it against official prayer times, had an AI re-derive the formulas independently, and got a friend to poke at edge cases. Once all three agreed, I stopped arguing with the output.

## Final thought

If you cannot point at each number in your output and say which page of the paper it came from, you do not understand the calculation yet. Prayer times are the Sun doing laps. The math just writes down the schedule.

This project is for learning. For actual worship times, refer to e-solat.gov.my.
