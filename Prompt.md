# Prompt.md — Current Request Log

## Request (2026-08-07, 12th): Quest guide offer + quest screen cleanup — IN PROGRESS

**User request:** "add a 1st no option for the turtorial guide and keep it only when the user goes to the quest screen and taps and also hide the finished quests and compact the quest screen"

### Analysis
- The quest tour had TWO entry points: (1) a NavHost auto-showing "Next quest" guide pill that popped up on ANY stable tab after 1.2s (with a Go button that launched the full tour when the current quest was the first one), and (2) tapping the first quest on the Quests page — which launched the tour IMMEDIATELY with no consent prompt.
- User wants: a first-time "No" option, the tour ONLY from a Quests-page tap, finished quests hidden, and a denser quest screen.

### Design
- **One-time offer (v8.2)** — new persisted `guide_tour_offered` flag (AppPreferences). Tapping the first quest on the Quests page opens a compact AlertDialog ("Take a quick tour?" / "No, thanks"). "No, thanks" OR dismissing marks the offer as seen → the first quest navigates normally from then on, never re-asking. The existing "Guided tour" Settings toggle becomes the master switch (offer only when ON; copy updated).
- **Quests-page-only trigger** — the NavHost auto-showing guide pill (state + LaunchedEffect + overlay block) is REMOVED; the tour can only be started from the Quests screen tap. `CurioQuests` import dropped from the NavHost (now unused).
- **Hide finished + compact** — `activeChains = Chains.filter { chainProgress < stages.size }` hides fully-completed chains (badge shelf still shows everything); spacing tightened across LevelCard, CurrentQuestCard, ChainCard, stage rows, DailyCard, BadgeShelf and BadgeTile, and the LazyColumn gap 10→8dp.

### Changes
- `data/AppPreferences.kt` — KEY_GUIDE_TOUR_OFFERED + `guideTourOfferedState` (seeded in initThemeMode) + `isGuideTourOffered`/`setGuideTourOffered`; guideEnabledState doc updated.
- `navigation/CurioNavHost.kt` — removed auto-guide state/effect/overlay + unused import; comments updated.
- `features/quests/QuestsScreen.kt` — offer dialog + `offerTour` gate on the first quest; `navigateFromQuest` removed; CurrentQuestCard takes `showTourCta`; finished chains filtered; compaction.
- `data/QuestGuide.kt` — KDoc updated (offered once, never auto-shown).
- `features/settings/SettingsSectionScreen.kt` — "Guided tour" toggle subtitle updated.
- `fastlane/.../20260810.txt` — changelog bullet.
- `Prompt.md` — this log.

### Validation
No Gradle in this env (per AGENTS.md) — static checks: brace balance, unused-ref grep, `git diff --check`, code review. Commit + push pending.

### Follow-ups
- None.
