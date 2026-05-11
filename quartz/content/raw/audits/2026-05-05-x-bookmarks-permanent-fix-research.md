---
type: audit
date: 2026-05-05
ingested: true
ingested_at: 2026-05-11
tags:
  - graph/leaf
---

# X Bookmarks Pipeline — Permanent Fix Research

**Context:** Today's incident (2026-05-05) re-exposed that `pi-workspace/bin/scrape-x-bookmarks.sh` is hostage to Chrome cookie expiry (~3–7 days). Recovery requires Andres at his Mac to re-import cookies. Multiple downstream pipelines (daily editorial, pattern-surfacer, weekly operating-brief, ChromaDB index) sit on this stream — fragility here is a load-bearing problem.

---

## 1. Verdict

**Switch to the X API (Option a), implemented via OAuth 2.0 PKCE with `offline.access` + `bookmark.read` (Option b is the implementation). Keep one piece of Option e — the weekly canary check — for general Brain hygiene, not as primary defense.**

The decisive finding: X retired the Basic ($200/mo) and Pro ($5,000/mo) tiers for new customers on 2026-02-06 and moved to **pay-per-use**. The bookmarks endpoint is classified as an "Owned Read" and is billed at **$0.001 per resource** since 2026-04-20. At ~200 bookmarks/day fetched once, that's **~$6/month** — an order of magnitude below the $200 ceiling Andres was bracketing. There is no minimum spend, no signup fee, no Basic tier to gate-keep us out. This collapses the hardest variable in the original decision tree: there is no longer a paywall scenario worth planning around. Hardened scraping (c) is strictly inferior — same ban risk, more code, worse fidelity. The instrumentation-only path (e) is a delay tactic, not a fix.

One caveat: a community report from late April flagged the bookmarks endpoint being billed at $0.005 instead of $0.001. Verify the actual billed rate during pilot week 1; even at $0.005 it's still ~$30/month and well under budget.

---

## 2. Comparison table

| Option | Monthly cost | Implement time | Reliability | Data fidelity | Risk | Verdict |
|---|---|---|---|---|---|---|
| **a) Paid X API (pay-per-use)** | **~$6** (200/day × $0.001 × 30) | 4–6 h | High — OAuth refresh = months; only break is X policy change | Full — handle, full text, URL, created_at, IDs, media | Low — sanctioned path, TOS-clean | **SHIP** |
| **b) OAuth 2.0 PKCE (impl strategy for a)** | (same as a) | (folded into a) | High — refresh token via `offline.access` lasts ~6 mo | Same as a | Low | **SHIP as the impl path for a** |
| **c) Hardened headless Chrome (persistent profile + Keychain)** | $0 | 8–12 h | Medium — survives Chrome restarts, but X periodically nukes sessions; 2FA + device-trust still drift | Same themes we get today | **High** — explicit TOS violation, suspension risk on `@roarkittys` | **REJECT** |
| **d) Alternative signal sources** | $0–$5 (Raindrop) | 2–20 h depending | Varies | **Lower** — not actual bookmarks unless behavior changes | Low | **REJECT as replacement; revisit Raindrop as future behavior change** |
| **e) Better instrumentation on current path** | $0 | 2–4 h | Defers — incidents quarterly instead of monthly | Same as today | Same TOS risk as today | **PARTIAL — keep weekly canary as belt-and-suspenders** |

---

## 3. Per-option deep-dives

### (a) Paid X API — pay-per-use

- **What it is:** Call `GET /2/users/:id/bookmarks` daily via X's official v2 API on the pay-per-use plan that replaced Basic/Pro for new customers on 2026-02-06.
- **Implementation work (4–6 h):**
  1. Register a developer app at `developer.x.com` (or confirm an existing one on `@roarkittys`).
  2. Generate OAuth 2.0 PKCE client credentials. Scopes: `bookmark.read tweet.read users.read offline.access`.
  3. One-time browser auth flow on Andres's Mac to mint the initial refresh token; store under `pi-workspace/.secrets/x-api/refresh_token` (mode 600).
  4. Python script `pi-workspace/bin/x-bookmarks-api.py`: load refresh token → exchange for access token → paginate `GET /2/users/:id/bookmarks?max_results=100&expansions=author_id&tweet.fields=created_at,text,entities&user.fields=username` → write same `raw/x-bookmarks-YYYY-MM-DD.md` format the current scraper produces → persist rotated refresh token.
  5. Replace `scrape-x-bookmarks.sh` body with the Python call. Leave the launchd plist untouched (still 19:00 daily).
  6. Add `kb-health` check that fails if no new file in 36 h.
