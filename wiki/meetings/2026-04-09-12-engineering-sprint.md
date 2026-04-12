---
tags:
  - graph/leaf
---
# Engineering Sprint — Apr 9–12, 2026

**Type:** meeting
**Last updated:** 2026-04-12
**Source:** [[raw/teams-2026-04-12]] (181 messages in Andres-Adeleke 1:1 + team chat)
**Related:** [[wiki/people/adeleke-tolulope]], [[wiki/moil/product-roadmap]], [[wiki/concepts/claude-code]]

---

## Summary

The most intensive engineering sprint captured in the Brain. Andres and Adeleke exchanged 181 messages in 4 days, with Andres driving development through Claude Code sessions and Adeleke pulling implementations to staging, testing, and pushing to production.

## Work Pattern

Andres uses Claude Code to prototype features, shares session links with Adeleke in Teams, Adeleke reviews the code, pulls to staging, tests locally, then pushes. This is the core Moil development workflow as of April 2026.

**Claude Code sessions shared this week (12+):**
- Business Coach onboarding redesign (website scraping, PDF intake)
- Content360 final review
- PDF and PPT implementation for Business Coach
- Bug fixes from Jacob's feedback document
- SEO and indexing improvements
- API chat implementation
- Document creation (Spanish language support)
- Moil 360 strategy fix
- Market insights improvements
- Multiple continuation/fix sessions

## Key Technical Decisions

1. **Business Coach as onboarding agent:** Static 22-step wizard replaced with an AI-guided process. Business Coach now scrapes websites, PDFs, and business plans to pre-fill information. Users get feedback after every question — guided process instead of cognitive-load fatigue
2. **Model cost optimization:** OpenAI `gpt-4o` alias silently upgraded to `gpt-5_4-2026-03-05` — 30x cost increase discovered. **Grok 4.1 Fast** ($0.20/$0.50, 2M context) identified as replacement
3. **Qwen Turbo 3.5 moved to paid tier** after free credits exhausted
4. **Speed vs cost tradeoff:** "Can't sacrifice speed even if the cost is better" — speed is a product requirement
5. **Push to production cadence:** Team adopted "fix bugs → test on staging → push to prod" rhythm instead of batching

## Bugs Fixed

| Bug | Status | Notes |
|---|---|---|
| Publish functionality broken | Fixed (Apr 7) | Adeleke fixed Monday |
| Strategy document generation | Fixed | Validation error — strategy data not being sent to backend |
| Moil 360 image creation 503 | Fixed (Apr 10 night) | Resolved same evening |
| Slow answers / Qwen failing | Mitigated | Moved to paid tier; considering model switch |
| Tour guide stuck in center | Open | 2 missing `data-guide-id` attributes |
| Generic waiting text | Open | UI copy work needed |
| Text streams too fast | Improved | Auto-scroll still aggressive |

## Bugs Still Open

- Website tour guide: 2 data-guide-id attributes (`dashboard-welcome-header`, `profile-badge`) don't exist in codebase
- Segment analytics: `No segment writeKey` error on staging
- Image conversation context: images "forgot" previous conversation context

## Products Touched

1. **Content360 / Moil 360** — strategy creation, image generation, document generation, speed optimization
2. **Business Coach** — new onboarding flow, website scraping, guided feedback
3. **Business Plan Creator** — PDF/PPT export implementation (Apr 11)
4. **SEO/Indexing** — pages not indexing enough (Apr 8 fix)
5. **Employer platform** — various fixes from Jacob's testing

## Deployment Notes

- `supabase functions deploy business-intake` — required from Business-plan-Staging/ to go live
- `supabase-migration-011.sql` — needs to run in Supabase SQL editor for Meridian
- Gemini API key shared directly in Teams chat for Taiwo: `AIzaSyCsCBv-NooHJuYY3V8jmrnCt5rluAc6WO4` (model: `gemini-3-flash-preview`)
