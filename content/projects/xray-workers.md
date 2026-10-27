---
date: '2026-09-20T00:00:00+08:00'
title: 'Xray Workers'
description: 'Serverless VLESS proxy system on Cloudflare Workers with D1 user management.'
weight: 9
status: 'OPEN SOURCE'
period: '2026'
stack: ['TypeScript', 'Cloudflare Workers', 'D1']
---

Open source: [github.com/hexrogue/xray-worker](https://github.com/hexrogue/xray-worker).

A VLESS proxy system on Cloudflare Workers with user management backed by D1. Edge-deployed, no servers to manage, no VPS to patch at 2 AM.

## The Problem

Personal infrastructure should be boring to operate. A VPS gives you control and then asks for it back in the form of updates, certificates, logs, and an alert at the worst possible time. The edge is a better fit for a small proxy: deploy it, forget it, and let someone else own the server.

## What I Built

- VLESS proxy connections handled by Cloudflare Workers.
- D1-backed user management and subscription logic.
- A deployment model with no traditional server, no OS updates, and no reboot button to find.
- A small enough surface that the whole thing can be understood in one sitting.

## The Result

A personal proxy that runs at the edge with almost no operational overhead. The trade is control: you are depending on a platform, and the platform has opinions. For this use case, that is a good trade.

## Stack

TypeScript, Cloudflare Workers, D1.

## Notes

Open source, so the code and the rough edges are public.
