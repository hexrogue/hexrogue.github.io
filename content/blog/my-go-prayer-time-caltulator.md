---
date: '2026-01-08T17:34:10+08:00'
title: 'My Go Prayer Time Caltulator: A "DIY" Journey'
description: "How I built an offline, terminal-based prayer time calculator for Malaysia using Go, Bubble Tea, and astronomical formulas from math headaches to TUI bliss."
tags: ['go', 'cli', 'astronomy', 'bubbletea', 'malaysia']
---

Hey everyone,
Ever had one of those "lightbulb" moments where you thought, "Man, I could totally build that myself"? That's kinda how my **PrayerTime TUI** project came to life. It's a command-line tool I whipped up in Go to calculate prayer times for Malaysian districts, right in your terminal. No fancy web apps, no constant API calls, just pure command-line goodness.

## The 'Aha' Moment: Why Bother Building It?

As a developer, I'm always looking for cool stuff to add to my portfolio. Something that really shows off a mix of coding logic, database interaction, and a decent user interface. Prayer times are something almost all Muslims check daily, and while there are tons of apps out there, most rely heavily on external APIs.

I started thinking: "What if I wanted something local? Something that just works offline? And what if I could make it look sick in the terminal?"

That's where **Go** came in. I love its simplicity, performance, and how easy it is to build robust CLI tools. For the terminal UI, I'd been eyeing Charmbracelet's Bubble Tea for a while – it makes building interactive TUIs surprisingly fun and elegant.

My goal was clear: A self-contained, offline prayer time calculator for Malaysia. This meant I needed to:

1. **Get Coordinates**: A database of Malaysian state/city coordinates.
2. **Do the Math**: Implement the actual astronomical calculation logic.
3. **Build a UI**: Create an interactive terminal interface.

## Diving into the Astronomical Brainiac Stuff (The "Pening" Phase)

This was, without a doubt, the biggest hurdle. Calculating prayer times isn't just a simple `if-then-else` statement. It involves some pretty serious astronomical geometry and a solid understanding of Earth's position relative to the Sun. I had to dive deep into research papers and complex formulas.

My main reference point was this gem: ["Prayer Times Calculation" by Mohamoud (2017).](https://astronomycenter.net/pdf/mohamoud_2017.pdf)

*Reading this felt like going back to school, but in a good way.*

Reading through the PDF was like entering a boss fight in a video game. It's packed with terms like Julian Days, Solar Declination, Equation of Time, Obliquity of the Ecliptic, and all sorts of trigonometric functions. Honestly, it felt like I was back in high school physics and math, but this time, it was genuinely fun because I was building something tangible.

## Challenge 1: Deciphering the Formulas & Radian/Degree Conversion Hell

The formulas looked daunting on paper. Translating `sin(latitude) * cos(declination)` into actual Go code, making sure all the angles were correctly converted to radians (which Go's `math` package expects) or degrees at the right time that was a constant head-scratcher.

The biggest headache was probably the **Equation of Time** (EoT) formula. If you get this wrong by even a tiny bit, your entire set of prayer times will be off by several minutes. I remember spending hours debugging why my Zohor time was consistently 15 minutes earlier than the official JAKIM times. It was driving me nuts!

*This seemingly simple formula caused so much pain... but also so much learning!*

**The Solution**: I broke down each complex formula into smaller, manageable Go functions. I created dedicated helper functions for `deg2rad` and `rad2deg` to prevent constant conversion errors. Then, I’d calculate one variable at a time (`declination`, `istiwa`), print intermediate results to the console, and compare them with values I'd manually punched into a scientific calculator or cross-checked with other online tools. It was a tedious process of trial and error, but slowly, meticulously, the pieces started fitting together.

Here's a peek at some of that core calculation logic in Go:

```go
// Snippet from prayer/calculation.go
func (w *PrayerTime) calculate() {
    // N is the number of days since Jan 1st - crucial for orbital position
    n := daySinceJan1(w.Year, w.Month, w.Day)
    t := 2 * math.Pi * float64(n-1) / 365 // Time in radians

    // Calculating Solar Declination (Earth's tilt relative to the sun)
    w.declination = 
        0.006918 -
        0.399912*math.Cos(t) +
        0.070257*math.Sin(t) -
        0.006758*math.Cos(2*t) +
        0.000907*math.Sin(2*t) -
        0.002696*math.Cos(3*t) +
        0.00148*math.Sin(3*t)

    // Calculating Equation of Time (EOT) and Solar Noon (Istiwa)
    eot := equationOfTime(w.Year, w.Month, w.Day, w.Zone)
    // Solar noon adjusted for longitude (Malaysia uses 120E reference)
    w.istiwa = (12 + eot/60) + ((120 - w.Longitude) / 15) 
}

// Function to calculate Hour Angle for specific prayer times like Fajr, Maghrib, Isya'
func hourAngle(w *PrayerTime, angle float64) float64 {
    a := deg2rad(angle) // Convert target angle to radians
    lat := deg2rad(w.Latitude) // Convert latitude to radians

    return rad2deg(math.Acos(
        (math.Sin(a)-math.Sin(w.declination)*math.Sin(lat))/
            (math.Cos(w.declination)*math.Cos(lat)),
    )) / 15 // Convert result from degrees to hours
}
```

*It’s not just about coding; it’s about understanding the science behind it!*

## The Database Dilemma: No More Manual Coordinates!

After sorting out the math, the next big piece was making the app user-friendly. I definitely didn't want users to type in latitude and longitude every single time they wanted to check prayer times. That’s just clunky. Malaysia has different zones, so I needed a way to store all the districts and their corresponding coordinates.

**Challenge 2: Where to get the data and how to store it efficiently?** I luckily had a head start with this, as I maintain a helper repository called `hexrogue/city2coordinates`. This project essentially scrapes and compiles coordinate data for Malaysian districts.

**Solution**: I created a simple `zones.db` SQLite database ((derived from my [city2coordinates](https://github.com/hexrogue/city2coordinates) project)). SQLite was the obvious choice for a local, file-based database which is perfect for an offline CLI tool. My `zone` package in the project then handles all the database interactions: fetching a list of states, then cities within a selected state, and finally the precise coordinates for a chosen district. It’s pretty neat because it means the app is fully self-contained and ready to go once the `zones.db` file is in place.

## Building the TUI: Making it Pretty in the Terminal

With the math and data handled, it was time for the user experience. Using **Charmbracelet's Bubble Tea** was a blast. It adopts this elegant Elm-like architecture (Model-Update-View) that makes building interactive terminal apps surprisingly easy and organized.

**Challenge 3: Managing UI states** How do I transition smoothly from selecting a state, to selecting a city, and then finally displaying the prayer times? Handling keyboard inputs (`up`, `down`, `enter`, `q`) without making the UI feel janky was the goal.

**The Solution**: The `Model` struct in my `tui` package became the single source of truth. I defined different `step` values (like `stepState`, `stepCity`, `stepResult`) and used a `switch` statement in the `Update` method to change what the user sees based on their input.

## ⚠️ The Reality Check (Disclaimer)

Building this was a massive win for my portfolio, but I have to be honest: astronomical math is complex. Things like elevation, atmospheric pressure, and specific regional sighting criteria can change the "official" time by a minute or two.

So, while this tool is great for a project showcase, if you need 100% verified accuracy for actual worship, you should always check **e-solat.gov.my**. They even have an API if you're building something for production!

## Wrap Up

This project taught me a ton about Go, TUI design, and why ancient astronomers were basically geniuses. If you're into Go or just want to see how I organized the code, check out the repo!
