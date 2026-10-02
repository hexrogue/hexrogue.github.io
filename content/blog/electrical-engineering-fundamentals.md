---
date: '2026-10-02T00:00:00+08:00'
title: 'Electrical Engineering Fundamentals, Without the Headache'
description: 'Study notes, plain version: voltage is pressure, current is flow, and everything else is just fancy plumbing with math.'
tags: ['study', 'electronics', 'ee']
---

I am a software guy. My world is if-else and semicolons. Then I touched electrical engineering and realized all my code runs on literal lightning we bullied into doing math. So I learned the basics. Here is my notebook, translated into human.

## Voltage is pressure, current is flow

Forget definitions for a sec. Picture a water pipe.

Voltage is how hard the water wants to move. Current is how much actually moves. Resistance is the narrow bit that says no. That mapping is the whole subject. Every confusing circuit I have hit turned into "wait, which part of the pipe is this."

| Thing | Water version | Unit | Symbol |
|---|---|---|---|
| Voltage | pressure | volts | \(V\) |
| Current | flow rate | amps | \(I\) |
| Resistance | narrow pipe | ohms | \(R\) |
| Power | how hard it works | watts | \(P\) |

<figure>
<img src="/images/memes/meme-ee-voltage.jpg" alt="No Yes meme about whether voltage is pressure">
<figcaption>Is voltage the pressure. Yes.</figcaption>
</figure>

Big pressure + tiny pipe = still no water. Big pipe + no pressure = also no water. You need both. That is 80% of EE intuition right there.

## Ohm's law is the whole first chapter

$$V = I \times R$$

Voltage is current times resistance. Flip it around when you get given the wrong two:

$$I = \frac{V}{R} \qquad R = \frac{V}{I}$$

My charger example, because it is the one I actually use. The brick says `5V ⎓ 2A`. Phone does not pull 2A all the time, it pulls whatever the circuit allows:

$$I = \frac{5\,\text{V}}{2.5\,\Omega} = 2\,\text{A}$$

$$P = V \times I = 5\,\text{V} \times 2\,\text{A} = 10\,\text{W}$$

So the label is not marketing fluff, it is Ohm's law printed on plastic. This also explains why a bad cable makes your phone charge slow or get hot. Thin cable means more ohms, and more ohms at fixed voltage means the whole budget burns as heat in the wire instead of reaching the battery.

Power has three faces, same formula rearranged:

$$P = V \times I = I^2 R = \frac{V^2}{R}$$

The \(I^2 R\) version is the one that scares electricians, because current squared means a short circuit gets exponentially worse fast. Laptop brick: \(19\,\text{V} \times 6\,\text{A} = 114\,\text{W}\). Enough to fry telur.

```python
# my "check it before I trust it" habit
V, R = 5.0, 2.5
I = V / R
P = V * I
print(f"{I:.1f} A, {P:.1f} W")   # 2.0 A, 10.0 W
```

<figure>
<img src="/images/memes/meme-ee-ohm.jpg" alt="Scientist meme about finally understanding Ohm's law">
<figcaption>Finally getting Ohm's law. Forgetting it by the next lab.</figcaption>
</figure>

## AC vs DC: battery vs TNB

DC flows one way, steady. Battery, USB, laptop, everything small and polite. Flat line on the oscilloscope. Easy mode.

AC flips direction constantly. In Malaysia that is 50 times per second, right out of the wall socket. Sine wave, which is why AC transformers work and why AC is what the grid runs on:

$$v(t) = V_{peak} \sin(2\pi f t), \qquad f = 50\,\text{Hz}$$

| Where | Type | What you get |
|---|---|---|
| Phone battery | DC | \(3.7\,\text{V}\) |
| USB charger out | DC | \(5\,\text{V}\) or \(9\,\text{V}\) |
| Arduino pin | DC | \(5\,\text{V}\) or \(3.3\,\text{V}\) |
| Malaysia socket | AC | \(240\,\text{V}\), \(50\,\text{Hz}\) |
| US socket | AC | \(120\,\text{V}\), \(60\,\text{Hz}\) |
| TNB pylon | AC | \(132\,\text{kV}\) to \(275\,\text{kV}\) |

Why does the grid bother with AC? Because of that \(I^2 R\) formula again. Wires have resistance, and power lost in a wire is \(I^2 R\), so the trick is to send low current and crank voltage insanely high. 275kV down the pylon, step it down at substations, step it down again in your area, 240V at the socket. DC cannot be transformed that easily, which is why every long HVDC line has converter stations at both ends paying for what a transformer does for free.

Your charger is the last translator in the chain. Wall gives \(240\,\text{V}\) AC, charger gives your phone \(5\,\text{V}\) DC. Transformer steps the voltage down, rectifier flips it, capacitor smooths it, regulator keeps it steady. One box, four jobs.

```text
TNB pylon 275kV AC
   -> substation transformer
   -> street transformer
   -> your socket 240V AC
      -> your charger -> 5V DC -> cable -> phone
```

<figure>
<img src="/images/memes/meme-ee-tnb.jpg" alt="Charlie conspiracy meme about TNB engineers and chargers">
<figcaption>They know why your charger needs four parts.</figcaption>
</figure>

