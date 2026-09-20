---
date: '2026-04-28T00:00:00+08:00'
title: 'Arch Linux Tips: Survive and Enjoy'
description: 'Read the news before updating, keep an LTS kernel, and other habits that keep Arch boring.'
tags: ['arch', 'linux', 'tips']
---

Arch has a reputation for breaking. Mine breaks about twice a year, takes twenty minutes to fix, and teaches me something each time. The secret is not skill. It is habits, all of them boring.

## Tip one: read before you press Y

Pacman tells you exactly what it is about to do. Read it. Version jumps on kernels, drivers, and bootloaders deserve a glance at the Arch news feed first. Major changes get announced there with manual steps attached. Five minutes of reading prevents ninety percent of breakage. The updates can wait until after coffee.

## Tip two: keep an LTS kernel as a spare tire

Install `linux-lts` alongside your main kernel. If a new kernel dislikes your hardware, reboot, pick LTS from the boot menu, and keep working while you sort it out. Boring insurance. Best package on my system after Neovim.

<figure>
<img src="/images/memes/meme-arch.png" alt="Success kid meme about kernels">
<figcaption>Success Kid runs Arch.</figcaption>
</figure>

## Tip three: snapshot before risky updates

This is why I run btrfs. One snapshot command before a big update, and any disaster becomes a rollback instead of a rescue mission. zstd compression keeps it cheap on disk. The one time I skipped the snapshot is, obviously, the time I needed it. Never again.

## Tip four: dotfiles in git, always

Neovim config, shell config, Tmux config. All in a repo. A fresh install feels like home within an hour instead of a weekend of "wait, how did I set that up." Your future self, mid reinstall, sends thanks backwards through time.

## Tip five: update weekly, not monthly

Rolling release means updates flow constantly, and small frequent updates break less than giant monthly ones. A weekly update touches a few packages. A monthly update touches hundreds, and when something breaks you get to guess which of the hundreds did it. Ten minutes every weekend beats a rescue evening every quarter.

<figure>
<img src="/images/memes/meme-sparta.png" alt="Sparta meme about Arch">
<figcaption>This is Arch Linux.</figcaption>
</figure> Consistency is the entire maintenance strategy.

## Tip six: the wiki is the documentation

The Arch Wiki answers questions for every distro, not just Arch. Search it before forums, before videos, before AI. It is current, precise, and written by people who fixed the thing yesterday. When in doubt, wiki.

> "Do, or do not. There is no try.", Yoda (1980). Also valid pacman advice. Commit to the update or do not run it.

## The pattern

Read first, keep a spare kernel, snapshot everything, version your configs, trust the wiki. Do these and Arch stops being scary and starts being the distro that keeps you sharp. Breakage becomes tuition, and tuition this cheap is a bargain.
