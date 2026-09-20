---
date: '2026-01-25T00:00:00+08:00'
title: 'Web Dev Tips: What to Avoid'
description: 'The mistakes every new web developer makes, including past me. Save yourself the evenings.'
tags: ['web', 'tips']
---

Nobody teaches you web dev by listing what not to do. So this is my list, earned the hard way. Every item below cost me at least one evening.

## Do not trust the browser

The browser is the attacker's computer. Anything your JavaScript checks, the attacker can skip. Validate on the server, every time, even when the frontend already did. Frontend validation is for friendly users. Backend validation is for everyone else. I learned this the way everyone does: by watching someone bypass my beautiful form with curl in ten seconds.

<figure>
<img src="/images/memes/meme-webdev-pooh.jpg" alt="Tuxedo Pooh meme about server validation">
<figcaption>Server validation is the fancy choice.</figcaption>
</figure>

## Do not store passwords, store fingerprints

Never save a raw password. Run it through a proper hashing function first and store the result. When the user logs in, hash what they typed and compare fingerprints. If your database ever leaks, the attacker gets useless fingerprints instead of everyone's keys. Libraries exist for this in every language. No excuses, no homemade crypto.

<figure>
<img src="/images/memes/meme-soup.png" alt="Soup Nazi meme about testing">
<figcaption>No tests. No deploy for you.</figcaption>
</figure>

> "With great power comes great responsibility.", Spider-Man (2002). Also applies to database access. Funny how often that quote fits.

## Do not N+1 your database

Fetching a list of 100 posts, then running one extra query per post inside a loop, means 101 trips to the database. That is the N+1 problem and it is the silent killer of side projects that suddenly get users. Fetch the related data in one joined query instead. Your page load time will drop like a stone, the good direction.

## Do not skip the boring headers

Security headers are one line each and block entire categories of attacks. Content Security Policy, HttpOnly cookies, the usual suspects. They feel like paperwork. They are seatbelts.

## Do not forget the smallest screens

Half your visitors arrive on a phone, on a bus, on a connection with opinions. If your layout only works on your monitor, it works for exactly one person. Shrink your browser while developing. Tap through with your thumbs. Watch images the size of billboards squeeze through a straw connection. Responsive design is not a feature you add later. It is the same site, flexing.

The ELI5 version: build a liquid, not a statue. Content should pour into any container instead of cracking outside it.

## Do not deploy on Fridays, do version everything

Okay, the Friday thing is half joke. The real rule: if it is not in git, it does not exist. Config files, database migrations, infrastructure notes. Future you, debugging at midnight, will thank present you.

## The pattern

Every tip above is the same lesson wearing different clothes. The user is not your friend, the network is not your computer, and convenience now is debugging later. Build like someone unfriendly is reading your code. Because someday, someone will be.
