---
tags:
  - graph/leaf
---
# Meeting: Jacob & Andrés — Business Insights Review (Automobile Repair Test)

**Type:** meeting
**Date:** 2025-05-14
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/2025-05-14-jacob-andres-2025-05-14-08-28-cdt-notes-by-gemini]]
**Attendees:** Andrés Urrego, Adeleke Tolulope (Steve)
**Meeting type:** 1:1 / product review
**Related:** [[wiki/people/adeleke-tolulope]]

---

## Summary

Section-by-section review of Moil's Business Insights output (tested with a "Rockstar" automobile repair shop in Round Rock, TX). Andres gave detailed feedback on each component. Meeting title says "Jacob & Andrés" but Jacob doesn't appear — Adeleke (Steve) was the primary attendee.

---

## Product Under Review

**Business Insights feature** — auto-generates market analysis, customer personas, competitor maps, financial projections, and a SWOT matrix from a business plan.

Key setup: Adeleke using Postman as API software to extract business insights into a document.

---

## Section-by-Section Feedback

| Section | Status | Key Feedback |
|---|---|---|
| Product Summary | Good | Check audience alignment with business plan |
| Business Model | Good | Need breakdown of key resources (why 10 diagnostic tools?) |
| Customer Personas | Good | Lifestyle, age, income, occupation, location all included; images being reused correctly |
| Market Size (TAM/SAM) | Needs Fix | 112B TAM and 11.2B SAM figures seem incorrect; need validation |
| Industry Trends | Good | Online scheduling, sustainability, customer education |
| Underserved Niches | Good | Display format works (grouped boxes) |
| SWOT Matrix | Improved | Mitigation strategies could be more comprehensive |
| Cost Structure | Fix Needed | Allow users to personalize fixed/variable costs with dropdown |
| Milestones | Fix Needed | Users should mark as complete/in-progress → trigger new milestone generation |
| Competitor Map | Relocate | Move from market/audience page to competitor page — so users can see competition density when deciding store location |

---

## Key Insights

- AI fills details not explicitly in the business plan via research (Adeleke confirmed)
- Image generation: AI reuses stored images that match customer personas (efficient)
- Grok credits being used for image generation — save images before they expire
- Competitor map use case: "you could literally make a decision on where to put your store" — powerful feature when properly placed

---

## Action Items

- [ ] Adeleke: Export results + compare business plan vs. business insights section by section
- [ ] Adeleke: Fix TAM/SAM calculation — validate or show text instead of incorrect chart
- [ ] Adeleke: Move competitor map from market/audience page to competitor page
- [ ] Adeleke: Add cost structure personalization (dropdown for fixed/variable costs)
- [ ] Adeleke: Add milestone completion/progress tracking → auto-generate new milestones
- [ ] Adeleke: Add descriptions for initial capital allocation categories
- [ ] Adeleke: Hide "suggestions" element until a proper suggestions screen exists
- [ ] Andres: Mass-test image generation (send prompts in bulk to build image pool)

---

## Key Quotes

> "We could even tell them where to put their business based on market analysis — recommend locations with lower competition density." — Andrés (vision for competitor map feature)

---

## Connections

- [[wiki/moil/positioning]] — Business Insights as a key differentiator
