---
date: '2026-10-17T08:00:00+08:00'
title: 'Lab rules'
description: 'One page, one rule. Every technique on this site is meant to be practised on your own hardware or on gear you have written permission to test.'
---

Every offensive technique I write about comes with the same prerequisite, so I am writing it once here instead of repeating a paragraph in each post.

Your gear, or written permission. That is the whole rule. Everything on this site can be learned on a five-dollar board and the access point you own. If a lesson needs a second radio, buy the second radio. If a lesson needs a second network, run one.

The things that go wrong when you skip this are not abstract:

- A deauth frame is a denial of service. Pointing one at somebody else's wifi is a denial of service attack, and it is illegal almost everywhere it lands.
- Packet capture on a network you do not own is interception. The law does not care that the payload was encrypted, only that you collected it.
- Beacon spam, auth floods and the rest of the 802.11 denial of service family are the same problem wearing a joke name. A list of funny SSIDs on your own phone is a prank. The same frames across a neighbourhood are not.
- A rogue access point wearing someone else's network name is a trap for their devices, and building one to catch strangers is wire fraud territory in a lot of places, not a prank.

I am not a lawyer, and this is not legal advice. Where I live, Malaysia's Communications and Multimedia Act 1998 covers unauthorised interception and improper use of network facilities, and most countries have an equivalent with similar teeth. If you are unsure whether your lab is a lab, treat it as not being one.

None of that makes the material less useful. The interesting work in wireless security is the same whether the target is your router or a stranger's. Build the detector before you build the attacker. Capture your own handshake and crack your own password. Run your own rogue AP and watch your own phone walk into it, then watch your own scan catch the twin. You will learn every layer twice, and the second time you will be the one who notices.

If you want the technique and not the lecture, the story starts at [wifi from zero](/wifi-from-zero/).
