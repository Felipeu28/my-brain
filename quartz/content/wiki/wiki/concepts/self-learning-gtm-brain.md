---
tags:
  - graph/spoke
---
# Self-Learning AI GTM Brain

**Type:** concept (AI tool / framework)
**Last updated:** 2026-04-12
**Source:** [[raw/x-bookmarks-2026-04-11 copy]]
**Related:** [[wiki/moil/gtm]], [[wiki/concepts/managed-agents]], [[wiki/concepts/brain-architecture]]

---

## Summary
A Claude-powered marketing intelligence system that learns from every campaign launch. Originated by @pierreeliottlal (Mar 31, 2026): "Self-learning AI GTM Brain powered by Claude — learns from each campaign launch." This is the feedback-loop pattern applied to go-to-market: every campaign produces signal, signal updates the AI's model of what works, next campaign is informed by that history.

## How It Works (Reconstructed)
1. **Launch campaign** — email, LinkedIn post, ad, or event
2. **Capture results** — open rates, reply rates, conversions, attendee counts
3. **Feed back to Claude** — add results to a running context file (CAMPAIGNS.md or similar)
4. **Claude learns the pattern** — which messages worked, which audiences responded, which channels converted
5. **Plan next campaign informed** — next launch starts from accumulated intelligence, not from zero

## Why This Matters
Most SMB marketing is reset-to-zero every campaign: "What should we post this week?" The self-learning pattern breaks this — the AI starts dumber than the human but gets smarter with every run, eventually surfacing patterns the human would never notice (e.g., Tuesday emails at 9am always outperform Thursday, mentions of [City] in subject line double opens for local businesses).

## Connections
- This is essentially what [[wiki/concepts/brain-architecture]] does for personal knowledge — applied to marketing campaigns
- Requires [[wiki/concepts/managed-agents]] or [[wiki/concepts/claude-cowork]] to run automatically after each campaign
- Feeds into and upgrades [[wiki/moil/gtm]]

## Moil Relevance
This pattern is directly buildable as a Moil feature or as a Moil Brain workflow for Andres's own GTM. Two versions:
1. **For Andres:** Build a CAMPAIGNS.md in `~/My Brain/knowledge-base/wiki/moil/` that tracks every EDC outreach, chamber email, and event attendance with results. Feed it to Claude before planning the next campaign.
2. **As a Moil product feature:** The "AI Co-Founder" learns your campaign history and auto-improves next month's content calendar. This is a strong product differentiation point — most competitors are static tools, not learning systems.

**Source:** @pierreeliottlal, Mar 31, 2026
