---
date: '2022-02-17T00:00:00+08:00'
title: 'Seven Ways I Broke My Own Website'
description: 'The mistakes every new web developer makes, including past me. Save yourself the evenings.'
tags: ['web', 'tips']
author: nuh
---

I have shipped code that worked perfectly on my laptop and fell apart the moment a real user touched it. The laptop is a controlled environment. A real user is a raccoon with a credit card. These are the mistakes that cost me the most evenings. Read them now, or pay the same tuition later.

## The form that worked until someone opened curl

The browser is the attacker's computer. Every check in your JavaScript is a suggestion. The attacker can skip it. Validate on the server, every time, even when the frontend already did. Frontend validation is for people who make typos. Backend validation is for everyone else.

I learned this by watching someone bypass my beautiful form with curl in ten seconds. Ten seconds. The form had a nice gradient and everything.

<figure>
<img src="/images/memes/meme-webdev-pooh.jpg" alt="Tuxedo Pooh meme about server validation">
<figcaption>Server validation is the fancy choice.</figcaption>
</figure>

## The password I almost stored in plain text

Never save a raw password. Hash it properly and store the fingerprint. When the user logs in, hash what they typed and compare. If the database leaks, the attacker gets fingerprints instead of keys. Use a real library. No homemade crypto. No "I will add salt later." Later is how you end up on Have I Been Pwned.

<figure>
<img src="/images/diagrams/webdev-auth-flow.svg" alt="Diagram showing a password hashed before storage and hashed again for comparison on login">
<figcaption>The password never reaches the database.</figcaption>
</figure>

## The deploy with no tests

You can test manually for an hour, or write one test that runs in a second. I know which one I pick now. The soup meme is not subtle: no tests, no deploy.

<figure>
<img src="/images/memes/meme-soup.png" alt="Soup Nazi meme about testing">
<figcaption>No tests. No deploy for you.</figcaption>
</figure>

## The page that made 101 database trips

Fetching a list of 100 posts, then running one extra query per post inside a loop, means 101 trips to the database. That is the N+1 problem, and it is the silent killer of side projects that suddenly get users. Fetch the related data in one joined query. The page load time drops like a stone, in the good direction.

## The headers I skipped because they looked boring

Security headers are one line each and block entire categories of attacks. Content Security Policy, HttpOnly cookies, the usual suspects. They feel like paperwork. They are seatbelts.

## The layout that only worked on my monitor

Half your visitors arrive on a phone, on a bus, on a connection with opinions. If your layout only works on your monitor, it works for exactly one person. Shrink your browser while developing. Tap through with your thumbs. Watch an image the size of a billboard squeeze through a straw connection.

Responsive design is the same site, flexing. You do not add it later.

The ELI5 version: build a liquid, not a statue. Content should pour into any container instead of cracking outside it.

## The Friday deploy and the missing config

Okay, the Friday thing is half joke. The real rule: if it is not in git, it does not exist. Config files, database migrations, infrastructure notes. Future you, debugging at midnight, will thank present you. Future you is also petty and will blame present you. Do not give future you the satisfaction.

## The pattern

Every mistake above is the same lesson wearing different clothes. The user is not your friend, the network is not your computer, and convenience now is debugging later. Build like someone unfriendly is reading your code. Someone will be.
