---
date: '2026-06-25T00:00:00+08:00'
title: 'Dune Is About Single Points of Failure'
description: 'My hypothesis: the spice is just a metaphor for every system with exactly one load bearing part.'
tags: ['movies', 'dune', 'theory']
---

<figure>
<img src="/images/wheat-field.jpg" alt="A desert that is definitely Arrakis">
<figcaption>Arrakis, probably. (Not Arrakis.)</figcaption>
</figure>

Dune looks like a story about a chosen one. I think it is a story about infrastructure. Specifically: what happens when your entire civilization has exactly one load bearing component, and it only grows on one planet, guarded by giant worms. That is not worldbuilding. That is a risk assessment screaming for help.

## The spice is every database with no replica

Strip the mystique. The spice lets ships navigate, extends life, and powers an empire. One substance, one planet, zero backups. Every engineer reading this just felt their eye twitch, because we have a name for this: a single point of failure.

The whole plot of Dune is what happens when someone finally kicks that point. Paul does not conquer the galaxy with an army. He conquers it by standing next to the off switch.

<figure>
<img src="/images/memes/meme-dune-handshake.jpg" alt="Epic handshake meme about single points of failure">
<figcaption>Shake hands with your single point of failure.</figcaption>
</figure>

Companies do this constantly, minus the worms. One cloud region. One vendor. One guy who knows the deploy script. Dune just scales the mistake up to interstellar and adds sand.

## My hypothesis: the real hero is the Fremen redundancy

Everyone argues Paul versus Leto. Wrong debate. The Fremen are the only faction with backups for everything: distributed tribes instead of one capital, water discipline instead of assumed supply, desert survival instead of imported comfort. They are the civilization with replicas. Of course they inherit the planet. They are the only ones engineered to survive losing any single piece.

> "Fear is the mind killer.", Dune (1984 and 2021, twice the fear). Also what I whisper before major version upgrades.

## The worms are the firewall

Think about the sandworms for a second. They make spice harvesting dangerous, which limits supply, which keeps the price astronomical. In security terms, the desert is a really aggressive rate limiter. Nobody DDoSes the spice flow because the desert eats the bots.

But every firewall shares one flaw: it guards the perimeter, not the design. The Fremen do not fight the worms. They ride them. Every defense assumes the attacker plays by defender rules, and the winner is whoever stops assuming first. Paul wins by becoming the thing the desert cannot filter: a native process, running with full privileges, standing next to the off switch.

## He who controls the bottleneck controls everything

The famous line says it plainly. Power flows to whoever holds the narrowest part of the pipe. That is true of spice, of app stores, of search engines, of the one DNS provider half the internet shares. Dune is often called unfilmable and prophetic. I think it is just the clearest diagram ever drawn of what happens when nobody builds a second pipe.

Build the second pipe, and skip the worms if you can.