- **Monthly cost:** ~$6 at 200 bookmarks/day × $0.001 owned-read × 30 days. Even at the disputed $0.005 rate, ~$30/month. Hard ceiling: pay-per-use caps at 2M post reads/month before forcing Enterprise — irrelevant at our volume.
- **Reliability profile:** Refresh token lives ~6 months with `offline.access` and rotates on each use. Only break modes are (i) X changes pricing/policy, (ii) Andres revokes app, (iii) network. RTO measured in minutes (re-run with cached token).
- **Data we'd get:** Cleaner than today — structured JSON with author handle/name, full tweet text, tweet URL, `created_at` timestamp, entity-extracted URLs, media keys, conversation IDs. Trivial to thematize the same way Claude does today.
- **Data we'd lose:** Nothing material. The scrape today is already a lossy projection of the same underlying objects.
- **Risk / red flags:** Lowest of any option. Sanctioned path. The only real risk is X reverting the cheap owned-read rate — at which point cost still rounds to nothing for our volume.

### (b) OAuth 2.0 PKCE — implementation strategy for (a)

Not a separate option; the implementation detail under (a). Worth stating explicitly because the original framing treated it as parallel.

- **Scope set:** `bookmark.read tweet.read users.read offline.access`. The `offline.access` scope is what gets you a refresh token.
- **Flow:** OAuth 2.0 Authorization Code + PKCE (X does not support client_credentials for user-context endpoints). One interactive auth at setup; thereafter the refresh token rotates silently on every access-token mint.
- **Token lifetimes:** Access token ~2 h. Refresh token ~6 months as long as `offline.access` is in the original grant and the refresh is exercised before expiry.
- **Paywall coupling:** Independent. OAuth works on pay-per-use. There is no longer a "valid OAuth but no API access" failure mode for new accounts because the only plan IS pay-per-use.

### (c) Hardened headless Chrome with stored credentials

- **What it is:** Stay on Playwright/gstack-browse with a persistent `--user-data-dir`, Keychain-stored password, scripted login on session-loss.
- **Implementation work (8–12 h):** Carve out a dedicated Chromium profile dir; pre-warm with one manual login; wire Playwright to drive the login form when redirected; integrate macOS Keychain via `security find-generic-password`; handle 2FA via TOTP secret stored alongside.
- **Monthly cost:** $0.
- **Reliability profile:** Better than today (survives Chrome quit/restart) but X invalidates sessions on detected automation, on suspicious IP patterns, and on periodic server-side cycles. Realistic MTBF: 2–8 weeks per cycle. RTO requires Andres or working scripted re-login.
- **Data fidelity:** Same as today.
- **Risk / red flags:** **This is the high-risk option.** X's TOS explicitly forbids non-human automation and scripted credential entry. `@roarkittys` is Andres's personal account — suspension would also cost the audience and DM history, not just the data feed. We have already proven the underlying approach is unstable; making it more sophisticated does not address the root cause.

### (d) Alternative signal sources

Each evaluated for whether it actually replaces "what Andres bookmarks on X":

- **Nitter / RSS frontends:** Effectively dead in 2026. The remaining instances are unstable mirrors. **Does not preserve value.**
- **X Lists API (own-context):** Returns what Andres's network *posts*, not what he *bookmarks*. Different signal. Currently the daily editorial already pulls from elsewhere for that. **Does not preserve value.**
- **Mentions API:** Wrong signal. **Reject.**
- **Mastodon / Bluesky / Threads:** Andres is not active on these as a primary bookmarking surface. Building a parallel pipeline doesn't capture his actual reading. **Does not preserve value.**
- **Raindrop / Pocket / Instapaper:** Real APIs, durable. But this requires a **behavior change** — Andres has to switch from "bookmark in X" to "save to Raindrop." Worth flagging as a longer-term consideration if Andres wants OS-level reading-list ownership, decoupled from any single platform. Cost: Raindrop Pro is $3/month. **Does not replace the X stream short-term; revisit as a separate decision.**

