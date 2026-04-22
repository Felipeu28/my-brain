# Brain UI — Theme primitives (Phase 0)

**Created:** 2026-04-22
**Goal:** Modern, fun, not crazy. Distinct from OpenClaw's dark-slate/cyan look — the Brain UI is personal, daytime-first, warm.

## Design direction

**Keywords:** warm · calm · confident · readable · a little bit playful.

Think "morning coffee at a beautiful cafe," not "mission control." The Brain UI is the first thing Andres looks at most mornings — it should feel inviting, not operational.

## Typography

| Role | Family | Weight | Notes |
|---|---|---|---|
| Display (H1, big numbers) | **Instrument Serif** | 400 | Warm, literary feel for headers. Free Google font. Italic cuts are stunning. |
| Body / UI | **Inter** | 400, 500, 600 | The reliable workhorse. Optical-sized at display sizes. |
| Mono (code, action IDs, timestamps) | **JetBrains Mono** | 400, 500 | Friendly curves, crisp at small sizes. |

**Why not Geist or Space Grotesk?**
- Geist reads as "Vercel brand" and feels engineering-ops-ish.
- Space Grotesk is already OpenClaw's voice — we want distinction.
- Instrument Serif + Inter is a small pattern currently trendy with Linear, Vercel's newer demos, and personal-site aesthetics — warm without being cute.

**Fallback:** `ui-serif`, `ui-sans-serif`, `ui-monospace` — local stack for offline.

## Color

Single accent + neutral scale. No rainbow.

### Light mode (default)

| Token | Value | Use |
|---|---|---|
| `--bg` | `#FAF9F6` (warm off-white) | Page background |
| `--bg-raised` | `#FFFFFF` | Cards |
| `--bg-muted` | `#F3F1EC` | Inset panels, disabled rows |
| `--ink` | `#1A1814` (near-black warm) | Primary text |
| `--ink-soft` | `#5A564E` | Secondary text |
| `--ink-mute` | `#9A958B` | Tertiary / timestamps |
| `--border` | `#E8E4DC` | Card borders, separators |
| `--accent` | `#C2410C` (burnt orange, Tailwind orange-700) | Primary accent — interactive, highlights |
| `--accent-soft` | `#FED7AA` (orange-200) | Hover backgrounds, badges |
| `--accent-ink` | `#7C2D12` (orange-900) | Text on accent-soft |
| `--success` | `#15803D` (green-700) | Completed state |
| `--warn` | `#B45309` (amber-700) | Stale / snoozed |
| `--danger` | `#B91C1C` (red-700) | Red deploys, overdue |

**Why burnt orange?** Warm but not loud. Signals energy without feeling corporate. Pairs with warm off-white better than saturated accents would.

**Completion treatment:** strike-through + move to muted opacity (50%), don't delete the row. Visual feedback that "yes, I did that."

### Dark mode (Phase 2)

Defer. Daytime tool, daytime colors first. When added: warm near-black (`#171410`) not cool slate, accent stays orange.

## Spacing & rhythm

Tailwind default scale. Use generous spacing — the UI should feel uncluttered.

- Page padding: `px-6 md:px-12`
- Section gap: `gap-y-10` between widgets
- Card padding: `p-6`
- Bullet list gap: `gap-y-3`
- Max content width: `max-w-3xl` (forces readable line length; the Brain UI is a reading surface first)

## Radius & elevation

- Cards: `rounded-2xl` (16px) — soft, confident
- Buttons / chips: `rounded-full` for small, `rounded-lg` for larger
- Shadows: `shadow-sm` default, `shadow-md` on hover for interactive cards. Never `shadow-xl`.

## Motion

- Hover: 150ms ease-out, color + elevation
- Checkbox toggle: 200ms, spring feel (scale 1 → 1.08 → 1)
- Snooze / dismiss: slide-out-left 220ms, row collapses
- Page load: no skeleton, no spinner — just render. SQLite is fast.

**Hard rule:** no scroll-triggered animations. No "cute" micro-interactions. Playfulness is in the typography and the burnt-orange accent, not in wiggles.

## Components — visual spec sketches

### Action row (the workhorse component)

