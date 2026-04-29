---
tags:
  - graph/spoke
date: 2026-04-28
---
# 2026-04-28 — Website Update Review (Internal — Linda no-show → Engineering Review)

**Type:** meeting
**Last updated:** 2026-04-28
**Source:** [[raw/teams-transcript-website-update-review-call-2026-04-28]]
**Related:** [[wiki/people/jacob-oluwole]], [[wiki/people/taiwo-ola-balogun]], [[wiki/orgs/connectex]], [[wiki/orgs/fitlogic]], [[wiki/orgs/siren-beauty]], [[wiki/people/inna-benyukhis]], [[wiki/moil/active-projects]], [[wiki/concepts/moil360]]

---

## Context

58-min Teams call (1:00–1:58 PM CT). Originally scheduled to review website work with **Linda (`jungleflavorz@gmail.com`)** — Linda did not join. The call became an internal Moil engineering review of multiple parallel client projects: Inna, Connect X, FitLogic, Siren Beauty, and the moilapp.com SEO audit. Andres had a back-to-back at 1:45 with [[wiki/people/mark-polanco|Mark Polanco]] (separate transcript: [[wiki/meetings/2026-04-28-mark-polanco-connectex-walkthrough]]), so the last few minutes are him preparing for that hand-off.

## Key decisions

- **Repo discipline (NEW HARD RULE).** Taiwo pushes Connect X work to remote ASAP. All future engineering work is pushed for visibility. Andres works on branches, never pushes to main without coordination — but he needs visibility into what Taiwo has built.
- **FitLogic ships tonight.** Taiwo to finalize, deploy on Vercel, set environmental variables, test contacts upload + Google account connection.
- **Inna demo slips one week.** Inna messaged Andres saying she's busy → demo pushed back, gives the team time to fix the contact-add hang and Gemini API key.
- **Siren Beauty brand kit goes in repo as `brand.md`** so all future Siren-related work matches her brand DNA.
- **Moil website SEO audit becomes a workstream** — schemas, robots.txt, indexability all need fixing. Rule applies to all future client builds too.
- **Multi-CRM → unified white-label product** is the explicit strategy. No premature unification until Inna + Connect X + FitLogic are all finished. Once all three are done, do a full repo look, build the best one, deploy as the white-label.
- **Calendar etiquette.** Taiwo to put fit-logic test sessions on Andres's calendar rather than waiting on Andres to find time at 10 PM / 2 AM Nigeria time.

## Action items

- **Taiwo:** Push Connect X to remote repo (was working locally only); deploy FitLogic tonight with env vars; finalize readable WYSIWYG editor + variable selector (replace HTML-only email editor); verify Gemini API key on Inna; add Jacob as Google OAuth test user.
- **Jacob:** Send Gmail address to Taiwo for OAuth test-user list; continue social-media outreach plan, share message draft with Andres so they can split the list.
- **Andres:** Add Siren Beauty brand kit to project as `brand.md`; SEO audit + fixes on moilapp.com (only ~12 of ~60 pages indexed; schemas wrong; robots.txt wrong); send Mark a separate site review during 1:45 call; circle back with Taiwo when FitLogic is on the calendar.

## Notable threads

- **Moil website SEO crisis.** Andres ran a full SEO audit — only ~12 of ~60 pages indexed, schemas are wrong, robots.txt is wrong. Two years of accumulated SEO debt. Cited as the reason *"nobody can ever find us. We're literally unfindable."* Anything deployed forward (including client sites) must not repeat this. **First time SEO is on the record as a Moil-website workstream.**
- **Inna project (CRM dashboard).** Taiwo built it; Jacob is testing as `jacob@mylab.com`. Bugs surfaced live: adding contacts hangs, Gemini API key not working (Taiwo plans to grab the same key used on FitLogic), screen freezes during demo. Inna messaged Andres saying she's busy → demo pushed back a week.
- **Connect X (Mark Polanco's CRM) — repo visibility crisis.** Andres has zero visibility into Taiwo's work because Taiwo moved the repo to "his landing page" and never pushed. With the Mark meeting in 15 minutes, Andres realized he'd be showing the same thing he showed three weeks ago. Pushed firmly: keep repos pushed, work in branches. *"I'm never going to push to main but I need visibility."* Taiwo committed to pushing. **First time Andres has framed repo discipline as a non-negotiable team-wide rule.**
- **FitLogic project — readable email editor.** Email editor currently requires HTML; Taiwo wants to replace with a readable WYSIWYG-style editor with **variable selector** (contacts, email, distance) — the same pattern he just implemented for Inna. Plan: deploy tonight (Taiwo stated 10 PM Nigerian time = ~4 PM CT availability; Andres asked him to put it on the calendar instead of always meeting at 10 PM / 2 AM).
- **Siren Beauty brand kit.** Andres received it during the call, forwarded to Taiwo and Jacob, plans to add it as `brand.md` in the project. **First time a customer's brand kit becomes a repo-level artifact** — extends the per-asset MD file pattern Andres is rolling out (user.md, design.md, agent.md per profile).
- **Operating reality check — Claude was down.** Credit reset day; X also briefly down. Andres riffed on **$200/mo Claude spend vs. 6 deals closed last month** bringing 20× that in pipeline (Siren Beauty paid partial, Connect X to be quarterly). *"All these little projects, $500 here, just a simple website. We charge $5–600 bucks, and it costs us $200 to do for an entire month with four people working off it."*
- **CRM unified-product strategy.** Jacob asked why not unify into one CRM. Andres: *"That's the goal. We start, figure out which one is the best, then white-label it and sell it. Right now nothing works because we haven't finished a single project all the way through the finish line."* Multi-CRM approach is **deliberate learning sprint, not duplication**.
- **YC Request for Startups — Agentic AI alignment.** Andres riffed mid-call: YC just published RFS, one category is *"startups that build for agents"* — make business data available to agents rather than build the agent. Andres: *"That's what I positioned Moil as in our YC application. We have all the data already. Once we upgrade the 21 questions flow, it doesn't feel like 21 questions anymore — it's a chat. From there on, game over."* Plan: per-profile MD files (user.md, design.md, agent.md, brand.md) so any external agent can come into Moil and consume context.
- **Outbound messaging — split list.** Andres asked Jacob about messaging the people Andres tagged in the social-media group; nothing sent yet. Plan to split the list and send today.

## Moil Relevance

This is the **first time engineering visibility surfaced as a non-negotiable rule** — Apr 18 raised the time-zone boundary, Apr 21 raised revenue urgency, Apr 24 raised weekend ownership, Apr 28 raises **repo push discipline**. Series of compounding ownership gates over 10 days.

The **per-profile MD file architecture** (user.md, design.md, agent.md, brand.md) emerging from this call is the practical implementation of the YC RFS framing — Moil as the data layer for external agents, with brand kits (Siren) being the first concrete instance.
