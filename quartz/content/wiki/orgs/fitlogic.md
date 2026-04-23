---
github_repo: Moil-Landingpages/fit-logic
tags:
  - graph/hub
owner: "[[wiki/people/megan-miller]]"
status: active
last_contact: 2026-04-21
---
# FitLogic Functional Medicine

**Type:** organization
**Last updated:** 2026-04-22
**Source:** [[raw/teams-2026-04-12]], [[raw/email-history-2months-2026-04-12]], [[raw/github-project-tracker.md]], [[raw/teams-2026-04-21]], [[raw/teams-transcript-megan-miller-2026-04-21]], [[raw/email-digest-2026-04-20]]
**Related:** [[wiki/people/megan-miller]], [[wiki/moil/customers]], [[wiki/moil/pipeline]], [[wiki/concepts/moil360]], [[wiki/meetings/2026-04-21-megan-fitlogic-working-session]]

---

## Summary

Fit Logic Functional Medicine is a solo-NP functional medicine clinic owned by [[wiki/people/megan-miller|Megan Miller, NP]] — hormone optimization, women's health, chronic-condition functional medicine. **Anchor Moil 360 customer** — onboarded onto CRM Apr 21, 2026 in a 89-minute hands-on working session. Trust depth is above average: Megan handed Andres her GoDaddy credentials for `fitlogicfunctionalmedicine.com` during the first CRM call.

Dual product surface: (a) hiring via Moil job postings (first Moil-sourced hire imminent as of Apr 12); (b) Moil 360 full stack — CRM, campaigns, sequences, site deployment, soon a native quiz. An external vendor, **Electric Bricks**, is mid-redesign of the clinic website; Moil is waiting for them to ship before layering CRM forms on top.

Domain: `fitlogicfunctionalmedicine.com` (GoDaddy). Sending address to be: `Megan@fitlogicfunctionalmedicine.com`.

## Deal Status

- **Moil hiring:** ✅ Active — first hire imminent as of Apr 12, 2026; second job posted Apr 12
- **Moil 360 CRM:** 🟡 Onboarded Apr 21, 2026 — live tour complete, deployment tonight
- **Website:** External vendor Electric Bricks mid-redesign; Moil layer comes after they ship
- **Payment plan ask (Apr 19, 2026):** Megan emailed asking to switch from **$500/mo × 3 to $250/mo × 6** — same total, stretched. Needs a revenue/collection decision + reply ([[raw/email-digest-2026-04-20]])

## Apr 21 Working Session — Key Decisions

See [[wiki/meetings/2026-04-21-megan-fitlogic-working-session]] for full transcript and context.

1. **Sales CRM stays separate from patient CRM.** Megan keeps Keap for patient records; Moil is sales pipeline + outbound only.
2. **Plain-text cold outreach, 50/day throttle, 3-email-over-6-days default sequence.** Avoids spam jail, feels personal.
3. **Deploy Moil CRM at `fitlogicfunctionalmedicine.com/CRM`** — tonight (Apr 21) using Megan's GoDaddy login.
4. **Wire `Megan@fitlogicfunctionalmedicine.com` as sender** — replaces `partners@moilapp.com` which lands in spam.
5. **100-lead validation test before mailing the full 5,000-contact list.**
6. **Native Moil quiz replaces Thrive Quizzes WordPress plugin** — built after Electric Bricks delivers the site redesign.
7. **Wait for Electric Bricks before Moil touches their code** (per-change fees too high).
8. **Push-back on Electric Bricks redesign** — too text-heavy, too busy, too similar to current site; Andres drafted formal blocker-list email (alt-text missing sitewide, no H1 on homepage, chiro-themed blog URL slugs) — Megan forwards it as the punch list.

## Apr 21 Product Feedback From FitLogic

The most concentrated customer feedback on Moil 360 to date. All items sourced from Megan, the single Moil 360 user under test:

| Issue | Type | Status |
|---|---|---|
| `partners@moilapp.com` lands in Gmail spam | Deliverability blocker | Workaround tonight: custom sender domain |
| Campaign link returned 404 (test email) | Wiring bug | Fix during tonight's deployment |
| Cannot switch "stuck" business plan once assigned | Core product bug | Hit her weeks ago; resurfaced Apr 21 — 20+ min debug with Jacob/Andres/Adeleke |
| Campaign link editing lives only in sequences, not campaigns | Feature-parity gap | Feature-parity audit warranted |
| Per-campaign click-rate dashboard not clearly surfaced | Feature ask | Partly visible; surface cleanly |
| Duplicate-contact detection on CSV import | Parity with Keap | Confirmed supported by Moil |
| Sequences feature | 🟢 Killer feature | "This is what I've been wanting" |

## Electric Bricks — External Website Vendor

External agency (not Moil) redesigning `fitlogicfunctionalmedicine.com`. Problem pattern:

- **Too text-heavy, too busy** — "Nobody will read this" (Andres)
- **Sitewide alt-text missing** — SEO and accessibility failure
- **No H1 on homepage**
- **Three blog posts have chiropractic-themed URL slugs** — wrong vertical, Megan is functional medicine, not chiro
- **FAQ collapsed into service pages** instead of being its own page
- **Per-change fees too high** — makes Electric Bricks unusable for small iterations

**Moil's play:** wait for Electric Bricks to finish, then layer the CRM form, quiz form, and `/CRM` route on top. If they can't deliver Andres's punch list, Megan asks for a refund.

## GitHub Projects

- [Moil-Landingpages/fit-logic](https://github.com/Moil-Landingpages/fit-logic) — client landing page (last push Apr 11, 2026 🟢)

## Contacts

- **Megan Miller, NP** — owner, primary Moil contact — [[wiki/people/megan-miller]]
- **Michelle** — clinic staff, in early clinical training (months before fully ramped)
- **Lori, Cassandra** — clinic staff (briefly mentioned)

## Workshop (Joint)

Megan and Andres co-planning a workshop — timing tight, Megan told one interested person, Andres has only mentioned it to Justin K. Push or postpone decision pending.

## Moil Relevance

FitLogic is the **flagship Moil 360 case study candidate for H1 2026.** Three reasons:
1. **Trust depth** — GoDaddy credentials on the first CRM call is rare.
2. **Full product surface** — hiring + CRM + campaigns + sequences + website + (eventually) native quiz — covers more Moil 360 surface area than any other customer.
3. **Vertical fit** — solo-practitioner healthcare is a target ICP where Moil's "personal clinic assistant" story resonates; the sequences killer-feature reaction confirms product-market fit for the nurture use case.

First Moil customer to make a Moil-sourced hire (announced Apr 12). First Moil 360 customer to complete a live CRM onboarding (Apr 21).
