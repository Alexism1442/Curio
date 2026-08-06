# Prompt — Profile + Settings redesign (v7.53)

## Request
Redesign Profile and Settings to match the Home/detail visual language, use compact options, and move main card/deck customization into a new always-visible Experiments page reachable from Settings.

## Decisions
- Profile: Home-style identity hero with compact detail-style cards.
- Settings: compact hub with subpages.
- Experiments: reachable from the Settings hub and always visible.

## Changes
- Added `SettingsHubScreen` as the compact Settings root with Personalize, Explore, and Safety & support groups.
- Added Appearance, Notifications, Recording, Backup & restore, and About subpage routing.
- Added `ExperimentsScreen` and moved main-card, deck-card, Material blend, 3D button, pastel crown, Smart Spin, Smart density, and voice-to-text controls there while preserving existing `AppPreferences` keys and setters.
- Added `BackupToolsScreen` for Curio backup/restore and additive FieldMind archive import, retaining previews, confirmations, status feedback, and last-backup display.
- Preserved notification permission requests and restored overlay special-access handling, including reminder-time chips and lifecycle refresh after returning from Android settings.
- Reduced Profile list/card spacing and tightened lane/stat card internals without removing content or quality.
- Kept `SettingsScreen` as a compatibility alias to the new hub so old callers do not retain a second settings implementation.
- Consolidated backup navigation onto `SETTINGS_DATA` and removed the redundant tools route.

## Validation
Brace checks are BALANCED for all changed/new Kotlin files and `git diff --check` is clean. No local Gradle build/compile/lint/test was run because the repository forbids Android build commands here; CI remains the compilation source of truth.

## v7.54 — compact paper/style/color controls in the editing page

- Paper style options (Ruled, Torn, Rules, Coffee, Folded, Red Margin, Watermark, Rounded top) now stay on one horizontally scrollable strip instead of wrapping into a tall multi-line block.
- Expanded Color swatches use the same horizontal scrolling treatment.
- Reduced the Paper/Format toggle bottom padding from 6dp to 2dp, the expanded Paper-to-Color gap to 1dp, and the formatting toolbar bottom padding to 2dp.
- Tightened the shared PaperLineField stack spacing from 8dp to 3dp so labels, controls, and the paper field read as one compact group.
- Collapse/expand animations and all paper options remain intact; no behavior or visual quality was removed.
- Validation: brace checks BALANCED for RichTextEditor.kt, PaperCard.kt, and CaptureFormatComponents.kt; `git diff --check` clean. No Gradle command run per repository rules.

## v7.55 — restore detail quote glyphs and tighten detail readability

- Restored the real Material Symbols `format_quote` glyph at the opening and closing edges of saved quote cards; quote text remains raw rich text, so spans and the five-line limit stay accurate.
- Tightened the detail metadata stack and reclaimed the lifted seam space before the format body, removing the oversized visual gap beneath Quick Facts without removing content.
- Added a detail-only watermark alpha scale so the background glyphs remain present but sit quietly behind readable text.
- Validation: brace checks BALANCED for EntryDetailScreen.kt and CurioWatermarkBackdrop.kt; `git diff --check` clean. No Gradle command run per repository rules.

## v7.56 — fix Experiments compilation and mood-board quote expansion

- Restored the missing Smart density labels and summaries in ExperimentsScreen so `densityModeSegmentLabel` and `densityModeSummary` resolve during compilation.
- Mood-board editor quote cards now grow to fit their typed content instead of destructively shortening the preview during measurement; dynamic measured height is used for drag bounds.
- Saved/read-only mood-board previews remain compact with ellipsis, while the existing 280-character/five-line editor limits remain unchanged.
- Validation: brace checks BALANCED for ExperimentsScreen.kt and MoodBoardZoom.kt; `git diff --check` clean. No Gradle command run per repository rules.

## v7.57 — make Smart Density labels compile-proof

- Replaced the two fragile `densityModeSegmentLabel` and `densityModeSummary` helper references in ExperimentsScreen with exhaustive inline `when` expressions over SmartDensityMode.
- Preserved the existing Off, Compact, 2x labels and explanatory summaries while ensuring the reported unresolved-reference failure cannot recur from stale helper scope.
- Validation: ExperimentsScreen brace check BALANCED; `git diff --check` clean; no old helper references remain. No Gradle command run per repository rules.

## v7.58 — remove the obsolete legacy module

- Removed the entire frozen legacy Android tree (346 files) after confirming it is not included by Gradle and is not loaded by Curio at runtime.
- Kept Curio's self-contained FieldMind archive importer, copied fonts, active app source, build configuration, and required assets intact.
- Rewrote Curio's font/module documentation so no active source or DOX guidance depends on the deleted legacy tree.
- Filesystem-date audit found no checkout files older than July 6, 2026; no unrelated active files were removed under the date rule.
- Validation: no remaining legacy-tree references, only `:app` is included, and `git diff --check` is clean. No Gradle command run per repository rules.

## v7.59 — remove obsolete repository surfaces

- Removed the old web landing site, wiki, historical docs, standalone worker, root legacy assets, workspace metadata, and unused package/deployment files.
- Kept Curio Android source/resources, topic data and schema, all topic-maintenance scripts, Gradle/wrapper configuration, CI/release metadata, fastlane date-based Curio notes, and DOX instructions.
- Removed legacy numeric store changelogs and deleted stale references to removed design documents.
- Rewrote README and project indexes around Curio; no runtime code or active app files were removed.
- Standalone topic validation passed: 11 files, 2,312 topics, 2,312 unique IDs, zero errors. `git diff --check` passed. No Gradle command run per repository rules. The ignored local release keystore was preserved as a private credential.

## v7.60 — rewrite the root README as Curio-only documentation

- Replaced the root README with a standalone Curio project guide covering the current app, repository layout, requirements, topic data, development workflow, CI/release metadata, and local validation.
- Removed the old archive-import/history wording and any FieldMind, Rhythm, or legacy product references from the README.
- Marked Gradle build and schema tasks as CI-only so the README matches the repository's no-local-Gradle rule; retained `python3 scripts/validate_topics.py` as the local content check.
- Validation: README assertions passed, standalone topic validation passed for 11 files and 2,312 topics with zero errors, and `git diff --check` is clean. No Gradle command run.

## v7.61 — rewrite GitHub templates and workflows for Curio

