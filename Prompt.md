# Prompt — narrow-width dice alignment

## Request
The previous shared icon centering change did not resolve the visible issue on a narrow Poco M2 Reloaded screen. The Home profile/menu pills also needed to remain stable, and the casino dice looked slightly low inside its pill. The same dice issue is present on the dedicated Shuffle/Spin page.

## Finding
The icon layout boxes were already centered. The visible Material Symbols `casino` glyph has a small optical low bias, so changing the shared renderer did not fully correct it. Spin also has a separate Canvas-rendered animated `ShuffleGlyph` state that must match the resting `casino` glyph.

## Implementation
- Added a small `-1.dp` optical lift to Home's circular `Shuffle the deck` casino icon.
- Added a matching `-1.5.dp` lift to both Spin button dice states: the resting `CurioIcons.Casino` glyph and animated `ShuffleGlyph`.
- Left the Home menu/profile pill geometry, button circles, and shared icon renderer unchanged.

## Validation
- `git diff --check` passed.
- Comment-aware Kotlin structural checks passed for HomeScreen.kt and SpinScreen.kt.
- Confirmed the Spin `offset` import and all three dice offsets.
- No Gradle build, compile, lint, or test commands were run because repository policy forbids them locally; CI should validate the Android artifact.
