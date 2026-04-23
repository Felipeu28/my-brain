# Claude Code Maximization Setup
**Date:** 2026-04-22
**Author:** Claude Code (automated setup)

## What was implemented

### 1. Universal rules — `~/.claude/CLAUDE.md`
Added a "Universal Claude Code Rules" section at the top of the global CLAUDE.md (preserving existing gstack content below it). Covers:
- Identity: Andres is CEO of Moil, 3 active repos
- Worktree discipline: always isolate tasks, never work on main directly
- Commit style: conventional commits + Co-Authored-By Claude
- Push rule: explicit confirmation required; always `timeout 30 git push`
- Ambiguity rule: ask ONE question before starting
- Simplicity rule: minimum code that solves the problem
- Surgical edits: touch only what the task requires
- No launchctl in any bash commands
- Test before marking done

### 2. Stop hooks — all 3 repos
Each repo now has:
- `.claude/hooks/stop.sh` (executable) — fires macOS "Glass" notification + appends timestamp to `~/.claude/task-log.txt`
- `.claude/settings.json` — registers the hook via the `Stop` event

Repos covered:
- `~/My Brain/pi-workspace/.claude/`
- `~/My Brain/knowledge-base/.claude/`
- `~/luna-brain/.claude/`

> Note: Claude Code's official hook config format is `settings.json`, not `hooks.json`. The task spec mentioned `hooks.json` but `settings.json` is what Claude Code actually reads. The stop.sh scripts are in `.claude/hooks/` as requested.

### 3. pi-workspace CLAUDE.md — created from scratch
`~/My Brain/pi-workspace/CLAUDE.md` is a new file documenting:
- What the workspace is and what NOT to do (don't refactor production scripts)
- Hard rules: `timeout N`, read-before-edit, manual test, no launchctl
- Full `bin/` script reference table: trigger, input, output, success condition for 18 scripts
- Error handling conventions (log vs. crash)
- Skills reference for all 6 `.pi/skills/`
- Karpathy principles section

### 4. GitHub MCP config — `~/.claude/mcp.json`
Created with the `@anthropic-ai/mcp-server-github` entry. `GITHUB_TOKEN` is left blank for manual fill.

**Where to get the token:** github.com → Settings → Developer settings → Personal access tokens (classic) → Generate new token. Scopes needed: `repo`, `read:org`, `read:user`.

### 5. Karpathy principles — added to luna-brain and knowledge-base CLAUDE.md
Added "Code Quality Principles (Karpathy-Inspired)" section to both:
- `/Users/jarvisurrego/luna-brain/CLAUDE.md` (before "Sibling doc" section)
- `knowledge-base/CLAUDE.md` (after `/brain-lint` command section)

Four principles: Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution.

---

## 3 things Andres must do manually

1. **Fill in GITHUB_TOKEN in `~/.claude/mcp.json`**
   Open `~/.claude/mcp.json` and set `"GITHUB_TOKEN": "ghp_..."` with a personal access token from github.com → Settings → Developer settings → Personal access tokens. Scopes: `repo`, `read:org`, `read:user`.

2. **Install the Karpathy plugin via Claude Code**
   Open any Claude Code session and run:
   ```
   /plugin install andrej-karpathy-skills@karpathy-skills
   ```
   The CLAUDE.md sections add the principles as static rules; the plugin adds interactive skill commands on top.

3. **Test the Stop hooks**
   Run any task in pi-workspace, knowledge-base, or luna-brain using Claude Code. When the session ends you should:
   - See a macOS notification: "Task complete in [repo-name]"
   - See a new line in `~/.claude/task-log.txt` with the timestamp

---

## Follow-up improvements (optional)

- **Add a PreToolUse hook** that logs every bash command Claude runs — useful for auditing what the automation scripts are doing
- **Add a `timeout N` lint rule** to the Stop hook: scan the last session's bash commands for missing `timeout` prefixes and log a warning
- **Sync Karpathy principles to luna-brain/AGENTS.md** — the CLAUDE.md was updated but AGENTS.md (Codex sibling) was not touched; update it when doing the next luna-brain task
- **Set `AUTH_ENFORCE=strict`** in luna-brain Vercel once the env mismatch from the 2026-04-20 incident is confirmed resolved
