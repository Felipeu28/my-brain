---
type: claude-code-session
session_id: 6757c15e-0fe0-4093-bf18-9194106b8aac
project: Brain/Automations
date: 2026-04-25
duration_minutes: None
source_jsonl: /Users/jarvisurrego/.claude/projects/-Users-jarvisurrego-My-Brain-pi-workspace/6757c15e-0fe0-4093-bf18-9194106b8aac.jsonl
ingested: true
ingested_at: 2026-05-04
---
# Claude Code Session — Pull today's Microsoft Teams meeting transcripts and add them to the Brain.

**Date:** 2026-04-25 (session ran 2026-04-25T23:01 → )
**Project:** Brain/Automations
**Duration:** None min
**Volume:** 1 user messages · 5 assistant responses · 8 tool calls

## Ask

Pull today's Microsoft Teams meeting transcripts and add them to the Brain.

1. Use m365 request to get today's online meetings:
   m365 request --url 'https://graph.microsoft.com/v1.0/me/onlineMeetings?$filter=startDateTime ge 2026-04-25T00:00:00Z'

2. For each meeting that has a transcript, fetch it:
   m365 request --url 'https://graph.microsoft.com/v1.0/me/onlineMeetings/{meetingId}/transcripts'
   Then fetch the transcript content:
   m365 request --url 'https://graph.microsoft.com/v1.0/me/onlineMeetings/{meetingId}/transcripts/{transcriptId}/content'

3. If transcripts found, save each one to ~/My Brain/knowledge-base/raw/teams-transcript-{meeting-subject}-2026-04-25.md with:
   - Meeting subject, date, attendees
   - Full transcript text
   - Key decisions and action items extracted...
