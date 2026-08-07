# Prompt — dark-mode rose hero-card shade

## Request
The shared Home rose hero-card color is too bright in dark mode. Darken that hero-card family across Home and the other screens that reuse it, while leaving unrelated category colors and light mode unchanged.

## Analysis
- Home, Profile, Settings, Cabinet, and Onboarding resolve their shared torn-banner fill from `CurioColors.HomeRosewood` through duplicated `homeRoseAccent`, `profileRoseAccent`, and exported `settingsRoseAccent` helpers.
- The non-pastel branch currently lightens the base rose regardless of theme, so dark mode receives a bright fill instead of a dark rose.
- Pastel dark mode has a separate muted branch, but the request is specifically for one darker dark-mode treatment for this shared hero family.
- Quests also uses the raw shared rose for its current-quest inset; it should follow the shared settings hero shade in dark mode. Promo artwork is intentionally self-contained and remains unchanged.

## Plan
1. Add one dark companion token for the shared HomeRosewood hero family.
2. Route all shared hero helpers, including the Quests rose inset, to that token only in dark mode; preserve light mode, category accents, and promo artwork.
3. Review the diff and run permitted static validation only; local Gradle/build/lint/test commands are forbidden by project policy.
4. Update the store changelog and this request log, then commit and push.

## Implementation completed
- Added `CurioColors.HomeRosewoodDark` as the single dark companion for the shared rose hero family.
- Routed Home, Profile, Settings, Cabinet, and Onboarding hero helpers to the dark companion only in dark mode.
- Updated the Home drawer replay icon and Quests current-quest inset with an explicit dark-only branch while preserving their original light-mode raw rose.
- Left category accents and the self-contained promo artwork unchanged.

## Validation
- `git diff --check` passed.
- Comment/string-aware delimiter checks passed for all changed Kotlin files.
- Final review removed an unused Home local and confirmed the dark-only scope.
- No Gradle compile/build/lint/test commands were run because repository policy forbids local Android builds.

## Closeout
The fix is ready to commit and push.
