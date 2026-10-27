---
date: '2026-08-01T17:40:00+08:00'
title: 'WPA3 SAE, without the fairy tales'
description: 'What the dragonfly handshake actually removes, what it does not, and why transition mode keeps the old offline attack alive on a network that says WPA3 on the box.'
tags: ['wifi', 'security', 'explainer']
author: nuh
---

WPA3 has a reputation problem. Marketing calls it unhackable, forums call it broken, and both are wrong in useful ways. The honest version is narrower and more interesting: WPA3 kills the offline dictionary attack, which is the technique most people mean when they say their wifi got hacked.

<figure>
<img src="/images/memes/meme-wpa3-fine.jpg" alt="This Is Fine dog meme: WPA3 is unhackable while transition mode quietly keeps WPA2 alive">
<figcaption>Marketing says unhackable. Transition mode says hold my WPA2.</figcaption>
</figure>

## The thing SAE removes

Start with what WPA2 gives an attacker. The passphrase becomes a key, the four-way handshake derives session keys, and the whole exchange is readable on the air. A recording contains everything needed to test guesses at home, at full speed, on a machine that never has to touch the network again. The cracker is not attacking your router. They are attacking a file.

SAE stands for Simultaneous Authentication of Equals. It is a password-authenticated key exchange built on a design called Dragonfly, and its point is that both sides prove they know the passphrase without sending anything that can be tested offline. The recording stops being a guess-checker.

```mermaid {alt="The SAE exchange: client and access point each send a commit, both derive the same secret from their own private value, then each sends a confirm that proves the secret without revealing the password"}
sequenceDiagram
  participant C as client
  participant A as access point
  Note over C,A: both know the passphrase, neither sends it
  C->>A: commit (scalar and element)
  A->>C: commit (scalar and element)
  Note over C,A: each derives the same secret from its own private value
  C->>A: confirm (hash proving the secret)
  A->>C: confirm (hash proving the secret)
  Note over C,A: session keys derived, nothing offline-testable was sent
```

## Commit, confirm, done

Each side picks a private random value and turns it into a public element using the password. The commit message carries that element and a scalar. Both sides then compute the same shared secret from their own private value and the other side's public one. The confirm message proves they got the same answer.

A wrong password means the confirms do not match and the session dies. An eavesdropper with the recording cannot check a guess without talking to the access point, because the secret depends on values that were never sent and on an exchange that has to happen live.

Two properties fall out of this. Every guess needs a real exchange with the access point, so an attacker has to be present and patient while the access point rate-limits or bans them. And the session keys are not derivable from the password alone, so a recording made today stays sealed even if the passphrase leaks next year. That is forward secrecy, and WPA2 does not have it.

## What it does not fix

A weak password still falls. Rate limiting makes online guessing slow, not impossible. The dictionary moved from "run for five minutes on a laptop" to "run for weeks against a live access point", which is a huge improvement and still not a reason to use the dog's name.

The access point is still an access point. An evil twin can stand up a fake WPA3 network and collect whatever the client sends. SAE makes the captured exchange less useful. It does nothing about a user typing a password into the wrong portal. [The rogue access point post](/blog/watching-your-own-air-rogue-aps/) is the relevant one.

Downgrade survives in transition mode. Most routers run WPA3 and WPA2 on the same network name with the same passphrase so old devices keep working. That leaves the WPA2 path alive, and an attacker can push a client onto it. The defence is transition disable, a flag from the access point telling modern clients to refuse the fallback. Plenty of routers bury it.

Implementations had holes. The Dragonblood research found timing and cache side channels in early SAE, plus downgrade issues. One of the fixes was hashing the password directly into a group element, called hash-to-element, instead of the original hunting-and-pecking loop. Old firmware may still run the slow, leaky path.

<figure>
<img src="/images/memes/meme-wpa3-expanding-brain.jpg" alt="Expanding brain meme: using a strong password, then WPA3 with SAE, then WPA3 and WPA2 side by side, and finally the WPA2 side being downgraded so the password is the whole defence">
<figcaption>Each step up feels like progress. The top panel is where most homes stop.</figcaption>
</figure>

## Hunting and pecking, in one paragraph

The original Dragonfly method turned a password into a group element by trying candidates in a loop until one fit. The time that loop took depended on the password, which leaked information about it. Hash-to-element takes the password and a counter, hashes them, and derives the element in constant time. When a router menu says "SAE H2E", that is the version you want.

## What to set

WPA3-only if every device in the house supports it. Check the oldest thing first, because the printer, the smart plug or the 2016 laptop is the one that will complain.

Otherwise, transition mode with transition disable on. Without the disable flag, the WPA2 door is open and labelled.

WPA3 requires PMF. If a device cannot do management frame protection, it cannot do WPA3, and no amount of setting changes that. The [PMF half of this story](/blog/wpa2-wpa3-pmf-what-stops-them/) explains why.

And keep the passphrase strong. The protocol removed the offline shortcut, not the need for entropy.

## The part people skip

WPA3 is not a different kind of wifi. It is the same frames with a better way to agree on a key and a rule that management frames get protection. That is enough to break the assembly line that turned a weak password into a five minute crack. It is not enough to make a bad password good or a fake access point honest. Those two problems are yours.
