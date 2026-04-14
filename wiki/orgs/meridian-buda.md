---
github_repo: Moil-Landingpages/meridian-buda
tags:
  - graph/spoke
---
# Meridian Buda

**Type:** organization
**Last updated:** 2026-04-13
**Source:** [[raw/teams-2026-04-12]], [[raw/imessages-people-2026-04-09]], [[raw/github-project-tracker.md]], [[raw/teams-transcript-monday-collaboration-2026-04-13]]
**Related:** [[wiki/people/john-costilla]], [[wiki/moil/customers]], [[wiki/moil/pipeline]]

---

## Summary

Meridian Buda is a "Coffee, Live Music & Community" venue in Buda, TX. It is a **closed Moil client deal** — Andres announced to the team April 9, 2026: "Meridian has been closed team!!!" Taiwo is actively building a full ticketed events platform with Stripe integration and an organizer dashboard.

## Key Details

- **Business type:** Coffee shop / live music venue / community space
- **Location:** Buda, TX
- **Website:** meridian-buda.vercel.app (live — includes admin portal)
- **Deal status:** ✅ CLOSED April 9, 2026
- **Product:** Full custom platform — ticketed events, Stripe payments, organizer dashboard, check-in system
- **Community tie:** John Costilla shared the meridian-buda.vercel.app link to Andres via iMessage — they are connected socially

## GitHub Projects

- [Moil-Landingpages/meridian-buda](https://github.com/Moil-Landingpages/meridian-buda) — full client platform (last push Apr 10, 2026 🟢)

## Platform Features Being Built (as of Apr 2026)

- Stripe payment integration (Stripe credentials provisioned Apr 8)
- Ticketed events system (one event per time slot — no overlap)
- Organizer dashboard with event stats and check-in management
- Email system for organizer secret key (domain verification pending Apr 10)
- Admin portal at /admin

## Timeline

- Apr 7: Taiwo unable to test dashboard changes — waiting on credentials
- Apr 8: Stripe credentials provided; event overlap rules defined
- Apr 9: Andres announces "Meridian has been closed team!!!"
- Apr 9: Supabase migration needed — Taiwo to run migration
- Apr 10: Taiwo pushes to new branch (taiwo/finish); domain email issue blocking organizer dashboard unlock
- Apr 11: Taiwo reports "Changes are deployed"

## Current Blocker (Apr 13, 2026)

**Stripe webhook URL not configured** — ticket confirmation emails not sending. Taiwo has the endpoint, Andres needs to add it in Stripe's developer section (Meridian test account). Additionally, cron job secrets in Vercel are using placeholder values, not real secrets. Email sending works via Resend (partner email, limited to 100/day) — sufficient for now.

See [[wiki/meetings/2026-04-13-monday-collaboration]].

## Connections

- [[wiki/people/john-costilla]] — personal friend of Andres, connected to Meridian Buda community
- [[wiki/people/taiwo-ola-balogun]] — engineer building the platform

## Moil Relevance

Most technically complex Moil-Landingpages client to date — full SaaS-like platform with payments, events, and organizer tools. If successful, becomes a replicable template for venue/event clients. Community venue adds local Buda ecosystem credibility.
