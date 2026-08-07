# Prompt — Profile responsive polish and detail category/tear fix

## Request
Fix the remaining visual issues in Profile and Entry Detail:
- Material Symbols icons still look optically low; inspect the font box/baseline treatment and correct the shared renderer.
- On narrow Profile screens, Edit profile, streak, and the level/synthesizer control misalign or wrap unevenly.
- Profile hero/stat text is clipped at narrow widths.
- Merge XP progress, quests, and achievements into one coherent Profile card.
- The Entry Detail category label must scroll with the page instead of sticking over the content.
- The Entry Detail hero tear must not render as a black/dark strip; it should read as the paper-colored seam.

## Analysis
- `CurioIcon` already removes platform font padding and centers its line box, but Material Symbols' visible ink has a small optical lower bearing. Apply a very small shared upward optical translation to the glyph text without changing its layout box.
- Profile hero actions use intrinsic-width FlowRow children. Replace the narrow-screen layout with equal-width compact action cells and ellipsized labels so all controls share one baseline and cannot extend beyond the hero gutter.
- Profile hero stat labels need single-line ellipsis protection. The separate XP, quests, and achievements cards should become one progress-and-achievements card with the existing quest navigation preserved.
- `EntryDetailCategoryLabel` is currently outside the `verticalScroll` column and is overlaid at a fixed offset; move it directly into the scrolling content after the hero and remove the compensating spacer.
- The detail tear's explicit `Color.Black.copy(alpha = 0.20f)` layer is the source of the black edge. Keep the layered edge treatment but use the existing paper/sheet color so the seam stays paper-colored in both themes.

## Plan
1. Update the shared icon renderer for optical centering.
2. Stabilize Profile hero controls and stat labels for small widths.
3. Replace separate Profile progress/quest/achievement cards with one combined card.
4. Put the Entry Detail category row in the scroll content and remove the black seam color.
5. Review, run permitted non-build checks, update this log, and commit/push.

## Implementation completed
- `CurioIcon` now applies a small paint-only upward optical correction while preserving its centered layout box.
- Profile hero actions use equal-width, aligned action cells with two-line ellipsis-safe labels; hero stat labels are protected from clipping.
- XP progress, quest navigation, and achievement progress/preview now share one Profile gamification card.
- Entry Detail category identity now sits in the vertical scroll flow instead of a fixed overlay.
- The detail tear no longer uses a black shadow; dark mode uses a warm paper-colored seam.

## Validation
- `git diff --check` passed.
- Targeted brace/parenthesis balance checks passed for all three Kotlin files.
- Confirmed removed Profile helper symbols and fixed category block symbols have no remaining references.
- Final review found no remaining blockers after removing the unused `zIndex` import.
- No Gradle compile/build/lint/test commands were run because repository policy forbids local Android builds.
