---
tags:
  - graph/leaf
---
# Prompt Reviews — Business Plan Creator Quality

**Type:** meeting
**Last updated:** 2026-04-12
**Source:** [[raw/meetings/transcript-2025-05-17-prompt-reviews.md]]
**Related:** [[wiki/moil/product-roadmap]], [[wiki/people/adeleke-tolulope]], [[wiki/people/jacob-oluwole]]

---

## Summary

Andres, Jacob, and Steve (Adeleke) reviewed the Business Plan Creator output quality. The session identified major weaknesses in the AI-generated business plans and discussed architectural improvements.

## Attendees

- Andres Urrego (andres@moilapp.com)
- Jacob Oluwole (jacob@moilapp.com)
- Adeleke Tolulope / Steve (steve@moilapp.com)

## Key Quality Issues Identified

1. **Vague numbers** — AI generates non-specific statistics; needs real data sources
2. **Bad personas** — Customer personas are generic, not grounded in business context
3. **Hallucination** — Real-time data requests cause LLM to fabricate statistics and citations
4. **Lack of citations** — No source attribution for market data
5. **Generic language** — Business descriptions lack specificity
6. **Financial section unreliable** — Numbers feel fabricated; no verification possible
7. **Map utility questioned** — Location map shows business address (user already knows this); Andres pushed to repurpose for competitor visualization instead

## Technical Decisions

- **Brave API proposed** by Adeleke: Use Brave Search API for real-time web data fetching (internet-sourced competitor data, market statistics) instead of relying on LLM fabrication
- **Competitor map** — Relocate business address pin to competitor map section; show actual competitors on map using geocoded competitor data
- **JSON capture** — Steve needs to update JSON schema to capture additional section data for display
- **Model pipeline:** Using OpenAI o3-mini for business insights generation

## Andres Management Style Note

Andres explicitly told the team to not take his criticism as personal attacks — "I need you guys to always take what I say with a..." — showing awareness that his direct feedback style can feel harsh to the Nigerian development team.

## Moil Relevance

This is the most detailed product quality review in the Brain. The BPC was the flagship product at this point, and the hallucination/citation problem is the #1 technical debt item. The Brave API decision represents a shift from pure LLM generation to retrieval-augmented generation for business plans.
