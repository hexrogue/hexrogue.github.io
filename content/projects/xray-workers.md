---
date: '2026-09-20T00:00:00+08:00'
title: 'Xray Workers'
description: 'VLESS proxy system on Cloudflare Workers. Edge-deployed, no servers.'
---

Open source: [github.com/hexrogue/xray-worker](https://github.com/hexrogue/xray-worker).

VLESS proxy system on Cloudflare Workers with user management backed by D1. Edge-deployed, no servers to manage.

The point was personal infrastructure: secure tunneling without maintaining a VPS. Workers handle the connections at the edge, D1 holds the user data, and there is nothing to patch or reboot.

## Stack

TypeScript, Cloudflare Workers, D1.
