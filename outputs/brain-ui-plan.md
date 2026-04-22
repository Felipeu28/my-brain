# Brain UI — Implementation Plan

**Created:** 2026-04-22
**Last updated:** 2026-04-22 (Phase 0 complete)
**Owner:** Andres Urrego
**Status:** Phase 0 complete — awaiting sign-off to start Phase 1

**Phase 0 deliverables live in `outputs/brain-ui/phase0/`:**
- `schema.sql` — SQLite schema
- `action-id-hashing.md` — stable ID spec + test fixtures
- `theme.md` — visual design primitives
- `briefing-schema.md` — canonical briefing format (v1.0, locked)

---

## Goal

Replace the passive email briefing with an **interactive Brain UI** that:

1. Surfaces every daily artifact (`briefing-*.md`, `github-activity-*.md`, `email-digest`, `content-calendar`, `pulse`, `heartbeat`, `kb-health`) in one unified view.
2. Makes every bullet in "Today's Priorities", "Inbox / Action Needed", "Awaiting Reply", "Going Cold", "Deals Going Stale" a clickable action with state.
3. **Closes the loop** — when an action is completed or snoozed, tomorrow's briefing generator knows about it and stops re-surfacing it.

The value isn't a todo app. The value is the Brain stops repeating itself once you act.

---

## Locked architectural decisions

| Decision | Choice | Reason |
|---|---|---|
| Host app | **Standalone** at `~/My Brain/brain-ui/` | OpenClaw is zombie UI — only Apollo MCP works there. Don't inherit broken departments in the sidebar. |
| Framework | **Next.js 14 (App Router)** + TypeScript + Tailwind | Stack Andres knows; easy to deploy later if needed. |
| Theme | **Fresh and modern** — not OpenClaw's dark slate. Own identity. | User preference: "modern and fun, nothing crazy". Clean type, generous whitespace, one accent color. |
| State store | **SQLite** via `better-sqlite3` | Local-first (v3 plan bias), one file, easy to migrate to Postgres later. No cloud dep. |
| Auth | **None in v1** (solo, localhost-only) | Single env-var password only if deployed to Vercel later. |
| Mobile | **Phase 5** — Tailscale tunnel to localhost:3001 | Zero infra cost. Vercel deploy is optional later. |
| Email briefing | **Stays as fallback** | Not removed. UI becomes primary, email stays for offline/phone-glance. |
| OpenClaw | **Punt** — don't touch until Brain UI is proven | Decide later: strip to Apollo, archive, or revive. |

---

## System architecture

```
~/My Brain/
  brain-ui/                          ← NEW Next.js app
    app/
      layout.tsx                     Root layout + theme
      page.tsx                       Today view (single scroll, all widgets)
      archive/[date]/page.tsx        Past briefings
      api/
        artifacts/route.ts           GET parsed artifacts for a date
        actions/route.ts             POST toggle completion / snooze / note
    lib/
      parsers/
        briefing.ts                  briefing-YYYY-MM-DD.md → structured JSON
        github.ts                    github-activity-*.md   → commits by repo
        heartbeat.ts                 heartbeat-*.md         → artifact freshness
        calendar.ts                  content-calendar weekly plan (Phase 4)
      db.ts                          SQLite schema + queries (better-sqlite3)
      feedback.ts                    Append completion events to feedback log
      ids.ts                         Stable action IDs (see action-id-hashing.md)
      sources.ts                     Multi-root scanner (see Source paths below)
    components/
      TodayView.tsx                  Main page composition
      PriorityCard.tsx               Large accented priority row
      ActionRow.tsx                  Workhorse checkbox + snooze + note
      PeopleRadar.tsx                Unified Awaiting + Going Cold + Stale Deals
      InboxList.tsx                  Action / FYI / Wait tabs
      ScheduleWidget.tsx             Today's calendar
      GitHubSummary.tsx              Commits collapsed
    styles/
      globals.css                    Tailwind base + Instrument Serif/Inter/JB Mono
    brain-state.db                   SQLite (gitignored)
    package.json
    tailwind.config.ts               Per outputs/brain-ui/phase0/theme.md
    .env.local                       BRAIN_KB_PATH=/Users/jarvisurrego/My Brain/knowledge-base

  knowledge-base/
    outputs/completed/               ← NEW folder (Phase 2)
      2026-04-22.md                  Append-only feedback log (one per day)
    outputs/brain-ui/phase0/         ← Phase 0 design docs (this plan + schema + theme)
    scripts/kb-health.py             ← Phase 0.5: add check_briefing_schema()

  pi-workspace/bin/
    morning-briefing.sh              ← Phase 3: modify to read outputs/completed/
```

### Source paths (corrected after Phase 0 audit)

Briefings and daily artifacts land in **multiple roots**. The Brain UI scanner must read all three:

