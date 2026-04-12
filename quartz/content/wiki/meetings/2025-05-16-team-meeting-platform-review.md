---
tags:
  - graph/leaf
---
# Meeting: Team Meeting — Platform Review, AI Models, Social Automation

**Type:** meeting
**Date:** 2025-05-16
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/2025-05-16-team-meeting-2025-05-16-09-28-cdt-notes-by-gemini]]
**Attendees:** Andrés Urrego, Adeleke Tolulope, Jacob Oluwole (Taiwo invited)
**Meeting type:** Team / engineering + product
**Related:** [[wiki/people/adeleke-tolulope]], [[wiki/people/jacob-oluwole]]

---

## Summary

Comprehensive review session covering the improved business plan generation pipeline, job posting feature bugs, social media automation via AI, Azure access issues, and plans for the interview tool MVP. Long meeting covering many topics.

---

## Key Decisions — AI Processing Pipeline

- New pipeline: processes section-by-section → uses initial user input + AI to generate executive summary + customer targets → builds full business plan with **o3-mini** model
- **Two-model division:**
  - **o4-mini** → Business Insights generation
  - **o3-mini** → Full business plan (detailed sections)
- Customer persona bug fixed: personas not being passed to o3-mini → now resolved
- Ability to upload existing business plan would speed up testing (requested)

---

## Key Decisions — Business Plan UX

- Zoom hint on competitor map: add explicit text "zoom in or out to see where your local competitors are located"
- Left menu in business insights: should remain open (currently collapses)
- Multiple business plans per user: **internal testing only** — in production, one active business plan per user (new business = new account)
- Preview button may be redundant — "view business insights" button is primary
- Plan display for subscriptions: purchased yearly plan should default to showing current plan, not showing "upgrade" everywhere

---

## Key Decisions — Social Media Automation

- **New idea approved:** Auto-generate social media job posts when a job is posted
  - Pull job info captured in Moil → use Grok AI to generate images from a template + logo
  - Adeleke: can be triggered automatically upon job creation
- This eliminates the need for manual social post creation for every job

---

## Key Decisions — Interview Tool

- MVP development can start **without a full design** — functionality test first, rough sketch is enough
- Add **"bi-weekly"** as a payment frequency option
- Job posting skill tests: make automatic (don't ask users "do you want to generate a skill test?" — just do it)

---

## Azure Access Issue

- Adeleke cannot access their Azure resources for the last 2 weeks
- Andres submitted a support case
- Resources should be displayed but are missing from login

---

## Client Testing

- Andres tested the platform with a woman client (created a new account the day before)
- Job matching failed immediately for her account — Adeleke to investigate

---

## Action Items

- [ ] Adeleke: Fix customer persona pipeline → pass personas correctly to o3-mini
- [ ] Adeleke: Add "zoom in/out" hint to competitor map
- [ ] Adeleke: Fix left menu (keep open in business insights)
- [ ] Adeleke: Fix plan display (default to current plan for subscribed users)
- [ ] Adeleke: Add "bi-weekly" payment frequency option
- [ ] Adeleke: Make skill test generation automatic on job post creation
- [ ] Adeleke: Resolve Azure access issue (support case submitted)
- [ ] Adeleke: Build social media job post automation (Grok + template on job creation trigger)
- [ ] Adeleke: Investigate job matching failure for new customer account
- [ ] Andres: Develop interview tool MVP (no-design approach)

---

## Connections

- [[wiki/moil/positioning]] — feature-rich platform maturing rapidly
- [[wiki/meetings/2025-05-14-jacob-andres-business-insights-review]] — insights review from 2 days earlier
