---
github_repo: Moil-Landingpages/fit-logic
tags:
  - graph/hub
owner: "[[wiki/people/megan-miller]]"
status: active
last_contact: 2026-04-29
---
# FitLogic Functional Medicine

**Type:** organization
**Last updated:** 2026-04-29
**Source:** [[raw/teams-2026-04-12]], [[raw/email-history-2months-2026-04-12]], [[raw/github-project-tracker.md]], [[raw/teams-2026-04-21]], [[raw/teams-transcript-megan-miller-2026-04-21]], [[raw/email-digest-2026-04-20]], [[raw/teams-transcript-CRM-GOOGLE-Setup-with-Megan-2026-04-23]], [[raw/teams-transcript-megan-moil-crm-test-and-delivery-2026-04-29]]
**Related:** [[wiki/people/megan-miller]], [[wiki/people/michelle-fitlogic]], [[wiki/moil/customers]], [[wiki/moil/pipeline]], [[wiki/concepts/moil360]], [[wiki/meetings/2026-04-21-megan-fitlogic-working-session]], [[wiki/meetings/2026-04-23-megan-crm-google-setup]], [[wiki/meetings/2026-04-29-megan-fitlogic-crm-delivery]]

---

## Summary

Fit Logic Functional Medicine is a solo-NP functional medicine clinic owned by [[wiki/people/megan-miller|Megan Miller, NP]] — hormone optimization, women's health, chronic-condition functional medicine. **Anchor Moil 360 customer** — onboarded onto CRM Apr 21, 2026 in a 89-minute hands-on working session. Trust depth is above average: Megan handed Andres her GoDaddy credentials for `fitlogicfunctionalmedicine.com` during the first CRM call.

Dual product surface: (a) hiring via Moil job postings (first Moil-sourced hire imminent as of Apr 12); (b) Moil 360 full stack — CRM, campaigns, sequences, site deployment, soon a native quiz. An external vendor, **Electric Bricks**, is mid-redesign of the clinic website; Moil is waiting for them to ship before layering CRM forms on top.

Domain: `fitlogicfunctionalmedicine.com` (GoDaddy). Sending address to be: `Megan@fitlogicfunctionalmedicine.com`.

## Deal Status

- **Moil hiring:** ✅ Active — first hire imminent as of Apr 12, 2026; second job posted Apr 12
- **Moil 360 CRM:** 🟢 **Delivered Apr 29** — full 88-min walkthrough with Megan + Michelle covering CRM + Campaigns + Content360. First Moil 360 customer to receive end-to-end delivery in a single session. See [[wiki/meetings/2026-04-29-megan-fitlogic-crm-delivery]]. **Time-to-handover: 8 days** from Apr 21 first hands-on tour. Open bug list from delivery: pipeline-stage propagation, Content360 February-date default, edit-image regeneration constraint, Brand DNA color propagation
- **Practice manager named (Apr 29):** [[wiki/people/michelle-fitlogic|Michelle]] is the day-to-day Moil 360 operator. Megan provides brand voice + clinical authority; Michelle drives the platform. **First "owner trains a manager" delivery pattern at Moil 360**
- **Moil 360 / Coach:** ✅ Working again for Megan as of Apr 23 (Jacob confirmed the fix by email that morning)
- **Website:** External vendor Electric Bricks mid-redesign; **Megan + vendor compliance meeting Fri 2026-04-24 12:30 PM CT** (Andres plans to attend) — "doctor vs. health coach" scope-of-practice issue is non-negotiable
- **Payment plan ask (Apr 19, 2026):** Megan emailed asking to switch from **$500/mo × 3 to $250/mo × 6** — same total, stretched. Needs a revenue/collection decision + reply ([[raw/email-digest-2026-04-20]])

## Apr 23 Handoff Architecture — CRM Stack Owned by Megan

Source: [[wiki/meetings/2026-04-23-megan-crm-google-setup]]

The CRM is being built and deployed, but **every account is owned by Megan's credentials**, not Moil's. Taiwo is a collaborator only. This lets Moil hand the whole stack over cleanly at go-live.

