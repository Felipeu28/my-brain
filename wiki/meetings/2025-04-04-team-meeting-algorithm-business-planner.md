---
tags:
  - graph/leaf
---
# Meeting: Team Meeting — Job Matching Algorithm + Business Planner UX

**Type:** meeting
**Date:** 2025-04-04
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/2025-04-04-team-meeting-2025-04-04-08-39-cdt-notes-by-gemini]]
**Attendees:** Andrés Urrego, Jacob Oluwole, Adeleke Tolulope, Taiwo Ola-Balogun, Abiodun Solomon
**Meeting type:** Team / product + engineering
**Related:** [[wiki/people/jacob-oluwole]], [[wiki/people/adeleke-tolulope]], [[wiki/people/abiodun-solomon]]

---

## Summary

Product-heavy meeting covering: job matching algorithm improvements (weighted approach), business plan creator enhancements, UI/UX polish, mobile app feasibility, and a significant partnership signal — a potential UTSA license deal for the Business Plan Creator.

---

## Key Decisions — Job Matching Algorithm

- **Problem:** Construction manager resume was matching "plumber" as top result — algorithm was purely title-based with no prioritization
- **Fix:** Weighted algorithm prioritizing:
  1. Most recent job experience
  2. Top stated preference
  3. Skills
- Adeleke confirmed this is being implemented

---

## Key Decisions — Business Plan Creator

- Larger text boxes needed (textarea > input fields) — Taiwo estimated 1-2 hours to fix
- Loading indicator bug: doesn't show after button click — users abort → UX fail
- **Different question sets** by business stage: new / established / growing
- Add "year founded" and other missing fields
- Competitor analysis prompt needs refinement (currently weak)
- Fix output consistency — some plans too short, some too long; aim for ~4 pages
- Jacob to create a Moy business plan using the tool as a test

---

## Key Decisions — UI/UX

- Gray text needs to be darker for readability
- Microphone icon placement needs to be consistent
- Animate the voice input element (moving/pulsing)
- Mobile business planner: remove text from bottom bar (too cramped)

---

## Strategic Signal — UTSA License Deal

> Andres met with someone from the **economic development corporation** who offered to connect Moil with **University of Texas San Antonio (UTSA)** to potentially **license the Business Plan Creator**.

Discussed options:
- License to UTSA
- License to the city
- Broader institutional licensing (EDCs, chambers, etc.)

---

## Operational Decision — Migration to Microsoft Teams

- Google Workspace credits expiring → migrating to Microsoft Teams for team communication
- MS Teams has simultaneous translation feature (benefit for international team)

---

## Client Intelligence — Sakuri Corporation

- Jacob had only posted a subset of Sakuri's available jobs
- Andres stressed: post ALL available jobs — this is what the client is paying for
- Job posting strategy: create spreadsheet, organize by proximity to major cities for social media campaigns, post across multiple platforms

---

## Action Items

- [ ] Adeleke: Implement weighted job matching algorithm
- [ ] Adeleke: Fix loading indicator bug for business plan generator
- [ ] Adeleke: Update business plan text areas (textarea > input)
- [ ] Taipei/Taiwo: Fix mobile business planner bottom bar
- [ ] Jacob: Create Moy business plan in tool, review competitor analysis
- [ ] Jacob: Create videos showcasing business plan creator + job posting features
- [ ] Team: Integrate payment system (next priority)
- [ ] Team: Investigate converting web app to mobile app (platform for conversion)
- [ ] Jacob: Post ALL Sakuri Corporation Texas jobs; organize by city proximity

---

## Key Quotes

> "I mean we have to think about school presentations, career fair involvement, connecting students with internship opportunities." — Andrés (new distribution channel emerging)

---

## Connections

- [[wiki/moil/gtm]] — UTSA license deal signals new B2B/institutional channel
- [[wiki/moil/positioning]] — AI tools pivot now has school/education use case
