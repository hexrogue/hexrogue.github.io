---
date: '2026-10-27T00:00:00+08:00'
title: 'SKC Advisor Chatbot'
description: 'Cloudflare Workers chatbot for WhatsApp admissions conversations, with memory and human handover.'
weight: 7
status: 'PRIVATE'
period: '2026'
stack: ['TypeScript', 'Cloudflare Workers', 'KV', 'OpenRouter', 'WhatsApp']
---

Private project. Source is not public. This is the outline I can share.

A WhatsApp-first admissions assistant for UNIRAZAK MBA and PhD programmes. It answers routine questions, keeps context across messages, and hands the conversation to a human advisor when the lead is ready.

## What I Built

- A Cloudflare Worker with a pipeline: inbound webhook, AI response, intent detection, outbound reply.
- A WhatsApp adapter layer so the provider can be swapped without rewriting the pipeline.
- Multi-provider AI support behind one interface.
- Per-user memory in Cloudflare KV.
- A handover flow: the model emits a marker, the outbound pipeline strips it, and the conversation is sent to the advisor API.
- HMAC-signed webhooks and a small test harness.

## Why It Is Interesting

The hard part is not the prompt. It is the plumbing: keeping a conversation stateful, handling provider failures, and making handover reliable when the model decides it is time to stop talking. The adapter and pipeline boundaries keep the WhatsApp, AI, and memory layers independent.

## Stack

TypeScript, Cloudflare Workers, Workers KV, OpenRouter and GPT, WhatsApp API, HMAC.
