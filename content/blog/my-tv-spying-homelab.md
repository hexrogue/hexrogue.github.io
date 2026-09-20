---
date: '2026-06-08T00:00:00+08:00'
title: 'My TV Was Spying on Me'
description: 'How a cheap OpenWrt router and Wireshark turned my living room into a surveillance audit.'
tags: ['homelab', 'networking', 'openwrt']
---

I bought a used router to flash OpenWrt on a bored Saturday. The plan was simple: better WiFi. Three weeks later I had VLANs, WireGuard back home, and a spreadsheet of every domain my TV talks to at 3 AM. This is how that happens. Nobody plans a homelab. It accretes.

## It started with one VLAN

The TV was the trigger. It wanted internet for Netflix and nothing else, but it knocked on telemetry endpoints all night. So it got its own VLAN with no access to the rest of the LAN, DNS forced through my filter, and inter-VLAN routing denied by default.

Fifteen minutes of firewall rules. The TV never noticed. My laptop stopped seeing its mDNS spam, which was the real quality of life win.

Then the IoT stuff followed it into exile. Cheap smart plugs with firmware from who knows where. They get internet and nothing else. My main network now holds exactly the machines I trust, which is a short list.

<figure>
<img src="/images/memes/meme-homelab-tv.png" alt="Drake meme about VLANs">
<figcaption>Drake explains network segmentation.</figcaption>
</figure>

## WireGuard changed how I leave the house

The second thing that stuck was WireGuard back into the home network. Coffee shop WiFi goes straight through an encrypted tunnel to my own router, and DNS resolves at home too, so ad blocking works everywhere. Setup took maybe twenty minutes, most of it staring at firewall zones wondering why the handshake succeeded but nothing routed. (It is always the firewall zone. It is always the zone.)

Reverse proxies came last. One entry point, subdomains per service, TLS handled once. Services that used to be port-forwarded roulette are now names behind auth.

## What is a VLAN, really

A VLAN is a imaginary wall inside one physical box. Picture an apartment building. Everyone shares the walls and the wiring, but your neighbor cannot walk into your living room. One router, several sealed networks. The TV lives in its apartment, my laptop lives in mine, and the router plays strict landlord: no visiting between units unless I sign a written exception.

Without that wall, every device can chat with every other device. Your lightbulb can knock on your laptop's door. Most of the time it just says hello a thousand times a day and wastes everyone's time. Sometimes it has a vulnerability from 2019 and says something worse. Walls are cheap. Use walls.

My TV, by the way, never stopped trying. Blocked tracking domains just pile up in the filter log like flies on a screen door:

```
 _________________
|  I'M WATCHING   |
|      YOU        |
|__             __|
   |  .---.    |
   |  |   |    |
   |___________|
```

> "Good morning, and in case I don't see ya: good afternoon, good evening, and good night!", The Truman Show (1998). My TV says this to its ad servers. I just stopped letting it call out.

## Wireshark is the microscope

Honestly the best purchase was nothing. Wireshark is free and it ended every argument I had with my own network. Slow evening speeds? Capture for a minute and watch the retransmits. Device acting weird? Filter by its MAC and read what it actually says instead of guessing. I learned more about TCP from one bad evening of packet loss than from any tutorial.

<figure>
<img src="/images/memes/meme-harold.png" alt="Harold meme about network pain">
<figcaption>TV phoned home again. Hides the pain.</figcaption>
</figure>

## The honest total

All it took was a used router and a Raspberry Pi, plus a weekend that got out of hand. The lab breaks regularly. That is the point. Every outage taught me something my production work later needed: subnets, DNS, tunnels, certs. If you are a dev who has never owned the network under your code, flash a router. You will come back different.
