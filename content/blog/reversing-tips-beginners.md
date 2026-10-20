---
date: '2023-01-19T00:00:00+08:00'
title: 'Everything in My First Binary Was Named FUN_00101060'
description: 'What I wish someone told me before my first binary: strings first, rename everything, debugger early.'
tags: ['reversing', 'tips', 'security']
author: nuh
---

The first binary I opened looked like a city with no street signs. Ghidra handed me a map full of FUN_00101060 and expected me to navigate. I did what every beginner does: stared at it, changed nothing, and closed the laptop.

A few binaries later, I have a loop that works.

<figure>
<img src="/images/diagrams/reversing-workflow.svg" alt="Diagram of the reversing loop: run strings, rename what you understand, then let the debugger settle it">
<figcaption>Strings, rename, debugger, then back around for another pass.</figcaption>
</figure>

## Start with strings, because binaries are bad at keeping secrets

The `strings` command prints every readable piece of text inside a binary. Error messages, URLs, passwords someone forgot to hide. Half of beginner challenges fall over right here because the answer was sitting in plain text. Thirty seconds of work. Do this before anything clever.

<figure>
<img src="/images/memes/meme-reversing.png" alt="Philosoraptor meme about obfuscation">
<figcaption>The raptor asks the hard questions.</figcaption>
</figure>

## Rename everything until the code confesses

Open the binary in Ghidra and you will drown in names like FUN_00101060. Fight back by renaming. Every variable you figure out gets a real name. Every function you understand gets a real name. You are rebuilding the author's intent one label at a time, and after an hour the code starts reading like code instead of static. This habit separates people who finish from people who stare.

## Let the debugger settle the argument

Static analysis is your theory. The debugger is the experiment. When Ghidra suggests what a function does, set a breakpoint in GDB, run it, and watch the actual values. Registers are the CPU's pockets, and peeking inside them ends every debate about what the code means. Theory proposes, the debugger disposes.

## Pick one tool and get dangerous

Ghidra, radare2, GDB, Binary Ninja, Frida. The list tempts you to collect tools instead of skills. Pick Ghidra plus GDB and stay there until you are dangerous. New tools later. Depth first.

## Keep a notebook, because day three you will forget day one

Write down everything. Every guess, every breakpoint address, every renamed function and why. Reversing sessions span days, and day three you will not remember what day one you proved. My notebook for one crackme had forty lines and saved me from re-solving the same function twice. Professionals document. Amateurs rely on memory and redo work. The notebook costs nothing.

<figure>
<img src="/images/memes/meme-knuckles.png" alt="Knuckles meme about entry points">
<figcaption>Do you know de wey into main.</figcaption>
</figure>

## Stay legal

Crackmes, CTF challenges, your own programs. Never someone else's software without permission. The skills are identical either way. One path builds a portfolio, the other builds a record. Choose the portfolio.

> "Do not try to understand it. Feel it.", Tenet (2020). Terrible reversing advice. Understand it, then feel smug. In that order.

## The loop

Strings for the easy wins, renaming for comprehension, the debugger for truth, one tool at a time, and stay legal. Do that on ten binaries and you will not be a beginner anymore.

The binary is patient. You can outlast it.
