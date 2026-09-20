---
date: '2026-07-27T00:00:00+08:00'
title: 'Arch Broke, and I Am Glad'
description: 'A routine update ate my bootloader entry. Fixing it from a TTY taught me more than the install ever did.'
tags: ['arch', 'linux']
---

Yes, Arch is my daily driver. No, I will not shut up about it. But this is not a conversion post. This is about the Tuesday an update left me staring at a boot menu with no Arch in it, and why I am glad it happened.

## The update that removed my OS (from the menu)

Pacman did its thing, I rebooted, and the bootloader offered me exactly one option: the fallback that also did not work. My root partition was fine. My kernel was fine. The boot entry was just gone. Somewhere between the kernel package and my EFI partition, a path disagreed with another path.

Old me would have reinstalled. Current me made coffee and chrooted in from a USB stick, because Arch forces you to keep one around like a fire extinguisher. Mount root, mount boot, arch-chroot, reinstall the kernel, regenerate the bootloader config, reboot. Twenty minutes, most of it typing mount commands very carefully while double checking device names. lsblk is the most re-read output in my life.

<figure>
<img src="/images/memes/meme-facepalm.png" alt="Picard facepalm meme">
<figcaption>Mounted boot after generating the config. Classic.</figcaption>
</figure>

<figure>
<img src="/images/dirt-road.jpg" alt="The road to recovery">
<figcaption>The road to recovery. Paved with mount commands.</figcaption>
</figure>

## What a bootloader entry even is

When your computer wakes up, it is briefly very stupid. It knows how to read one small partition and run one small program, the bootloader. That program shows you a menu and then hands control to your actual system. A bootloader entry is one line on that menu: which disk, which kernel, which options.

My entry vanished, so the menu had nothing to hand control to. The system was intact behind a door with no handle. Reinstalling the kernel and regenerating the config carved a new handle. That is the entire rescue, and once you see it, boot problems stop being scary and start being a checklist: entry, kernel, disk, in that order.

> "Your scientists were so preoccupied with whether or not they could, they didn't stop to think if they should.", Jurassic Park (1993). Me, installing Arch: yes. Me, fixing it at midnight: also yes.

## What daily driving Arch actually teaches

People think Arch teaches you Linux. It teaches you recovery. Installing is a tutorial. Maintaining is the course. You learn to read pacman output before pressing Y, to check the news feed when something core updates, to keep LTS kernels around like spare tires. I run linux-lts alongside main now. Boring insurance, and the best decision I made.

Dotfiles are the other lesson. My Neovim and Tmux configs live in git, so a fresh install feels like home in an hour. The first time I set up Arch it took a weekend. The last time it took a lunch break plus font downloads.

The filesystem is btrfs with zstd compression, which quietly saves gigabytes on a system full of text and containers. Snapshots before every risky update, because I have learned. Backups go through borg to the homelab, and anything big coming down comes through aria2c. Moving things between machines is rsync, same as it has been for decades. Boring tools, all of them, and every one earned its place by surviving something.

## The honest tradeoff

Arch breaks a couple of times a year and always tells you why if you read. Ubuntu never broke on me and never taught me anything either. I will take the breakage. My servers run the boring distros. My laptop runs the one that keeps me sharp.

If you are curious, install it in a VM first. Break it there. Fix it there. Then decide if you want that relationship full time. I did, and apart from one Tuesday, no regrets.
