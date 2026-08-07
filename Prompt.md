# Prompt.md — Current Request Log

## Request (2026-08-07, 9th): Quest rebalance + guided tour — DONE (committed, NOT pushed)

**User request:** (1) The 50-level XP curve is still too steep/slow at high ranks — rebalance the thresholds. (2) Rebalance quest tasks — some are too hard; add small easy tasks to make it rewarding. (3) The quest guide: when the user taps the FIRST quest, take them through everything so they know where things are — a proper auto-navigating system (auto-navigate on next tap) with a small TOAST-TYPE OVERLAY, NOT a full dialog. Clarified via follow-up: "by the toast i meant in app overlay system" — an in-app floating overlay, not a system Toast. "don't ask me, do it on your own."

### Changes
- **XP curve rebalance** (`data/CurioQuests.kt`) — first 12 thresholds unchanged (quick early levels); after that the per-level step now grows +8/level from 90 and caps at **240 XP** (was +12 from 110, cap 360). Total ~**8.6k XP** (was ~12.1k): Level 30 ≈ 3.8k, Level 40 ≈ 6.2k, Level 50 ≈ 8.6k. Existing XP is cumulative, so existing users instantly gain levels — no progress lost.
- **Small easy quest stages added** (kept every existing stage id so awarded badges never reset / XP never double-pays): The Deck + Spin 3/10/50; Discovery + Explore 3/10 + "Lane Hopper" (3 lanes); Keepsakes + Save 3/10/50; The Shelf + 3 quotes; Pin Board + 3 pins; The Flame + 1-day & 14-day streaks; Taste + 3 likes.
- **Quest guide → in-app overlay + full tour** (new `data/QuestGuide.kt` + new `ui/components/QuestGuideToast.kt`):
  - The old full `AlertDialog` guide in the NavHost is replaced by a compact **in-app floating pill** overlay (flag marker, title, one-line message, footer, Next/Go button, close X).
  - Tapping the **first quest** ("First Spin" — via the Quests page Start button, a chain's Go chip, or the guide overlay's Go) launches a **7-step guided tour** that **auto-navigates** through Home → Spin → Cabinet → Profile → Quests → Settings → done, advancing on every overlay tap; the Spin step **waits for the real spin** (`CurioQuests.onSpin` reports via `QuestGuide.onWait`, same wiring for explore/save/profile/settings) and auto-advances when it happens. Finishing lands the user back on a stable tab.
  - `navigation/CurioRoutes.kt` — new shared `navigateToQuestRoute()` (tabs via navigateToTab, others pushed) used by both the Quests page and the tour runner.
- Changelog bullets added to `20260810.txt`.

### Status
- Statically validated (no Gradle in this env per AGENTS.md): no leftover `showGuideDialog`/`navigateToQuest` references, old dialog block fully removed (no duplicate `guideQuest` declarations), `git diff --check` clean, code review passed.
- Committed locally. **Not pushed** — branch is ahead of origin/main by `cc26e15`, `e9f46de`, `a2d0198` + this commit, all awaiting the user's go-ahead to push.