### (e) Better instrumentation on current path

- **What it is:** Keep cookie-based scraping; layer detection + faster recovery.
- **Concrete pieces:**
  - **Weekly canary login check** (~30 min to build): Saturday morning launchd job runs `browse goto https://x.com/home` and checks for login redirect. Emails Andres if detected.
  - **Auto-import on login** (~30 min): launchd LaunchAgent at user-login runs `cookie-import-browser chrome --domain x.com` from KB_DIR. Catches the drift case where Chrome is fine but the headless session has drifted.
  - **Cookie age fingerprint** (~45 min): inspect `auth_token` issuance timestamp; warn at 5 days.
  - **Multi-browser fallback** (~90 min): try Chrome → Brave → Edge in order.
- **Monthly cost:** $0.
- **Reliability profile:** Defers incident frequency from ~monthly to maybe ~quarterly. Does not eliminate the root cause.
- **Data fidelity:** Identical to today.
- **Risk:** Same TOS risk as today (unchanged).
- **Verdict:** Keep the weekly canary regardless — it's cheap insurance and useful for other auth-dependent pipelines (Teams, calendar). Skip the rest if we ship (a).

---

## 4. Decision matrix for Andres

The original framing assumed the calculus turned on whether bookmarks were paywalled to Pro/Enterprise. **That assumption is obsolete.** The 2026 pay-per-use model removes the paywall entirely for our volume.

**Path A — Paid API (recommended):**
- Work: 4–6 h end-to-end (app registration is the only step that can stall).
- Cost: ~$6/month at current rate; worst plausible scenario ~$30/month.
- ETA to ship: same-week if app registration approved; ~3 days realistic.
- Reliability: 6-month refresh-token horizon; no human-in-the-loop recovery for cookie expiry.
- Ban risk: zero.

**Path B — Hardened scraping (c + e):**
- Work: 10–16 h.
- Cost: $0.
- ETA to ship: ~1 week with debugging.
- Reliability: incidents quarterly instead of monthly. Still requires Andres for recovery.
- Ban risk: real, on his personal account.

**Recommendation: Path A.** The cost differential is ~$6/month against engineering hours we'd otherwise spend re-debugging cookie drift. Path B's only advantage (zero dollar cost) evaporates against the account-ban exposure on `@roarkittys`.

---

## 5. Open questions for Andres

1. **Does `@roarkittys` already have an X developer app registered?** If yes, what tier? (Legacy Basic at $200/mo would also work; we'd just be overpaying.) If no, expect a 1–3 day approval window.
2. **Acceptable monthly spend?** Confirm even ~$6–$30/month on X data is OK in principle. (Likely trivial, but a new recurring vendor charge is the kind of thing that should be a yes/no, not an assumption.)
3. **Verify the $0.001 owned-read rate is actually being billed for bookmarks** during pilot week 1 — there's a community report from late April that bookmarks were billed at $0.005. Even at that rate it's still under budget, but worth confirming before committing the architecture.
4. **Behavior-change appetite (longer horizon):** If Andres ever wants to decouple his reading list from X entirely, Raindrop ($3/mo) is the cleanest path. Not part of this fix, but worth flagging.

---

## Sources

- [X API Pricing Update: Owned Reads Now $0.001 — Effective April 20, 2026 (X Developers)](https://devcommunity.x.com/t/x-api-pricing-update-owned-reads-now-0-001-other-changes-effective-april-20-2026/263025)
- [X (Twitter) API Pricing in 2026: All Tiers (Postproxy)](https://postproxy.dev/blog/x-api-pricing-2026/)
- [Pricing — X Docs](https://docs.x.com/x-api/getting-started/pricing)
- [Bookmarks endpoint reference — X Docs](https://docs.x.com/x-api/posts/bookmarks)
- [OAuth 2.0 Authorization Code Flow with PKCE — X Docs](https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code)
- [Owned Reads $0.001 not applied to bookmarks — billed at $0.005 (X Developers)](https://devcommunity.x.com/t/owned-reads-0-001-rate-not-applied-to-bookmarks-endpoint-billed-at-0-005-instead/263311)
