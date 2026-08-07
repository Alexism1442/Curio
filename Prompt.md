# Prompt — Topic Reveal done button and icon alignment

## Request
Improve the existing “Already watched/listened/read/explored” button on Topic Reveal because it looks bad, and analyze/fix icons that appear slightly low inside buttons on some screens.

## Findings
- Topic Reveal used a full-width custom `Surface` pill for the secondary done action, making it visually compete with the primary Start exploring CTA.
- `CurioIcon` renders Material Symbols as `Text`. The surrounding Box was centered, but platform font padding and the font’s ascent/descent metrics made the visible glyph look slightly low in icon+text controls.

## Implementation
- Replaced the Topic Reveal done `Surface` with a lighter full-width secondary `TextButton`, retaining mark/unmark behavior, labels, and accessible action semantics.
- Added `PlatformTextStyle(includeFontPadding = false)` and centered `LineHeightStyle` metrics to the shared `CurioIcon` text style, fixing the source of the cross-screen optical vertical drift.
- Kept the primary CTA, sentiment controls, navigation, and done-state persistence unchanged.

## Validation
- `git diff --check` passed.
- Comment-aware Kotlin brace/string checks passed for the changed files.
- Code review found no blockers; the shared icon fix and Topic Reveal styling were considered safe.
- No Gradle build, compile, lint, or test commands were run because repository policy forbids them locally; CI should validate the Android artifact.
