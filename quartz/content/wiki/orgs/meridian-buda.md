---
github_repo: Moil-Landingpages/meridian-buda
owner: "[[wiki/people/travis-sutherland]]"
status: active
last_contact: 2026-05-12
tags:
  - graph/spoke
---
# Meridian Buda

**Type:** organization
**Last updated:** 2026-05-12
**Source:** [[raw/teams-2026-04-12]], [[raw/imessages-people-2026-04-09]], [[raw/github-project-tracker.md]], [[raw/teams-transcript-monday-collaboration-2026-04-13]], [[raw/teams-transcript-travis-andres-2026-05-12]]
**Related:** [[wiki/people/travis-sutherland]], [[wiki/orgs/zoiwell]], [[wiki/moil/customers]], [[wiki/moil/pipeline]], [[wiki/meetings/2026-05-12-travis-meridian-platform-handoff]]

---

## Summary

Meridian Buda is a "Coffee, Live Music & Community" venue in Buda, TX **owned by [[wiki/people/travis-sutherland|Travis Sutherland]]** — the same founder as [[wiki/orgs/zoiwell|Zoiwell]]. It is a **closed Moil client deal** — Andres announced to the team April 9, 2026: "Meridian has been closed team!!!" Taiwo is actively building a full ticketed events platform with Stripe integration and an organizer dashboard.

## Key Details

- **Owner:** [[wiki/people/travis-sutherland|Travis Sutherland]] (also owns [[wiki/orgs/zoiwell|Zoiwell]])
- **Business type:** Coffee shop / live music venue / community space
- **Location:** Buda, TX
- **Website:** meridian-buda.vercel.app (live — includes admin portal)
- **Deal status:** ✅ CLOSED April 9, 2026
- **Product:** Full custom platform — ticketed events, Stripe payments, organizer dashboard, check-in system

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

- [[wiki/people/travis-sutherland]] — **owner** (also owns [[wiki/orgs/zoiwell]])
- [[wiki/orgs/zoiwell]] — sister company under Travis Sutherland
- [[wiki/people/taiwo-ola-balogun]] — engineer building the platform
- [[wiki/people/john-costilla]] — works for Buda EDC (not a Meridian owner); community connection between Andres and the Buda EDC / Meridian ecosystem

## Moil Relevance

Most technically complex Moil-Landingpages client to date — full SaaS-like platform with payments, events, and organizer tools. If successful, becomes a replicable template for venue/event clients. Community venue adds local Buda ecosystem credibility.

## 2026-05-12 — Platform handoff + credential transfer

Source: [[wiki/meetings/2026-05-12-travis-meridian-platform-handoff]]

End-to-end product walkthrough with Travis at Meridian Buda (~31 min). Andres demoed: recurring events, ticketing tiers, customizable RSVP labels, QR + name check-in, analytics dashboards, bookings inbox, menu management, 4-stage email flow (confirmation → 7-day → 24-hour → post-event). Session closed with **all production artifacts moving under Travis's accounts**: GitHub (new account `travis@zoiwell.com`), Vercel (free), Resend (free under 1,000/day), GoDaddy (Travis sent admin invite). Andres retains push access but won't ship without image approval from Travis first.

**Open bugs (in-flight):**
- Artist autofill broken — **deprecated Gemini model**, API key needs replacement (Andres: fix today May 12)
- Check-in button stays disabled after live event time change (Andres: fix tomorrow May 13)
- Event update form shows stale opening time after time change (same root cause as above)

**Pending deliverables (Andres → Travis):**
- Landing page push with new Stan Martinez hero images (by May 13)
- Provision `info@meridianbuda.com` as staff check-in login
- Credentials doc (GitHub, Vercel, Resend, GoDaddy) shared with Travis after landing-page push

**Captured feature requests for v2:**
- On-the-fly custom email to upcoming event attendees (today only the templated 24-hour and follow-up are editable)
- Search check-ins by guest name rather than ticket number

**Cross-pattern signal:** This is the **first explicit credential-discipline handover under the May 11 Monday-Collaboration rule** — applied in both directions (Moil-side under @moilapp.com sales emails, client-side under the client's own accounts). Becomes the canonical pattern for every venue/website client handoff going forward.
