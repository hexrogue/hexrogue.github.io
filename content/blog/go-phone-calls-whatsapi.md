---
date: '2026-03-02T00:00:00+08:00'
title: 'How I taught Go to make phone calls'
description: 'WhatsApp messages are just text. Calls are a different animal. How I tamed it:'
tags: ['go', 'whatsapp', 'voip']
---

Texting through code is easy. Your program sends words, the other side receives words. Done. Then someone asks "can it also call people" and you discover that voice is a whole different animal. This is the story of teaching my Go gateway to speak.

## Messages are letters, calls are conversations

Think of a text message like a letter. You write it, you post it, it arrives whenever. Nothing needs to be live at the same time. A phone call is a conversation: both sides talking at once, reacting instantly, and if the words arrive late or jumbled, the whole thing falls apart.

That is why calls need a constant live connection, not letter delivery. My gateway holds that connection open all day using something called a WebSocket. Picture a tin-can telephone string between my server and WhatsApp that never gets cut. Messages travel down the string as events, and my code listens and reacts in real time.

<figure>
<img src="/images/memes/meme-go-calls.png" alt="Spongebob meme about voice calls">
<figcaption>Mocking the idea that calls are easy.</figcaption>
</figure>

## The string keeps getting cut

The tin-can analogy lied about one thing. Strings get cut constantly. The connection is a secure WebSocket, which means every fresh connect starts with a TLS handshake: several round trips of cryptographic introductions before a single useful byte flows. On a good network that costs a blink. On a bad one it costs the call.

Worse, the network murders idle connections. Home routers and mobile carriers silently drop connections that sit quiet too long, usually somewhere between one and five minutes, and they never tell you. Your side thinks the string is intact. The other side is gone.

Messages pile up unsent until something notices. The fix is ping frames, tiny heartbeats every few dozen seconds that say "still here." Plus reconnect logic with backoff for when heartbeats fail: wait a second, try again, wait longer, try again, and never hammer the server like a panicking ex.

The stupid overhead nobody warns about: each reconnect replays the handshake, re-registers the session, and re-syncs missed events. My logs from that week are just connect, die, reconnect, die, with my spirit dying in parallel. Getting this boring machinery right took longer than the actual calling features. Nobody demos reconnect logic. Everybody needs it.

## The call nobody documented well

The messaging side had examples everywhere. The calling side had whispers. I spent days watching raw events flow past, logging everything, trying to spot the exact moment a call starts ringing versus gets answered versus drops. It felt like learning a language by eavesdropping.

The breakthrough was boring, like all good breakthroughs. I stopped guessing and wrote a logger that printed every single event with timestamps. Within an hour I could see the pattern: this event means ringing, that one means picked up, this other one means the other side hung up. The protocol was never mysterious. It was just undocumented.

## What is VoIP, really

Voice over IP means chopping sound into tiny digital envelopes and mailing them very fast. Your voice gets sliced dozens of times per second, each slice numbered, fired across the internet, and reassembled on the other side in order. If slices arrive late, the software guesses to fill the gap. If too many vanish, the voice goes robotic, then silent.

That numbering is the whole game. Text messages do not care about order or timing. Voice cares about both, constantly, with no pause button. A call is thousands of little deliveries per minute where late equals lost. Once that clicked, every design decision in the gateway made sense: persistent connection, instant event handling, and logs detailed enough to replay a failure after the moment passed.

> "Can you hear me now?", the Verizon guy (2002). Me, staring at event logs at 2 AM, asking the void the same question.

## Delay turns people into walkie-talkies

The frustration nobody explains until you live it: sound takes time to travel, and humans notice at around 150 milliseconds. Past that, both sides start talking over each other, then both stop, then both apologize, then both start again. A 300 millisecond delay turns a phone call into two people operating a walkie-talkie badly. My first test calls sounded exactly like that. Over. No. You go. Sorry. You go.

Jitter makes it crueler. Delay is constant lateness. Jitter is random lateness: slices arriving 20ms apart, then 200ms, then 5ms. The fix is a jitter buffer, a small waiting room that holds early slices so late ones can catch up. Too small and the voice stutters.

Too big and you add delay, which causes the walkie-talkie problem. Tuning that buffer meant calling myself between two phones for an entire evening, adjusting numbers, listening to my own voice arrive late like a delayed broadcast. There is no formula. There is only your ear and patience.

The cruelest part: none of this shows up in logs as an error. Every packet delivered, every metric green, call quality garbage. Real time systems fail in ways dashboards cannot see. You have to listen.

## Why Go was the right animal for this

Go loves doing many things at once. Every live connection gets its own lightweight worker, thousands of them running without breaking a sweat. A call, a message stream, a status update: each handled concurrently while the main program stays calm. For a gateway that must never miss an event, that is exactly the personality you want.

It runs in Docker now. One container, restarts itself if it ever falls over, logs everything. The CRM plugs into it and suddenly follow-up calls and reminders go out on their own.

## What I actually learned

Real time systems are not faster versions of normal systems. They are a different species with different rules: never block, never assume order, log everything because you cannot replay a live moment. Messages forgave my early mistakes. Calls did not. That strictness made the whole gateway better. If your side project only handles requests and responses, find the live part of your problem. That is where the education lives.
