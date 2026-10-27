---
date: '2026-10-27T00:00:00+08:00'
title: 'SKC Central'
description: 'Internal operations platform for a private education group: finance, scheduling, teaching records, and admin.'
weight: 5
status: 'PRIVATE CLIENT'
period: '2026 - PRESENT'
stack: ['Next.js', 'TypeScript', 'PostgreSQL', 'Drizzle', 'Better Auth', 'TanStack Table', 'Recharts']
---

Private client work. Source and business data are not public. This is the outline I can share.

SKC Central is the internal operations platform behind a private education group. It brings finance, scheduling, teaching records, and admin into one Next.js application, so staff stop moving the same student data between spreadsheets and browser tabs.

## The Problem

The group runs programmes, lecturers, agents, payments, commissions, timetables, and teaching files across several teams. The data lived in spreadsheets, exported reports, and a scheduling app that only covered one slice of the problem. Every team had its own version of the truth.

## What I Built

- **Finance**: fee schedules, payments, slips, collections, commissions, PIC payouts, student accounts, and CSV and Excel export.
- **Scheduling**: semesters, subjects, venues, lecturers, timetable publishing, clash detection, and student-level timetable checks.
- **Teaching operations**: courses, course cards, lecturer records, ODL lecturer data, teaching files, pre-recorded claims, TVAL, and analytics.
- **Admin**: user management, roles, audit log, file linking, portal review, and traceability.
- **Integrations**: Excel imports, UROX roster sync, Canvas sync, Google sign-in, and Vercel Blob storage.

## The Hard Parts

- The scheduling module started as a standalone timetable and clash detector. Folding it into the wider platform meant keeping the data model and the permissions coherent while the scope grew.
- Finance data is unforgiving. The importers had to handle inconsistent spreadsheets, and the interface had to make the current state obvious without hiding where a number came from.
- Every table needed real pagination, filtering, and detail pages. Internal tools are used all day, so small friction compounds.

## The Result

One staff platform instead of a collection of spreadsheets and single-purpose apps. The teams can see the same student, payment, and timetable records, and the audit trail makes it clear who changed what.

## Stack

Next.js, TypeScript, PostgreSQL, Drizzle ORM, Better Auth, TanStack Table, Recharts, ExcelJS, Vercel Blob, and the usual Linux and Docker deployment plumbing.

## Notes

Private client work. No public repository or demo.