- Replaced the stale bug form with a Curio-specific Android report covering reproduction, affected area, versions, logs, and sanitized screenshots.
- Replaced the feature form with a discovery/capture/library-focused request form and removed the old assignee and unrelated install options.
- Rewrote the pull-request template around Curio experience, UI/data/persistence impact, validation, visual evidence, permissions, and reviewer checks.
- Replaced branch CI with a focused Curio workflow that runs standalone topic validation, `lintDebug`, Gradle topic validation, and `assembleDebug`, then uploads reports and the debug APK.
- Replaced release automation with a tag-only signed release workflow; it requires all four signing secrets, rejects debug-signed APKs, and publishes only the tagged release APK.
- Updated `.github/AGENTS.md` to document the new triggers, checks, artifacts, templates, and signing contract.
- Removed the unsupported Android platform/build-tools installation that caused CI's `platforms;android-37` package lookup to fail; restored dynamic build-tools discovery for release signature verification.
- Validation: all GitHub YAML files parsed successfully, structure assertions passed, no stale product references or tracked signing artifacts remain, and `git diff --check` is clean. No Gradle command run.

## v7.62 — build the release variant on pull requests

- PR/branch CI now runs `assembleDebug` and `assembleRelease` alongside lint and topic validation.
- CI uploads both debug and release-variant APKs in one artifact for PR testing.
- PR CI does not receive release signing secrets; the release variant uses the existing debug-signing fallback and is not treated as an official production release.
- Tag-based release publishing remains unchanged and still requires the official signing secrets.
- Updated `.github/AGENTS.md` and the PR template to describe both build variants.
- Validation: GitHub YAML structure and workflow assertions passed; no Gradle command run.

## v7.63 — upgrade GitHub Actions to Node 24 and re-target CI to main

- Upgraded `gradle/actions/setup-gradle` from v4 to v6 (Node 24 runtime) in both workflows, clearing the Node.js 20 deprecation annotation for that action.
- Upgraded `softprops/action-gh-release` from v2 to v3 (Node 24 runtime) in the release workflow, clearing its Node.js 20 deprecation annotation; the `prerelease`, `generate_release_notes`, `files`, and `fail_on_unmatched_files` inputs are unchanged in v3.
- Re-targeted the android.yml `push` and `pull_request` triggers from the removed `revamp` branch to `main`, the repository's active branch, so CI runs on every push to main.
- Updated `.github/AGENTS.md` to describe the `main` trigger target.
- Validation: both workflow YAML files parsed successfully, action versions resolve, and `git diff --check` is clean. No Gradle command run per repository rules.

## v7.64 — rebrand project to Curio (config and branding only)

- Changed `rootProject.name` in `settings.gradle.kts` from "FieldMind" to "Curio" (the old app name).
- Rebranded the root `AGENTS.md` title and purpose line from FieldMind to Curio.
- Updated stale FieldMind headers/comments in `app/proguard-rules.pro`, `scripts/generate_sounds.mjs` (header + console title), and `scripts/generate_species_catalog.py` (header + iNaturalist User-Agent), plus the team-expertise row in `app/CURIO_DATA_PLAN.md`.
- Per user decision, the FieldMind legacy import feature (FieldMindLegacyImport, FieldMindObservationScreen, FieldMindMetadata/Species, Legacy Cabinet chip/section, restore UI) and all its code references remain fully intact; only config, branding, and stale comments were touched.
- Historical release notes (fastlane changelogs) and the Prompt.md request log retain their original FieldMind references as records.
- Validation: remaining FieldMind references are confined to feature code, feature documentation, and historical records; `git diff --check` clean. No Gradle command run per repository rules.

## v7.65 — sign CI release APKs with the production keystore (best-effort)

- The Android CI workflow (push to `main`, PRs, manual dispatch) now signs its `assembleRelease` output with the same `KEYSTORE_*` secrets as the release workflow instead of the debug-signing fallback.
- Added a best-effort keystore decode step: when `KEYSTORE_BASE64` is present it decodes `release.keystore` and exports the four signing env vars to the Gradle build; when absent (fork PRs, where GitHub strips secrets) it warns and the build falls back to debug signing per the existing `hasReleaseSigningMaterial` guard in `app/build.gradle.kts`.
- Added a signature-verification step that runs only when a keystore was actually decoded; it fails if no signed release APK is produced or if the release APK is signed with the Android debug key.
- Updated `.github/AGENTS.md` to describe the best-effort signing contract.
- Validation: workflow YAML parsed successfully and `git diff --check` is clean. No Gradle command run per repository rules.

## v7.66 — Profile hero joins the Home torn-banner family

