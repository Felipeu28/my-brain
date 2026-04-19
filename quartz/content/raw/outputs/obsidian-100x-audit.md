---
type: audit
date: 2026-04-19
tags: [brain-audit, obsidian, productivity]
---

# Moil Brain vs. 100X Productivity Framework — Honest Audit

**Date:** 2026-04-19
**Scope:** Current `wiki/` vault + `pi-workspace/` automation layer vs. the "100X Productivity" Obsidian framework (12 top-level sections)
**Bottom line up front:** The Brain is already ~60% of a 100X setup and the most valuable pieces are the hard ones — real automation, structured data, business-grounded content. The remaining 40% divides cleanly into 3–4 things worth doing and a long tail of framework overhead that would add complexity with zero payoff.

---

## Already Have (and Maps Well)

### 1. Inbox & Capture → `wiki/inbox/` + `raw/` + morning briefing
- `raw/` is the immutable drop zone for all external sources (93 ingested)
- `wiki/inbox/` exists as the manual capture landing pad
- `morning-briefing.sh` (weekday 8:45am) pulls calendar, email, GitHub — that IS a systematic daily capture ritual, just automated not manual
- `teams_pull.py` + `teams_ingest.sh` capture all async communication context

**Gap within this category:** No capture mechanism for *in-the-moment* decisions, ideas, or observations during the day. The briefing is pull (from outside). There's no place to push.

### 2. Projects → `wiki/moil/active-projects.md` + `wiki/projects/`
- `active-projects.md` is a real project ledger: client ↔ owner ↔ repo ↔ status, updated from GitHub activity
- `wiki/projects/` has 7 standalone project pages (Fantelo, Lunabella, campaign-control, etc.)
- `ANDRES.md` "This Week's Priorities" section is an effective project dashboard substitute
- Weekly compile script reconciles GitHub + pipeline automatically

**Gap:** No project retrospective or closure protocol. Closed clients linger in active-projects.md, degrading its signal-to-noise over time.

### 3. Areas — Business → `wiki/moil/` (10 strategic pages)
This is the strongest section of the Brain. Fully covers the "Business" area:
- Positioning, GTM, ICP, Product Roadmap, Metrics, Customers, Pipeline, Referral Partners, Competitors, Active Projects
- Each page is a genuine living document with structured data, not a dump

### 4. Areas — Relationships → `wiki/people/` (60+ profiles) + `wiki/orgs/` (22+ orgs)
- Every person has `status`, `last_contact`, `person/*` sub-tag
- Org pages link to people and Moil deals
- This maps directly to the Relationships area of the 100X framework and is better-maintained than most implementations

### 5. Resources — Permanent Notes + Literature Notes → `wiki/concepts/` + `wiki/summaries/`
- 35 concept pages = permanent notes (brain-architecture, smart-hiring, moil360, etc.)
- `wiki/summaries/` = one structured summary per raw source = literature notes
- `wiki/minds/` = 10 public thought leaders tracked over time (Karpathy, Altman, etc.)

### 6. Resources — Frameworks/Mental Models → embedded in `wiki/concepts/`
- Concepts like ai-org-design, brain-architecture, gtm-system-multi-channel, self-learning-gtm-brain ARE frameworks
- Not in a `frameworks/` folder but that's fine — folder naming is aesthetic, not functional

### 7. Daily Systems — Morning Ritual → `morning-briefing.sh` + `ANDRES.md`
- Automated morning briefing delivers calendar, inbox summary, GitHub activity, priorities
- ANDRES.md says "Open this first every morning" — that's the daily anchor
- The ritual exists; it's just automated rather than template-driven

### 8. Daily Systems — Weekly/Monthly Reviews → `weekly-pulse.sh` + `outputs/pulse/`
- `weekly-pulse.sh` synthesizes the week's activity into `outputs/pulse/`
- `weekly-compile.sh` reconciles GitHub + pipeline into a structured summary
- This is functionally a weekly review; the gap is whether Andres actually annotates it

### 9. Automation & Intelligence Layer → 10 launchd jobs + pi-workspace/bin/
This is the Brain's biggest competitive advantage. No generic Obsidian setup comes close:
- morning-briefing, teams-daily, email-digest, content-calendar, weekly-compile, weekly-pulse, chroma-index, kb-health, heartbeat, x-bookmarks
- Shell scripts for every operation, Python for ChromaDB indexing and transcript processing
- Claude Code sessions auto-ingested via `ingest-claude-sessions.py`

The "AI/Claude Prompts" and "Auto-Tagging" sub-items of this section are live — Claude Code IS the automation intelligence.

### 10. Review & Optimization → `outputs/health/` + heartbeat
- kb-health.py runs Sunday 8am, writes to `outputs/health/kb-health-*.md`
- heartbeat-*.md files provide daily brain freshness checks
- brain-lint.sh reports stubs, orphans, contradictions

