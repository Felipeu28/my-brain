---
type: claude-code-session
session_id: 91dac017-da04-4907-be54-5a2bc64a18e9
project: "Brain/Automations"
date: 2026-05-13
duration_minutes: None
source_jsonl: /Users/jarvisurrego/.claude/projects/-Users-jarvisurrego-My-Brain-pi-workspace/91dac017-da04-4907-be54-5a2bc64a18e9.jsonl
ingested: true
ingested_at: 2026-05-18
---
# Claude Code Session — Pull today's Microsoft Teams meeting transcripts and add them to the Brain.

**Date:** 2026-05-13 (session ran 2026-05-13T23:15 → )
**Project:** Brain/Automations
**Duration:** None min
**Volume:** 1 user messages · 7 assistant responses · 21 tool calls

## Ask

Pull today's Microsoft Teams meeting transcripts and add them to the Brain.

1. Use m365 request to get today's online meetings:
   m365 request --url 'https://graph.microsoft.com/v1.0/me/onlineMeetings?$filter=startDateTime ge 2026-05-13T00:00:00Z'

2. For each meeting that has a transcript, fetch it:
   m365 request --url 'https://graph.microsoft.com/v1.0/me/onlineMeetings/{meetingId}/transcripts'
   Then fetch the transcript content:
   m365 request --url 'https://graph.microsoft.com/v1.0/me/onlineMeetings/{meetingId}/transcripts/{transcriptId}/content'

3. If transcripts found, save each one to ~/My Brain/knowledge-base/raw/teams-transcript-{meeting-subject}-2026-05-13.md with:
   - Meeting subject, date, attendees
   - Full transcript text
   - Key decisions and action items extracted...

## Wiki entities referenced (1)

- [[wiki/moil/directory]]
