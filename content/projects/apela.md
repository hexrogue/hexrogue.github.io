---
date: '2026-10-27T00:00:00+08:00'
title: 'APEL.A Admissions Portal'
description: 'The first APEL.A admissions portal in Malaysia: a 23-step workflow, a structured portfolio builder, payments, and an exam integrity engine that runs MediaPipe face detection in the browser.'
weight: 1
status: 'PRIVATE CLIENT / FIRST IN MALAYSIA'
period: '2026 - PRESENT'
stack: ['Next.js', 'TypeScript', 'PostgreSQL', 'Drizzle', 'Better Auth', 'MediaPipe', 'WebRTC', 'Puppeteer', 'Tailwind CSS']
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

## Exam Integrity

The biggest single piece of the system. A sitting has to be watchable without a human staring at a video wall, and whatever it produces has to survive a dispute months later.

- **Detection runs in the candidate's browser.** The exam runner reads the camera stream with MediaPipe and flags no face, multiple faces, a turned head, a phone, and a book. There is no inference server to operate and no video has to leave the candidate's machine for detection to work.
- **Signals are scored, not asserted.** Every event carries a confidence score, gets de-duplicated so one head turn does not become forty rows, and is stored with a JPEG snapshot captured at the same moment.
- **A human still decides.** Signals never end a sitting and never fail an attempt on their own. Staff review them before a result is published. Only repeated tab-switch and fullscreen violations terminate a session.
- **Live proctoring runs on the same session.** Camera and microphone publish over WebRTC and staff subscribe while the sitting is in progress. It uses STUN by default and joins TURN only when the server provisions it, with a STUN-only fallback so the camera never hard-fails. Recorded chunks stay available for replay, and exam chat is kept with the session.

## Under the Hood

The parts I would talk about in an interview:

- **One workflow engine, not a pile of screens.** The APEL.A process runs 23 steps across application, payment, aptitude, portfolio, interview, and completion. Each step declares its stage, the actor expected to move it forward, and whether entering it should notify the candidate. Transitions are validated, so a case cannot skip payment or jump to an interview, and every change lands in an audit trail with the actor, role, and remarks.
- **Permissions that only narrow.** Nine roles, from candidate to superadmin. A per-user override can remove a section but cannot add one the role does not already have, and every API route re-checks the session on the server instead of trusting the UI.
- **Payments with a manual floor.** ToyyibPay FPX handles online payment when the owner enables it, with callbacks matched by an external reference. When it is off, candidates upload proof and finance verifies it. Receipts are generated as PDFs either way.
- **The official form, as data.** The portfolio is structured, not a scanned form: work experience, formal and non-formal learning, evidence, referees, declaration, and signature. Export renders the official layout, merges uploaded evidence PDFs with labelled appendix pages, and compresses images to stay under the function payload limit.
- **Two guides, one source.** The public applicant guide and the staff guide are built from one Docusaurus source tree. A build guard fails the deploy if a staff route, heading, link, or search-index entry reaches the public site.

For scale: 101 API route handlers, 45 database tables, 46 versioned migrations, and 106 components.

## The Hard Parts

- The official portfolio form is long and inconsistent. Turning it into a structured builder meant modelling the data properly, not just rendering a PDF. Autosave, validation, and amendment reasons had to work across a multi-step journey.
- Candidate and staff views share the same records but not the same permissions. The system had to make the next action obvious without leaking data across roles or across PICs.
- Exam integrity is a product problem as much as a technical one. The system records camera and proctoring signals, but it still has to leave the candidate enough room to finish the assessment.

## The Result

The admissions team works from one system instead of a chain of forms, inboxes, and spreadsheets. Candidates can see where they are. Assessors can see what they have to do. Finance can see what has been paid. The first APEL.A admissions system in Malaysia is running on the same codebase.

## Stack

Next.js 16, React 19, TypeScript, Tailwind CSS, Better Auth, Drizzle ORM, PostgreSQL, Puppeteer, pdf-lib, pagedjs, Nodemailer, Vercel Blob, Recharts, MediaPipe, WebRTC, ToyyibPay, and Docusaurus.

## Notes

Private client work, so there is no public repository or demo. The scope, architecture, and trade-offs are available in a conversation.
