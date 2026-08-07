# Prompt — Topic Reveal landed-card morph handoff

## Request
When a topic lands on Spin and Topic Reveal opens, the reveal hero should visibly feel like the landed Spin ticket expands/morphs into the Topic Reveal card. The current page does not show that continuity.

## Analysis
- Spin already has an `isOpening` handoff state and an `Opening…` pulse, but `isOpening` was never set to `true` before the auto-navigation delay, so the source card never communicates the handoff.
- Topic Reveal already wraps `HeroCard` in `MorphEntrance`, but the wrapper first mounts while `resolved` is still null. When the topic data arrives, the same wrapper remains mounted and only its contents update, so the card's entrance animation has already been consumed before the real topic hero appears.
- The generic NavHost forward transition slides every destination horizontally. That masks the intended card expansion. Reveal needs a reveal-specific fade/near-scale transition instead of the generic slide.

## Plan
1. Set Spin's opening state during the landing-to-reveal handoff and give the source ticket a restrained expansion.
2. Key Topic Reveal's hero entrance to the resolved topic so the real hero card plays its morph after topic data lands.
3. Use a reveal-specific NavHost fade/near-scale transition to preserve visual continuity with the expanding ticket.
4. Give manual landed-card taps the same handoff delay, review, run permitted non-build checks, update Prompt/changelog, and commit/push.

## Implementation completed
- Auto-land navigation now sets `isOpening` before the handoff delay; the Spin ticket scales up and shows `Opening…`.
- Manual landed-card opens use the same reveal-handoff delay instead of navigating immediately.
- Topic Reveal keys `MorphEntrance` to the resolved topic id, so the real hero animates after data loads.
- Reveal navigation now uses a fade + near-scale entry and no longer relies on the generic horizontal slide for this handoff.

## Validation
- `git diff --check` passed.
- Balanced-delimiter checks passed for Spin, Topic Reveal, and NavHost sources.
- Targeted assertions confirmed both auto and manual opening paths, keyed hero entrance, and reveal-specific transition.
- Final review found and fixed the immediate manual-navigation and unused-import issues.
- No Gradle compile/build/lint/test commands were run because repository policy forbids local Android builds.
