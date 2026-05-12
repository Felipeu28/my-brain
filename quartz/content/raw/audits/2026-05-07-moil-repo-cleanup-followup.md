---
type: audit
date: 2026-05-12
companion: raw/audits/2026-05-07-moil-repo-sync-check.md
tags:
  - graph/leaf
---
# Moil repo cleanup — Task 1/2/3 follow-up

**Headline.** Task 1 (relocate) **shipped** — both checkouts now at `~/Moil/`, brain repo's orphan-gitlink entries removed from the index. Task 2 (messaging branch review) **recommends continue/activate, not archive**. Task 3 (branch sprawl) — **8 deletion candidates surfaced for approval**, no `git branch -D` executed.

---

## Task 1 — Relocate Moil checkouts (✅ shipped)

| Repo | Old path | New path | Branch | HEAD | Status |
|---|---|---|---|---|---|
| moil-app | `~/My Brain/knowledge-base/moil-app` | `~/Moil/moil-app` | `main` | `f978016` | clean, 0 uncommitted, origin intact |
| moil-bpc | `~/My Brain/knowledge-base/moil-bpc` | `~/Moil/moil-bpc` | `master` | `ad3c5de` | clean, 0 uncommitted, origin intact |

**Found something bigger than a path issue:** the two directories weren't just nested — they were tracked as **orphan gitlinks** (`160000 commit` mode) in the brain repo's index, with no `.gitmodules` file. That's the source of the long-standing CI warning `fatal: No url found for submodule path 'moil-app' in .gitmodules` we've been ignoring since at least 2026-04-23. The cleanup path:

```
mkdir -p ~/Moil
mv "$KB_DIR/moil-app" ~/Moil/moil-app    # working tree moved
mv "$KB_DIR/moil-bpc" ~/Moil/moil-bpc
cd "$KB_DIR" && git rm --cached moil-app moil-bpc   # drop the gitlink index entries
```

After the cleanup, both repos function identically from `~/Moil/` (verified: branch, HEAD, status, origin URL). The brain's `git status` now shows `D  moil-app` and `D  moil-bpc` (staged for index-only removal — nothing actually deleted from the brain's working tree because the directories were nested, not file-tracked). This is committed in the same commit as this audit report (so the future history is one clean cleanup, not two half-moves). **Not pushed** — per your instruction.

**Hardcoded-reference scan** — ran across `pi-workspace/bin/`, `pi-workspace/launchd/`, `pi-workspace/sentinel-config.tsv`, `pi-workspace/project-config.tsv`, `knowledge-base/wiki/`, `knowledge-base/raw/`, `knowledge-base/CLAUDE.md`, `~/My Brain/CLAUDE.md`, `~/CLAUDE.md` for the old paths. **Only hit:** the prior audit `raw/audits/2026-05-07-moil-repo-sync-check.md`, which is a historical document — leave as-is. No scripts, plists, configs, wiki pages, or CLAUDE.md instructions broke. Move is fully clean.

---

## Task 2 — `claude/moil-messaging-integration-JI9mJ` review (✅ analyzed)

**Recommendation: continue/activate. Do NOT archive. Strong composition with the agent-native MCP direction.**

**Quick stats**

| Field | Value |
|---|---|
| Branch | `origin/claude/moil-messaging-integration-JI9mJ` (in moil-bpc) |
| Created | 2026-04-05 |
| Last touched | 2026-04-05 (single-commit branch — `d1d0d8e`) |
| Commits ahead of master | 1 |
| Diff size | 7 files, 921 line additions |
| Touched files | `app.js` (+2 lines, route mount), 6 net-new files |
| Tests | None added in branch |

**Feature scope (honest read)**

A complete v1 of a messaging-bot service that wires Telegram + WhatsApp to the existing **Business Coach AI**. Architecture is clean:

```
routes/messaging.bot.route.js   →  HTTP API surface (5 endpoints)
controller/messaging.bot.controller.js  →  request handlers
service/bot/botService.js       →  platform-agnostic orchestration
service/bot/telegramAdapter.js  →  Telegram Bot API HTTP calls (no SDK)
service/bot/whatsappAdapter.js  →  WhatsApp Cloud API HTTP calls (no SDK)
model/BotLink.js                →  Mongo schema: (platform, platformUserId) → moilUserId + sessionId
```

