---
name: know-me-extraction-prompts summary
description: Summary of three interview prompts (Claude/ChatGPT/Grok) for extracting Andres's personal + business context
type: summary
tags: [resource, personal, seed]
---

# Summary — Know Me: Extraction Prompts for The Brain

**Type:** summary
**Last updated:** 2026-04-11
**Source:** [[raw/know-me-extraction-prompts.md]]
**Related:** [[wiki/concepts/brain-architecture]], [[wiki/summaries/brain-guide]]

---

## Summary
Tooling document — not ingestible content. Contains three LLM interview prompts (Claude, ChatGPT, Grok) that Andres can run to produce a structured personal intelligence brief, plus a list of quick-hit raw inputs (voice memos, email forwards, decks, tweet saves) that enrich the Brain.

## Key Points
- **Prompt 1 (Claude):** Six sections — Who You Are, Moil Right Now, Your Vision, How You Think, Relationships, 2026 Priorities. Output = "Andres Urrego — Personal Intelligence Brief".
- **Prompt 2 (ChatGPT):** Five rounds — Identity/origin, Moil status, market/competition, people/capital, operating style. Output = 600-word "Moil Context Brief".
- **Prompt 3 (Grok):** Unfiltered five-part interview — truth about Moil, personal edge, network/ecosystem, content/brand, next 90 days. Output = 500-word "Founder Intelligence Brief".
- **Quick-hit raw inputs suggested:** voice memo dumps (Whisper), email forwards, past decks, tweet threads, meeting notes.
- **Workflow:** Pick a prompt → fresh LLM session → answer honestly → save output as `andres-intelligence-brief-[date].md` → drop into `raw/` → ingest.

## Connections
This is a *raw input generator*, not knowledge to extract. The outputs from these prompts would become new `raw/` files that the ingestion pipeline processes normally.

## Moil Relevance
- **Action:** run Prompt 1 (Claude) to seed a first "Andres Intelligence Brief" for the Brain.
- Without a personal brief, synthesis queries fall back on generic framing — see [[wiki/summaries/brain-guide]] on MOIL.md context file.
