---
type: claude-code-session
session_id: 22a230bb-a94e-42d4-ae4a-bf58871340ae
project: Brain/Automations
date: 2026-04-16
duration_minutes: None
source_jsonl: /Users/jarvisurrego/.claude/projects/-Users-jarvisurrego-My-Brain-pi-workspace/22a230bb-a94e-42d4-ae4a-bf58871340ae.jsonl
---
# Claude Code Session — Pull today's Microsoft Teams meeting transcripts and add them to the Brain.

**Date:** 2026-04-16 (session ran 2026-04-16T23:00 → )
**Project:** Brain/Automations
**Duration:** None min
**Volume:** 1 user messages · 2 assistant responses · 4 tool calls

## Ask

Pull today's Microsoft Teams meeting transcripts and add them to the Brain.

1. Use m365 request to get today's online meetings:
   m365 request --url 'https://graph.microsoft.com/v1.0/me/onlineMeetings?$filter=startDateTime ge 2026-04-16T00:00:00Z'

2. For each meeting that has a transcript, fetch it:
   m365 request --url 'https://graph.microsoft.com/v1.0/me/onlineMeetings/{meetingId}/transcripts'
   Then fetch the transcript content:
   m365 request --url 'https://graph.microsoft.com/v1.0/me/onlineMeetings/{meetingId}/transcripts/{transcriptId}/content'

3. If transcripts found, save each one to ~/My Brain/knowledge-base/raw/teams-transcript-{meeting-subject}-2026-04-16.md with:
   - Meeting subject, date, attendees
   - Full transcript text
   - Key decisions and action items extracted...