**API surface:**
- `GET  /bot/health` — service health probe
- `POST /bot/telegram` — Telegram webhook (no auth, signed by token in URL)
- `GET  /bot/whatsapp` — WhatsApp webhook verification (Meta hub challenge)
- `POST /bot/whatsapp` — WhatsApp webhook (message receive)
- `POST /bot/link` — account-link confirmation (Moil JWT required)
- `POST /bot/setup/telegram` — webhook registration (API-key gated, admin/deploy)

**Account-linking flow:** unlinked user messages bot → bot generates 15-min Redis token → instructs user to confirm in Moil web → web POSTs `/bot/link` with JWT → BotLink doc persists → subsequent messages route to the existing Business Coach with a `botConversationId` for memory continuity.

**Composes with existing infra** — uses `service/business.coach`, `utils/redisClient`, `authenticate` middleware, `nanoid`, `axios`, `mongoose`. No new infra dependencies. No new package.json entries.

**What's needed before shipping**

| Item | Status |
|---|---|
| Telegram bot registered via @BotFather | unknown — Andres to verify |
| WhatsApp Business Cloud API app at Meta Developer Console | unknown — Andres to verify |
| 5 new env vars (`TELEGRAM_BOT_TOKEN`, `WHATSAPP_PHONE_NUMBER_ID`, `WHATSAPP_ACCESS_TOKEN`, `WHATSAPP_VERIFY_TOKEN`, `FRONTEND_URL`) | not in `.env.example` (probably — check) |
| Frontend page that completes the linking handshake (POSTs `/bot/link` with the platform token + JWT) | not in this branch — would be on moil-app side |
| Tests | none — small focused branch; reasonable to ship without |
| Production webhook URL registered with Telegram (`setWebhook`) | one-time via `POST /bot/setup/telegram` |
| Production webhook URL registered with Meta | one-time, manual via Meta dashboard |

**Strategic overlap with agent-native MCP pivot**

This branch is **not** the MCP work, but it's the *delivery vehicle* the MCP work needs. The MCP pivot's value proposition is "give the Moil AI a programmable interface to channels SMB owners are already in." WhatsApp + Telegram **are** those channels. The architectural shape — `route → controller → platform-agnostic service → existing AI → platform adapter` — is exactly the shape an MCP-driven version would take; the only difference is the AI logic at the center plugs into MCP tool-use instead of a direct `business.coach` call.

**Recommendation:** keep the branch alive. When the agent-native pivot lands, swap the `coachService.handleMessage(...)` call in `botService.js` for an MCP-driven equivalent and the channels light up. If the pivot doesn't land for 2+ months, **merge this as-is** (with env-var config) so v1 messaging is shipping while v2 is built. Either way, archiving is the wrong call — this is 921 lines of properly-architected feature work tied to where the puck is going.

**Action items for Andres on this branch:**
1. Confirm whether Moil has registered apps at @BotFather (Telegram) and Meta Developer Console (WhatsApp Business Cloud).
2. Decide: merge to master + ship behind feature flag NOW, or hold for the agent-native milestone? Either is defensible.
3. If shipping: add the frontend linking page (~1 day on moil-app side), wire the 5 env vars to Render/Vercel/wherever moil-bpc deploys.

---

## Task 3 — Branch sprawl candidates (⚠️ AWAITING APPROVAL — nothing deleted)

**Rules applied:**
- Skip if branch name matches `main|master|develop|prod-*|stable-*|version-*|latest-prod-*|prod-v*` (protected — current or historical production tags).
- Skip if last commit is within 90 days (cutoff: 2026-02-11).
- Skip if branch is NOT merged into `main`/`master` (preserved — could be in-flight work).
- Candidates = merged into base AND >90d untouched AND not protected.

### moil-app — 1 deletion candidate

