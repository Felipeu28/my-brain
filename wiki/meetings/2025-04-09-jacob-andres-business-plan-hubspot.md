---
tags:
  - graph/leaf
---
# Meeting: Jacob & Andrés — Business Plan Refinement + HubSpot + Google→Microsoft Migration

**Type:** meeting
**Date:** 2025-04-09
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/2025-04-09-jacob-andres-2025-04-09-08-44-cdt-notes-by-gemini]]
**Attendees:** Andrés Urrego, Jacob Oluwole, Adeleke Tolulope, Taiwo Ola-Balogun
**Meeting type:** 1:1 + team / product + operations
**Related:** [[wiki/people/jacob-oluwole]], [[wiki/people/adeleke-tolulope]]

---

## Summary

Three focus areas: (1) business plan creator question refinement, (2) HubSpot CRM lead management, and (3) migration from Google Workspace to Microsoft 365. Also: matching algorithm fixes confirmed pushed to production.

---

## Key Decisions — Business Plan Creator

- **Hybrid question approach:** Use Set 2 (concise questions) as the primary interface; Set 1 (detailed) as optional expansion — let AI enrich with research
- Test both sets with ChatGPT: which produces the better business plan with minimal user input?
- Financial questions need improvement — current version yields fabricated answers
- **Template needed:** consistent structure defining order of sections
- Deliver plans in PDF and Word formats
- Adeleke to handle backend adjustments for new questions / key-value pairs

---

## Key Decisions — Matching Algorithm

- Adeleke confirmed: matching tool improvements pushed to production (experience-based ordering)
- Based on Jacob's previous suggestion — algorithm fix is live

---

## Key Decisions — HubSpot (CRM)

- Andres intended to upload ~65-70 leads (received from Jacob) into HubSpot
- **Lead quality issue:** ~20% dropout rate at personal information stage
- Jacob had view-only permissions → Andres fixed to give edit access
- Moil is on the **free HubSpot plan** → can't automate emails
- Jacob to contact users individually (manual outreach until paid plan)
- Andres considering having Jacob learn HubSpot email functionality

---

## Key Decisions — Google to Microsoft Migration

- **Google Workspace being shut off due to storage + collaboration costs**
- Migrating to:
  - **Outlook** for email
  - **OneDrive** for file storage
  - **Microsoft Teams** for communication
- Deadlines for Google shutdown discussed (challenging due to data lock-in)
- Microsoft pricing tiers reviewed; Azure credits could help offset costs

---

## User Data Discovery

- Multiple user lists exist with inconsistent numbers:
  - One list = users who completed full profile creation
  - Others = users who only provided email or phone at signup
- Adeleke confirmed email collected for ALL signups; phone numbers not yet collected
- Andres requested list of incomplete-profile users for follow-up email campaign

---

## Action Items

- [ ] Adeleke: Test revised hybrid prompt; push to production; share results
- [ ] Adeleke: Create consistent business plan template (section order, content)
- [ ] Andrés: Work on UI/UX design for additional business plan screens
- [ ] Jacob: Contact users individually from HubSpot list
- [ ] Jacob: Learn HubSpot email automation for future campaigns
- [ ] Jacob: Investigate Microsoft migration process (consult ChatGPT for steps)
- [ ] Team: Migrate from Google Workspace to Microsoft 365 before Google shuts off
- [ ] Andres/Adeleke: Fix OpenAI API key configuration issue (compare to Grok implementation)

---

## Connections

- [[wiki/moil/gtm]] — HubSpot CRM, lead management
