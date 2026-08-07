# Prompt — Topic Reveal pop entrance and confetti removal

## Request
When Topic Reveal appears, make its main topic card pop in smoothly from the card presentation. Remove the automatic confetti that currently fires every time Topic Reveal opens.

## Implementation
- Reused Curio's existing `MorphEntrance` motion wrapper around the Topic Reveal `HeroCard`, giving the main card a smooth fade-and-scale pop on entry.
- Removed the Topic Reveal-only confetti trigger state, delayed launch, overlay, and now-unused `ConfettiBurst`, `CurioColors`, and `CurioMotion` imports.
- Confetti behavior on Spin and Save/Capture remains unchanged.
- Existing reveal content, navigation, and explore flows remain unchanged.

## Validation
- `git diff --check` passed.
- Comment-aware Kotlin structure check passed for `TopicRevealScreen.kt`.
- Targeted assertions confirmed `MorphEntrance` wraps `HeroCard` and no Topic Reveal confetti references remain.
- Code review found no blockers.
- No Gradle build, compile, lint, or test commands were run because repository policy forbids them locally.
- Local commit only; no push, following the user's every-third-commit workflow.
