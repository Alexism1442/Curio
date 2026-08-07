# Prompt — promo palette, dark hero cards, and Detail tear refinement

## Request
Improve promo colors and dark non-pastel hero cards, then refine the Detail screen so its white torn-paper lip is not too wide and seeded heroes never read as a straight line.

## Completed
- Promo artwork uses a richer rose-plum palette with unified phone mockups and lower-white overlays.
- Shared non-pastel dark category fills deepen toward black; Entry Detail frost and selected category surfaces use restrained midnight treatment.
- Detail's white tear lip is narrower without changing the metadata layout reservation.
- Detail hero and under-sheet use the same deterministic Detail-only tear personality, with a salted seed and secondary oscillation to prevent unlucky seeds from producing a visually flat seam.
- Other screens retain their existing tear behavior.

## Validation
- `git diff --check` passed.
- Comment-aware static Kotlin brace/string checks passed for all changed Kotlin files.
- Code review found no blockers; hero/sheet tear parameters are aligned and the Detail layout reservation is preserved.
- No Gradle build, compile, lint, or test commands were run because repository policy forbids them locally; CI should validate the Android artifact.
