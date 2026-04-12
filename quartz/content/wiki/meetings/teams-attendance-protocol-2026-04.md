# Moil Team — Daily Attendance & Operating Rhythm (Teams)

**Type:** meeting (recurring async protocol)
**Last updated:** 2026-04-12
**Source:** [[raw/teams-2026-04-12]]
**Related:** [[wiki/concepts/moil-team-ops]], [[wiki/moil/metrics]]

---

## Summary

The `#attendance-n-break` channel in the Moil Microsoft Teams workspace runs a daily automated workflow (7:00 AM) that enforces a structured clock-in and start-of-day status protocol. This is the team's primary synchronization mechanism — not a meeting, but the cadence that replaces one. 30 days of data (Mar 13–Apr 12, 2026) captured 21 automated Workflow posts and no human messages, meaning this raw pull captured only the bot side.

---

## Channel: #ATTENDANCE AND BREAK INS

**Medium:** Microsoft Teams automated Workflow (7:00 AM daily)
**Window observed:** Mar 13 – Apr 12, 2026 (21 weekday posts captured)
**Human messages visible in this pull:** 0

### The protocol (from Workflow message text)

The Workflow message posts two required actions each morning:

**Step 1 — Clock In**
Post in `#attendance-n-break`:
> Clocked in – [Your Name]

Purpose: confirms the team member is live, available, and ready.

**Step 2 — Start-of-Day Status**
Post in the project or team thread:
> Today: [What you plan to tackle]
> Blockers: [Any issues, or say "None"]

Example format:
> Today: Homepage mobile fixes, team onboarding
> Blockers: None

### Operating philosophy (from Workflow message)

> "This is not just routine — it's how we sync, scale, and show up as a team. Skipping this = you're not visible, not aligned, and not in the rhythm of impact."

This framing positions the clock-in as a **cultural accountability signal**, not just time-tracking. Visibility, alignment, and rhythm are the stated values.

---

## Key Decisions

- The team operates with a **7:00 AM daily synchronization** cadence, enforced by automation rather than a human scheduling the reminder.
- The protocol distinguishes between **presence** (clock-in in attendance channel) and **intent** (start-of-day status in the project thread). Two separate posts.
- Blockers are surfaced asynchronously at the start of each day — no blocker sync meeting needed.

---

## Action Items from this source

None extracted — this raw file contained only automated bot messages. No human decisions, directives, or commitments were captured in this 30-day pull.

---

## Follow-ups / Gaps

- **Gap:** The Teams pull only captured the Workflow bot side. Human responses (actual clock-ins) were not included in `raw/teams-2026-04-12.md`. A future pull with human messages would reveal: who actually clocks in, who skips, who posts blockers, team composition by daily presence.
- **Gap:** `#Alerts` channel had a header in the raw data but no messages — unclear what this channel is used for.
- **Intelligence opportunity:** A pull of human responses in `#attendance-n-break` over 30 days would give a complete Moil team roster (every person who has clocked in) and attendance patterns.

---

## Connections

- [[wiki/concepts/moil-team-ops]] — this protocol is the operational rhythm that page describes
- [[wiki/moil/metrics]] — attendance consistency is a leading indicator of team health
- [[MEMORY]] — no new action items; this is informational
