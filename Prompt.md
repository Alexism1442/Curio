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
