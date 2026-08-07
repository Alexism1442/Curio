# Prompt — optical icon centering refinement

## Request
Icons still appear slightly misaligned inside pills and compact controls. Improve their visual centering without disturbing the pill geometry or already-correct layout behavior.

## Analysis
- `CurioIcon` renders Material Symbols as text glyphs. Its measured box is centered, but the glyph's visible ink is bottom-heavy.
- The shared renderer previously applied only a `0.5dp` upward painted-ink correction.
- Dice controls in Home and Spin added separate `1dp`/`1.5dp` offsets, creating inconsistent correction amounts across pills and buttons.
- The issue is optical/font-metric alignment, not container alignment; changing pill sizes, padding, or row arrangements would risk regressions.

## Plan
1. Increase the shared painted-ink correction to `1dp` while keeping the layout/touch box unchanged.
2. Normalize the known casino/dice call-site offsets so their total correction remains intentional rather than stacking unpredictably.
3. Review and run permitted static validation only; local Gradle/build/lint/test commands remain forbidden by repository policy.
4. Update the changelog, commit, and push.

## Implementation
- `CurioIcon` now applies a shared `-1dp` optical lift.
- Home's casino controls use a `-0.5dp` local addition, preserving their prior net lift while matching the stronger shared correction.
- Spin's animated and idle dice use a `-1dp` local addition, preserving a consistent stronger casino correction.

## Validation
- Comment/string-aware delimiter checks passed for the changed Kotlin files.
- `git diff --check` passed.
- Review confirmed the correction preserves layout boxes and touch targets; no Gradle/build/lint/test commands were run because repository policy forbids local Android builds.

## Closeout
The icon-centering refinement is ready to commit and push.
