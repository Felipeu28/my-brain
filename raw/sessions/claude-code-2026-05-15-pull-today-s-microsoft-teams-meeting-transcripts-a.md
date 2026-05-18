---
type: claude-code-session
session_id: d9ea4747-0918-41fd-8c44-966e9a24905e
project: "Brain/Automations"
date: 2026-05-15
duration_minutes: None
source_jsonl: /Users/jarvisurrego/.claude/projects/-Users-jarvisurrego-My-Brain-pi-workspace/d9ea4747-0918-41fd-8c44-966e9a24905e.jsonl
ingested: true
ingested_at: 2026-05-18
---
# Claude Code Session — Pull today's Microsoft Teams meeting transcripts and add them to the Brain.

**Date:** 2026-05-15 (session ran 2026-05-15T23:15 → )
**Project:** Brain/Automations
**Duration:** None min
**Volume:** 1 user messages · 7 assistant responses · 13 tool calls

## Ask

Pull today's Microsoft Teams meeting transcripts and add them to the Brain.

1. Use m365 request to get today's online meetings:
   m365 request --url 'https://graph.microsoft.com/v1.0/me/onlineMeetings?$filter=startDateTime ge 2026-05-15T00:00:00Z'

2. For each meeting that has a transcript, fetch it:
   m365 request --url 'https://graph.microsoft.com/v1.0/me/onlineMeetings/{meetingId}/transcripts'
   Then fetch the transcript content:
   m365 request --url 'https://graph.microsoft.com/v1.0/me/onlineMeetings/{meetingId}/transcripts/{transcriptId}/content'

3. If transcripts found, save each one to ~/My Brain/knowledge-base/raw/teams-transcript-{meeting-subject}-2026-05-15.md with:
   - Meeting subject, date, attendees
   - Full transcript text
   - Key decisions and action items extracted...

## Files touched

**Created (1):**
  - `/Users/jarvisurrego/My Brain/knowledge-base/raw/teams-transcript-moil-marketing-team-call-2026-05-15.md`

## Wiki entities referenced (1)

- [[wiki/projects/moil]]