## Resistor, capacitor, inductor

Three parts. That is the whole toolkit for first-year circuits.

Resistor fights the flow and gets warm doing it. That is the entire trick, the rest is picking the right value. Drop a voltage across it and you get:

$$V_R = I \times R$$

Capacitor is a bucket. It fills up with charge and dumps it fast, and it hates DC because once full it stops accepting more. Which means it lets AC through and blocks DC. Used to smooth power, filter noise, time circuits:

$$Q = C \times V, \qquad I = C\frac{dV}{dt}$$

Inductor is a heavy flywheel. It resists changes in current, not current itself, so it lets DC through and fights AC. Transformers, motor coils, radio stuff:

$$V = L\frac{dI}{dt}$$

<figure>
<img src="/images/memes/meme-ee-capacitor.jpg" alt="They don't know meme about explaining capacitors">
<figcaption>Me explaining capacitors. Also me, reading it back a week later.</figcaption>
</figure>

Memorize this table, it passes exams and builds intuition at the same time:

| Part | Stores | Blocks | Passes | Water version |
|---|---|---|---|---|
| Resistor | nothing, wastes it as heat | nothing | everything | narrow pipe |
| Capacitor | charge in a field | DC | AC | rubber bucket |
| Inductor | energy in a field | AC | DC | heavy wheel |

Put a capacitor and an inductor together and you get an oscillator, the thing that picks one frequency and ignores the rest. That is how a radio tuner works. Frequency it likes:

$$f_0 = \frac{1}{2\pi\sqrt{LC}}$$

## Kirchhoff: two rules, no new physics

Kirchhoff did not add any physics. He just wrote down two things that were already true, and together they let you solve any circuit.

Current rule: at any junction, current in equals current out. Water cannot appear at a T-junction:

$$\sum I_{in} = \sum I_{out}$$

So if \(2\,\text{A}\) comes in, you can split it as \(0.5\) and \(1.5\), or \(1\) and \(1\), or whatever. It has to balance, and that balance is your equation.

Voltage rule: walk any closed loop and you finish at the same height you started:

$$\sum V_{loop} = 0$$

Battery \(+9\,\text{V}\), two resistors dropping \(4\,\text{V}\) and \(5\,\text{V}\):

$$+9 - 4 - 5 = 0$$

That is it. Label your currents, walk the loops, write the sums, solve. Every circuit analysis I have done is this procedure with different numbers, which is honestly a relief after software where nothing is guaranteed.

```python
# sanity check before I trust a circuit I drew
battery = 9.0
drops = [4.0, 5.0]
assert abs(battery - sum(drops)) < 1e-9, "loop does not balance, redraw it"
print("balances:", sum(drops), "V")
```

## Digital is analog pretending

This is the bit that made EE click for me as a programmer. Your 1s and 0s are voltages. That is literally all they are.

\(0\,\text{V}\) means 0. \(5\,\text{V}\) means 1. Below some threshold it counts as 0, above it counts as 1, and in the middle the hardware cannot promise you anything:

| Level | 5V logic | 3.3V logic |
|---|---|---|
| Counts as 0 | \(0\) to \(0.8\,\text{V}\) | \(0\) to \(0.8\,\text{V}\) |
| Garbage zone | \(0.8\) to \(2.0\,\text{V}\) | \(0.8\) to \(2.0\,\text{V}\) |
| Counts as 1 | \(2.0\) to \(5.0\,\text{V}\) | \(2.0\) to \(3.3\,\text{V}\) |

A transistor is a switch that a voltage controls. Billions of them, switching billions of times a second, is a logic gate. Gates make adders, adders make memory, memory and gates make a CPU. Then someone writes JavaScript on top of that and complains about it, which is where I come in.

```c
// what I type:
if (x) { led_on(); }

// what the silicon is doing:
//   x above ~2V  -> HIGH -> transistor conducts -> LED lights
//   x below ~0.8V -> LOW  -> transistor blocks  -> LED dark
//   x in between  -> undefined, and the datasheet warned you
```

<figure>
<img src="/images/memes/meme-ee-digital.jpg" alt="Megamind meme about ones and zeros being voltages">
<figcaption>My ones and zeros were always voltages.</figcaption>
</figure>

So every `if` you have ever written is a few billion switches opening and closing pipes. Software is plumbing with extra steps.

## The Malaysian corner

Our wall is \(240\,\text{V}\) at \(50\,\text{Hz}\). Double America's voltage, so our shocks are worse and our kettles are faster. Fair trade, arguable.

And respect TNB infrastructure, please. People die every year trying to steal copper or trimming trees near lines. \(240\,\text{V}\) is already enough to stop a heart, and those substations and \(33\,\text{kV}\) feeders are not survivable. If a homelab project ever needs mains wiring, get someone certified. Arduino at \(5\,\text{V}\), play all you want. Wall socket, call an electrician.

## The one sentence version

Voltage pushes, current flows, resistance fights, and every gadget you own is clever plumbing that turns wall lightning into math.

> "With great power comes great current times voltage.", Uncle Ben, almost certainly an electrical engineer. Respect the watts.