| Kind | Path | Cadence |
|---|---|---|
| Morning briefing | `knowledge-base/quartz/content/raw/briefings/briefing-YYYY-MM-DD.md` | Weekday 8:45am |
| GitHub activity | `knowledge-base/outputs/github-activity-YYYY-MM-DD.md` | Daily 8:45am |
| Heartbeat | `knowledge-base/outputs/health/heartbeat-YYYY-MM-DD.md` | Periodic |
| Brain Says queries | `knowledge-base/quartz/content/raw/outputs/YYYY-MM-DD-query-*.md` | On-demand |
| Content calendar | `knowledge-base/outputs/content-calendar/calendar-YYYY-W##.md` | Weekly Monday |

> Heartbeat's own check is currently wrong — it still looks for briefings in `outputs/` instead of `quartz/content/raw/briefings/`. Not blocking; flag for cleanup when we touch briefing infra.

### Data flow

```
morning-briefing.sh (launchd 8:45am Mon–Fri)
    ↓ writes
quartz/content/raw/briefings/briefing-YYYY-MM-DD.md
    ↓ read by
brain-ui parsers (on page load)
    ↓ produces
structured JSON (actions with stable IDs)
    ↓ merged with
SQLite state (completions, snoozes, notes)
    ↓ rendered in
TodayView (interactive)
    ↓ user clicks checkbox
SQLite update + append to outputs/completed/YYYY-MM-DD.md
    ↓ next morning
morning-briefing.sh reads last 7 days of completed/ and drops resolved items
```

---

## Data model

**Full schema:** [`outputs/brain-ui/phase0/schema.sql`](brain-ui/phase0/schema.sql)

Key tables:
- `artifacts` — one row per parsed source file (cache)
- `actions` — structured action items with stable IDs
- `action_appearances` — many-to-many: "this action has shown up in these N briefings"
- `completions`, `snoozes`, `dismissals` — user state
- `events` — append-only audit log (for Phase 6 learning)
- Views: `v_actions_today`, `v_completion_log`

### Action ID stability

**Full spec:** [`outputs/brain-ui/phase0/action-id-hashing.md`](brain-ui/phase0/action-id-hashing.md)

Composite hash of (section, primary_entity, intent, disambiguator). Includes a fuzzy-match fallback layer that unifies actions with same section+entity but drifted wording across days. Test fixtures included.

**Future hardening (Phase 3+):** have the briefing generator emit stable IDs in frontmatter so we don't rely on hashing.

### Feedback log format (`outputs/completed/YYYY-MM-DD.md`)

```yaml
---
date: 2026-04-22
---
- action_id: a1b2c3d4e5f6
  event: complete
  at: 2026-04-22T11:42:00-05:00
  source: briefing-2026-04-22.md#priorities
  text: "Text Jacquie to confirm Board agenda"
  note: "Done — she confirmed on agenda"

- action_id: 9f8e7d6c5b4a
  event: snooze
  until: 2026-04-24
  source: briefing-2026-04-22.md#inbox_action
  text: "Reply to Becky Torres with prep questions"
```

This is what `morning-briefing.sh` reads in Phase 3.

---

## Phased implementation

### Phase 0 — Research & schema lock ✅ COMPLETE (2026-04-22)

- [x] Audit all available briefings — 9 files (Apr 13 → Apr 22), schema stable from Apr 13+
- [x] Discovered correct source paths (briefings are in `quartz/content/raw/briefings/`, not `outputs/`)
- [x] Audit github-activity, heartbeat, content-calendar formats
- [x] Draft SQLite schema → [`phase0/schema.sql`](brain-ui/phase0/schema.sql)
- [x] Define action ID hashing with test fixtures → [`phase0/action-id-hashing.md`](brain-ui/phase0/action-id-hashing.md)
- [x] Pick theme primitives → [`phase0/theme.md`](brain-ui/phase0/theme.md) (Instrument Serif + Inter + JetBrains Mono, burnt-orange accent on warm off-white)
- [x] Lock canonical briefing schema → [`phase0/briefing-schema.md`](brain-ui/phase0/briefing-schema.md)

**Side findings flagged:**
- Double "Brain Says" section bug in today's briefing (task spawned)
- Heartbeat check has wrong path (still looks in `outputs/` for briefings) — fix during Phase 3 when we're in morning-briefing.sh anyway

### Phase 1 — Read-only viewer (1 day)

- [ ] `npx create-next-app@14 brain-ui` with TS + Tailwind + App Router
- [ ] Install `better-sqlite3`, `gray-matter`, `remark`, `remark-parse`, `date-fns`
- [ ] Build `lib/parsers/briefing.ts` — parse into structured JSON
- [ ] Build `lib/parsers/github.ts` — simpler, commits grouped by repo
- [ ] Build `app/page.tsx` with widgets rendering today's artifacts
- [ ] Verify against last 5 briefings — no parsing regressions
- [ ] **Milestone:** UI replaces email as daily consumption surface. No writes yet.

