# Prompt.md — Current Request Log

## Request (2026-08-07): Topic-data CI fix + Cabinet/Quests/Guide overhaul

### Part 1 — DONE, pushed as `c7d4967` (CI validator now passes)
- Raised `exploreAction.instruction` cap 450 → 600 chars in:
  - `app/build.gradle.kts` (validateTopics Gradle task — the CI failure)
  - `scripts/validate_topics.py` (`MAX_INSTRUCTION_LEN`)
  - `app/src/main/assets/topics/SCHEMA.md` (contract doc)
- Removed `book-sympathizer-dupe` broken stub (empty instruction, tier 0) from `books.json`
- Committed the two user batch scripts (`batch_authors_books.py`, `batch_all_remaining.py`)
- Validator: 11 files, 3133 topics, **0 errors**

### Part 2 — DONE (uncommitted → next commit)
Big multi-part request (user answered ask_user: guide toggleable default-ON with Go-button dialog; quests: unify EVERYTHING into chains + UI redesign; levels → 50):

1. **Cabinet chips** — `CabinetChipBarRestTop` 10dp → 4dp below hero (closer to tear); content tops 18 → 12dp.
2. **Cabinet card redesign** (`CurioTopicCard.kt`) — compact 96dp hero header with mini category watermark scatter (BoxScope.MiniHeroWatermark/MiniHeroGlyph), body = title + Today/Yesterday + format symbol only (body preview + tags removed) → cleaner shared-element morph.
3. **CurioQuests v8.0** — full rewrite:
   - 50-level XP curve (12 legacy thresholds + widening steps → level 50 at ~18,458 XP), 50 rank titles
   - Unified **quest chains**: Deck (spin), Discovery (explore), Keepsakes (save), Tour (guided walkthrough w/ navRoutes), Shelf (quote), Pin Board (pin), Flame (streak), Taste (like), Ladder (XP ranks)
   - Stage-based awarding (`awardedStagesState`), legacy journey/achievement id migration map, `checkAll` while-loop (XP stages cascade), guarded write
   - Public API: `Chains`, `allStages()`, `stageProgress()`, `isStageDone()`, `chainProgress()`, `currentQuest()`; hooks unchanged
4. **QuestsScreen** — rewritten for chains: rank card (50 levels), CURRENT QUEST hero w/ Go button, chain cards w/ clickable stage Go rows + progress bars, Today's quests, unified badge shelf.
5. **ProfileScreen** — quest card migrated to new API (`currentQuest()`, `allStages()`, `isStageDone()`).
6. **Auto-guide** — `AppPreferences.guideEnabledState` (default true, KEY_GUIDE_ENABLED), Settings Appearance "Guided tour" toggle; CurioNavHost guide dialog (1200ms delay on stable tab, "Go · +XP" navigates to quest screen, "Later" dismisses per-quest via rememberSaveable).
7. **PromoMode** — `DEMO_XP` 960 → 20000 (sits above level-50 threshold so promo shows Curio Sovereign).

### Remaining
- Commit + push Part 2, then any follow-ups the user requests.
