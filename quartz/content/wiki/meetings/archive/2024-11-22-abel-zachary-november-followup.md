---
tags:
  - graph/leaf
---
# Abel Zachary — November Follow-Up Call

**Type:** meeting
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/transcript-2024-11-22-abel-and-andr-s-follow-up-november.md]]
**Related:** [[wiki/people/jacob-oluwole]], [[wiki/people/adeleke-tolulope]], [[wiki/moil/customers]]

---

## Summary

Andres held a follow-up call with Abel Esquivel Luna from Zachary Corporation (Moil's first major client, $699/yr). The session included Jacob and Steve reviewing Moil's platform against a competitor (Skilly), identifying UX improvements, and planning multi-user/hierarchy features for enterprise business accounts. Abel's feedback informed key product decisions around the employer experience.

## Key People

- **Abel Esquivel Luna** — Contact at Zachary Corporation (abel.luna@zachrycorp.com); champion for Moil within Zachary; attends industry conferences and offered to refer other companies
- **Andres Urrego** — Led the call
- **Jacob Oluwole** — PM, participated
- **Adeleke Tolulope (Steve)** — Lead AI/ML engineer, participated

## Competitor Analysis: Skilly

Andres walked the team through Skilly (competitor focused on construction sector workers in FL, TX, GA):
- 5,000+ craft professionals; automatic resume creation; rigorous worker profiles
- 80% response rate claimed; 10 days to job offer
- Assessment feature for skilled workers (certifications displayed on profiles)
- Missing: Spanish language — **Moil advantage**
- Founded ~2021/2022 — 3-4 years ahead of Moil in product maturity

**Key takeaways:** Moil needs assessments tab, help center videos, certifications on profiles. Spanish is a major differentiator Skilly doesn't have.

## Product Decisions

1. **Employer-side UX problem** — Abel had been on Moil 50+ times but never noticed the "Switch to Business" option. Action: Make the business/candidate toggle much more prominent.
2. **User hierarchy for enterprise** — Need Admin vs. User roles for business accounts. Admin: full access; User: view/communicate only. Build invite-by-email system for business sub-users.
3. **Assessments tab** — Create basic skill assessments for the 20 most common jobs on the platform. Show completed assessments on candidate profiles.
4. **Certifications field** — Add industry certifications (construction trades) to profiles; auto-suggest based on job title.
5. **Automated job image creation** — Zachary has 40-50 jobs; manual design is unsustainable. Need template system (20 templates by industry) + OpenAI/Canva API automation.

## Action Items

- [ ] Make "Switch to Business" toggle impossible to miss (UX priority)
- [ ] Build user hierarchy: Admin + User levels with email invite
- [ ] Build assessments tab with top 20 job types
- [ ] Add certifications field to candidate profiles
- [ ] Research automated job post image generation pipeline (Canva API + OpenAI summarize → template overlay)
- [ ] Abel will connect Andres to conferences where Moil can exhibit

## Customer Intelligence

- Abel is a loyal champion — offering conference introductions, actively engaged
- Zachary Corporation posting 40-80+ jobs through Moil
- Abel's engagement rate validates the $699/yr plan for enterprise-scale clients
- Pain point: employer-side UX still too complex for non-technical business users

## Moil Relevance

This is the deepest customer feedback session captured. Abel's engagement (80+ jobs, conference referrals) validates Moil's product-market fit in the construction sector. The UX issues identified here (business/candidate toggle, user hierarchy) are highest-priority enterprise product improvements.
