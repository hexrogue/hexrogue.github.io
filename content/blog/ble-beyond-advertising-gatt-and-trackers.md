---
date: '2026-06-08T13:35:00+08:00'
title: 'BLE past advertising: GATT, bonding and why trackers work'
description: 'Advertising is the shallow half of Bluetooth Low Energy. Connections, services, pairing, and the rotating addresses that item trackers quietly depend on.'
tags: ['ble', 'security', 'explainer']
author: nuh
---

[The recon post](/blog/passive-recon-wifi-and-ble/) stops where most Bluetooth writing stops: a device shouts small packets into the room and you write down its name and address. That is advertising, and it is the shallow half. The other half is what happens once two devices agree to talk.

## Advertising is a bulletin board

A peripheral that wants to be found advertises. The packet is small and it announces, in effect: I exist, my name is this, and these are the kinds of service I offer. A central that is interested replies and, if both agree, the two stop broadcasting and open a private two-way channel. From the radio's point of view, that is the transition from shouting to a phone call.

Not every device wants the call. A sensor that just reports a number every minute can broadcast it in the advertising packet and never connect at all. A heart-rate strap wants the call, because the data changes constantly and the phone wants updates as they happen.

<figure>
<img src="/images/hardware/ble-tracker.jpg" alt="A small coin-cell Bluetooth tracker tag">
<figcaption>A tag that never opens a connection. It advertises a rotating number and lets the network do the rest. Photo by KKPCW, CC BY-SA 4.0, via Wikimedia Commons.</figcaption>
</figure>

## GATT, the data model on top

<figure>
<img src="/images/diagrams/gatt-structure.svg" alt="A BLE device exposing services and characteristics">
<figcaption>A device is a tree of services and characteristics, and the identifiers are published. That is a feature of the design and a map for anyone listening.</figcaption>
</figure>

Once connected, the conversation follows a fixed shape called GATT. A device exposes services, each service holds characteristics, and each characteristic has a value plus permissions: readable, writable, or notify-me-when-it-changes. The notify permission is why a phone gets a live number from a fitness sensor instead of polling it.

The useful and slightly unsettling part is that this structure is not secret. Services and characteristics have numeric identifiers, many of them from a public standard list, and a device often asks for the ones it needs by their published numbers. That is why a scan of a room full of gadgets reads like a catalogue: this one has a battery service, this one has a heart-rate service, this one is wearing a keyboard profile and absolutely is not a keyboard. A passive listener gets a device's job from the identifier before it gets anything else.

## Pairing and bonding, two words that get merged

Pairing is the one-time key exchange when two devices first trust each other. Remember this bit: the cheapest pairing mode, the one most gadgets use because it has no user interface, offers no protection against a device in the middle. It is called Just Works precisely because it just works, and it means an attacker who is present during the first pairing can be part of it. Devices you cannot type a code into cannot do better without a screen or a button to press.

Bonding is what happens after: both sides store the keys, so future connections skip the exchange and skip the prompt. An unbonded device still connects on request. A bonded device still connects without a prompt. If you have ever wondered why a peripheral reconnects the instant it is powered on, that is bonding, and it is why the pairing decision is the one that matters.

## The rotating address, and why trackers ignore it

Both wifi and Bluetooth randomise their hardware address to stop you being followed by a fixed number. Bluetooth does it properly: the address rotates, and a device you are bonded to can still recognise you because you share a key that resolves the rotation. To everyone else, the address changes every few minutes to half an hour, and the trail breaks.

That is a real privacy win, and it is also the exact place item trackers reveal what the privacy was designed to protect. A tracker is not followed by its address. It is followed by its relationship. The tag broadcasts a rotating address, and any phone from the tracking network that hears it relays the sighting home, so the network does the locating. The rotating address protects you from the sniffer standing next to you. It does nothing about the network, because the network was built to resolve the rotation on purpose. That is the design, not a flaw, and it is why the anti-stalking features had to be added separately: a tag that has been away from its owner for a while starts chirping, and both major phone platforms will warn you about a tracker travelling with you.

The lesson generalises past tags. Rotating your identifier defeats local observation and does nothing about the party you told your identity to.

<figure>
<img src="/images/memes/meme-ble-change-my-mind.jpg" alt="Change my mind meme: a rotating MAC address keeps me anonymous">
<figcaption>To the sniffer, yes. To the network that resolves the rotation, no.</figcaption>
</figure>

<figure>
<img src="/images/memes/meme-ble-tracker-always-been.jpg" alt="Always has been meme about the finder network resolving the tracker's rotating address">
<figcaption>Rotating the address was never going to stop the network that knows the key.</figcaption>
</figure>

> "Privacy is not something that I'm merely entitled to, it's an absolute prerequisite.", Marlon Brando. Bluetooth agreed, then handed the resolution key to the network.

## Try this

Scan Bluetooth Low Energy on your own devices and pick five entries you cannot name. Guess what each one is from its advertised services alone, then confirm by turning devices off one at a time. You will find you can classify almost everything without connecting, which is the same metadata story as wifi: the shape of the traffic gives the device away before the contents do.

The advertising half of this is in [what a sniffer learns without joining anything](/blog/passive-recon-wifi-and-ble/).