### Phase 2 — Interactivity (1–2 days)

- [ ] Initialize SQLite + migrations on first boot
- [ ] `lib/db.ts` — CRUD helpers for actions / completions / snoozes / events
- [ ] `api/actions/route.ts` — POST toggle completion / snooze
- [ ] `ActionChip` component: checkbox + snooze dropdown + note popover
- [ ] Optimistic UI updates; persist to SQLite on action
- [ ] `lib/feedback.ts` — append event to `outputs/completed/YYYY-MM-DD.md`
- [ ] **Milestone:** check a priority in UI → line appears in completed log + row in SQLite. One-way feedback working.

### Phase 3 — Loop closure (1 day)

- [ ] Modify `pi-workspace/bin/morning-briefing.sh` to read last 7 days of `outputs/completed/*.md`
- [ ] Pass completed/snoozed action text into the briefing generation prompt as "do not re-surface these"
- [ ] Test: complete "Text Jacquie" today → tomorrow's briefing doesn't list it
- [ ] Add regression check: kb-health.py verifies at least one "don't re-surface" entry when completions exist
- [ ] **Milestone:** Brain stops repeating itself. This is the whole point of the system.

### Phase 4 — Unified intake (1 day)

- [ ] Parsers for `email-digest`, `content-calendar`, `pulse`, `heartbeat`
- [ ] Cross-artifact dedupe: if a person appears in inbox + cold + stale deals, show one card with all three signals
- [ ] `PeopleRadar` widget: combined awaiting/cold/stale sorted by urgency
- [ ] Archive view `/archive/[date]` — browse any past day
- [ ] **Milestone:** one-stop-shop for daily intake.

### Phase 5 — Mobile (0.5 day, optional)

- [ ] Ensure Tailscale is running on Mac mini + phone
- [ ] Bind Next.js dev server to `0.0.0.0:3001`
- [ ] Responsive layout pass (test on phone)
- [ ] **Milestone:** Brain UI on phone at `http://brain.tailnet.ts.net:3001`

### Phase 6 — Learning (future)

- [ ] Track: chronically-snoozed action types → down-rank in future briefings
- [ ] Track: time-to-complete by action type → surface stale work earlier
- [ ] Surface "patterns" widget: you consistently complete priorities but ignore FYI inbox items
- [ ] This is where the Brain becomes *adaptive*, not just reactive.

---

## Risks & mitigations

| Risk | Mitigation |
|---|---|
| Briefing template drifts → parsers break silently | Add `kb-health.py` check that last 3 briefings parse without error |
| Action ID collisions across days are fragile | Phase 3+: have the briefing generator emit stable IDs in YAML frontmatter |
| Two sources of truth (UI state + MEMORY.md) | **Hard rule:** UI only writes to `outputs/completed/`. Briefing generator is the only thing mutating MEMORY.md |
| User ticks something and regrets it | `events` table is append-only; uncomplete possible; history visible |
| UI becomes a zombie like OpenClaw if the loop isn't closed | Phase 3 is non-negotiable. Don't ship interactivity without loop closure |
| SQLite file corruption / loss | File lives in `brain-ui/` — add to a weekly backup cron (separate task) |

---

## Success criteria

- **Week 1 after launch:** Andres opens the UI daily instead of reading the email.
- **Week 2:** >50% of "Today's Priorities" get checked off in the UI the same day they appear.
- **Week 3:** Zero items re-appear in tomorrow's briefing after being marked complete the day before.
- **Month 1:** The daily email becomes read-only confirmation; the UI is the primary surface.

---

## What is deliberately NOT in scope

- ❌ Auth / multi-user (solo use)
- ❌ Cloud hosting in v1 (localhost + Tailscale)
- ❌ Real-time collaboration
- ❌ AI-generated responses inline (open in Claude Code for drafting)
- ❌ Mutating MEMORY.md from the UI (feedback log only)
- ❌ Reusing OpenClaw shell (verified zombie UI; don't inherit)
- ❌ RAG / embeddings (per v3 plan; navigate by wikilinks instead)
- ❌ Replacing the email briefing (stays as fallback)

---

## Open questions for later

1. Should the Brain UI ever **trigger** agent actions (e.g., "draft reply to Becky" → Claude session opens)? Deferred to Phase 6+.
2. Should Apollo MCP surface inside the Brain UI (e.g., "enrich contact" button on PeopleRadar)? Tempting; defer until after Phase 4 proves daily usage.
3. When OpenClaw is touched again, is there a path where Brain UI *becomes* the OpenClaw homepage? Possible, but reassess after Brain UI proves itself.

---

## Immediate next step

Start Phase 0 — audit briefing format stability and commit the SQLite schema. No code yet. Andres confirms and work begins.
