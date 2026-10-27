---
date: '2026-09-20T00:00:00+08:00'
title: 'AdvisorNext'
description: 'Private stock analysis dashboard with a weighted scoring engine across technical indicators.'
weight: 6
status: 'PRIVATE'
period: '2026'
stack: ['Next.js', 'TypeScript', 'Prisma', 'PostgreSQL', 'TanStack Query']
---

Private project. Source is not public. This is the outline I can share.

## The Problem

Technical analysis across a watchlist is repetitive and easy to do inconsistently. One person looks at momentum, another looks at trend, a third ignores both and goes with a feeling. The goal was not to predict the market. The goal was to make the same inputs produce the same verdicts.

## What I Built

A dashboard that scores a watchlist against a fixed set of technical indicators:

- A weighted scoring engine across eight indicators.
- Automatic watchlist scans that produce BUY, SELL, or HOLD verdicts.
- A data model that keeps the inputs, scores, and verdicts traceable.
- A dashboard designed for quick comparison, not for pretending a chart is a guarantee.

## The Result

The analysis is consistent, repeatable, and inspectable. The score is not magic and it is not financial advice. It is a deterministic opinion built from the indicators it was given, which is a much more honest product than a black box with a green arrow.

## Stack

Next.js, TypeScript, Prisma, PostgreSQL, TanStack Query.

## Notes

Private project, so there is no public demo. The scoring model is intentionally rule-based and explainable.
