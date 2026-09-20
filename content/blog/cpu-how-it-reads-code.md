---
date: '2026-09-09T00:00:00+08:00'
title: 'How Your CPU Reads Code'
description: 'Study notes, plain version: fetch, decode, execute, repeat billions of times. Plus why binary.'
tags: ['study', 'cpu']
---

Computer organization sounded dry until week two, when I realized it answers the best question in computing: how do words I type become electricity doing math. My notebook version, short:

## Everything is switches

A CPU understands exactly two things: on and off. Every photo, song, and game is patterns of ons and offs, ones and zeros. Eight of them make a byte, enough for one character. Billions of them make everything else. It feels absurd until you realize all of human language is also just patterns of a few dozen sounds. Same trick, different medium.

<figure>
<img src="/images/memes/meme-cpu.png" alt="Stonks meme about CPU cycles">
<figcaption>Fetch, decode, execute, stonks.</figcaption>
</figure>

## The CPU does three things, forever

Fetch, decode, execute. Grab the next instruction from memory. Figure out what it means. Do it. Then the next one, billions of times per second. Your 3 GHz processor does this dance three billion times a second, and every app you have ever used is just a very long choreography of these three steps.

Registers are the CPU's pockets: a handful of super fast slots where the current numbers sit. RAM is the desk: bigger, slower, holds what you are working on. Storage is the filing cabinet across the room. The whole field of performance is, roughly, keeping the pockets full and avoiding trips to the cabinet.

## Interrupts: the CPU's doorbell

The CPU cannot just run its loop in peace, because hardware needs attention. Your keyboard pressed a key. A packet arrived. The disk finished reading. Each event rings a doorbell called an interrupt: the CPU pauses its current instruction, handles the urgent thing, and resumes like nothing happened. Thousands of doorbells per second, and your music never skips.

Without interrupts, the CPU would have to constantly ask every device "anything new," like refreshing an inbox forever. The doorbell inverts the relationship. Devices call the CPU instead. That one inversion is why modern computers feel instant instead of sleepy.

## Why this helps a programmer

Knowing the dance changes how you write. Loops cost fetches. Jumping around memory costs trips to the cabinet. Data sitting neatly together runs faster than data scattered everywhere, for physical reasons, not stylistic ones. My reversing hobby got easier too: assembly stopped looking like runes and started looking like the fetch decode execute loop with the mask off.

> "It is alive!", close enough to what I said when my mental model of a CPU finally booted. Frankenstein energy, semester edition.

## The one sentence version

Your code becomes numbers, the CPU fetches each number, figures it out, does it, and repeats until your program ends. Everything else in the course is details. Useful, examinable details, but details.