---

## High-Value Gaps

These are things the 100X framework covers that are genuinely missing AND would add real value for Andres specifically.

### Gap 1: Daily Notes / Ephemeral Capture (High Impact, Low Effort)
**What's missing:** There's no place to capture decisions, ideas, or observations mid-day. The morning briefing is input; everything after that disappears into Teams, email, or memory.

**Why it matters:** Andres is making 3–5 important business decisions daily (pricing, client prioritization, product direction). Right now those decisions exist only in his head. A month later, when Travis asks why they took a certain approach, there's no artifact.

**What to do:** Create `wiki/andres/daily/` with a simple daily note template. Obsidian daily notes plugin would generate these automatically. Minimum viable version: a `YYYY-MM-DD.md` per day with three fields: `### Decisions:`, `### Observations:`, `### Tomorrow:`. The morning briefing script could seed each day's file automatically.

**Complexity:** Very low. One Obsidian plugin, one template. Don't automate everything — this one should be manually written.

### Gap 2: Dataview Queries (High Impact, Low Effort)
**What's missing:** The `wiki/concepts/obsidian.md` page explicitly calls this out as a pending action item. No Dataview queries have been installed.

**Why it matters:** Andres's relationship maintenance is currently manual. A Dataview query like `TABLE last_contact WHERE contains(tags, "person/customer") SORT last_contact ASC` would surface every P1 client he hasn't touched in 30+ days, automatically, inside Obsidian. The data is already there — just no query layer.

**What to do:** Install Obsidian, point vault at `wiki/`, install Dataview plugin. Then write 3 saved queries:
1. Contacts not updated in 30+ days (relationship maintenance)
2. Open pipeline deals with no recent activity
3. Concepts with no inbound wikilinks (orphaned knowledge)

**Complexity:** Low. The data model already supports it. This is 2 hours of work, no new files.

### Gap 3: Project Closure / Archive Protocol (Medium Impact, Low Effort)
**What's missing:** When a client finishes or a project closes, the work stays in active-projects.md. Over 6–12 months, the hub page becomes a graveyard mixed with live deals.

**Why it matters:** The active-projects.md page is one of the most-referenced pages in the Brain. Keeping closed work there degrades it.

**What to do:** Simple two-step protocol:
1. When a client fully offboards, move their row to a new `wiki/moil/clients-archive.md` page
2. Leave a single line in active-projects.md: `[[wiki/moil/clients-archive|Closed clients →]]`

No new folder structure needed. Just a convention.

**Complexity:** 30 minutes of work, ongoing 5-minute habit.

### Gap 4: Decision Log (Medium Impact, Low Effort)
**What's missing:** A searchable record of major business decisions with brief rationale.

**Why it matters:** In 6 months, when Andres is reviewing why Moil pivoted to chambers-and-EDCs or why KidsGPT was shelved, there's no single place to find that reasoning. Meeting notes capture the context but not the explicit decision.

**What to do:** Single page `wiki/andres/decisions.md`. Append-only table:
```
| Date | Decision | Why | Outcome |
| 2026-04-15 | Pursue Buda EDC Incubator contract | Jennifer Storm introduction, B2G recurring revenue model | Board vote passed |
```

This is NOT a Notion board, not a project tracker, not a complex system. One markdown table, ~2 rows per week.

**Complexity:** Trivial to create. Habit cost: 2 minutes when a major decision is made.

---

## Low-Value / Skip

These are from the 100X framework that would add complexity without payoff for Andres's actual workflow:

### Skip: Focus & Deep Work Section
Time-blocking templates, distraction-blocker integrations, attention audits, and flow-state trigger logs. This assumes the bottleneck is focus discipline. Andres's bottleneck is not focus — it's the volume of context he needs to carry across 13 active clients, 2 public roles, and product development. No template fixes that; the Brain already addresses it.

### Skip: Feynman Technique / 5 Whys / Pros & Cons Templates
Generic thinking templates that come pre-populated in every Obsidian starter kit. Andres already captures reasoning in meetings/ and concepts/. The issue isn't that he lacks templates — it's that those templates are never filled in because the thinking happens in conversation, not in structured forms.

### Skip: Multi-Vault Strategy and Team Collaboration
The Brain is a personal + business brain. Team collaboration lives in Moil repos, Slack/Teams, and OpenClaw. Merging them would destroy the Brain's clarity of purpose. One vault is the right architecture. The "multi-vault" section of the 100X framework is built for someone who wants to separate "work" from "personal" into different vaults — Andres has already made the correct call to unify them.

