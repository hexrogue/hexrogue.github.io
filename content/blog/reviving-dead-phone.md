---
date: '2026-08-19T00:00:00+08:00'
title: 'Reviving a Dead Phone'
description: 'An abandoned Android, an unlocked bootloader, and a custom ROM. E-waste versus an evening of fastboot.'
tags: ['android', 'rooting']
---

My old phone stopped getting updates two years ago. Still good hardware, perfect for a home dashboard or a test device, except the stock ROM got slower with every year and the battery stats blamed everything except itself. So I unlocked the bootloader and gave it a second life.

## Unlocking is the easy scary part

Every vendor hides the unlock in a different menu and warns you like you are defusing something. Back up first, obviously, because unlocking wipes the device. Enable OEM unlocking, boot into fastboot, run the unlock command, confirm on the tiny volume-key menu while questioning your choices. The phone wipes itself and reboots like nothing happened, except now it trusts whatever you flash.

<figure>
<img src="/images/memes/meme-phone.png" alt="This is fine meme about unlocking">
<figcaption>Everything is fine (after the wipe).</figcaption>
</figure>

Root came after, via a patched boot image. No custom recovery needed for the first step, just the stock firmware, a patcher app, and fastboot flash. The moment the root checker app said yes, the phone felt like mine in a way it never had. That meant full backups, system-wide ad blocking, and CPU profiles, while the telemetry the vendor shipped went in the bin.

## What unlocking actually unlocks

Your phone boots through a chain of trust. Each stage checks the signature of the next, like a bouncer checking IDs down a line. A locked bootloader only lets signed code from the manufacturer through the door. Unlocking tells the first bouncer to stop checking IDs. After that, any code can run: root patches, custom recoveries, whole new operating systems.

That is also why unlocking wipes your data. An unlocked phone with your old data on it would be a gift to any thief with a USB cable. The wipe is not punishment. It is the one honest part of the deal.

> "IT'S ALIVE!", Frankenstein (1931). Me, watching a two year abandoned phone boot a fresh ROM in half the time. Same energy.

## Then the custom ROM

Stock firmware rooted is nice. A clean custom ROM is nicer. I flashed one maintained for this model, plus the minimal Google apps package, and the phone woke up. Same chip, same battery, but everything responded faster and standby drain dropped by half. Two years of cruft gone in one flash.

The risk is real and worth naming. A wrong image for your exact model can brick the device, and SafetyNet-style checks mean banking apps may complain forever. This phone holds no banking apps. It holds a dashboard and my experiments. Know what the device is for before you start.

## Why bother

Because it works. A device headed for a drawer now runs my home dashboard 24/7, sipping power. And because the skills transfer: partitions, boot chains, images, backups. Phones are just small computers with trust issues. Once you have flashed one, every embedded device looks a little less mysterious.
