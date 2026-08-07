# Prompt.md — Current Request Log

## Request (2026-08-07, 18th): Hero watermark morph not smooth — DONE (pushed)

**User request:** "the watermark animation morph isnt that smooth" → clarified: "ther hero watermark" — the big category glyph on the card itself, not the page backdrop.

### Analysis — root cause
- The shared `"reveal-hero"` element still contained the **150dp category glyph** (the card's watermark) on both sides (the v8.3 fix for the main-card TEXT left the glyph inside the face).
- The SharedTransitionScope overlay scales the shared content to the interpolated bounds; the ticket (286×310) and hero (~392×260) have different aspect ratios → the glyph scales **non-uniformly** → reads as a stretched oval mid-morph. On BACK the overlay draws the *destination* (ticket) face content starting at hero-bounds scale — the ticket's glyph is blown up to hero size (a big blurry icon) then shrinks → visibly "not smooth".

### Fix — glyph out of the shared element on both sides
- **`features/spin/SpinScreen.kt`** — the ticket's glyph was removed from the shared face Box (which is now a pure gradient + rim-light); it's rendered as a non-shared sibling in the content Box (same CenterEnd + 6dp, 150dp, ink@0.16) and fades in with the page on back.
- **`features/reveal/TopicRevealScreen.kt`** — the hero's glyph was removed from the shared gradient Box; it's now a sibling wrapped in `HeroPillEntrance(delayMillis = 250)` (the same bloom the text pills use), so it appears right after the ~320ms bounds morph settles.
- Result: the morph animates only the smooth gradient (+ imperceptible rim-light stroke); the hero watermark and text never squash in either direction.

### Validation
No Gradle in this env (per AGENTS.md) — static checks: brace balance (SpinScreen 395/395, TopicReveal 202/202), shared face Boxes contain only comments, glyphs are now non-shared siblings (`.align()` still in BoxScope: content Box on Spin, BoxWithConstraints on Reveal), `git diff --check` clean. Changelog + Prompt.md updated. Code review ran. CI on the pushed HEAD is the compile gate.

### Follow-ups
- None.