### Skip: Plugins & Extensions Hub
Tracking which Obsidian plugins are installed is not a knowledge artifact. If it matters, it goes in CLAUDE.md or a setup script. A wiki page for this would be maintained for exactly one week.

### Skip: System Version History and 100X Upgrades Log
Git IS the version history. Every change to the Brain is committed with a message. Adding a human-maintained "upgrades log" would be a lossy duplicate of `git log --oneline`.

### Skip: Habits, Health, Finance Areas
These are conspicuously absent from the current Brain, and that's probably intentional. The Brain is a *Moil business brain* first. Adding personal habit tracking, health journals, and financial dashboards would blur the lens and make the Brain harder to navigate. If Andres wants these, they should live in a separate `wiki/andres/personal/` subfolder with strict wikilink isolation — not mixed into the main graph.

### Skip: Quarterly Audit / 100X Experiments Log
The kb-health.sh job already runs Sunday weekly. Adding a quarterly audit ritual on top of automated health checks is redundant unless Andres consistently acts on the weekly reports first. Don't add another review layer before the existing one is being fully used.

---

## Prioritized Recommendations

These are ordered by impact-to-effort ratio, specific to Andres's current setup.

### 1. Install Obsidian + Dataview (This Week)
**Why now:** The Brain is already structured as an Obsidian vault. This is the single highest-leverage change because it turns 225 pages of markdown into a navigable, queryable knowledge graph you can use from your phone, with zero new data entry. The obsidian.md concept page already laid out the action — it just hasn't been executed.

**Specific steps:**
1. Install Obsidian → point vault at `~/My Brain/knowledge-base/wiki/`
2. Install: Dataview, Templater, Calendar plugins
3. Write the 3 Dataview queries above (contacts, pipeline, orphans)
4. Set ANDRES.md as your "Homepage" plugin start page

**Estimated time:** 2 hours. **Impact:** Immediate — daily relationship visibility, mobile access to the full graph.

### 2. Add Daily Notes to morning-briefing.sh (This Month)
**Why:** Seed a `wiki/andres/daily/YYYY-MM-DD.md` file each morning alongside the briefing. Three blank sections: `Decisions`, `Observations`, `Open Questions`. Andres fills it in Obsidian during the day. This gives the Brain an input channel that captures ephemeral thinking before it evaporates.

**Specific change:** Add 5 lines to `pi-workspace/bin/morning-briefing.sh` that create the daily file if it doesn't exist. Template lives in `wiki/andres/daily-template.md`.

**Estimated time:** 30 minutes of scripting. **Impact:** High over time — creates a searchable record of decisions and thinking.

### 3. Add the Decision Log Page (This Week)
**Why:** Takes 5 minutes to create. Andres is in a high-velocity phase (10 deals in April, two new public roles, Cohort 4 launch). The decisions being made right now are the ones he'll want to understand in 6 months.

**Action:** Create `wiki/andres/decisions.md` with the table structure above. Add it to ANDRES.md Quick Access section.

**Estimated time:** 5 minutes to create, 2 minutes per entry. **Impact:** Compounding — the earlier you start, the more valuable it becomes.

### 4. Install Obsidian and Enable the Graph View (Part of #1)
Once Obsidian is installed, Andres should spend 10 minutes in Graph View with these filter settings:
- Show: all hubs and spokes (exclude leaves)
- Filter: add `path:wiki/moil` and see the business graph
- This single exercise will surface 3–5 connections that aren't in the current wikilink structure

This isn't a separate action — it's a byproduct of recommendation #1, but worth calling out explicitly because the graph view is where the "100X" insight often comes from.

### 5. Archive Protocol for Closed Clients (One-Time, Then Ongoing)
**Why:** active-projects.md has 3–4 closed clients already in the table. Create clients-archive.md now, move them, establish the habit. As the Moil business scales past 20 active clients this year, keeping the project hub clean becomes critical.

**Action:** Create `wiki/moil/clients-archive.md` as a hub page. Move Connectex (closed Apr 9), any other completed projects. Update active-projects.md with a pointer row.

**Estimated time:** 20 minutes one-time. **Impact:** Protects the signal quality of the most-used operational page.

---

## What NOT to Build

To be explicit: the Brain should NOT adopt:
- Daily habit tracker → adds maintenance cost without business leverage
- Thinking templates (Feynman, 5 Whys) → used by nobody, abandoned in 2 weeks
- Multi-vault architecture → the unified brain is the right call
- Plugin hub / upgrades log → Git history + CLAUDE.md are sufficient
- Deep work time-blocking system → not the binding constraint

The Brain is already better than 95% of "100X productivity" setups because it has *real automation* producing *real business artifacts*. The remaining gains come from adding a lightweight human input layer (daily notes, decision log, Dataview queries) — not from adding more system complexity.

---

*Generated by KB Agent — 2026-04-19*