| Layer | Account | Owner | Notes |
|---|---|---|---|
| Domain / hosting entry | GoDaddy (`fitlogicfunctionalmedicine.com/crm`) | Megan | Credentials previously shared in Teams private chat |
| App hosting | Vercel | Megan | Free tier |
| Database | Supabase | Megan | Free tier; Moil-built schema for contacts |
| Outbound email | Resend | Megan | Authenticated via Megan's GitHub login |
| Code repo | GitHub | Megan | Taiwo added as collaborator |
| Gmail / Calendar OAuth | Google Cloud Console project (Megan's `hello@` Gmail) | Megan | Scopes finalized: Gmail `send` + `readonly` + `compose`, Calendar `readonly`. Authorized redirect URIs will hold multiple entries (local / staging / production) |
| LLM API | Gemini API key | Megan (at deploy time) | She pays usage directly |

**Why this matters for the Moil 360 playbook:** this is the first time Moil has set up a customer as the owner of every infrastructure account from day one. Historically Moil owned Vercel/Supabase/etc. and had to migrate later. Establishing the "own from inception" pattern at FitLogic makes her the clean template for H1 case-study handoff stories and for how future Moil-built CRMs get priced and delivered.

## Apr 21 Working Session — Key Decisions

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

## Apr 29 Delivery — Brand Voice Rules + Live Bugs

Source: [[wiki/meetings/2026-04-29-megan-fitlogic-crm-delivery]]

**Brand voice rule for AI email generation:**
- Hook-style openers (*"You may be wondering…"*, *"Are you still struggling with…"*) — NEVER *"I wanted to share…"*
- Reader-centered, not founder-centered. Megan: *"I don't care what you want. I want it to be about what they need."*
- Edits via the free-form prompt box, not AI rewrites (avoid unnecessary API calls)

**Lead segmentation taxonomy agreed:**
- cold / previous client / active patient / inactive patient / IC-only (initial-consultation-only) / massage-only legacy
- Andres extracts patient vs. non-patient from the 5,000-row export (Megan already shared the patient list on a prior call)
- Megan tags IC-only manually; bulk-tag shortcut: identify the day Jill's contacts were imported into Charm and mass-tag those rows as one segment

**P0 bugs surfaced live:**
- Pipeline-stage updates in pipeline view don't propagate back to contact card / analytics
- Content360 calendar defaulted to **Feb 28** instead of current month
- "Edit image" appears stuck on the original image (image-to-image vs. text-to-image regression — Megan tried "happy gut" + "image of a person who is happy" — both produced continuations of the gut-reset image)
- Brand DNA colors may not propagate to Content360 image generator if calendar created before colors saved

**Feature requests from Megan + Michelle:**
- "Last contacted" filter on contacts
- `previous client` option on lead-source / pipeline status
- Customizable lead-source drop-down: social media, website, driving by, friend/family referral, networking event, **other (with free-text)**
- Closed-captioning on generated videos (Michelle — accessibility)
- Centralized link library (paste once, reuse across emails)
- Chat/FAQ widget tied to website once Electric Bricks delivers; book-a-call link → Megan's Square calendar

**Cadence rules:**
- Daily posting, not weekly. On image+video days, post twice
- Cold-email rollout: ~10/day, rotate variants, never blast all 5,000 with the same template
- Default image format: Stories (vertical) — performs best on Facebook/Instagram
- Test sends only against new test contacts, never existing customers

## Contacts

- **Megan Miller, NP** — owner, primary Moil contact — [[wiki/people/megan-miller]]
- **[[wiki/people/michelle-fitlogic|Michelle]]** — practice manager (started ~mid-April 2026, ~2 weeks tenure as of Apr 29). De facto **day-to-day Moil 360 operator** at FitLogic. Has prescription/pharmacy authority (handled Buda Drug Store medication-refill call live during the Apr 29 delivery walkthrough). Knows [[wiki/people/daniel-mann|Daniel D. Mann]] ("Firefly") socially — warm second-degree loop back to Moil's #1 referral partner.
- **Lori, Cassandra** — clinic staff (briefly mentioned)

## Workshop (Joint)

Megan and Andres co-planning a workshop — timing tight, Megan told one interested person, Andres has only mentioned it to Justin K. Push or postpone decision pending.

## Moil Relevance

FitLogic is the **flagship Moil 360 case study candidate for H1 2026.** Three reasons:
1. **Trust depth** — GoDaddy credentials on the first CRM call is rare.
2. **Full product surface** — hiring + CRM + campaigns + sequences + website + (eventually) native quiz — covers more Moil 360 surface area than any other customer.
3. **Vertical fit** — solo-practitioner healthcare is a target ICP where Moil's "personal clinic assistant" story resonates; the sequences killer-feature reaction confirms product-market fit for the nurture use case.

First Moil customer to make a Moil-sourced hire (announced Apr 12). First Moil 360 customer to complete a live CRM onboarding (Apr 21).
