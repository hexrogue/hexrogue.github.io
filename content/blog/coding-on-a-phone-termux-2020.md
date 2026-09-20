---
date: '2026-09-20T00:00:00+08:00'
title: 'I Learned to Code on a Phone'
description: '2020, no laptop, just nano and Termux. How a phone keyboard taught me Python, scraping, and security.'
tags: ['story', 'termux', 'python']
---

In 2020 I had no laptop. What I had was an Android phone, a charger that only worked at one angle, and a lot of free time. Everyone said you need a real computer to learn programming. My phone had other plans. This is the story of nano, Termux, and the year I coded with my thumbs.

## A Linux terminal hiding in the Play Store

It started with one app: Termux. Imagine someone smuggled a tiny Linux computer inside your phone. A terminal that works, packages that install, Python that runs. I typed `pkg install python` on a bus and nearly dropped the phone when it worked. A full programming language, installed like a game, running on a device that also received my mom's calls.

The editor was nano, because nano is the only editor that tells you the controls at the bottom of the screen. Ctrl+X to exit, and yes, on a phone keyboard that means summoning the special keys row, holding CTRL like a claw, and praying.

My first programs were written at 2 AM with the screen brightness at minimum so nobody knew I was awake. Every programmer has an origin story. Mine has a low battery warning in it.

## My first project that mattered: a scraper with a grudge

I wanted scholarship announcements from three different websites, and checking them daily felt like a job for a robot. So I built one. Python plus the requests library: download the page, hunt for keywords, print what is new. Twenty lines. It worked on the third try, and I stared at the output the way people stare at newborns.

Then I got ambitious, the way beginners do right before learning about rate limits. I pointed it at bigger targets, added loops, and watched my phone heat up like a tiny stove. One site blocked me within an hour.

That block taught me more than any tutorial: send requests like a polite guest, not a battering ram. Headers that identify you, delays between hits, respect for robots.txt. Scraping is easy. Scraping without being a menace takes manners.

<figure>
<img src="/images/memes/meme-mordor.png" alt="Boromir meme about running Nuclei on a phone">
<figcaption>Boromir, warning me about my own plans.</figcaption>
</figure>

## Then I found the security rabbit hole

Scraping teaches you how websites are built. Security starts the day you wonder how they break. Someone mentioned Nuclei, a scanner that checks websites for known weaknesses using crowd sourced templates. I installed it in Termux half expecting the phone to refuse. It ran. Slowly, heating the room, but it ran.

What kept me up was learning to read findings instead of collecting them. One evening I traced one by hand on my own test project and finally saw it: how a reflected input becomes a script running in someone else's browser. An abstract warning turned into a concrete mechanism in my head. That click is the whole drug of security work. I chased it into CTFs and never came back.

And yes, everything stayed legal. Test targets, my own code, and later a school club site whose admin had said yes in writing. The skills do not care where you aim them. The law does. Aim carefully.

## What a phone keyboard teaches that laptops do not

Typing code with thumbs is miserable, and misery is a great teacher. Every character cost effort, so I learned to write less code that does more. I read documentation fully instead of skimming because switching apps was painful.

I planned programs in my head on walks because the phone was charging. Constraints I cursed at the time became habits I still use on a proper machine: think first, type second, keep it short.

> "Your focus determines your reality," Qui-Gon Jinn, Star Wars (1999). Mine was a 6 inch screen and it determined everything.

## The night the screen stayed black

Eight months in, my entire life lived in that phone. Every script, every note, every scraper. All of it in Termux, none of it pushed anywhere, because backups were something other people needed. Then one night the screen went black mid charge and stayed black. Button combos did nothing. The charger angle trick did nothing. An hour of nothing.

I sat on the floor doing math I did not want to do. Eight months of work. No laptop to recover from. No cloud copies because mobile data cost real money and I had been cheap. I had backed up nothing, and the universe had noticed.

Twenty minutes later, on the fifth charger and the third cable, the battery icon blinked on. Zero percent. It was never dead. It was just empty, too empty to even show the charging screen, and my panic had spent an hour troubleshooting a phone that needed twenty minutes of wall time.

I charged it in silence, booted up shaking, and typed my first ever git commands that night: init, add, commit, push. Eight months of code went to a remote in eleven minutes.

<figure>
<img src="/images/memes/meme-patrick.png" alt="Patrick meme about pushing code">
<figcaption>No backups. Push it somewhere else.</figcaption>
</figure>

I back up everything now. Borg on a schedule, dotfiles in git, paranoia as policy. People call it discipline. It is just the memory of a black screen.

You do not need the gear. You need the reps. The phone I learned on could barely hold a charge, and it still out-taught every course I have taken since, because it was always in my pocket and excuses were not.

## The laptop summer of 2022

By 2022 I had outgrown the phone the way you outgrow shoes. It still worked fine. My ambitions just stopped fitting on it: bigger projects, longer sessions, tools that wanted real keyboards. So I worked, saved every spare ringgit for months, and bought my first laptop with my own money. No box has ever felt heavier on the walk home.

The first boot was almost disappointing. A real keyboard, a screen that fits more than forty columns, a battery that outlives lunch. Within a week the phone retired to test device duty, running my scrapers headless in a corner like an old soldier reassigned to guard duty. I still keep it around. It earned the shelf.

It came with Windows, of course. I gave it two months. Two months of updates rebooting my machine mid thought, of settings that reset themselves, of feeling like a guest in a computer I owned. I hated every week of it.

<figure>
<img src="/images/memes/meme-kermit.png" alt="Kermit meme about Windows updates">
<figcaption>Windows reboots mid thought. None of my business now.</figcaption>
</figure> So I wiped the whole thing and installed Linux. Not Mint, not Ubuntu. Arch, straight, no training wheels. Everyone said start easy. I heard them and did it anyway.

<figure>
<img src="/images/memes/meme-interesting.png" alt="Interesting man meme about Arch">
<figcaption>I dont always install Arch. But when I do, I skip Ubuntu.</figcaption>
</figure>

Guess what. It did not boot. For three days it did not boot. I installed it again. It did not boot. I installed it again, slower, reading every line. Three days of install, fail, read, repeat.

No AI to ask, just the wiki, random blogs, and YouTube videos at double speed. Each failure taught one thing: this error means the bootloader entry is wrong, that one means I forgot the microcode, the other means I mounted boot after generating the config instead of before.

On day three it booted. I sat there staring at a black screen with white text like it was a sunrise.

<figure>
<img src="/images/memes/meme-gandalf.png" alt="Gandalf meme about failed boots">
<figcaption>Three days of installs. You shall not boot.</figcaption>
</figure> Then I did what any sane person would do: I wiped it and installed again, to prove the first time was skill and not luck.

By the fifth install I could do it from memory. People ask how I learned Arch. Reps. Failed reps, over and over, until the failures stopped.

What surprised me: the laptop did not make me better. It made me faster at being the person the phone years built. The habits transferred whole: plan before typing, read the docs, back up everything, suspect every input. Tools upgrade in a day. Instincts take years. Mine were forged on a cracked screen at minimum brightness, and no amount of RAM changes that.

Start where you are. Use what you have. The terminal fits in your pocket now. It always did.
