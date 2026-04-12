# Business Plan Creator Design Session

**Type:** meeting
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/transcript-2025-03-12-business-plan-creator-session.md]]
**Related:** [[wiki/people/jacob-oluwole]], [[wiki/people/abiodun-solomon]], [[wiki/moil/product-roadmap]]

---

## Summary

An early-morning (6 AM) design session on March 12, 2025 with Andres, Jacob, and Ablad mapping out the Business Plan Creator product. Finalized the UX architecture: 8 sections, 3 subscription tiers (Idea/Plan/Grow), conversational question flow replicating the resume builder's UX. That same day, Andres was presenting Moil to the Center for Child Protection.

## Product Design Decisions Made

### Structure
- **8 sections** in the business plan output
- **20-40 questions total**, distributed across sections
- **3 tiers:**
  - **Idea** — lightweight entry tier
  - **Plan** — standard full business plan
  - **Grow** — expanded/scaling tier
- Conversational UX: same voice/text input approach as the resume builder

### Technology
- **DeepSeek** for specific analytical components
- **Gemini** for market research and competitive analysis
- Architecture mirrors the resume builder pipeline — questions → AI synthesis → structured output

### Pricing Direction
- "$1,500 traditional business plan → $100 with Moil" — this framing was solidified here (used later in HubSpot Marketing Kickoff)

## Same-Day Context: Center for Child Protection

Andres was presenting Moil to the Center for Child Protection on March 12, 2025 — the same day as this design session. This suggests a busy day of product-building AND business development. The CCP is a non-profit; this may be a community partnership (candidate acquisition) not an enterprise sales call.

## Action Items (from this session)

- [ ] Finalize question set across all 3 tiers (20-40 questions)
- [ ] Map each question to one of the 8 output sections
- [ ] Implement conversational flow (same pattern as resume builder)
- [ ] Validate DeepSeek + Gemini split for market analysis

## Connections

- Business Plan Creator launched as operational by May 2025 (see [[wiki/meetings/2025-05-21-ai-advisory-azure-foundry]] — confirmed operational at Paula call)
- Product framing used in [[wiki/meetings/2025-04-28-hubspot-kickoff-sebastian-full-transcript]] ("21 questions, $100 vs $1,500")

## Moil Relevance

This session documents the architectural foundation of Moil's second major AI product. The 3-tier model (Idea/Plan/Grow) creates a natural upgrade path and pricing ladder. The conversational UX decision keeps the product consistent with the resume builder, lowering the learning curve for existing users.
