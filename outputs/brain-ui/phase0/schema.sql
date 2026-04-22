-- Brain UI — SQLite schema (Phase 0 draft)
-- Target DB file: ~/My Brain/brain-ui/brain-state.db (gitignored)
-- Engine: better-sqlite3 (synchronous, native Node)
-- Created: 2026-04-22
--
-- Design principles:
--   1. Parsed artifacts are cache, not source of truth. If the DB is deleted,
--      we can re-parse briefings from disk and rebuild everything except
--      completions/snoozes/notes (user state).
--   2. Events table is append-only. Completions/snoozes are derived state.
--   3. Action IDs must be stable across days (see action-id-hashing.md).

PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;

-- ──────────────────────────────────────────────────────────────────────
-- artifacts: one row per parsed source file (briefing, github-activity, …)
-- ──────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS artifacts (
  id              TEXT PRIMARY KEY,           -- e.g. "briefing-2026-04-22"
  kind            TEXT NOT NULL,              -- briefing | github | heartbeat | content_cal | pulse
  source_path     TEXT NOT NULL,              -- absolute path on disk
  source_date     TEXT NOT NULL,              -- YYYY-MM-DD
  file_mtime      TEXT NOT NULL,              -- ISO — detect re-parse needed
  parsed_at       TEXT NOT NULL,              -- ISO timestamp of last parse
  parser_version  INTEGER NOT NULL DEFAULT 1, -- bump when parser logic changes
  raw_hash        TEXT NOT NULL               -- sha256 of file contents
);

CREATE INDEX IF NOT EXISTS idx_artifacts_date ON artifacts(source_date);
CREATE INDEX IF NOT EXISTS idx_artifacts_kind ON artifacts(kind);

-- ──────────────────────────────────────────────────────────────────────
-- actions: structured action items extracted from artifacts
-- One action may appear across many briefings (same id) — we update
-- last_seen each time. first_seen is the earliest date we detected it.
-- ──────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS actions (
  id              TEXT PRIMARY KEY,           -- stable hash (see hashing spec)
  section         TEXT NOT NULL,              -- priorities | inbox_action | inbox_fyi
                                              -- awaiting_reply | going_cold | stale_deal
                                              -- one_thing | brain_says | code_activity
  text            TEXT NOT NULL,              -- normalized bullet text
  text_raw        TEXT NOT NULL,              -- original bullet markdown
  primary_entity  TEXT,                       -- "Megan Miller" / "Buda HIVE" / NULL
  entity_type     TEXT,                       -- person | deal | project | repo | NULL
  intent          TEXT,                       -- ping | fix | reply | review | confirm | …
  people          TEXT NOT NULL DEFAULT '[]', -- JSON array of people referenced
  wikilinks       TEXT NOT NULL DEFAULT '[]', -- JSON array of [[...]] targets
  due_date        TEXT,                       -- optional YYYY-MM-DD (parsed from text)
  first_seen_date TEXT NOT NULL,              -- YYYY-MM-DD this action first appeared
  first_seen_at   TEXT NOT NULL,              -- ISO timestamp
  last_seen_date  TEXT NOT NULL,              -- YYYY-MM-DD most recent occurrence
  last_seen_at    TEXT NOT NULL               -- ISO timestamp
);

CREATE INDEX IF NOT EXISTS idx_actions_section ON actions(section);
CREATE INDEX IF NOT EXISTS idx_actions_last_seen ON actions(last_seen_date);
CREATE INDEX IF NOT EXISTS idx_actions_entity ON actions(primary_entity);

