# Prompt — Cabinet dates and Entry Detail tear layout

## Request
Fix Cabinet relative dates so an entry from Aug 5 is 2 days ago and an entry from Aug 6 is yesterday when today is Aug 7. On Entry Detail, narrow the white tear and place the topic category text below the tear in a fixed, non-scrolling layer.

## Implementation
- `CurioEntry.capturedAtDaysAgo` now compares local calendar dates instead of elapsed 24-hour blocks, so midnight transitions label entries correctly while preserving stored timestamps.
- Entry Detail's visible white under-sheet was reduced to a narrow 16dp lip with a smaller 3dp offset / 7dp baseline treatment.
- Extracted the category identity row into `EntryDetailCategoryLabel`, positioned outside the vertical scroll immediately below the hero and white lip.
- Reserved the category row's footprint inside the scrolling content so the Quick fact and capture body begin below it without overlap.
- Removed the old category row from the scrolling metadata block; Quick fact and tags remain scrollable.

## Validation
- `git diff --check` passed.
- Comment-aware Kotlin structure checks passed for both changed Kotlin files.
- Targeted assertions passed for local calendar date comparison, title-row extraction, removed `EntryDetailMetaLift`, and narrow tear parameters.
- Code review found no blockers.
- No Gradle build, compile, lint, or test commands were run because repository policy forbids them locally.
- Local commit only; no push, following the user's every-third-commit workflow.
