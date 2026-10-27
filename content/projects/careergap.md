---
date: '2026-09-20T00:00:00+08:00'
title: 'CareerGap'
description: 'Private deterministic skill-gap analyzer against ESCO occupation requirements.'
weight: 4
status: 'PRIVATE'
period: '2026'
stack: ['Next.js', 'TypeScript', 'Drizzle', 'PostgreSQL']
---

Private project. Source is not public. This is the outline I can share.

## The Problem

Most skill-gap tools are either a keyword match with a nicer font or a language model asked to guess. Neither gives a candidate a clear, reproducible answer to a simple question: which requirements for this occupation are actually missing?

## What I Built

A deterministic analyzer that compares a candidate's skills against occupation requirements from ESCO:

- Rule-based matching with explicit criteria, not a model with a confident tone.
- A weighted gap score that separates missing skills from weak evidence.
- A result view that shows what is missing and why it matters for the occupation.
- No AI in the scoring path. The same inputs produce the same output, every time.

## The Result

The output is explainable. A candidate can see which requirements are covered, which are missing, and which need stronger evidence. The system does not pretend to know whether someone can do the job. It shows the gap between the profile and the occupation data, which is a narrower and more honest claim.

## Stack

Next.js, TypeScript, Drizzle, PostgreSQL.

## Notes

Private project. The interesting design constraint was keeping the scoring deterministic while still making the result useful to a human.
