---
tags:
  - graph/leaf
---
# Meeting: Team Meeting — AI Model Selection & Workforce Capital Partnership

**Type:** meeting
**Date:** 2025-01-22
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/2025-01-22-team-meeting-2025-01-22-09-29-cst-notes-by-gemini]]
**Attendees:** Andrés Urrego, Jacob Oluwole, Adeleke Tolulope (Steve), Taiwo Ola-Balogun, Abiodun Solomon
**Meeting type:** Team / engineering + strategy
**Related:** [[wiki/people/jacob-oluwole]], [[wiki/people/adeleke-tolulope]], [[wiki/people/abiodun-solomon]], [[wiki/people/taiwo-ola-balogun]]

---

## Summary

Weekly team meeting focused on two tracks: (1) selecting the right AI model for code integration in Moil, and (2) a strategic partnership opportunity with Workforce Capital Solutions (a $15–20M workforce development org). Also included sign-up UX improvements.

---

## Key Decisions

- **AI model selection:** Prioritize DeepSeek R1 (efficient, open-source) over Polycoder, Code T5, and SantaCoder; smaller models suit their limited codebase
- **Deployment options:** Azure GPU (for team access) vs. quantized model (local use) — both being evaluated
- **Collaboration protocol:** Adeleke (Steve) to guide Taiwo through fine-tuning AFTER successfully completing a model — no redundant parallel work
- **Admin dashboard:** Use AI/MongoDB queries instead of building a complex UI
- **Sign-up UX:** Simplify to two clear "pills" — phone number OR email. US numbers → SMS, non-US → WhatsApp
- **Azure credits:** Use off-peak hours to optimize training cost

---

## Strategic Signal — Workforce Capital Solutions

Andres has a meeting with the CEO of Workforce Capital Solutions (facilitated by a congresswoman referral). The org handles workforce development and recently completed an AI course. Contract value: **$15–20 million**. Their vision statement aligns strongly with Moil. Opportunities discussed:
- Job postings through Moil platform
- Teaching/training opportunities
- White-labeled solutions

---

## Action Items

- [ ] Adeleke: Select AI model immediately (DeepSeek R1 priority) and begin training
- [ ] Adeleke: Guide Taiwo through fine-tuning process after completing a model
- [ ] Adeleke/Taiwo: Investigate MongoDB efficient querying for admin dashboard
- [ ] Jacob: Pause staging server when not actively testing (cost savings)
- [ ] Andres: Remove authenticator from NVIDIA account, share password with developers
- [ ] Team: Explore mobile app development once model is trained
- [ ] Future: Build user management / hierarchies for business accounts

---

## Key Quotes

> "Prioritize speed over eliminating all potential mistakes." — Andrés

---

## Team Roster Confirmed

- **Andrés** — CEO/founder
- **Jacob Oluwole** — Project Manager
- **Adeleke Tolulope (Steve)** — Lead engineer / AI
- **Taiwo Ola-Balogun** — Engineer
- **Abiodun Solomon (Ablad)** — Designer

---

## Links

- [[wiki/people/jacob-oluwole]]
- [[wiki/moil/positioning]]