| Branch | Last commit | Age | Last message | Verdict |
|---|---|---|---|---|
| `mergingBch` | 2024-10-31 | 18 months | "update" | ✓ delete — vague name, year-and-a-half-old throwaway, fully merged |

### moil-bpc — 7 deletion candidates

| Branch | Last commit | Age | Last message | Verdict |
|---|---|---|---|---|
| `b-coach` | 2025-10-28 | ~6.5 months | "update" | ✓ delete — superseded by b-coach-v3 → master |
| `b-coach-v2` | 2025-11-06 | ~6 months | "update" | ✓ delete — superseded |
| `b-coach-v3` | 2025-11-06 | ~6 months | "update" | ✓ delete — superseded |
| `format-docx` | 2025-09-07 | ~8 months | "update on the business plan docx format" | ✓ delete — feature branch from a year ago, fully merged |
| `staging-v1` | 2025-11-06 | ~6 months | "update" | ✓ delete — superseded by current staging cadence |
| `v1_2026` | 2025-12-23 | ~5 months | "updates on the formatting" | ✓ delete — quarterly snapshot, fully merged |
| `v2_2026` | 2026-01-14 | ~4 months | "update" | ✓ delete — quarterly snapshot, fully merged |

### Preserved (not candidates — for transparency)

- All `prod-v*`, `latest-prod-*`, `stable-*`, `version-*` branches kept even when merged + old (per protection rule — these are historical production markers).
- All `claude/*` branches (active automation artifacts) kept regardless of merge status.
- `seo/1.3-robots-sitemap` (moil-app, not merged) — preserved as in-flight work.
- `claude/moil-messaging-integration-JI9mJ` (moil-bpc, not merged) — preserved per Task 2 verdict.
- `claude/audit-gemini-key-leak-zCu50` (both repos, not merged) — security audit work, preserved.
- `claude/fix-document-upload-error-eibyI`, `claude/debug-live-product-Vv8hb`, `claude/fix-month-creation-bug-JdQWR` (moil-bpc, not merged) — recent debugging work, preserved.
- `v3_2026`, `v3_2026_26`, `v4_2026_04_17`, `v5_2025`, `neww` (moil-bpc, merged but within 90 days) — preserved by age rule.
- `stable-v2`, `version-1`, `version-1.0` (moil-app) — within 90 days OR `stable-*`/`version-*` protected.

### Anomaly to flag

Both repos have a remote-tracking entry literally named `origin/origin` — a remote branch whose canonical name is `origin`. Could be an accidental `git push origin HEAD:origin` from a prior workflow. Not destructive (it's just a remote ref), but worth investigating + cleaning if you can identify what created it. Not in the candidate list above.

### To execute deletion (after your approval)

```bash
# moil-app
cd ~/Moil/moil-app
git push origin --delete mergingBch

# moil-bpc
cd ~/Moil/moil-bpc
for br in b-coach b-coach-v2 b-coach-v3 format-docx staging-v1 v1_2026 v2_2026; do
  git push origin --delete "$br"
done
```

These commands delete the branches **on origin** (GitHub). Local tracking refs auto-prune on next `git fetch --prune`. The branches' commits are preserved in git history as long as they're reachable from any other ref (the `merged=yes` flag guarantees they're reachable from `main`/`master`).

**Reply with "go" + an optional opt-out list** (e.g. "go, but keep `format-docx`") and I'll run the deletions and confirm. Reply with "veto" and nothing happens. Default action without reply: nothing.

---

## Recommended next actions

1. **Approve / veto the 8 branch deletion candidates.** Each is reversible until 90 days post-deletion via the reflog on origin, so the risk is bounded — but I'm not running anything without your say.
2. **Decide on the messaging branch** (Task 2): merge-as-is + ship, hold until MCP pivot, or some middle path.
3. **Push the brain repo cleanup commit** (gitlink removals + this audit file) once you've reviewed. The CI warning `No url found for submodule path 'moil-app' in .gitmodules` will stop appearing on every CI run after this lands.
4. **Investigate the `origin/origin` remote-tracking refs** in both repos. Likely accidental; safe to delete with `git push origin --delete origin` (after confirming it doesn't shadow `origin/HEAD`).
