# Prompt — white torn-paper under-layers

## Request
The white torn-paper layer is correct, but in dark mode the layer beneath the tear appears black/dark on Profile, Settings pages, Cabinet, the Home drawer, and the intro. Keep the paper layer white like the reference surfaces.

## Finding
The affected hero implementations painted their under-sheet with `MaterialTheme.colorScheme.background`, which correctly follows the page theme but becomes midnight/black in dark mode. Cabinet additionally passed a category/page wash through a `sheetColor` parameter.

## Implementation
- Switched the under-sheet in Profile, the shared Settings hero, Cabinet, Home drawer, and Onboarding to `CurioColors.CreamWhite` (`#FFFBF5`).
- Removed Cabinet's obsolete `sheetColor` parameter and call argument; the torn backing is now consistently physical paper rather than a page/category background.
- Left the dark hero/banner fills, page backgrounds, watermark, and torn-edge shadow unchanged.

## Validation
- `git diff --check` passed.
- Comment-aware Kotlin structural checks passed for all five changed feature files.
- Verified all five under-sheet backgrounds use `CurioColors.CreamWhite` and no `sheetColor` references remain.
- Code review found no blockers.
- No Gradle build, compile, lint, or test commands were run because repository policy forbids them locally; CI should validate the Android artifact.
