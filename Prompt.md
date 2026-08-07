# Prompt.md — Current Request Log

## Request (2026-08-07, 6th): Reveal morph fixes — headline fade, layout-stable bottom bar — DONE (committed, NOT pushed)

**User request:** fix the Topic Reveal morph — the watermark shifts down, the title text morph is weird/stretched for long names, the back animation can start at the wrong position, and the morph starts slightly low because the bottom bar disappears. User chose "fade the title in" and asked for full implementation committed WITHOUT pushing.

### Root causes (verified from sources)
1. **Layout shift (watermark + morph offset):** `CurioNavHost`'s invisible placeholder reserved `80dp + nav-bar inset`, but M3 `NavigationBar` (1.5.0-alpha20 source verified) consumes the inset INSIDE its 80dp min height → placeholder was taller than the bar by the inset. When the bar is swapped for the placeholder (Spin→Reveal), Scaffold `innerPadding` changes → `SharedTransitionLayout` resizes mid-morph → the exiting Spin screen re-lays-out (bias-aligned watermark re-positions, bottom-anchored deck shifts) and the shared-element source bounds are offset ("morph starts a little down").
2. **Weird text morph:** animation 1.11.2 `sharedElement` has no `resizeMode` — text is always SCALED from its stable layout (never re-wrapped; framework docs explicitly say Text is the hard case). The 34sp ticket title (≈246dp wide) scaled to a full-width 40sp headline distorts long names, and the reverse morph could capture wrong bounds.

### Changes
- **`CurioNavHost.kt`** — the placeholder now reserves the REAL bar's measured height (`onSizeChanged` → `bottomBarHeightPx`, `rememberSaveable`), falling back to the old estimate if never measured. `innerPadding` is now identical between tab and Reveal/EntryDetail → no relayout, watermark pinned, morph starts exactly at the ticket.
- **`TopicRevealScreen.kt`** — headline is no longer a shared element; it blooms in via `RevealContentEntrance(delayMillis = 80)` (fade + rise). Removed the title shared-element state.
- **`SpinScreen.kt`** — removed the ticket title's `sharedElement`; added `LaunchedEffect(opening)` that settles `settleScale` to exactly 1f before the morph (the ticket rested at `LandedRestScale = 1.02`, so the overlay started 2% smaller than the visible card).
- **`RevealSharedScopes.kt`** — removed now-unused `RevealTitleSharedElementKey` + doc.
- Changelog bullet added to `20260810.txt`.

### Verification
No Gradle in this environment (AGENTS.md) — static checks only: grep shows zero remaining `RevealTitleSharedElementKey` / `titleSharedTransitionScope` / `revealTitleState` references, `git diff --check` clean. CI is the compile gate; NOT pushed per user request (push when ready to validate).

### Status
- Implemented and committed locally. **Not pushed** (user explicitly requested no push).