- Replaced Profile's category-gradient hero card with the Home quest family's TORN rose banner (ProfileScreen.kt only): solid rose-wood fill resolved exactly like Home's (`profileRoseAccent`/`profileReadableInk` private replicas), the same bold `SoftTornBottomShape`/`SoftTornSheetShape` tear (seed `0xC0FEE`, `bold = true`), a hairline torn-edge shadow, and a theme-matched under-sheet (`MaterialTheme.colorScheme.background`) instead of Home's hardcoded creamy white — the tear now sits on the page color in every theme.
- Added the mirrored watermark collage INSIDE the banner — `CurioIcons.heroWatermarkSymbols` for your most-explored lane's family (wildcard before the first save) — the "pop-up icons" treatment from Home's quest hero.
- Moved the Streak · Saved · Lanes stats INTO the hero: the standalone `StatsStrip` below is gone, replaced by a stat bar pinned just above the tear on the soft rose gradient pane with icon/value/label segments and `VerticalDivider` hairlines (the exact Home stat bar, icons in the hero ink).
- Back + Settings now ride as glass pills over the banner (Home's top-bar treatment); the old top title bar was removed in favor of the "YOUR PROFILE" kicker inside the banner.
- Added the shared `CurioWatermarkBackdrop` behind the page with `topClearance` (lower-band mode) so glyphs stay below the hero; content cards are wrapped in 16dp padding so the banner bleeds edge-to-edge.
- Fixed-height hero (372dp) holds flex slack for large font scales; tagline capped at one line. Level, Lanes, Settings, and Support cards unchanged.
- Validation: ProfileScreen.kt brace check BALANCED and `git diff --check` clean. No Gradle command run per repository rules (CI compiles on push).

## v7.67 — v1.0 launch document

- Added `docs/v1.0-launch.md` — a complete, launch-facing product document for Curio v1.0: app basics (name, pitch, problem solved), why-now highlights, 3-5 marquee features (Spin deck, six capture formats + paper editor, mood-board quote boxes, explore sessions with floating bubble, Cabinet), platform & requirements (Android 8.0+/API 26, English, permissions), how to get it (GitHub Releases APK — not on Play at v1.0), honest limitations/roadmap (Android-only, no cloud sync/accounts, English-only, content growth open for topic suggestions), feedback & support (GitHub Issues + in-app bug report), an exhaustive category-organized feature list (discovery, exploring, capturing, mood boards, Cabinet, Profile, Settings, design, privacy, reliability), and credits (Firefly).
- Facts sourced from the codebase: 2,312 topics across 11 lanes, six CaptureFormat values, minSdk 26 / targetSdk 37 / version 1.0.0, Manifest permissions, Settings hub/Experiments surface, backup + FieldMind import, and the release workflow. Per user answers: distribution = GitHub Releases APK; support = GitHub Issues + in-app report; credits = "just Firefly"; file = `docs/v1.0-launch.md`; roadmap = Android-only, no cloud/accounts, content growth with open topic suggestions, plus explicit callouts of the Material+custom style, Spin deck, mood-board quotes, and explore sessions.
- Validation: `git diff --check` clean; markdown content reviewed. No Gradle command run per repository rules.

## v7.68 — cap mood-board quote cards at two lines

- Fixed a bug where a long mood-board quote stretched its paper slip to the full board height: the editor preview rendered the quote with `maxLines = Int.MAX_VALUE` in `MoodBoardFloatingCard` (MoodBoardZoom.kt), so the card grew with content and could cover the entire board.
- Quote cards now show up to TWO lines with ellipsis on the board — editor and saved/read-only views alike (the full text stays editable in the edit sheet, where the RichTextEditor still enforces the real 280-char / five-line input limit). The editor's `heightIn(min = slot)` now only ever exceeds the slot by one extra line, so drag bounds stay sane.
- All four render paths (editor via GalleryWallFormat, saved entry detail ×2, PNG export) go through the single fixed component; the RichTextEditor's typing field was verified to be the edit surface, not the board preview, so it was left untouched.
- Validation: MoodBoardZoom.kt brace check BALANCED and `git diff --check` clean. No Gradle command run per repository rules.

## v7.69 — tear family: torn cards + full watermark on Profile and Settings

- Added a shared `CurioTornCard` component (PaperCard.kt): a small cream paper slip with rounded top corners, a soft torn bottom seam, hairline edge, no rules, and a required STABLE seed per card (so tears never re-roll across opens or LazyColumn recycling).
- Profile (ProfileScreen.kt): the watermark backdrop now renders the FULL-PAGE collage like Home (removed the `topClearance` lower-band mode, which left the glyphs hidden behind the hero and cards — the reported "background didn't get the watermark"); the four content cards (Level, Settings nav, Lanes, Support) are now torn paper cards instead of the generic settings card.
- Settings expanded to the same family: SettingsHubScreen (rewritten), SettingsSectionScreen, ExperimentsScreen, and BackupToolsScreen each sit on the wildcard-led `CurioWatermarkBackdrop`, and every section card is a `CurioTornCard` with a distinct fixed seed.
- The shared `SettingsHeader` is now a SMALL TORN CARD (fixed seed 0x5EED) — back button, title, and subtitle on a cream torn slip — so all four settings screens automatically wear the torn-card header.
- Validation: brace checks BALANCED for all six touched files, `git diff --check` clean, no leftover CurioSettingsCard references in the touched screens. No Gradle command run per repository rules.

## v7.70 — 30 handcrafted film topics (modern → old, canon + crowd-pleasers + niche)

- Added `scripts/batch_films_add_30.py` and appended 30 NEW handcrafted entries to `assets/topics/films.json` (130 → 160 topics). The user asked for handcrafted descriptions that make you WANT to watch, good facts, more titles, in a 30-batch for consistent quality, from modern to old, some niche, wide variety.
- Coverage (1927 → 2022): classics (Metropolis, Modern Times, Double Indemnity, Sunset Boulevard, 12 Angry Men, Some Like It Hot, The Graduate), 70s/80s pillars (One Flew Over the Cuckoo's Nest, Alien, The Shining, Raiders of the Lost Ark, E.T., Die Hard) incl. niche (Come and See), 90s icons (The Silence of the Lambs, The Shawshank Redemption, Heat, Fight Club) incl. niche (La Haine), 2000s (Memento, Amores Perros, The Lives of Others), 2010s (Interstellar, La La Land, The Handmaiden, Coco, Lady Bird), 2020s (Minari, Aftersun, The Banshees of Inisherin).
- Every entry: hooky teaser + real verifiable fact (e.g. Hopkins' 16-minute Oscar win, Ford's dysentery ad-lib, Thorne's Gargantua physics paper, the real HGW XX/7 Stasi file, Khatyn for Come and See), a watch-guide instruction passing the quality bar (specific artifact, time-bounded — partial-watch targets for epics), genre+decade+region tags (new regions: Soviet, Mexican, Korean, Irish), tier 1, `film-{slug}-{year}` IDs, `_trim` guard at 450.
- Reviewer pass caught two factual slips, both fixed in the script AND the JSON: La La Land "tied the record for most Oscars won in a single night" (wrong — it won six and tied the 14-NOMINATION record) and a muddled Metropolis robot-Maria ending line.
- Validation: `scripts/validate_topics.py` passes — 11 files, 2,342 topics, 2,342 unique IDs, zero errors; appends are guarded against duplicate IDs/names. No Gradle command run per repository rules.

## v7.71 — expand films to 400 topics (1920s → 2010s, 240 new entries)

- Continued the handcrafted film pass from 160 → 400 topics via 8 new batch scripts (`scripts/batch_films_add_2.py` … `batch_films_add_9.py`, 30 entries each), same format as the first batch: hooky teaser that makes you WANT to watch + real verifiable fact + watch-guide instruction (specific scene, time-bounded, quality bar), `film-{slug}-{year}` IDs, genre+decade+region tags, tier 1, 450-char caps, duplicate-id/name guards.
- Decade spread after the pass: 1920s (7) · 1930s (14) · 1940s (21) · 1950s (44) · 1960s (46) · 1970s (49) · 1980s (60) · 1990s (65) · 2000s (49) · 2010s (27) · 2020s (18) — the pool was previously 2000s/2010s-heavy, now balanced across cinema history with a wide regional mix (German, French, Italian, Japanese, Swedish, Soviet, Czech, Mexican, Korean, Irish, etc.) and niche picks (Plan 9, Come and See, La Haine, Shoah, Grave of the Fireflies, Delicatessen, Run Lola Run, The Handmaiden-adjacent etc.).
- Reviewer pass over all 8 scripts caught six factual slips, all fixed in BOTH `films.json` and the reusable scripts: Nashville did NOT win the Palme d'Or (1975 went to Chronicle of the Years of Braise); Das Boot's 209 minutes is the 1997 director's cut (1981 original 149) and the set was full-scale (~67 meters, not 67 feet); Jurassic Park's 1993 run was ~$914M not $1B (Titanic was first to a billion); Birdman (2014) predates both Deadpool and Endgame; The Thin Red Line gap is 20 years (1978→1998), not 17; The Battle of Algiers is canonically 1966, not 1965 (id updated to `film-the-battle-of-algiers-1966`).
- Validation: `scripts/validate_topics.py` passes — 11 files, 2,582 topics, 2,582 unique IDs, zero errors. No Gradle command run per repository rules.

## v7.72 — rebalance films with 60 modern entries (2010s + 2020s, 400 → 460)

- The user flagged that the 400-film pool leaned old (only ~45 from 2010+); per their answers (~60 more, 2010s + 2020s balanced), added two new batch scripts: `scripts/batch_films_add_10.py` (30 handcrafted 2010s films) and `scripts/batch_films_add_11.py` (30 handcrafted 2020s films), bringing `films.json` to 460 topics and the 2010+ share from 45 → 105.
- 2010s batch: Black Swan, Toy Story 3, Drive, The Artist, The Avengers, Django Unchained, Skyfall, Zero Dark Thirty, 12 Years a Slave, The Wolf of Wall Street, Frozen, Prisoners, Gone Girl, Edge of Tomorrow, Nightcrawler, Ex Machina, The Revenant, Spotlight, Room, Sicario, The Big Short, Manchester by the Sea, Blade Runner 2049, Dunkirk, The Shape of Water, Spider-Man: Into the Spider-Verse, Shoplifters, Once Upon a Time in Hollywood, Knives Out, Uncut Gems.
- 2020s batch: Promising Young Woman, Sound of Metal, Nomadland, The Father, Judas and the Black Messiah, CODA, West Side Story, The Worst Person in the World, Licorice Pizza, The Batman, Top Gun: Maverick, RRR, Triangle of Sadness, The Whale, Decision to Leave, The Menu, All Quiet on the Western Front, Marcel the Shell with Shoes On, John Wick: Chapter 4, Spider-Man: Across the Spider-Verse, The Boy and the Heron, Godzilla Minus One, May December, Air, Dune: Part Two, Challengers, Anora, The Brutalist, Conclave, The Substance.
- Same quality bar as prior batches: hooky teaser + real verifiable fact + watch-guide instruction (specific scene, what to notice), `film-{slug}-{year}` IDs, correct bylines/runtimes, genre+decade+region tags (incl. Norwegian, German, Korean, Indian, Japanese), tier 1, 450-char caps, duplicate-id/name guards.
- Reviewer pass caught four slips, all fixed in BOTH `films.json` and the scripts via `scripts/fix_films_batch10_11_facts.py`: Marcel is voiced by Jenny Slate, not director Dean Fleischer Camp; Zero Dark Thirty's Abbottabad raid is ~20 minutes, not 40; Nightcrawler's Gyllenhaal dropped ~30 lbs, not 20; Godzilla Minus One is ~69 years after the original (1954→2023), softened to "nearly 70 years".
- Validation: `scripts/validate_topics.py` passes — 11 files, 2,642 topics, 2,642 unique IDs, zero errors. No Gradle command run per repository rules.

## v7.73 — settings hero header + reverted cards + profile pill animations

- User reported the settings page "isn't showing anything," asked for a PROFILE-STYLE hero on settings (just at the header), Home-style pop + color-morph on Profile's back/settings icons, and to REVERT the torn-card look on the buttons/cards ("it doesn't look good").
- **Settings hero header:** rewrote SettingsHubScreen.kt around a new shared `SettingsHeroHeader` — a compact Profile-style torn rose banner (same `SoftTornBottomShape`/`SoftTornSheetShape` bold tear, seed `0x5EED`, theme-matched under-sheet, mirrored wildcard watermark collage, back pill + a quiet non-interactive gear glyph, title/subtitle pinned above the tear, 180dp with flex slack for large fonts). All four settings screens (hub, sections, experiments, backup) now share it — the old torn-card `SettingsHeader` is gone.
- **Reverted torn cards:** every `CurioTornCard` content card across Profile (Level/Lanes/Settings nav/Support) and all settings screens reverted to the clean `CurioSettingsCard` (rounded surfaceContainerLow); the now-unused `CurioTornCard` component was removed from PaperCard.kt (0 references remain).
- **Blank-page hardening:** every settings root Box now has an explicit `.background(MaterialTheme.colorScheme.background)` (Profile always had one — the known-good screen); this guarantees the pages paint a real background instead of relying on the window behind the nav host.
- **Profile pills pop + color morph (Home's exact mechanism):** Back + Settings moved out of `ProfileHero` into a pinned scroll-reactive sticky bar in ProfileScreen — `derivedStateOf` over the LazyListState (90dp threshold), `FastOutSlowInEasing` progress, scale `lerp(0.97→1.0)` pop, lift + shadow that grow with scroll, and three `animateColorAsState` values morphing the hero-ink glass pills into frosted floating pills. The hairline rim only appears once scrolling starts, so the resting look is unchanged; the hero keeps a spacer where the pills were.
- Reviewer pass caught three refinements, all applied: banner height 164→180dp (large-font safety), rest-state pills stay borderless (rim fades in with scroll), and the decorative gear is a plain low-alpha glyph instead of a button-looking Surface.
- Validation: brace checks BALANCED on all six touched files, `git diff --check` clean, zero `CurioTornCard`/`SettingsHeader` references, no literal-escape artifacts. No Gradle command run per repository rules.

## v7.74 — quests, levels & achievements with its own page

- User asked for proper levels + quests + achievements, a bigger guided quest to navigate the app, and its own page. Per their answers: always-on (no toggle), everything included (guided beginner journey, daily quests, achievements, XP-based levels), and the Profile level card upgraded to the shared XP system.
- **New data layer** `app/src/main/java/com/curio/app/data/CurioQuests.kt` — prefs-backed (`curio_quests`, added to backup), reactive Compose state seeded from MainActivity: 12 XP-based levels (thresholds 0/15/40/80/135/205/290/390/505/635/780/940; First Spark → Grand Curator; `levelForXp`/`xpProgress`/`maxLevel`), a 10-step guided Journey that walks the app (spin → explore → save → settings → profile → pin → quote → daily → five saves → achievement; XP paid once per quest, `currentJourneyQuest` = first incomplete), 3 rotating daily quests (pool of 8, seeded by calendar day so they reset at midnight; auto-award XP on completion), and 18 one-time Achievements (spins/explores/all-lanes/saves/all-formats/quotes/pins/streaks/likes/journey/level milestones; each badge pays its own XP exactly once).
- **Event hooks wired where real actions happen:** SpinScreen spin landed (`onSpin` +2), ExploreSessionStore.recordExplored (`onExplore` +5), SaveCaptureScreen first-time save only — edit re-saves never re-count (`onSave` +10, format feeds Every Format), AppPreferences pinTopic/saveQuote/setTopicSentiment (`onTopicPinned` +3 / `onQuoteSaved` +3 / `onTopicLiked` +2 / `onTopicDisliked` +1), StreakTracker.recordActivity (`onStreakRecorded` → streak badges), ProfileScreen open (`onProfileVisited`), SettingsHubScreen open (`onSettingsVisited`).
- **Own page** `app/src/main/java/com/curio/app/features/quests/QuestsScreen.kt` — the settings-family hero (shared `SettingsHeroHeader` torn rose banner) on a watermark backdrop, then: the XP rank card (big level badge + progress bar), Your journey (current quest highlighted with a Start button that jumps to Spin/Settings/Profile, full 10-step checklist, journey-complete banner), Today's quests (3 daily quests with mini progress bars and XP chips), and the Achievements shelf (two-column grid of badge tiles with per-badge progress). Registered as `CurioRoutes.QUESTS` in the NavHost.
- **Surfaces:** Home gains a compact Quest summary card (level + next quest + XP bar, one tap to the Quests page) right below the quest block, plus a "Quests & Levels" drawer item; Profile's LevelCard is now XP-based (old saved-count `levelFor`/`progressTowardsNextLevel`/`levelTitle` helpers removed) with a new "Quests & achievements" entry card showing the next quest; new glyph constants added to CurioIcons (emoji_events, flag, workspace_premium, task_alt).
- Reviewer pass caught one critical bug — achievement XP was never actually credited in `checkAll` (badges unlocked but their `xpReward` was dead data) — fixed by paying each badge's reward on unlock; also applied: dead icon constants removed, `maxLevel` helper used instead of `levelForXp(Int.MAX_VALUE)`, and edit-mode saves gated out of the save economy.
- Validation: brace checks BALANCED on all 15 touched files, `git diff --check` clean, no leftover references to removed helpers, no literal-escape artifacts. No Gradle command run per repository rules.

## v7.75 — flat content on Profile and Settings (no card shells) + hero to the status bar

- User asked to "remove the card of each button" and place the buttons directly on the background, applied to Settings and Profile only. Per their answers: ALL settings screens (hub + subpages + experiments + backup tools) plus everything below the hero on Profile go flat, and the settings hero headers extend up BEHIND the status bar like Profile/Home.
- **Profile** (ProfileScreen.kt): all five content blocks below the hero — LevelCard, QuestsNavCard, SettingsNavCard, LanesCard, SupportCard — dropped their `CurioSettingsCard` shell (the surfaceContainerLow fill, border, and card padding) and now render their inner content directly on the watermark backdrop: transparent clickable rows, icon-chip headers, inset dividers, and the lane chip pills all keep their own styling. `CurioSettingsCard` import removed; doc comment updated.
- **Settings family** (SettingsHubScreen, SettingsSectionScreen, ExperimentsScreen, BackupToolsScreen): every `CurioSettingsCard` group (hub sections, Appearance/Notifications/Recording/Data/About sections, experiment groups, backup/import groups) became a plain `Column` so rows sit flat on the background; section labels and `CurioCardHeader` chips keep the grouping.
- **Hero to the status bar:** each settings screen's root `Column` lost its outer `statusBarsPadding()`, so the torn rose banner now starts at the very top edge and runs behind the status bar (the shared `SettingsHeroHeader` still applies its own internal inset so the back pill clears it) — the exact Profile/Home construction. The now-unused `statusBarsPadding` imports were removed from the three subpage screens; SettingsHubScreen keeps its import because the header lives there.
- **QuestsScreen deliberately untouched** (user scoped to Profile + Settings only) — it still uses card shells and the pre-status-bar hero; a reviewer note flags it as intentionally inconsistent with the settings family for now.
- Validation: brace checks BALANCED on all five touched files, `git diff --check` clean, zero `CurioSettingsCard` references left in the touched screens, unused imports removed. Reviewer pass found no blockers (ColumnScope maps 1:1 from the card's inner Column; tap targets and ripples work on the transparent rows; divider insets still read on the flat background). No Gradle command run per repository rules.

## v7.76 — quieter watermark glyphs behind flat content (Detail + Profile + Settings)

- User: "make the detail page below hero background glyph and the settings and profile glyph a less visible so the texts are readable" — after flattening, the flat rows on Profile/Settings sit directly on the watermark collage, and the detail page's glyphs still competed with the text.
- The shared `CurioWatermarkBackdrop` already supported an `alphaScale` (detail had 0.68); every relevant screen now passes `alphaScale = 0.45f`: EntryDetailScreen (0.68 → 0.45, below-hero band), ProfileScreen (added), and all four settings screens — SettingsHubScreen, SettingsSectionScreen, ExperimentsScreen, BackupToolsScreen (added). At 0.45 the base alphas roughly halve (light inactive ~0.15 → ~0.07, active ~0.30 → ~0.14), so the palette stays as a faint whisper behind the flat rows, headers, chips, and saved-entry text.
- Home, Spin, Cabinet, Recent, Topic Reveal, and Quests keep their current (card-covered) backdrops untouched per the request's scope. The component's `alphaScale` doc comment now documents the shared usage.
- Validation: brace checks BALANCED on all seven touched files, `git diff --check` clean. No Gradle command run per repository rules.

## v7.77 — Cabinet gets the torn-rose hero banner; Profile pills go opaque hero color

- User asked to extend the hero-card style to the Cabinet screen and make Profile's pop-up-style icons opaque; per their answers: Cabinet gets the FULL torn-rose hero banner, and Profile's Back/Settings pills + the avatar circle keep the hero card's color (solid at rest, morphing to frosted on scroll).
- **Cabinet** (CabinetScreen.kt): the plain top bar was replaced with a full torn-rose hero banner (`CabinetHeroHeader`) — the shared rose family via `settingsRoseAccent()`/`settingsReadableInk()` (made public in SettingsHubScreen), its own fixed `CABINET_TEAR_SEED` bold SoftTorn tear + theme under-sheet (sheet color follows the active filter's category wash), mirrored wildcard watermark collage, and the back pill (when a filter/legacy view is active) + action pills riding the top row through a `trailing: @Composable (ink: Color) -> Unit` slot: Select/Sort/Search in browse mode, Select-all/Delete/Cancel in selection mode. Title + subtitle pin just above the tear. Root Box lost its `statusBarsPadding` (banner runs behind the status bar), the search bar + filter chip row moved below the hero, and the watermark backdrop dropped to `alphaScale = 0.45f` to match the quieted family. A one-off `scripts/fix_cabinet_hero.py` handled the mechanical top-bar replacement; imports (BiasAlignment, BoxScope, Dp, CategoryFamily, offset/size/clip/graphicsLayer, SoftTorn shapes, settings helpers) were completed by hand.
- **Profile** (ProfileScreen.kt): the scroll-reactive Back + Settings pills now rest in the SOLID hero-card color (restPillBg = heroFill, rim = lerp(heroFill, heroInk, 0.42f) — Home's TopBarPill construction) and the hairline rim now rides the pills the whole way instead of appearing only after scroll; on scroll they still morph into the solid frosted pills with the 0.97→1.0 pop. The avatar circle dropped its translucent ink wash for a solid hero fill with a hairline ink ring (alpha 0.30) so it reads as part of the banner. `androidx.compose.foundation.border` import added.
- Reviewer pass: no blockers — confirmed the trailing-composable slot pattern is sound, the avatar modifier order (clip → background → border) is correct, and cross-package reuse of the settings helpers is safe (state read inside composition). Verified no orphaned references to the old cabinet top bar and no private dupes of the settings helpers.
- Validation: brace checks BALANCED on all three touched files, `git diff --check` clean, orphan-grep clean. No Gradle command run per repository rules.

## v7.78 — no fake gear on settings heroes; content scrolls UNDER the ragged tear

- User asked to remove the "fake settings icon" from the hero card on the settings sub-pages, and to make the settings/menu texts below the hero disappear below the tear in a real way when scrolling ("not just behind a background which looks bad" — clarified: they should go UNDER the ragged tear, not clip at a straight line).
- **Fake icon removed:** the decorative non-interactive `CurioIcon(Settings)` glyph that floated opposite the back pill inside the shared `SettingsHeroHeader` is gone — one edit in the shared header removes it from every settings screen (hub, all sub-pages, Experiments, Backup tools) and Quests at once. The top row now holds just the back pill.
- **Content scrolls under the tear:** every settings-family screen was restructured from `Column { hero; LazyColumn }` (which clipped content at a straight line below the hero) to a Box overlay: the `LazyColumn` (in `ScreenEntrance` where it existed) now fills the screen first, and `SettingsHeroHeader` is drawn AFTER it (on top). Content padding top became `SettingsHeroTotalHeight + 8/10.dp`, so the first row sits just below the hero at rest, and as the user scrolls up the rows slide behind the OPAQUE torn banner + under-sheet and vanish exactly at the ragged tear seam — no straight-line cutoff, matching Home's sticky-bar feel (the hero Box has no pointer input besides the back pill, so scroll gestures pass through to the list). Applied to SettingsHubScreen, SettingsSectionScreen, ExperimentsScreen, BackupToolsScreen, and QuestsScreen (same shared header — keeping it carded would have left the same bad clip). `SettingsHeroTotalHeight` made public for the sibling screens; Quests also dropped its outer `statusBarsPadding` (hero now tears from the very top edge like the settings family) and the unused import.
- Reviewer pass: no blockers — confirmed the opaque banner+under-sheet hide content exactly at the pixel-aligned tear (no leak through the up-bites or the 1dp shadow lip), gesture pass-through is the desired sticky-header behavior, and the single-child SpaceBetween back-pill row is fine. Quests scope noted as a family-consistency call.
- Validation: brace checks BALANCED on all five touched files (one initial imbalance in the hub fixed), `git diff --check` clean, no leftover decorative-icon references, no unused imports. No Gradle command run per repository rules.

## v7.81 — Home quest badge removed; reveal screen "Already …" done button; done topics never re-deal

- User asked to remove the quest level badge from the Home screen, and to replace the reveal screen's "Shuffle again instead" with a button that marks a topic as already watched/listened/read/explored (per category). Per their clarification: tapping it marks the topic DONE and asks if they want to write about it; if not, keep it marked done (never record unexplored) and never show that topic in the shuffle again. Also: any explored topic should be marked done and excluded from the shuffle deck.
- **Home badge removed** (HomeScreen.kt): the `QuestSummaryCard` (level + next-quest + XP bar card below the quest block) is gone — call site and the whole composable deleted, and the now-unused `CurioQuests` and `LinearProgressIndicator` imports removed. The Quests page itself stays reachable via the drawer and Profile's entry card.
- **Done-topics data layer** (ExploreSession.kt): a new persistent `KEY_DONE` pref (JSON array of {categoryId, topicName}) drives a reactive `doneTopicsState` (Set of "CATEGORY::topicName" keys), seeded in `seed()`. `recordExplored()` now also adds the topic to the done set (exploring = done); `removeExplored()` rolls the done mark back (conflict-dismissal restores a topic to the deck). Public `markDone()` (delegates to recordExplored — marks done, shows in Home recents, feeds quests) and `isDone()`.
- **Reveal screen** (TopicRevealScreen.kt): "Shuffle again instead" replaced with a full-width bordered pill labeled by category — `alreadyDoneLabel(cat)`: FILMS/DIRECTORS → "Already watched", ALBUMS/ARTISTS → "Already listened", BOOKS/AUTHORS → "Already read", ARTWORKS → "Already seen", PAINTERS/others → "Already explored". Tapping it sets `engaged=true` (so back never records unexplored), calls `ExploreSessionStore.markDone`, then shows a dialog — "Write about it" jumps to capture; "Not now"/dismiss pops back to the deck with the topic still marked done.
- **Spin deck** (SpinScreen.kt): the shuffle pick now excludes done topics (`doneIds` merged into `exploredIds` for `pickFrom`, so they can't land while alternatives remain — the existing "never run dry" fallback still holds), AND the fan/peek hand is built from `deckPool` (filtered pool minus done topics, falling back to the full pool when everything is done) so done topics don't even show as peek cards.
- Reviewer pass: three refinements applied — peek cards now filtered via `deckPool`, PAINTERS reads "Already explored" (person category) instead of "Already seen", and the dialog's dismiss/"Not now" returns to the deck (it replaced the shuffle-again button). No recursion (markDone→recordExplored→addDone terminates), the `::` done-key separator is unambiguous (split at first occurrence; readDone rebuilds from JSON fields), and reading `doneTopicsState` inside the onClick lambda is fine (click-time read, not recomposition).
- Validation: brace checks BALANCED on all four touched files, `git diff --check` clean, no leftover CurioQuests/LinearProgressIndicator in Home, TextButton still used (9×) in reveal, CurioIcons.Refresh removal safe. No Gradle command run per repository rules.

## v7.82 — notification taps open the app at their promised action

- User: "when i tap done exploring from notifications open the app with its action and in reminder when it says do that when user taps like open it in shuffle page like that" — (1) the "Done exploring" action must actually open the app with its action, (2) tapping a reminder should open the app at the shuffle/spin page (or the action the reminder promises).
- **Root-cause fix** (ExploreReminderReceiver.kt): the ACTION_STOP/ACTION_CANCEL handler cleared the session (`ExploreSessionStore.clearSession`) BEFORE reading it back with `getActiveSession()`, so the "Done exploring" → write-it-down navigation was dead code and the tap silently did nothing. The session is now captured BEFORE the teardown; ACTION_STOP navigates to the write-it-down entry page with that session's category slug + topic name (extras unchanged), ACTION_CANCEL stays quiet.
- **Explore-nudge body tap** (ExploreReminderReceiver.kt): the "Done exploring X? … come back and write it down" notification's content tap now carries `PendingEntryOpen.EXTRA_CATEGORY_SLUG`/`EXTRA_TOPIC_NAME`, so tapping the body opens the write-it-down page for that topic instead of plain Home (same handoff the action uses; request code 4212 + FLAG_UPDATE_CURRENT refreshes the topic extras per session).
- **Daily reminder → Spin deck** (DailyReminderReceiver.kt + CurioRoutes.kt + MainActivity.kt + CurioNavHost.kt): new `PendingSpinOpen` object mirroring `PendingEntryOpen` (boolean `EXTRA_OPEN_SPIN` extra, `capture`/`trigger`/`take` with a Compose-observable counter). The daily reminder's content tap puts the extra; MainActivity captures it on cold start (gated on `savedInstanceState == null`) and warm start (onNewIntent); the NavHost's handoff `LaunchedEffect` (now keyed on both triggers) consumes the spin request first and lands on the Spin tab via `navigateToTab(SPIN)` (popUpTo-HOME save-state), otherwise falls through to the entry-page navigation. Boot gates (splash/onboarding/crash) still defer consumption until a stable root.
- Reviewer pass: no blockers — ordering fix correct, PendingIntent extras update reliably under FLAG_UPDATE_CURRENT + FLAG_IMMUTABLE (identity ignores extras; same slot re-posted per session), cold/warm-start navigation paths sound, no double-fire risk, no missing imports. One noted (non-blocking) quirk: tapping the nudge body leaves the session active, so the pre-existing "are you done exploring?" resume dialog can appear above the write-it-down page — dismissible and consistent with the nudge's conditional wording, left as-is.
- Validation: brace checks BALANCED on all five touched files, `git diff --check` clean, PendingSpinOpen wired through all four call sites, no orphaned references. No Gradle command run per repository rules.

## v7.83 — in-app bug reports open a pre-filled GitHub issue

- User: "make it possible to report bugs from the app". A bug-report form already existed (BugReportScreen.kt: title/description, include-crash-logs toggle, device info) but its button only copied to clipboard + opened a generic ACTION_SEND share chooser (user had to choose a destination). Per user answers: destination = **GitHub Issues** (browser, pre-filled); entry points = keep the existing Profile entry + add a button on the crash screen (NOT the settings hub).
- **BugReportScreen.kt**: `shareReport()` replaced with `openGitHubReport()` — same body (description, device, Android version/SDK) now also includes the app version via `com.curio.app.BuildConfig.VERSION_NAME`, plus optional crash logs (from CurioCrashReporter.getCrashHistory, capped 3×2000 chars). Clipboard copy kept as a safety net, then opens `https://github.com/firefly-sylestia/Curio/issues/new?title=…&body=…` (title truncated to GitHub's 256-char cap; `Uri.Builder.appendQueryParameter` URL-encodes the multiline markdown body) via `Intent(ACTION_VIEW)` with a `resolveActivity` null-guard. Button renamed "Share report" → "Report on GitHub" with a helper caption; the old ACTION_SEND/createChooser code and unused imports were removed.
- **CurioCrashScreen.kt**: a full-width OutlinedButton "Report a bug" below the View log/Share row navigates to the bug-report form (`CurioRoutes.BUG_REPORT`, launchSingleTop) — users can file a GitHub issue with the saved crash logs right after a crash via the form's include-logs toggle.
- Docs updated to match: README (Contributing + Support & Feedback) and docs/v1.0-launch.md (Feedback & Support) now say the in-app report opens a pre-filled GitHub issue, and the crash-recovery screen links to it too.
- Reviewer pass: no blockers — `appendQueryParameter` correctly encodes newlines/`#`/backticks in the markdown body, BuildConfig package/import correct (`buildConfig = true`, same pattern as SettingsSectionScreen), no leftover ACTION_SEND references, CRASH → BUG_REPORT push navigation is a plain back-stack push (Back returns to the crash screen), LocalContext is the Activity so no NEW_TASK needed. One runtime-only note: with the repo's `bug-report.yml` form template, `issues/new` auto-redirects to the form and GitHub's prefill carries title/body into the form fields — worth a one-time manual check after a build.
- Validation: brace checks BALANCED on both Kotlin files, `git diff --check` clean, no orphaned ACTION_SEND/createChooser/shareReport references. No Gradle command run per repository rules.

## v7.84 — in-app update checker (About + Profile) with accurate build version

- User: "add update checker inside about apps add that in profile with version number accurately from the build tag number". Verified ground truth: release tags are `v*` (release.yml trigger) and the only tag on GitHub is `v1.0.0` == `BuildConfig.VERSION_NAME`; no GitHub *release* has been published yet (API `releases/latest` 404s); the bundled Material Symbols font is a SUBSET — `system_update`/`new_releases` missing, `download` verified present via fontTools.
- **NEW `app/src/main/java/com/curio/app/data/UpdateChecker.kt`** — `UpdateInfo(tagName, htmlUrl)` + `object UpdateChecker`: `suspend fun fetchLatestRelease(): UpdateInfo?` (withContext(Dispatchers.IO), plain `HttpURLConnection` GET against `https://api.github.com/repos/firefly-sylestia/Curio/releases/latest`, 8s timeouts, `Accept: application/vnd.github+json`; returns null on ANY non-200 incl. 404/offline/parse — no new dependencies) and `fun isNewer(latestTag, currentVersion)`: strips leading "v", component-wise compare with string-inequality fallback for unparseable tags. try/catch rethrows CancellationException so a cancelled check isn't swallowed into a misleading failed state.
- **NEW `app/src/main/java/com/curio/app/ui/components/CurioUpdateCheckRow.kt`** — shared row (existing `CurioSettingsRow`): Idle subtitle shows the version straight from the build ("Version 1.0.0 · build 20260804"), tap → Checking → UpToDate / UpdateAvailable (row becomes a link that opens the release page via ACTION_VIEW, runCatching-guarded) / Failed ("tap to retry"); double-tap guard while Checking prevents stacked parallel checks.
- **Settings → About Curio** (SettingsSectionScreen.kt): the Version row now reads `"${VERSION_NAME} · build ${VERSION_CODE}"` (accurate per-build readout; was just VERSION_NAME) and a `CurioUpdateCheckRow()` sits below the divider.
- **Profile → Support & diagnostics** (ProfileScreen.kt): added the same accurate Version row + `CurioUpdateCheckRow()` between Crash logs and Test crash; imports `CurioSettingsInfoRow` + `CurioUpdateCheckRow` added.
- **Supporting changes**: `INTERNET` permission added to AndroidManifest (required for the API call — the app previously had no network permission); `CurioIcons.Download = "download"` added after verifying the glyph exists in the subset font.
- Reviewer pass: no blockers — threading correct (network strictly on Dispatchers.IO), `return@runCatching`/`getOrNull` typing sound, isNewer handles v1.0.10 > 1.0.9 and prerelease suffixes, 404 → neutral state, BuildConfig fully-qualified matches the file's existing style. Two hygiene nits applied: CancellationException rethrown (not swallowed), and taps ignored while a check is running. Known limitation surfaced to the user: no release is published yet, so the check currently lands in the neutral "couldn't check" state until the first `v*` release exists on GitHub.
- Validation: brace checks BALANCED on all six Kotlin files, `git diff --check` clean, INTERNET permission present, Download glyph verified in font. No Gradle command run per repository rules.

## v7.85 — Cabinet: search inside the hero, scroll-under-tear, sticky morphing chip bar

- User asked the Cabinet to match the settings pages: the search bar opens INSIDE the hero card, content scrolls underneath the hero, and the category chip row moves up a little on scroll with the same pop-up morph-pill animation, becomes sticky just below the tear, and the cards pass under it. Single-file change: `app/src/main/java/com/curio/app/features/cabinet/CabinetScreen.kt`.
- **Restructured to the settings overlay pattern**: the root Box now layers WatermarkBackdrop → scroll content (grid / empty states, fills the screen) → new `CabinetStickyChipBar` (drawn on top) → `CabinetHeroHeader` (drawn on top, last). The grid's `contentPadding` top = `CabinetContentTop` (hero 204dp + chip bar 52dp + 18dp) and the empty states are wrapped in a `Box` with that same top padding, so cards run UNDER the ragged tear and the pinned chips as they scroll — the tear visibly eats the cards, matching the settings screens.
- **Search opens inside the hero**: `CabinetHeroHeader` gained `searchActive/searchQuery/onSearchQueryChange/onCloseSearch/searchFocus`. While searching, the top row swaps the Select/Sort/Search pills for a single "Cancel" pill and the title/subtitle block is replaced by a frosted `OutlinedTextField` styled for the rose banner (`OutlinedTextFieldDefaults.colors` with ink alphas, rounded 50, leading search + trailing clear, `focusRequester` keeps the keyboard auto-up).
- **NEW `CabinetStickyChipBar`**: the filter chip row (All / categories / Legacy, moved verbatim from the old below-hero slot) is now a scroll-reactive overlay. Progress is derived from `gridState.layoutInfo.visibleItemsInfo.first().offset` — the first card row's top edge inside the viewport (starts ~274dp, falls as cards rise) — so the lift is tied to the cards actually arriving at the bar, not raw scroll offset (which would include the big top padding and pin instantly). `FastOutSlowInEasing` frostShift drives: pop scale `lerp(0.97→1.0)`, an 8dp lift (`offset(rest 214dp)` + `graphicsLayer translationY`) pinning just below the tear at 206dp (clears the 204dp hero footprint), and a frosted pill Surface morphing in behind the chips (transparent → White/0xFF23242C at 0.94 alpha, hairline rim, `animateColorAsState` `tween(CurioMotion.Durations.Quick)`, `shadowElevation = 8.dp * frostShift`, border appears past 0.02 shift). The chips keep their category tints — only the container morphs, so the pills read as the Profile/Home frosted morph.
- Constants added: `CabinetChipBarRestTop/PinnedTop/Height`, `CabinetChipStickyThreshold (56dp)`, `CabinetContentTop`. Imports added: `animateColorAsState`, `FastOutSlowInEasing`, `tween`, `LazyGridState`, `OutlinedTextFieldDefaults`, `derivedStateOf`, `graphics.lerp`, `LocalDensity`, `CurioMotion`, `isCurioDarkTheme`.
- Reviewer pass: no blockers — layering/z-order sound (bar pins at 206dp clear of the 204dp hero, hero drawn last), `Modifier.align` valid in the BoxScope receiver, `Surface(border = null)` and `Dp * Float` compile, `OutlinedTextFieldDefaults.colors` names valid for the M3 BOM (1.2+), both `items` imports resolve by receiver scope, no dead code, selection mode and search can't coexist (search pill only reachable outside selection mode). Two notes acted on: (1) the progress formula was reworked to track the first card row's viewport position so the lift is smooth and tied to the cards arriving (the initial scroll-offset reading would have pinned almost instantly due to the 274dp content padding); (2) vertical drags over the chip bar pass through to the grid (horizontal-only LazyRow sibling overlay) — flagged for a quick on-device sanity check.
- Validation: brace check BALANCED, `git diff --check` clean, no leftover old search/chip-row references, all imports used. No Gradle command run per repository rules.

## v7.79 — CI fix: Cabinet hero script artifacts

- CI (compileDebugKotlin/compileReleaseKotlin) failed on CabinetScreen.kt with two real errors from the earlier `scripts/fix_cabinet_hero.py` output: (1) `CABINET_TEAR_SEED = 0xCAB1N` — `N` is not a hex digit, so the literal broke parsing and cascaded into ~10 downstream "Unresolved reference 'CabinetHeroPair'" errors; fixed to `0xCAB1E`. (2) The search bar Row used `.padding(horizontal = 16.dp, top = 14.dp)` — `horizontal` and `top` are from different overloads; fixed to `.padding(start = 16.dp, end = 16.dp, top = 14.dp)`. Audited the rest of the hero region: all other `.padding()` calls are single-overload-consistent, no other invalid hex literals, all icon constants used by the action pills (Close/Search/ArrowDownward/ArrowUpward) exist, `heroWatermarkSymbols` exists, settings helpers are public, imports complete. Braces BALANCED, `git diff --check` clean. Committed as `2b232a7`. No Gradle command run per repository rules.
