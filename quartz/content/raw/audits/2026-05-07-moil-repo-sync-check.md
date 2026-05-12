---
type: audit
date: 2026-05-12
ingested: true
ingested_at: 2026-05-12
tags:
  - graph/leaf
---
# Moil repo sync check

**Verdict:** both checkouts now in sync with their respective `Moil-Code/*` origins. Both were significantly behind (84 + 237 commits) but local trees were clean, so `git pull --ff-only` was safe and applied. No diverged branches, no uncommitted work, no submodule references, no orphan `agent-mcp`/`feat/mcp` branches found. **One unusual structural fact for Andres to consider:** the placement is `~/My Brain/knowledge-base/moil-app` and `~/My Brain/knowledge-base/moil-bpc` — i.e. production checkouts nested *inside* the Brain repo. This is preserved (not changed), but it's worth deciding whether to move them to a more conventional path.

---

## moil-app

- **Local path:** `~/My Brain/knowledge-base/moil-app`
- **Origin:** `https://github.com/Moil-Code/Moilapp_business`
- **Identity (README + package.json):** Create-React-App-bootstrapped frontend; `package.json` name = `moil-employer-app`. This is the **Moil Employer Platform** front-end — production, not a fork.
- **Default branch (origin HEAD):** `main` ✓ matches checked-out branch
- **Last commit (pre-pull):** `01bdbe3` · 2026-04-21 17:40 · `fix(moil360): stop frame templates silently failing to apply`
- **Last commit (post-pull):** `f978016` · 2026-05-12 17:43 · `fixed the error toast in the chat`
- **Status pre-pull:** clean, behind by **84 commits**
- **Status post-pull:** clean, **0 commits behind / 0 ahead** ✅
- **Uncommitted changes:** none (pre and post)
- **Total remote branches:** 19 — including `claude/audit-gemini-key-leak-zCu50`, `claude/debug-live-product-Vv8hb`, `claude/fix-asset-download-error-BpLxb`, `claude/fix-company-image-generation-Zu7WE`, `claude/fix-content-sizing-images-HUKot`, `claude/fix-document-upload-error-eibyI`, `claude/investigate-client-issue-9YdzD`, `claude/audit-moil-360-tools-XJpAP`, `seo/1.3-robots-sitemap`, `latest-prod-1`, `mergingBch`, `prod-v1`, `prod-v2`, `prod-v3-latest`, `stable-v1`, `stable-v2`, `version-1`, `version-1.0`, `main`.
- **Orphan / agent-native branches:** none matching `agent-mcp`, `feat/mcp`, or `agent/*`. The `claude/*` branches are routine Claude Code automation artifacts, not pre-existing agent-native work.
- **Submodule status:** no `.gitmodules` file; `git submodule status` returns empty. No stale submodule reference to worry about.
- **Verdict:** ✅ **clean** — fast-forwarded 84 commits to match origin/main. The local checkout is now current.

## moil-bpc

- **Local path:** `~/My Brain/knowledge-base/moil-bpc`
- **Origin:** `https://github.com/Moil-Code/Business-plan-beta-prod`
- **Identity (README + package.json):** Node/Express backend that generates `.docx` business plans from JSON; `package.json` name = `moil-businessplan-creator-beta`. This is the **Moil Business Plan Creator** — production beta, not a fork.
- **Default branch (origin HEAD):** `master` ✓ matches checked-out branch
- **Last commit (pre-pull):** `b4fd270` · 2026-04-21 17:41 · `fix(content360): make frame compositing more resilient + report status`
- **Last commit (post-pull):** `ad3c5de` · 2026-05-12 17:47 · `update`
- **Status pre-pull:** clean, behind by **237 commits**
- **Status post-pull:** clean, **0 commits behind / 0 ahead** ✅
- **Uncommitted changes:** none (pre and post)
- **Total remote branches:** 28 — including `b-coach`, `b-coach-v2`, `b-coach-v3`, `claude/audit-gemini-key-leak-zCu50`, `claude/audit-moil-360-tools-XJpAP`, `claude/debug-live-product-Vv8hb`, `claude/fix-asset-download-error-BpLxb`, `claude/fix-company-image-generation-Zu7WE`, `claude/fix-content-sizing-images-HUKot`, `claude/fix-document-upload-error-eibyI`, `claude/fix-month-creation-bug-JdQWR`, `claude/investigate-client-issue-9YdzD`, `claude/moil-messaging-integration-JI9mJ`, `format-docx`, `latest-prod-1`, `neww`, `prod-v1`, `prod-v1-latest`, `prod-v2`, `staging-v1`, `stable-version-1.0`, `v1_2026`, `v5_2025`, `master`.
- **Orphan / agent-native branches:** none matching `agent-mcp`, `feat/mcp`, or `agent/*`. One feature-flavored remote-only branch worth noting: `claude/moil-messaging-integration-JI9mJ` — `feat: add Moil Mini Bot — WhatsApp & Telegram AI coach integration`. That's a substantive feature branch, not just a fix; surface in case Andres has lost track of it.
- **Submodule status:** no `.gitmodules` file; `git submodule status` returns empty.
- **Verdict:** ✅ **clean** — fast-forwarded 237 commits to match origin/master. The local checkout is now current.

---

## Recommended next actions

1. **Decide repo placement.** Both repos sit inside `~/My Brain/knowledge-base/`. Three downsides: (a) every `kb-health` and `sync_wiki.sh` walk has to skip them via .gitignore (currently fine because `.gitignore` covers them implicitly via missing extensions, but worth verifying); (b) the Quartz build at `quartz/content/` could accidentally pick up these subdirectories' README/markdown files if the include patterns ever expand; (c) the placement is unconventional — production checkouts typically live in `~/projects/` or `~/code/` for clean tooling. Suggested move: `mv ~/My\ Brain/knowledge-base/moil-app ~/Moil/moil-app && mv ~/My\ Brain/knowledge-base/moil-bpc ~/Moil/moil-bpc`. Reversible; not urgent.

2. **Review feature branch `claude/moil-messaging-integration-JI9mJ` in moil-bpc.** It's a Moil Mini Bot (WhatsApp + Telegram coach) integration. Not merged to master. Verify it's not lost work — if it's a stalled feature, decide ship vs delete.

3. **Curate the production branch sprawl.** moil-bpc has 28 remote branches and moil-app has 19. Many look like point-in-time prod snapshots (`prod-v1`, `prod-v2`, `latest-prod-1`, `stable-v1`, `version-1`, `version-1.0`, `b-coach-v2/v3`, `v1_2026`, `v5_2025`). These accumulate forever in `git branch -r` output and clutter every fetch. Not urgent — purely cosmetic. Could be batch-deleted on the remote with a quick review.

4. **Add `kb-health.py` skip rules for these directories.** Confirm that the wiki-health linter doesn't try to validate frontmatter on the moil-app/moil-bpc internal docs. (Probably already excluded by extension or path rules, but worth verifying.)

5. **Routine cadence.** Both repos were >2 weeks behind. If Andres regularly uses these checkouts for any debugging or reference work, a weekly `git pull --ff-only` on both — added to one of the existing launchd weekly jobs — would prevent future drift. Effort: 5 lines of bash. Skip if these checkouts are dormant reference copies, not active.

---

*Audit generated 2026-05-12. Both repos confirmed clean and current. No items needing immediate decision; the placement question (item 1) and the dormant feature branch (item 2) are the two worth Andres's attention when he has a few minutes.*
