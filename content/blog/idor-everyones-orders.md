---
date: '2026-05-28T00:00:00+08:00'
title: 'The One-Number Bug That Leaked Orders'
description: 'One changed number in a URL, and I was reading strangers receipts. A bug hunting story.'
tags: ['security', 'pentesting', 'bugbounty']
---

Some bugs crash your app. The scary ones politely hand you other people's data. I found one of those in a test shop, and it took changing a single number.

## What is an IDOR, explained with lockers

Imagine school lockers. Yours is number 42. You ask the office "what is in locker 42" and they tell you. Now imagine you ask "what is in locker 43" and they tell you that too, no questions asked. That is an IDOR: a bug where the app checks who you are, but never checks whether the thing you asked for is yours.

<figure>
<img src="/images/memes/meme-idor.png" alt="Fry meme about user IDs">
<figcaption>Fry squints at your order IDs.</figcaption>
</figure>

Websites do this with order pages, invoices, and profiles. The address bar says something like order number 1001. Change it to 1002. If someone else's receipt loads, you found the bug.

## How the evening went

I was poking at a test store the way I always do: click everything, read every URL, ask "what if I change this." The order history page showed my test purchase at number 1001. Curiosity did the rest.

I typed 1002 and someone else's order appeared. Name, address, phone, what they bought, what they paid. My stomach dropped a little, which is how you know it is a real finding and not a puzzle.

I stopped there. That matters and I want to be clear about it. Reading one record proves the hole exists. Reading fifty records makes you the villain. I documented the steps, took a screenshot of my own test data only, and wrote the report: what I did, what it exposed, and the one line fix. Check ownership on every request, on the server, every time. Never trust the URL.

## Why this bug never dies

Developers assume the app only requests what it should. But the app lives in the attacker's browser, and the attacker can request anything. Every IDOR is the same mistake: the front door checks your ID, the back rooms do not.

Frameworks do not save you here. Only a habit saves you: for every piece of data, ask who is allowed to see it, and enforce the answer where the user cannot reach it.

## How to test your own app in five minutes

You do not need tools for this one. Two test accounts and a browser.

One, log in as user A and open anything personal: an order, an invoice, a settings page. Two, copy the URL. Three, log in as user B in another window and paste that URL. If B sees A's stuff, you have an IDOR. Four, try skipping numbers up and down, and try it logged out entirely. Five, write down everything you tried, because that list becomes your regression test forever.

The fix is equally unglamorous. On the server, for every request, look up who is asking and who owns the thing, and refuse when they differ. Do it in one shared function so nobody forgets. Boring, airtight, done.

> "With great power comes great responsibility.", Spider-Man (2002). Ben Parker was describing server side authorization checks and I will not be taking questions.

## The takeaway for builders

If you write software that shows users their own stuff, go try this on your own app today. Log in as two test users. Swap the numbers. If user A sees user B's data, you just saved yourself a very bad email. Five minutes of curiosity beats a breach disclosure every time.
