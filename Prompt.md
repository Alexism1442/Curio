# Prompt.md — Current Request Log

## Request (2026-08-07, 17th): CI compile — unresolved `coil.request.filterQuality` — DONE (pushed `f5d5c1e`)

**User request:** "fix this" (CI log: `Unresolved reference 'filterQuality'` at MoodBoardZoom.kt 58/218 and AdaptiveImageGallery.kt 34/152).

### Analysis
`coil.request.filterQuality` does NOT exist in Coil 2.7.0 — it's a Coil 3 (coil3-core) API. My previous fix (ef1052e) wrongly assumed it existed when moving `FilterQuality.High` off the `Image(painter=…)` overload (removed in foundation 1.4+). The two request-level `.filterQuality(FilterQuality.High)` calls + their imports were the 4 failing sites.

### Fix
- **MoodBoardZoom.kt / AdaptiveImageGallery.kt** — removed `import coil.request.filterQuality` and the `.filterQuality(High)` request calls (AdaptiveImageGallery painter back to plain `rememberAsyncImagePainter(tile.uri)`); also dropped the now-unused `FilterQuality`/`ImageRequest` imports. Comments updated to note sharpness comes from the **4096px decode caps** (the real anti-pixelation fix — Coil 2 has no request-level filter quality).
- **Kept**: the 4096px zoom/export decode caps, the bounded export preload, and MoodBoardExport's `filterQuality = FilterQuality.High` on the `Image(bitmap = …)` overload (valid — only the painter overload lost the param).
- No changelog (behavior-neutral compile fix; the decode caps still deliver the sharpness).

### Validation
Grep: zero `coil.request.filterQuality` references; the only remaining `filterQuality` site is the valid bitmap-overload one in MoodBoardExport + comments. Braces balanced 105/105 and 49/49. `git diff --check` clean. CI on the pushed HEAD is the compile gate.

## Request (2026-08-07, 16th): Main card texts glitchy when tapping back — DONE (pushed)

**User request:** "the main card texts still looks glitchy when tapping back"

### Analysis — root cause
- The Spin ticket and the Topic Reveal hero are matched `"reveal-hero"` shared elements (`RevealSharedElementKey`). The **entire** ticket (title 34sp, tags, teaser, byline pill) and the **entire** reveal hero (action badge, byline, subtype pills) were INSIDE their respective `Modifier.sharedElement` layouts.
- In `SharedTransitionScope`, the overlay always draws the **destination** screen's shared content animating from the source bounds to the destination bounds. On **back** (Reveal → Spin), the destination is the Spin ticket — so the overlay draws the *ticket's* content shrinking from the hero's bounds (~392×260) to the ticket's (286×310). Because the aspect ratios differ, the shared content scales **non-uniformly** → the ticket's title/tags/teaser squash/stretch during the pop — the "glitchy main card texts on back". (Forward: the same happens to the reveal hero's pills when opening.)
- The earlier headline fix (v8.2) only moved the reveal HEADLINE out of the hero; the pills and the ticket's whole text block were still shared → the glitch persisted.

### Fix — text lives OUTSIDE the shared elements on both sides
- **`features/spin/SpinScreen.kt`** — the ticket's `sharedElement` moved from the outer card Box onto the inner **card face** Box (gradient + glyph + rim-light only). The byline pill and the content column (title/tags/teaser/tap-hint) are now siblings in a new content `Box`, so they never render inside the morphing overlay — on back they simply fade in with the page's popEnter fade.
- **`features/reveal/TopicRevealScreen.kt`** — the hero's `sharedElement` moved from the outer Surface onto the inner **gradient + glyph** Box; the three text pills (action badge, byline, subtype) became siblings wrapped in a new `HeroPillEntrance` — they bloom in with a 300/340/380ms delay (paced to the ~320ms `RevealBoundsTransform` morph) and fade out with the page on back.
- Both shared pieces are now gradient + glyph only (plus the ticket's rim-light), so the morph scales only graphics — never text — in either direction.

### Validation
No Gradle in this env (per AGENTS.md) — static checks: brace balance (SpinScreen 395/395, TopicReveal 201/201), exactly one `Modifier.sharedElement` per file on the intended Boxes, the hoisted byline/Column still inside a BoxScope (`Box` content) so `.align()` compiles, `git diff --check` clean. Changelog + Prompt.md updated. Code review ran. CI on the pushed HEAD is the compile gate.

### Follow-ups
- None.
