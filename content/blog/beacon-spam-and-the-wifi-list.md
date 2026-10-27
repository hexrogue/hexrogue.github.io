---
date: '2026-05-12T09:05:00+08:00'
title: 'Beacon spam: how the air fills with junk network names'
description: 'A beacon is a router shouting its name ten times a second. Copy that frame at scale and you get thirty fake networks, a confused phone, and zero broken encryption.'
tags: ['wifi', 'security', 'explainer']
author: nuh
---

[A beacon](/blog/80211-frames-you-can-read/) is the simplest frame in wifi. A router announces its name about ten times a second, on its channel, to nobody in particular. It is unsigned, it is unencrypted, and any radio can transmit one.

Your phone treats that announcement like a guest list. No bouncer, no ID check, no guy named Chad at the door asking if you are on the list. Anyone with a radio can add a name. Copy that frame at scale and you have beacon spam.

A beacon is also the chimichanga of wifi frames: simple, deep-fried, and impossible to take seriously until someone shows up with three thousand of them.

## What it is

Beacon spam, also called SSID flooding, is transmitting fabricated beacons with invented names, usually thousands of them, across every channel. Each one becomes an entry in every phone's wifi list in range. Nothing has to associate or connect, and no victim is required. Just announcements, at volume.

The reason it works is that a beacon is not authenticated. There is no signature to check and no key to check it against, because a station has to be able to hear a network before it has any keys. Scanning is passive, and passive frames are gullible by design. The same property that lets any device see any network lets any device invent one.

## What it actually achieves

<figure>
<img src="/images/diagrams/beacon-spam-list.svg" alt="A phone wifi list full of joke network names with one real network">
<figcaption>One real radio, one real network, and a list that no longer means anything.</figcaption>
</figure>

Beacon spam breaks no encryption and gives no access. What it does is mess with the list:

- Your wifi menu becomes unusable. Thirty entries with joke names crowd out the two you actually use.
- A device that auto-joins by name can be handed a wrong network. If one spam name matches a network the device remembers, and the spam fake is open while the real one is not, an auto-joining device has a decision to make. That is the serious edge of a fairly silly attack.
- The phone burns battery, because scanning is not free and sorting a fake list is not free either.

The famous payoff is comedy: `FBI Surveillance Van`, `Virus.exe`, `GetYourOwnWifi`, `Pretty Fly for a Wifi`. Somebody makes one, then everybody makes one, and now the whole neighbourhood's list is a gag.

## The part nobody labels

At high enough volume, a beacon flood stops being a joke and becomes a denial of service on the air. The same is true of the rest of the 802.11 flood family: authentication flood, association flood, probe flood. The frame is trivial; the rate is the weapon. A phone trying to sort thousands of fake networks spends its radio time on the sorting and not on the network it was actually using.

Intent is where the line sits. On your own device, for twenty seconds, it is a demonstration of why beacons are not authenticated. Across a neighbourhood it is interference, and in most places that is against the same rules as jamming. My board runs it behind a deliberately lab-only command, and it stays pointed at my own phone.

## Catching it

You already have the tool. Beacon spam is loud in a sniffer: watch the count of unique BSSIDs, and if it jumps from a dozen to hundreds in a few seconds, that is not your neighbours redecorating. The tells are addresses that do nothing else. A real access point sends beacons and answers probes and carries data. A spam entry beacons and has no other life at all.

A detector worth having is a baseline: unique BSSIDs per minute, on your own air, for a quiet day. Then any spike explains itself.

<figure>
<img src="/images/memes/meme-beacon-spam-brain.jpg" alt="Expanding brain meme about one fake SSID, thirty fake SSIDs, the same SSID on every channel, FBI Surveillance Van">
<figcaption>At no point does the phone ask whether the network is real. It only asks which one is strongest.</figcaption>
</figure>

Some people want to watch the wifi list burn. I just want to know how long the fake names stay in the phone's memory before it gives up. That is a less dramatic goal, but it fits in a blog post.

## Try this

Run your own beacon spam for twenty seconds, pointed at your own phone, and watch the list. Then stop it and watch how long the entries linger before they age out. That timer is the thing worth measuring: it tells you how long a fake network stays in your device's memory after it stops existing, which is longer than most people expect.

For what a single beacon contains, the annotated one is in [802.11 frames you can read](/blog/80211-frames-you-can-read/). For where a fake name leads, it is [the evil twin post](/blog/watching-your-own-air-rogue-aps/).
