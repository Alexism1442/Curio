# Prompt.md — Current Request Log

## Request (2026-08-07): Topic-data CI fix + Cabinet/Quests/Guide overhaul + Settings search & DB scroll

### Part 1 — DONE, pushed as `c7d4967`
- Raised `exploreAction.instruction` cap 450 → 600 chars in `app/build.gradle.kts`, `scripts/validate_topics.py`, `app/src/main/assets/topics/SCHEMA.md`
- Removed `book-sympathizer-dupe` broken stub from `books.json`; committed the two user batch scripts
- Validator: 11 files, 3133 topics, **0 errors**

### Part 2 — DONE, pushed as `d85d143`
- Cabinet chips closer to tear; compact entry card redesign (mini watermark + title/time/symbol only)
- CurioQuests v8.0: 50-rank XP curve, unified quest chains (Deck/Discovery/Keepsakes/Tour/Shelf/Pin Board/Flame/Taste/Ladder), stage-based awarding, legacy migration
- QuestsScreen + Profile quest card migrated; auto-guide dialog (toggleable, default ON); PromoMode DEMO_XP → 20000

### Part 3 — DONE, pushed as `989ce3b`
- CI compile fix: `chainDone` hoisted out of `Row` scope in QuestsScreen ChainCard

### Part 4 — DONE, pushed as `24489d4`
- Settings search deep-indexes sub-sections (SettingsDeepRow + SettingsHighlightTarget handoff), row pulse on open; Topic Database scroll restore via rememberSaveable + LaunchedEffect scrollToItem

## Request (2026-08-07, 2nd): Editing toolbar redesign — DONE, pushed as `1756aa1`
- **RichTextEditor.kt tool dock**: surface `surfaceContainerLow` → `surfaceContainer`, radius 14→12dp, border accent 0.40→0.32; header row padding top/bottom 4→3dp (end 8→6dp); expanded Paper/Format sections padding 10/8→8/6dp with stack spacing 6→4dp; gap under dock 5→4dp.
- **Buttons → theme-aware tonal chips**: `ToolToggleButton`, `FormatToolButton`, `CompactPaperChip`, `NotePaperColorToggle` chip now use `surfaceContainerHighest` fill when inactive (was transparent) with `outlineVariant` rim; active = accent fill 0.16→0.18 alpha + rim 0.55→0.65.
- **Color picker**: chip padding 10/6→9/4dp (matches style-chip family), spacing 6→5dp, `labelSmall`→`labelMedium`, swatch unselected border alpha 0.7→0.85.
- Changelog bullet added to `fastlane/metadata/android/en-US/changelogs/20260810.txt`.

## Request (2026-08-07, 3rd): Explore-session polish — DONE, pushed as `7b7f6e5`
1. **Category-based reflection question in notifications** — shared `ExploreSession.reflectionQuestion()` (data layer): albums/artists → "Finished listening? What track or lyric landed hardest?", films/directors → watching, books/authors → reading, artworks/painters → looking, scientists/discoveries → exploring, wildcard → verb fallback. Added to the live timer notification AND the wrap-up reminder via `BigTextStyle`.
2. **Live timer above the progress bar now visibly updates** — `NOTIFICATION_REFRESH_MS` 60s → 15s (the shade chronometer ticks itself; the re-render refreshes the content text + progress). `body` computed once, reused by content text + big text (drift-proof).
3. **Bubble expand/collapse fixed** — `SizeTransform(clip = true)` stops the expanded panel's content from rendering outside the still-pill-sized window mid-animation; fades tuned 240/120 → 220/100.
4. **Stop moved off the pill** — removed Stop from the bubble's expanded panel + `onStop` param from `ExploreBubbleContent`/service; `CurrentlyExploringCard` gains a top-end corner circular Stop button (quiet teardown, same as notification Cancel) with header-row end padding so the title never runs under it.
- Changelog bullets added to `fastlane/metadata/android/en-US/changelogs/20260810.txt`.

## Request (2026-08-07, 4th): Rebalance 50-level XP curve — DONE, pushed as `XXXXXXX`
- `CurioQuests.XP_THRESHOLDS`: first 12 thresholds unchanged (0..940, v7.40 pacing — nobody loses rank); beyond that the per-level step now grows +12/level with a **360 XP cap** (old: +18/level unbounded → ~776 XP/level at the top).
- Result: L50 ≈ 12,140 XP (was 18,458), L40 ≈ 8,540 (was 11,328) — high ranks climb ~34% faster with a flat, non-grindy tail. Verified: 50 unique monotonic thresholds; `levelForXp(940)=12`, `levelForXp(12140)=50`, `levelForXp(20000)=50` (promo still max).
- Ladder chain targets derive from `XP_THRESHOLDS[i]` → auto-follow. `PromoMode.DEMO_XP` (20000) still above the new top; stale 940/18.5k comment cleaned.
- Changelog bullet added to `20260810.txt`.

### Status
- All requests complete. Working tree clean; all commits on `main` and pushed.
