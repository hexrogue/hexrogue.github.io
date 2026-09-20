---
date: '2026-02-18T00:00:00+08:00'
title: 'Reverse Engineering Tips for Beginners'
description: 'What I wish someone told me before my first binary: strings first, rename everything, debugger early.'
tags: ['reversing', 'tips', 'security']
---

People hear reverse engineering and picture hooded geniuses. The reality is calmer. It is reading, renaming, and testing guesses. The workflow that works:

## Tip one: run strings before anything else

The `strings` command prints every readable piece of text inside a binary. Error messages, URLs, passwords someone forgot to hide. Half of beginner challenges fall over right here, because the answer was sitting in plain text. Thirty seconds of work. Always start here.

<figure>
<img src="/images/memes/meme-reversing.png" alt="Philosoraptor meme about obfuscation">
<figcaption>The raptor asks the hard questions.</figcaption>
</figure>

## Tip two: rename everything you understand

Open the binary in Ghidra and you will drown in names like FUN_00101060. Fight back by renaming. Every variable you figure out gets a real name. Every function you understand gets a real name. You are rebuilding the author's intent one label at a time, and after an hour the code starts reading like code instead of static. This single habit separates people who finish from people who stare.

## Tip three: the debugger settles arguments

Static analysis is your theory. The debugger is the experiment. When Ghidra suggests what a function does, set a breakpoint in GDB, run it, and watch the actual values. Registers are just the CPU's pockets, and peeking inside them ends every debate about what the code means. Theory proposes, the debugger disposes.

## Tip four: learn one tool deeply, not five shallowly

Ghidra, radare2, GDB, Binary Ninja, Frida. The list tempts you to collect tools instead of skills. Pick Ghidra plus GDB and stay there until you are dangerous. New tools later, depth first.

## Tip five: keep a lab notebook

Write down everything. Every guess, every breakpoint address, every renamed function and why. Reversing sessions span days, and day three you will not remember what day one you proved. My notebook for one crackme had forty lines and saved me from re-solving the same function twice. Professionals document. Amateurs rely on memory and re-do work. The notebook is the difference, and it costs nothing.

<figure>
<img src="/images/memes/meme-knuckles.png" alt="Knuckles meme about entry points">
<figcaption>Do you know de wey into main.</figcaption>
</figure>

## Tip six: only touch binaries you are allowed to touch

Crackmes, CTF challenges, your own programs. Never someone else's software without permission. The skills are identical either way, but one path builds a portfolio and the other builds a record. Choose the portfolio.

> "Do not try to understand it. Feel it.", Tenet (2020). Terrible reversing advice. Understand it, then feel smug. In that order.

## The pattern

Strings for the easy wins, renaming for comprehension, the debugger for truth, one tool at a time, and stay legal. Do that loop on ten binaries and you will not be a beginner anymore.
