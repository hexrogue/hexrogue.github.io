---
date: '2026-03-15T08:50:00+08:00'
title: 'Passive recon: what a listener learns without joining anything'
description: 'Promiscuous mode, channel hopping, the MAC table, and Bluetooth advertising. What a sniffer actually collects in a room, and the limits nobody puts in the demo.'
tags: ['wifi', 'security', 'ble', 'explainer']
author: nuh
---

Your phone's wifi chip has opinions. It only hands the operating system frames addressed to it or to the network it belongs to, and it drops the rest without ceremony. Promiscuous mode turns that filter off and keeps everything the radio can hear.

That single switch is what "recon" means in every wifi security tool.

## Listening to the whole room

Managed mode is the polite mode your laptop lives in. Monitor mode is the mode where the card reports everything, providing it has the driver support, which on most laptop wifi cards in 2026 means a fight with firmware and a reboot. The ESP32 exposes promiscuous mode in its SDK, so a five-dollar board gives you the unfiltered view that a laptop often will not.

It is not real monitor mode. The frames arrive without radiotap headers, 5 GHz is out of reach, and the radio cannot hop channels while staying promiscuous. What you get is 802.11 frames on whichever channel the radio sits on, which is enough for everything I write about.

<figure>
<img src="/images/hardware/usb-wifi-adapter.jpg" alt="A USB wifi adapter with a short antenna">
<figcaption>The laptop route to the same view: an adapter like this, a chipset whose driver allows monitor mode, and a reboot. Photo by Marcus Wong Wongm, CC BY-SA 3.0, via Wikimedia Commons.</figcaption>
</figure>

Because a radio sits on one channel, a sniffer that wants to cover 2.4 GHz has to hop. Mine parks on each channel for 300 milliseconds and cycles 1 through 13. Two consequences: it misses every frame sent while the radio was elsewhere, and it yanks the radio away from its own connection, so the board drops off my home network for the duration. Hopping is a trade, not a free upgrade.

The arithmetic is worth doing once. Thirteen channels at 300 milliseconds each is a full sweep every 3.9 seconds, and a device that beacons every 100 milliseconds is heard about three or four times per sweep if nothing else is talking. Anything quieter, or anything that only transmits during the second it connects, can sit in the room for the whole session and never appear in the table. A device missing from a scan is not a device that is absent. It is a device that blinked while your radio was looking elsewhere.

<figure>
<img src="/images/diagrams/channel-hop-timeline.svg" alt="A beacon train against a 300 millisecond per channel hop schedule">
<figcaption>Thirteen channels, 300 milliseconds each, and five beacons out of twenty landing while the radio was listening. The rest happened somewhere else.</figcaption>
</figure>

## The table you end up with

After a few minutes of hopping, a sniffer has a list. For each address: when it was first seen, when it was last seen, how many frames, the last signal strength, whether it behaved like an access point, and the SSID when one was visible. That list is a portrait of everyone in range.

Some of what falls out of it is obvious and some of it surprises people:

- Every access point in range, with its BSSID, its channel, and its name from the beacons it keeps shouting.
- Every station that sent anything, because a frame carries its address whether or not it is encrypted.
- Rough proximity ranked by signal strength, enough to tell across the room from in the next building.
- Which networks are busy. The frame counters separate an empty apartment from a household streaming four shows.

What it does not give you: message contents, and fingerprints. Data frames are encrypted once the two sides finish their handshake, so the payload is opaque. What survives is metadata, meaning who is talking, how much, how often, and how loudly.

## MAC address games

Every frame carries a hardware address, and vendors used to embed their identity in the first three bytes. So a sniffer could once tell you "this is a Samsung phone" with high confidence.

That leaked. Modern phones randomise their address for probe requests, and for a while now they also use a per-network random address when joining, so the same phone can appear as three different devices in your table. The list stops being a name tag and becomes a fingerprint.

It still says plenty. The names a phone probes for are the networks in its history, and one device asking for a hotel chain, a campus, and a specific cafe is a specific person's phone. The address rotates. The habits do not.

And the hidden network in your neighbour's router settings is still not hidden. The beacon leaves the name out, then the client that knows the network asks for it by name, and the response carries it in clear text. The first device that joins reveals it.

## The Bluetooth half

Same radio, different protocol. Bluetooth Low Energy devices do not connect to scan, they advertise: small packets broadcast on three dedicated channels, numbered 37, 38 and 39, a few times every second. A phone scanning for a speaker is just listening on those channels, and a passive collector does the same. Nothing is paired or requested, so the target has nothing to refuse.

An advertising packet carries a device name when the vendor bothered, a list of service identifiers, and a transmit power number that hints at how close the device expects to be. Some carry vendor payloads instead: iBeacons, for example, are just a Bluetooth advertisement with a fixed vendor blob inside, which is how an airport can put a battery-powered puck on the ceiling and have your phone know which gate it is standing under.

<figure>
<img src="/images/esp32/ble-beacon.jpg" alt="Small white Bluetooth beacon mounted on a ceiling above an airline sign at an airport">
<figcaption>That little white puck above the sign is a Bluetooth beacon, shouting a fixed ID into the hall. Photo by ThomasM72, CC BY-SA 4.0, via Wikimedia Commons.</figcaption>
</figure>

Bluetooth randomises its address too, and rotates it, which is the same privacy move phones made on wifi. It has the same weakness: a rotating address in a stable place is still a stable signal. This is exactly the property that makes item trackers work, and exactly the property that made them a scandal.

<figure>
<img src="/images/memes/meme-recon-always-been.jpg" alt="Always has been meme about phones broadcasting every network they remember">
<figcaption>Every airport, every mall, every conference. The whole time.</figcaption>
</figure>

## What recon is actually for

Standing in a room with a sniffer is not spying. It is reading the room, and reading the room is the boring half of security work. You do it to establish a baseline: these are the access points that should be here, this is how many deauths a quiet hour contains, this is how many devices my neighbourhood has.

Then the baseline earns its keep the first time something moves away from it. An access point broadcasting your network's name that is not yours. A device that follows you from home to campus on the same randomised address. A burst of deauth frames while you are on a call. All of those are visible only because you know what normal looked like first.

> "Keep your friends close, but your enemies closer.", The Godfather Part II (1974). Me, about rogue access points pretending to be mine.

## Try this

Run a sniffer for ten minutes somewhere busy and leave it. Then look at the table and try to answer two questions: which device is a laptop, and which access points are on your street. Beacons every 100 milliseconds and a stream of data frames give a laptop away without decrypting a byte.

The board I use for this is written up in [the story of the ESP32 recon rig](/blog/esp32-recon-rig-driver-said-no/), and the biggest thing it finds is covered in [the frame anyone can forge](/blog/deauth-frames-anyone-can-forge/).
