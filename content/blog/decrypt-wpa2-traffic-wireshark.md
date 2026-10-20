---
date: '2026-09-11T20:10:00+08:00'
title: 'Decrypting your own WPA2 traffic in Wireshark'
description: 'Give Wireshark the passphrase and your own capture turns into readable traffic. What you need first, what you get after, and what WPA3 refuses to hand over.'
tags: ['wifi', 'wireshark', 'security']
author: nuh
---

A monitor mode capture is mostly noise: beacons, management frames, and encrypted data you cannot read. Wireshark will decrypt your own WPA2 traffic if you give it the passphrase and the capture contains the handshake. The gap between those two conditions is where most people get stuck.

## What you need before you start

- A capture that includes the four-way handshake for the client you care about. If you started capturing after the phone connected, the keys were negotiated before you arrived and the file contains nothing to derive them from.
- The SSID and passphrase, or the raw 32 byte PMK.
- Monitor mode on an adapter that supports it. The ESP32 can do it, and a laptop adapter is easier. [The capture tips](/blog/wireshark-tips-read-your-network/) cover the setup.

The handshake itself is [explained here](/blog/wpa2-wpa3-pmf-what-stops-them/). The short version: the passphrase is not the session key. Wireshark stretches the passphrase and SSID into the PMK with PBKDF2, then uses the nonces from the handshake to derive the pairwise key for that session. No handshake, no nonces, no decryption.

<figure>
<img src="/images/memes/meme-wireshark-gru-plan.jpg" alt="Gru's plan meme: capture wifi in monitor mode, add the passphrase to Wireshark, and discover the capture has no handshake in it">
<figcaption>Every failed decryption starts with a capture made a minute too late.</figcaption>
</figure>

## Doing it

Open Preferences, then Protocols, then IEEE 802.11. Tick enable decryption and press Edit to add a key. Two forms are useful:

- `wpa-pwd` with `passphrase:SSID`
- `wpa-psk` with the 64 character hexadecimal PMK

Include the SSID. Wireshark can sometimes guess it from the capture, and sometimes it guesses wrong, and then you spend twenty minutes wondering why the key does nothing. Apply, and frames that were encrypted become 802.11 data with a decoded LLC and IP layer. Normal filters start working again: `ip.addr`, `dns`, `http`.

## What you will and will not see

You will see unicast traffic for every client whose handshake is in the file. Broadcast and multicast use the group key, which Wireshark can also derive from the handshake, so those open up too.

You will not see traffic from clients whose handshake you did not capture. On your own network that is a temporary inconvenience. On someone else's network it is the line you should not cross, and [the lab rules](/lab-rules/) are the fence.

PMF protected management frames stay protected even after decryption. That is the entire point of PMF, and it is why enabling it changes what a passive observer can learn.

WPA3 and SAE traffic cannot be decrypted this way. There is no shared passphrase path from a capture to the PMK, which is the improvement [the SAE post](/blog/wpa3-sae-dragonfly-handshake/) describes.

## The application layer is still yours to lose

Decrypting wifi gets you to IP. It does not get you past TLS. If the decrypted stream shows plaintext HTTP, that is a finding about the website, not about wifi. The lesson is the one HTTPS has been shouting for years: an encrypted transport does not make an application secure, and a decrypted transport does not make a secure application readable.

## A clean workflow

1. Start the capture in monitor mode before the client connects.
2. If you missed the handshake, reconnect the client and capture the join.
3. Save as pcapng. Do not work on the live file.
4. Filter `eapol` to confirm the four messages are present.
5. Add the key, then switch to normal IP filters.
6. Stop the capture before you walk away. A forgotten monitor interface fills a disk quietly.

```mermaid {alt="The decryption pipeline: capture in monitor mode, check the file for EAPOL, recapture after a reconnect if it is missing, add the passphrase to Wireshark, then filter the decrypted IP traffic"}
flowchart LR
  A["monitor mode capture"] --> B{"EAPOL handshake in file?"}
  B -->|"no"| C["reconnect the client and recapture"]
  C --> A
  B -->|"yes"| D["Wireshark, 802.11 preferences"]
  D --> E["wpa-pwd passphrase:SSID"]
  E --> F["unicast frames decrypt"]
  F --> G["normal IP and TCP filters"]
```

## The thing worth taking away

The handshake is the whole key. A capture taken at the wrong moment is a pile of bytes, and a capture taken at the right moment is your entire session in plaintext up to the TLS layer. That asymmetry is why forcing a reconnect is a real attack step, and why [the PMKID shortcut](/blog/cracking-your-own-password-pmkid/) matters: it removes the need to wait for a client at all. Understand it on your own gear and the rest of the series stops being theory.
