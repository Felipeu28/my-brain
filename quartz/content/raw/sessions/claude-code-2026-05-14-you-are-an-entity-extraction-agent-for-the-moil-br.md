---
type: claude-code-session
session_id: 20c9cd17-ce57-4873-8120-4cef0d3bf79f
project: "-"
date: 2026-05-14
duration_minutes: None
source_jsonl: /Users/jarvisurrego/.claude/projects/-/20c9cd17-ce57-4873-8120-4cef0d3bf79f.jsonl
---
# Claude Code Session — You are an entity-extraction agent for the Moil Brain.

**Date:** 2026-05-14 (session ran 2026-05-14T05:15 → )
**Project:** -
**Duration:** None min
**Volume:** 1 user messages · 1 assistant responses · 0 tool calls

## Ask

You are an entity-extraction agent for the Moil Brain.

Extract every person mention from the data below. The goal is to enrich each person's wiki page with what they did yesterday and to track commitments.

# Ground rules

1. Extract ONLY real people (humans). Skip companies, products, meetings, tools.
2. Ignore Andres Urrego (the operator) — he's implicit in every source.
3. Normalize names to full "First Last" where possible; if only a first name appears, keep just the first name.
4. For each mention, determine:
   - **context**: what they were doing / saying / asking / deciding (1 short clause, 15 words max)
   - **source_type**: which source type this came from (teams, email-digest, whatsapp, etc.)
   - **source_file**: the filename (not the full path)
5. If the same person appears mu...

## Wiki entities referenced (1)

- [[wiki/weekly/2026-05-12]]
