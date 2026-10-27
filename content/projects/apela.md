---
date: '2026-10-27T00:00:00+08:00'
title: 'APEL.A Admissions Portal'
description: 'A full APEL.A admissions portal: portfolio building, evidence, assessments, scheduling, payments, and candidate tracking. The first of its kind in Malaysia.'
weight: 1
status: 'PRIVATE CLIENT / FIRST IN MALAYSIA'
period: '2026 - PRESENT'
stack: ['Next.js', 'TypeScript', 'PostgreSQL', 'Drizzle', 'Better Auth', 'Puppeteer', 'Tailwind CSS']
---

Private client work. The source and candidate data are not public. This is the outline I can share.

APEL.A is Malaysia's prior-learning assessment route for experienced professionals. The brief was to build the first APEL.A admissions system in the country: one portal where a candidate can build a portfolio, upload evidence, sit an assessment, book an interview, pay, and track the decision without chasing a folder of PDFs.

## The Problem

The process was split across forms, email, spreadsheets, and staff memory. Candidates had to assemble a long portfolio from an official form. Assessors had to schedule exams and interviews across multiple calendars. Staff had to keep documents, payments, and status changes in sync. Every handoff was a place for something to go missing.

## What I Built

A single Next.js application with separate candidate, assessor, PIC, finance, and admin surfaces.

- **Candidate portal**: Google sign-in, application journey, document uploads, status tracking, notifications, interview booking, payment pages, receipts, and appeals.
- **APEL.A portfolio builder**: work experience, formal, non-formal, and informal learning, reflective statements, competency checklist, evidence uploads, referees, declaration, signature, and branded PDF generation.
- **Assessment operations**: exam scheduling, slot patterns, auto-assignment, assessor availability, interview proposals, candidate self-booking, and calendar views.
- **Exam integrity**: timed sessions, camera recording, live monitoring, proctoring signals, replay, manual marking, and result publication.
- **Finance**: fee enforcement, payment requests, receipts, CSV and Excel export, and finance analytics.
- **Admin and access control**: role-based permissions, per-user dashboard access, audit trails, email templates, programme catalogue, PIC workspaces, and read-only share links.

## The Hard Parts

- The official portfolio form is long and inconsistent. Turning it into a structured builder meant modelling the data properly, not just rendering a PDF. Autosave, validation, and amendment reasons had to work across a multi-step journey.
- Candidate and staff views share the same records but not the same permissions. The system had to make the next action obvious without leaking data across roles or across PICs.
- Exam integrity is a product problem as much as a technical one. The system records camera and proctoring signals, but it still has to leave the candidate enough room to finish the assessment.

## The Result

The admissions team works from one system instead of a chain of forms, inboxes, and spreadsheets. Candidates can see where they are. Assessors can see what they have to do. Finance can see what has been paid. The first APEL.A admissions system in Malaysia is running on the same codebase.

## Stack

Next.js 16, React 19, TypeScript, Tailwind CSS, Better Auth, Drizzle ORM, PostgreSQL, Puppeteer, pdf-lib, pagedjs, Nodemailer, Vercel Blob, and Recharts.

## Notes

Private client work, so there is no public repository or demo. The scope, architecture, and trade-offs are available in a conversation.