```
┌─ ActionRow ────────────────────────────────────────────────┐
│  [☐]  Text of the action, can wrap to two lines if needed  │
│        Helotes EDC · 3 days nagging · snooze? note? ↗       │
└────────────────────────────────────────────────────────────┘
```

- Checkbox is 20px, left-aligned, accent-colored when checked
- Title: body weight 500, `--ink`
- Metadata row below: weight 400, `--ink-mute`, 13px
- On complete: strike-through title, 50% opacity on whole row, stays in list for the day (collapses tomorrow)

### Priority card (prominent, top of page)

```
┌─ PriorityCard (accented left border) ──────────────────────┐
│  #1  ·  🔥  ·  Helotes EDC / Kate Silvas — 10 AM call      │
│                                                             │
│      Walk in with: Buda EDC one-pager + draft proposal…    │
│                                                             │
│  [☐ Mark done]   [💤 Snooze]   [📝 Add note]                │
└────────────────────────────────────────────────────────────┘
```

### People radar card (unified awaiting + cold + stale)

```
┌─ Travis Sutherland ──────────────────────── ⚠ 2 days out ──┐
│  Zoiwell · Sun Show host                                    │
│  • Going cold  (14+ days silent)                            │
│  • Deal stale  (last touch Apr 9)                           │
│  [Ping]  [Snooze 3d]  [Open in wiki ↗]                      │
└────────────────────────────────────────────────────────────┘
```

## Example first-render screen

```
════════════════════════════════════════════════════════════
Wednesday, April 22                                  ≡ today
                                                  (archive)
════════════════════════════════════════════════════════════

Good morning. Three things matter today.

🔥 #1 Helotes EDC / Kate Silvas — 10 AM call
     Highest revenue lever on the board.
     [☐ Done]  [💤 Snooze]  [↗ Open wiki]

🔥 #2 Megan / FitLogic — 11 AM working session
     Fix fit-logic Vercel deploy FIRST.
     [☐ Done]  [💤 Snooze]

   #3 Buda HIVE Cohort 4 — confirm contract
     [☐ Done]  [💤 Snooze]

──────────────────────────────────────────────

⚠ Going cold                               8 contacts
   Travis Sutherland                       2 days → 🔥 urgent
   Jennifer Storm
   Jacquie Martinez
   …

──────────────────────────────────────────────

📬 Inbox · 15 unread                  4 action · 2 fyi
   Elisa Alaniz — proposes Friday call
   Stripe — webhook failures on stagebeta
   …

──────────────────────────────────────────────

🧠 Brain says
   The 10 AM Kate Silvas call is the day…

──────────────────────────────────────────────

{collapsed} ▸ Schedule
{collapsed} ▸ Code activity (5 PRs open)
{collapsed} ▸ People notes
```

Collapsed-by-default sections reduce visual noise. Priorities + Going Cold + Inbox Action are the three "always open" widgets.

## Tailwind config sketch

```js
// tailwind.config.ts (for reference — will finalize in Phase 1)
export default {
  theme: {
    extend: {
      fontFamily: {
        display: ['"Instrument Serif"', 'ui-serif', 'Georgia', 'serif'],
        sans:    ['Inter', 'ui-sans-serif', 'system-ui'],
        mono:    ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
      },
      colors: {
        bg:       { DEFAULT: '#FAF9F6', raised: '#FFFFFF', muted: '#F3F1EC' },
        ink:      { DEFAULT: '#1A1814', soft: '#5A564E', mute: '#9A958B' },
        border:   { DEFAULT: '#E8E4DC' },
        accent:   { DEFAULT: '#C2410C', soft: '#FED7AA', ink: '#7C2D12' },
        success:  '#15803D',
        warn:     '#B45309',
        danger:   '#B91C1C',
      },
      maxWidth: { prose: '48rem' },
      borderRadius: { '2xl': '1rem' },
    }
  }
}
```

## Open questions for Andres

1. **Orange accent OK?** Alternatives that would work: deep indigo `#4338CA`, forest green `#166534`, or muted coral `#E76F51`. Orange is my pick because it matches "warm, energizing" without being as common as blue/green.
2. **Instrument Serif for headers OK?** Alt: go all-sans with Inter at various sizes. Less visual personality but more conservative.
3. **Light mode only for v1?** Dark mode adds ~1 day. Given you check this in the morning, I'd skip dark mode until explicitly wanted.