-- ──────────────────────────────────────────────────────────────────────
-- action_appearances: many-to-many between actions and artifacts
-- Answers "which briefings has this action appeared in?" — used for
-- "this has been nagging for 5 days" UI badges.
-- ──────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS action_appearances (
  action_id    TEXT NOT NULL,
  artifact_id  TEXT NOT NULL,
  section      TEXT NOT NULL,
  text_raw     TEXT NOT NULL,                 -- that day's exact wording
  PRIMARY KEY (action_id, artifact_id),
  FOREIGN KEY (action_id)   REFERENCES actions(id)   ON DELETE CASCADE,
  FOREIGN KEY (artifact_id) REFERENCES artifacts(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_appearances_artifact ON action_appearances(artifact_id);

-- ──────────────────────────────────────────────────────────────────────
-- completions: current completion state (one row per completed action)
-- To "uncomplete" an action, delete the row (and log an event).
-- ──────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS completions (
  action_id     TEXT PRIMARY KEY,
  completed_at  TEXT NOT NULL,                -- ISO timestamp
  note          TEXT,                         -- optional user note
  FOREIGN KEY (action_id) REFERENCES actions(id) ON DELETE CASCADE
);

-- ──────────────────────────────────────────────────────────────────────
-- snoozes: hide an action until a date. Expired snoozes are ignored
-- but kept for history.
-- ──────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS snoozes (
  action_id      TEXT PRIMARY KEY,
  snooze_until   TEXT NOT NULL,               -- YYYY-MM-DD
  created_at     TEXT NOT NULL,
  reason         TEXT,
  FOREIGN KEY (action_id) REFERENCES actions(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_snoozes_until ON snoozes(snooze_until);

-- ──────────────────────────────────────────────────────────────────────
-- events: append-only audit log of every user interaction.
-- Used for learning (Phase 6): which action types get completed vs
-- snoozed vs dismissed. Never DELETE from this table.
-- ──────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS events (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  action_id   TEXT NOT NULL,
  event_type  TEXT NOT NULL CHECK (event_type IN (
                'complete', 'uncomplete',
                'snooze', 'unsnooze',
                'note_set', 'note_clear',
                'dismiss',                    -- "not relevant", hide forever
                'open',                       -- action expanded in UI
                'link_click'                  -- user clicked a wikilink
              )),
  payload     TEXT,                           -- JSON blob, event-specific
  created_at  TEXT NOT NULL                   -- ISO timestamp
);

CREATE INDEX IF NOT EXISTS idx_events_action ON events(action_id);
CREATE INDEX IF NOT EXISTS idx_events_type   ON events(event_type);
CREATE INDEX IF NOT EXISTS idx_events_date   ON events(created_at);

-- ──────────────────────────────────────────────────────────────────────
-- dismissals: "not relevant" — forever hide this action. Separate from
-- completions because semantically different ("done" vs "don't show me").
-- ──────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS dismissals (
  action_id    TEXT PRIMARY KEY,
  dismissed_at TEXT NOT NULL,
  reason       TEXT,
  FOREIGN KEY (action_id) REFERENCES actions(id) ON DELETE CASCADE
);

-- ──────────────────────────────────────────────────────────────────────
-- VIEWS — convenience queries for the UI
-- ──────────────────────────────────────────────────────────────────────

-- actions_today: everything visible in today's briefing that isn't
-- completed / dismissed / snoozed beyond today.
CREATE VIEW IF NOT EXISTS v_actions_today AS
SELECT a.*,
       c.completed_at IS NOT NULL AS is_completed,
       c.completed_at AS completed_at,
       c.note AS completion_note,
       s.snooze_until AS snooze_until,
       d.dismissed_at AS dismissed_at,
       (julianday(a.last_seen_date) - julianday(a.first_seen_date)) AS days_nagging
FROM actions a
LEFT JOIN completions c ON a.id = c.action_id
LEFT JOIN snoozes     s ON a.id = s.action_id
LEFT JOIN dismissals  d ON a.id = d.action_id
WHERE a.last_seen_date = DATE('now', 'localtime');

-- v_completion_log: what to write to outputs/completed/YYYY-MM-DD.md
-- Used by lib/feedback.ts to serialize daily completion events.
CREATE VIEW IF NOT EXISTS v_completion_log AS
SELECT e.created_at,
       e.event_type,
       e.action_id,
       a.text_raw,
       a.section,
       a.primary_entity,
       e.payload
FROM events e
JOIN actions a ON e.action_id = a.id
WHERE e.event_type IN ('complete', 'snooze', 'dismiss');
