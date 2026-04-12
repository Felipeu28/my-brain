---
tags:
  - graph/leaf
---
# Meeting: Team Meeting — Sign-up Redesign + Business Plan Creator MVP

**Type:** meeting
**Date:** 2025-03-12
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/2025-03-12-team-meeting-2025-03-12-05-09-cdt-notes-by-gemini]]
**Attendees:** Andrés Urrego, Jacob Oluwole, Taiwo Ola-Balogun, Adeleke Tolulope, Abiodun Solomon
**Meeting type:** Team / product design + engineering
**Related:** [[wiki/people/jacob-oluwole]], [[wiki/people/adeleke-tolulope]], [[wiki/people/taiwo-ola-balogun]], [[wiki/people/abiodun-solomon]]

---

## Summary

Two major topics: (1) redesigning the sign-up page for clarity and (2) planning the **Business Plan Creator** — a new Moil feature. Andres proposed building the Business Plan Creator by reusing the resume builder's components (copy-paste + reimagine strategy).

---

## Key Decisions — Sign-up Redesign

- Simplified to **3 clear options**: Google, phone number, email
- Only the selected option expands — no accordion chaos, no redundant text
- Manual translation for landing, signup, and signin pages (supplement Google Translate)
- US numbers → SMS verification; non-US → WhatsApp
- Jacob to collect current landing page text, send to Andres for review and revision
- Goal: persuasive copy, not just descriptions

---

## Key Decisions — Business Plan Creator

- **Architecture:** Reuse resume builder components — same flow, same design, copy-paste + reimagine with business questions
- **Conversational flow:** Welcome → AI-guided questions (20-25 total) → pre-fill known data (company name, city, phone, email) → editable preview → downloadable Word/PDF
- **Two AI layers:** one for text generation (DeepSeek or ChatGPT), one for real-time market data (Gemini / Google)
- **Business stages:** "Idea/Planning" vs. "Growing" — tailors financial projections accordingly
- Voice OR text answer options maintained
- Question count to test: 15, 25, and 40 questions to find optimal length
- Sections: intro, business overview, market + competitors, team structure, marketing + sales, financial overview, industry trends, competitive edge

---

## Action Items

- [ ] Jacob: Collect landing page text → send to Andres for revision
- [ ] Andres: Review and rewrite landing page copy
- [ ] Andres: Build Business Plan Creator MVP using resume builder as scaffold
- [ ] Abiodun (Ablad): Begin design for Business Plan Creator (same design system)
- [ ] Adeleke: Backend integration for question-answer → AI generation pipeline

---

## Key Quotes

> "I got to get the girls ready soon." — Andres (morning context: 6 AM meetings with family)

---

## Product Intelligence

- Moil's tech stack confirmed: Node.js, Express.js, React.js, Python (scraping + recommendations), Redis caching
- Resume builder already fully complete — now being repurposed as Business Plan Creator scaffold
