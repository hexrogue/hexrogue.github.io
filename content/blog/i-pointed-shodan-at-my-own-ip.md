---
date: '2026-01-10T00:00:00+08:00'
title: 'I Pointed Shodan at My Own IP'
description: 'What the internet sees when it looks at you: open ports, chatty banners, and one port forward I forgot about.'
tags: ['security', 'homelab', 'networking']
---

Last month I searched for myself on the internet. Not my name. My IP address. What came back was a list of my open doors, written up neatly like a menu. I had published myself and never noticed.

## Shodan is Google for machines

Google indexes websites. Shodan indexes everything else: routers, cameras, servers, smart fridges with opinions. It knocks on every door on the internet, writes down who answers and what they say about themselves, and puts it in a search bar.

That greeting a device gives is called a banner. Hi, I am an SSH server, version 8.2, running on this box. Harmless small talk, until you realize that version has a known hole and now a stranger knows exactly which hole to try. Looking at Shodan is legal. It only reads greetings. Walking through the doors is a different story and not one I will tell here.

## Act one: the port I forgot

I typed in my own public IP and there it was: a media server port I forwarded two years ago for a movie night, left open ever since. Plus my router admin page waving its banner. Plus SSH announcing its version like a name tag at a conference. Three doors, all mine, all visible to everyone. Nobody had broken in. I had simply never closed up after the party.

<figure>
<img src="/images/memes/meme-shodan-trade.jpg" alt="Trade offer meme about port forwarding">
<figcaption>The port forwarding deal, signed by me.</figcaption>
</figure>

## Act two: the knocking never stops

Then I checked my router logs. Bots knock on port 22 all day and night, trying common usernames with common passwords, never sleeping, never bored. This is the background noise of the internet: thousands of hands trying every door handle. My door had a good lock, but a good lock on a door nobody needed is still a door. Every open port is a conversation with strangers. I was having three of them for no reason.

<figure>
<img src="/images/memes/meme-shodan-reaper.jpg" alt="Grim reaper meme about bots knocking on open ports">
<figcaption>3 AM. Knock knock. It is never the postman.</figcaption>
</figure>

## Act three: the quiet evening

The fix took one evening and zero genius. Killed the port forwards. Moved remote access behind WireGuard so the only way in is the encrypted tunnel. SSH keys only, passwords off. Fail2ban for the rude guests. Updated everything. A week later I searched my IP again and got silence. Silence is the goal. The best server on the internet is the one Shodan knows nothing about.

<figure>
<img src="/images/memes/meme-shodan-exit.jpg" alt="Highway exit meme about VPN versus port forwarding">
<figcaption>Took the boring highway. No regrets.</figcaption>
</figure>

> "The only winning move is not to play.", WarGames (1983). Me, closing port forwards instead of defending them.

## Attack yourself first

Do this tonight. Search your IP on Shodan. Close what you do not need. VPN what you do need. Keys, not passwords. Most break-ins are walk-ins through doors opened for convenience and forgotten by Friday. I know, because mine were.
