---
date: '2026-05-14T00:00:00+08:00'
title: 'A Four-Evening Crackme'
description: 'Ghidra, GDB, and what a small binary reminded me after years of CTFs.'
tags: ['reversing', 'security', 'ghidra']
---

After years of CTFs, a tiny crackme that asks for a serial key should have been a one evening job. A friend sent it over and said it would take an hour. It took four. I regret nothing.

## Evening one: strings and false confidence

I ran strings on it and found the success message in plain text. I felt like a genius for about ten minutes. Then I opened it in Ghidra and the decompiler gave me a wall of FUN_00101060. Years of experience, same first reaction every time. My confidence filed for divorce.

What saved me was renaming things. Every variable I understood got a real name. Input became input. The comparison loop became check_loop. Ghidra lets you piece together what the original programmer meant, one renamed variable at a time. After an hour of that, the function started reading like actual code instead of alphabet soup.

<figure>
<img src="/images/memes/meme-crackme.png" alt="Morpheus meme about registers">
<figcaption>Morpheus, wiser than my first breakpoint.</figcaption>
</figure>

## Evening two and three: the debugger humbles you

Static analysis told me what the check probably was. GDB told me the truth. I set a breakpoint on the comparison, fed it a guess, and watched my input and the expected value sit side by side in registers. The algorithm was a simple transform on each character. I had stared at it in Ghidra for a night without seeing it, and in the debugger it took thirty seconds.

That is the lesson nobody told me upfront. Static analysis shows the map while the debugger shows the traffic, so you need both. radare2 got a look too, mostly so I could say I tried, but GDB plus Ghidra did the real work.

## What Ghidra actually does, in plain words

A compiled program is a machine talking to itself in numbers. Ghidra translates those numbers back into something shaped like code. Imagine finding a cake and wanting the recipe. The decompiler tastes the cake and guesses the recipe. It is often right about the ingredients and fuzzy about the order, which is why you rename things and test in the debugger until the guess becomes knowledge.

Registers, since you asked: they are the CPU's pockets. Tiny, fast, and very few. When the program compares your guess against the real key, both sit in pockets for one instruction, side by side. The debugger lets you peek into the pockets mid-thought. That is the whole trick. Everything else is patience.

> "There is no spoon.", The Matrix (1999). There is also no key check you cannot read, once you accept the binary is just text wearing a costume.

## Evening four: keygen in Python

Once the transform was clear I reimplemented it in Python, generated a valid key, and watched the binary print the success string. I may have said something out loud. My neighbors know nothing.

## Why I kept going

Reversing rewired how I write normal code. I think about what my binaries leak now. I strip symbols I used to leave in. I validate input like someone unfriendly is reading the disassembly, because someday someone might be.

If you build software and have never reversed any, grab a beginner crackme and a free weekend. Start with strings, rename everything, and set breakpoints early. You will come out paranoid in the useful direction.