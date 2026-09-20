---
date: '2026-07-10T00:00:00+08:00'
title: 'Teaching a Server to Answer Calls'
description: 'The WhatsAPI build story: from missed messages to a Go gateway that picks up the phone.'
tags: ['go', 'projects', 'voip']
---

<figure>
<img src="/images/coffee-beans.jpg" alt="Debugging fuel">
<figcaption>Debugging fuel. Consumed in large quantities during this project.</figcaption>
</figure>

My admissions CRM could text people automatically. Then the boss asked the obvious question: can it call them too? That question cost me a month and taught me more about real time systems than anything before it. This is that month.

## The gap between texting and talking

Texting through code is posting letters. Your program hands words to a server, the server delivers them whenever. Nothing has to be alive at the same time. I had that working in days.

Calling is a conversation, and conversations have rules letters do not. Both sides must be present. Words must arrive in order and on time. A half second delay turns dialogue into two monologues. So the gateway needed a permanent live wire to WhatsApp's servers instead of a mailbox: a WebSocket connection held open around the clock, with my code listening to every event that drips through it.

<figure>
<img src="/images/memes/meme-server-onering.jpg" alt="One does not simply meme about teaching a server to call">
<figcaption>One does not simply teach a server to pick up the phone.</figcaption>
</figure>

## Mapping the undocumented

The messaging side had examples. The calling side had rumors. Nobody wrote down which event means ringing, which means answered, which means the other side vanished into a tunnel. So I did the unglamorous thing: logged every raw event with timestamps and stared until patterns emerged.

There is a specific hour I remember, 2 AM, coffee number four, when the pattern clicked. Ringing looks like this event. Pickup looks like that one. Drop looks like a third. The protocol was never some encrypted mystery, just nobody's documentation priority. Most of engineering is like this: the answer exists, filed under nobody's job.

## Why this gateway runs on Go and Docker

Go hands every live connection its own lightweight worker. Calls, message streams, status pings: thousands of concurrent routines while the main program stays bored. That is the exact personality a gateway needs, because a missed event is a missed call, and missed calls are the product failing visibly.

Docker wraps it into one container that restarts itself when unhappy and logs everything always. The CRM talks to the gateway, the gateway talks to the wire, and follow-ups go out while everyone sleeps.

## What the month actually taught

Request based systems forgive you. Real time systems do not. Never block the event loop, never assume message order, and log like a historian because live moments cannot be replayed. My first version treated calls like slow texts and it showed. The rewrite treated them like conversations and everything downstream, including the texting side, got more reliable.

If your project only speaks in requests and responses, find its live edge. That is where the learning hides.
