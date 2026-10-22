---
date: '2026-03-06T20:15:00+08:00'
title: 'Deauth: the 26 bytes anyone can forge'
description: 'Why deauthentication frames work: unsigned, unauthenticated, and trusted anyway. What they achieve, and the one upgrade that ends them.'
tags: ['wifi', 'security', 'explainer']
author: nuh
---

A deauth frame is a wifi eviction notice. It says one thing: you are no longer associated with this network. Twenty-six bytes that prove nothing about who sent them.

That missing proof is the entire story. It is the bureaucratic version of a bouncer throwing you out and then handing you a form that says "we have no idea who did this."

## The frame

```
c0 00             <- frame control: management frame, subtype 12 (deauth)
3a 01             <- duration, filler, ignored
ff:ff:ff:ff:ff:ff <- address 1: the target. broadcast means everyone listening
02:11:22:33:44:55 <- address 2: who sent it (supposed to be the access point)
02:11:22:33:44:55 <- address 3: which network this concerns
f0 ff             <- sequence number
02 00             <- reason code 2: previous authentication no longer valid
```

<figure>
<img src="/images/diagrams/deauth-frame-layout.svg" alt="Byte by byte layout of the 26 byte deauthentication frame">
<figcaption>The whole 26 bytes, laid out. Six of them hold the sender's address, and none of them are proof that the sender is who they claim.</figcaption>
</figure>

The first byte pair `c0 00` is the giveaway. The top bits of `0xc0` say management frame, the rest say subtype 12. Disassociation is the sibling, subtype 10, byte `a0`. Over the air the two look nearly identical and are used the same way.

Read the addresses again. Address 2 is the sender, and it is just a field. Any radio that can talk on the channel can put a router's address there, or a random one, or a client's own address to make the client deauth itself. Nothing in the frame is checked against a key or a counter. If you can transmit, you can forge.

## Broadcast looks scary and mostly is not

Address 1 as `ff:ff:ff:ff:ff:ff` means the frame is addressed to everyone. Beginners assume that is the powerful option. It is the weak one. Most wifi clients quietly ignore a deauth that is not addressed to their own MAC, because why would a station act on a notice meant for somebody else.

A real eviction needs the victim's unicast address, which is not secret. It appears in every frame that station ever sends. Address 1 is readable off the air a second after the client connects.

## What a deauth actually does

One deauth drops one association. The client, having lost its link, usually rescans and rejoins within a second or two. A single forged frame is a hiccup.

Repeat it, continuously, and the client cannot stay connected. That is a denial of service, nothing more and nothing less. It does not reveal the password. It does not let you join the network. It does not touch the encryption. Anyone who tells you a deauth attack cracks wifi is selling something.

That gap between scary and useful is why the frame is interesting to study rather than to use on anyone.

## Why the frame exists at all

Access points need to evict people. The admin changes the password. The AP reboots. A client has gone quiet. So the standard includes a notice, and in 1997 the committee defined it without any way to prove the sender is the AP.

Wifi security spent the next twenty years adding layers on top of that frame instead of fixing it, because fixing it breaks old hardware. That is why the standard's name for the fix is not "remove deauth". It is announce that your AP will sign these frames, and hope your devices listen.

## The fix that finally landed

The fix is management frame protection, 802.11w, usually called PMF. It adds a message integrity check to management frames, so a deauth without the right key is discarded by the client.

WPA3 requires PMF. WPA2 supports it and almost never turns it on, because turning it on can boot old devices off the network. So in 2026 you find a wide split: modern phones with modern routers shrug off forged deauths, while a huge tail of access points, cheap IoT gear, and anything a landlord installed in 2015 still eats them whole.

If you want a one-line reason why a wifi attack that "stopped working in 2019" still works on half the street, PMF is the whole answer.

<figure>
<img src="/images/memes/meme-deauth-this-is-fine.jpg" alt="This is fine dog meme: any radio can send a deauth with your router's name on it, says your laptop">
<figcaption>It signs nothing, and the station obeys it anyway.</figcaption>
</figure>

## Catching one in the act

Deauths are also the easiest attack in wifi to notice, because the frame that does the damage is the same frame that announces it. A sniffer counts them. One deauth is the network doing housekeeping. A burst is a person.

The number I use in my own detector is ten or more deauths in one second from one source, which I borrowed from the Hydra project. It is folklore, not a standard. It catches a flood and mostly ignores normal churn, which is all a threshold has to do. The stronger tell is the source: deauths from a BSSID that is not the real AP, or from a client address at all, mean somebody is lying.

Everything the detector reads is in the clear, because management frames are unencrypted. The attack is loud and the defence is public.

> "The only winning move is not to play.", WarGames (1983). The AP could have signed this frame in 2009. Instead, decades of gear still believes random strangers.

## The lab only rule

Kicking devices off a network you do not own is a denial of service, and it is illegal almost everywhere you point it. The whole series runs on one rule, written down once at [the lab rules](/lab-rules/): your own gear, or equipment you have written permission to test. Everything interesting about this work is still legal on that footing.

The version that teaches you something is attacking yourself and watching your own detector catch it. You learn the frame twice, once as the hand that forges it and once as the code that catches the forgery. My ESP32 does both, and I wrote up the fight it took to make the chip transmit the thing at all over in [the driver that said no](/blog/esp32-recon-rig-driver-said-no/).

## Try this

Sniff your own network for a minute and count the deauths. If the count is zero or a handful, that is your baseline, and you now know what a quiet network looks like. Then attack your own access point with your own hardware and watch the counter jump.

If you want the frames underneath this, start with [the envelope every wifi packet shares](/blog/80211-frames-you-can-read/).
