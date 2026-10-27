---
date: '2026-10-17T08:30:00+08:00'
title: 'Wifi from zero: where to start'
description: 'A reading order for the wifi posts, from the vocabulary to the attacks and the defences. Start here if you found the middle of the series first.'
---

The wifi posts were written in the order I learned things, which is not the order they are easiest to read. This is the order. Six posts take you from "what is a station" to "why the attack I built does nothing on a modern router", and the build story sits at the end where it belongs.

<figure>
<img src="/images/esp32/wifi-architecture.svg" alt="Diagram of two 802.11 BSS networks joined by a distribution system into one ESS, connected to an 802.3 wired network">
<figcaption>Access point, station, BSS, ESS. Everything below is built on these four words. Diagram by Superspritz, CC BY-SA 4.0, via Wikimedia Commons.</figcaption>
</figure>

If you read one post out of order, read the first one. The rest assume it.

1. **[WiFi in plain words](/blog/wifi-ap-sta-how-devices-join/)**. Access points and stations, SSID against BSSID, channels, and the handshake your phone runs every time it joins something. Read this if "association" and "connected" sound like the same thing. They are not.
2. **[802.11 frames you can read](/blog/80211-frames-you-can-read/)**. The envelope every packet shares, the three families of frame, and what stays readable after encryption. Read this if you want to open a capture and not close it immediately.
3. **[Passive recon](/blog/passive-recon-wifi-and-ble/)**. Promiscuous mode, channel hopping, the station table, and the Bluetooth half of the same radio. Read this if you want to know what a listener gets without joining anything.
4. **[Deauth frames](/blog/deauth-frames-anyone-can-forge/)**. The 26 bytes with no signature on them, what the frame does and does not achieve, and the reason it still works in 2026. Read this if you have heard the word and want the frame.
5. **[WPA2, WPA3 and PMF](/blog/wpa2-wpa3-pmf-what-stops-them/)**. The security half: SAE, management frame protection, and the transition mode that quietly undoes both. Read this directly after the deauth post, because it is the answer to the question that post ends on.
6. **[Watching your own air](/blog/watching-your-own-air-rogue-aps/)**. Rogue access points, evil twins, and how to turn the recon table from a curiosity into a detector. Read this if you want the defence and not only the attack.

Then the story, which is where all of it came from: **[I taught a $5 board to sniff wifi, then fought its driver](/blog/esp32-recon-rig-driver-said-no/)**. The vocabulary is assumed by then, which is exactly how I want it. If you would rather build the board than read about mine, the **[build guide](/blog/esp32-recon-rig-build-guide/)** is the parts list, the wiring, and the mistakes.

## The side quests

Read these when the main path raises a question, or when you want the practical half instead of the theory.

- [RSSI and the noise floor](/blog/rssi-dbm-noise-floor/) for why the signal bars lie and the two numbers worth comparing instead.
- [2.4 GHz interference and channel planning](/blog/24ghz-interference-channel-planning/) for the three channels that are real, and why two networks sharing one channel beat two that overlap.
- [Sticky clients and roaming](/blog/wifi-roaming-sticky-clients/) for why your phone clings to the wrong access point, and what the network can and cannot do about it.
- [WPA3 and the dragonfly handshake](/blog/wpa3-sae-dragonfly-handshake/) for what SAE actually removes, and the transition mode that quietly puts it back.
- [Beacon spam](/blog/beacon-spam-and-the-wifi-list/) for the joke SSIDs in your phone's wifi list and what they cost a device.
- [Cracking your own password](/blog/cracking-your-own-password-pmkid/) for the other end of the PMKID story, ending in a hashcat run against your own network.
- [Decrypting your own traffic](/blog/decrypt-wpa2-traffic-wireshark/) for turning a capture into readable packets once you hold the passphrase.
- [BLE past advertising](/blog/ble-beyond-advertising-gatt-and-trackers/) for connections, services, and why item trackers work.
- [How a captive portal works](/blog/esp-captive-portal-explained/) for the hotel login page and how to build one on the board.
- [Sub-GHz primer](/blog/sub-ghz-primer-433mhz/) for 433 MHz weather stations and remotes, ahead of the second half of the project.

## The prerequisite

Before any of the attack posts, read [the lab rules](/lab-rules/). Own gear or written permission, and the reasons why. It is one page and it is not optional.
