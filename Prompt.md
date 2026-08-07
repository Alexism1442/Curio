# Prompt — maximum-quality promo and mood-board exports

## Request
The promo preview looks good, but the saved output changes slightly and its quality drops drastically. Increase promo export quality to maximum. Apply the same maximum-quality treatment to mood-board output.

## Completed
- Promo share exports now opt into fixed 4x density while regular entry share cards retain their established device-density behavior.
- Promo exports preserve the device font scale so text/layout remain faithful to the preview environment.
- Promo and mood-board PNG compression use quality 100 (PNG remains lossless).
- Mood-board exports target a 4096px long side and automatically scale down only when the device-aware ARGB bitmap budget requires it.
- Failed mood-board captures recycle partially allocated bitmaps; the budget reserves heap for tile bitmaps and Compose rendering.

## Validation
- `git diff --check` passed.
- Static Kotlin brace/string checks passed for all changed Kotlin files.
- Code review approved the promo scoping, density/font-scale fidelity, PNG quality, and failure cleanup.
- No Gradle build, compile, lint, or test commands were run because repository policy forbids them in this environment; CI should validate the Android release artifact.
