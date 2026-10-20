---
date: '2026-03-31T16:30:00+08:00'
title: 'WPA2, WPA3 and PMF: what actually stops the attacks I wrote about'
description: 'SAE instead of a shared key, signatures on management frames, and the transition mode that quietly undoes both. The security half of the wifi series.'
tags: ['wifi', 'security', 'explainer']
author: nuh
---

[The deauth post](/blog/deauth-frames-anyone-can-forge/) ends with a promise: the fix is management frame protection, and modern gear just ignores a forged eviction notice. That is the short version. The long version is that wifi security has two generations, and the reason half the networks you can see are still forged-frame food is a compatibility setting.

## What WPA2 actually does

<figure>
<img src="/images/diagrams/handshake-four-way.svg" alt="The four-way handshake between a station and an access point">
<figcaption>Four messages, all readable on the air, none of them containing the passphrase.</figcaption>
</figure>

WPA2 turns your passphrase into a key, though not directly. A passphrase is a sentence and a key is exact bytes, so the standard stretches it through a deliberately slow function and calls the result the pairwise master key. Then the two sides run the four-message handshake and derive keys for the session.

That design protects the traffic well and protects the passphrase badly. Everything the cracker needs to test guesses offline is in the handshake, and the passphrase is the only thing standing between a captured handshake and a dictionary. On WPA2 the password is the entire defence. It is also why [the PMKID is such a neat trick](/blog/cracking-your-own-password-pmkid/): the router hands out crackable material before anyone even connects.

The second weakness is quieter. WPA2 does not authenticate management frames. They are unencrypted and unsigned, which is how the whole deauth story is possible. The standard was amended in 2009 to allow a fix, and then the fix sat unused for a decade because turning it on breaks old hardware.

## What WPA3 changes

<figure>
<img src="/images/diagrams/wpa2-vs-wpa3.svg" alt="WPA2 compared with WPA3: a shared key and an offline-testable capture against SAE and nothing to test">
<figcaption>Two generations, side by side, and the one property that separates them: whether a recording can be checked against guesses.</figcaption>
</figure>

WPA3-Personal replaces the shared-key dance with a different exchange, called SAE. Both sides prove they know the passphrase through a cryptographic exchange, and each session ends up with a fresh key.

The important part is what an attacker can do with a recording of that exchange. With WPA2, a capture is a guess-checker you can run at your leisure. With SAE there is nothing in the recording to test a guess against, so the offline dictionary attack that defines wifi cracking simply does not exist. There is also forward secrecy: even if the passphrase leaks later, sessions recorded earlier stay sealed.

A well-chosen passphrase with WPA2 is still very hard to crack. SAE changes the shape of the problem, not physics. It closes the assembly line that turned weak passphrases into five-minute cracks.

## PMF, the part that saves you from my board

PMF is management frame protection. It adds a message integrity check to the frames that manage a connection, so a deauthentication or disassociation frame without the right key is dropped by the receiver instead of obeyed.

The timeline matters. It was written into the standard in 2009 and shipped as an optional feature of WPA2 a few years later. WPA3 requires it. Wi-Fi 6 requires it. WPA2, on its own, permits it and usually leaves it off.

That single sentence is the whole explanation of the split you see in the wild. A router running WPA3 in WPA3-only mode shrugs off anything my board can transmit. A router running WPA2 with PMF off eats a forged deauth whole. The same frame, two completely different outcomes, decided by one configuration checkbox nobody looks at.

## The catch: transition mode

You would think turning on WPA3 settles it. Often it does not.

To let old devices stay connected, most routers turn WPA3 on and leave WPA2 on beside it, on the same network name, with the same passphrase. That is called transition mode, and it is the default for a reason: without it, every device that cannot do SAE gets locked out.

The problem is that transition mode keeps the WPA2 path alive. Same network, same passphrase, so the passphrase can be recovered by attacking the WPA2 side with the ordinary offline attack. An attacker who cracks that shared passphrase gets the network, whether they use the WPA2 path or the WPA3 one. The strong protocol is only as strong as the weak protocol sharing its name.

There is a fix, and it is called transition disable: a signal from the access point that tells modern clients to refuse to fall back to WPA2 for this network, which blocks the downgrade trick. It is required for WPA3, and plenty of routers bury it, or you have to find it. If your router has both WPA3 and a "compatibility" option, they are describing different things.

## Enterprise, in one paragraph

Everything above is personal wifi. WPA3-Enterprise is a different animal: no shared passphrase, each device has its own credentials checked against a server, and the optional 192-bit mode tightens the cryptography further. That is the one to care about if you run a network for other people, because it removes the shared secret that makes both the offline crack and the "someone leaked the wifi password" problem possible. It also introduces a server to run, which is why home routers hand you a passphrase instead.

<figure>
<img src="/images/memes/meme-wpa3-two-buttons.jpg" alt="Two buttons meme about leaving PMF off so old devices work versus turning on WPA3">
<figcaption>The compatibility checkbox is a security decision. It is just an easy one to forget you made.</figcaption>
</figure>

> "The only truly secure system is one that is powered off, cast in a block of concrete and sealed in a lead-lined room with armed guards.", Gene Spafford. Wifi has to stay on. That is the engineering constraint the whole standard lives inside.

## Try this

Open your router's wifi settings and answer two questions: is it WPA2, WPA3, or both, and is PMF off, optional or required. Most people have never looked. Then, on your own gear, point a forged deauth at your own device and watch it ignore you. That experiment teaches the difference between the two generations faster than any table.

If you want the frame that this post is defending against, it is [the 26 bytes anyone can forge](/blog/deauth-frames-anyone-can-forge/).
