---
date: '2026-09-17T00:00:00+08:00'
title: 'OOP Clicked When I Stopped Memorizing'
description: 'Study notes, plain version: classes are cookie cutters, objects are cookies, and the four pillars in one paragraph each.'
tags: ['study', 'oop']
---

Object oriented programming confused me exactly as long as I tried to memorize definitions. Encapsulation, inheritance, polymorphism. Words to chant before exams. Then someone explained it with a kitchen, and it clicked in a minute. Passing that on.

## Classes are cookie cutters, objects are cookies

A class is a blueprint. It describes what a thing has (data) and what it can do (methods), but it is not the thing. An object is one actual thing stamped from the blueprint. One User class, thousands of user objects. The cutter is not a cookie. Say it with me.

<figure>
<img src="/images/memes/meme-oop.png" alt="Y U NO meme about encapsulation">
<figcaption>Y U NO encapsulate.</figcaption>
</figure>

## The four pillars, one paragraph each

Encapsulation means hiding the messy insides. Your object exposes buttons and hides wiring. You drive a car with pedals, not by hugging the engine. When the wiring changes, everyone using the buttons stays happy.

Inheritance means making a specialized copy. A Student is a Person plus student stuff. You write the Person part once and reuse it instead of copying. Less copying, fewer bugs, and when Person gets fixed, Student inherits the fix.

Polymorphism means same button, different behavior. Every animal object gets a speak method. Dog barks, cat meows, the caller just presses speak. Your code handles ten animal types without a single if statement checking which is which.

Abstraction means showing only what matters. A map is not the terrain, it is the useful lie. Classes expose the ten percent you need and bury the ninety you do not.

## Interfaces: job descriptions

One more piece that unlocked everything. An interface is a job description with no worker attached. It says "anyone applying must be able to start, stop, and report status," without saying how. Your code then talks to the description instead of the person. Swap a real payment system for a fake test one, and nothing else changes, because both applied for the same job.

This is how big programs stay flexible. Depend on descriptions, not individuals. New hires welcome, as long as they can do the job. It is management advice disguised as code.

## The mistake that delayed my click

I kept asking what each pillar means in isolation. Wrong question. They only make sense together, in a real program, where hiding mess (encapsulation) lets you reuse shapes (inheritance) while swapping behaviors (polymorphism) through clean surfaces (abstraction). One sentence, all four, each earning its place. Memorize that sentence and the exam definitions write themselves.

> "Wax on, wax off.", The Karate Kid (1984). Me, writing getters and setters for weeks before understanding why. The drill was the lesson.

## The one sentence version

Model things as objects that hide their mess, reuse their parents, and respond to the same messages in their own way. That is OOP. The rest is syntax, and syntax is what documentation is for.
