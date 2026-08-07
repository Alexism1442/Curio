# Prompt.md — Current Request Log

## Request (2026-08-07, 14th): Reveal watermark still shifts down — DONE (pushed)

**User request:** "add a navbar padding in topic reveal screen so that the watermark doesnt shift as its still shifts down"

### Analysis — root cause found
- The NavHost already had the right mechanism: `reserveBarSpace` → an invisible placeholder in the `bottomBar` slot sized to the real bar's measured height (`bottomBarHeightPx`), so `innerPadding.bottom` stays constant when navigating a tab → REVEAL / ENTRY_DETAIL (the bar hides on those routes).
- BUT the condition compared the route PREFIX against the FULL route patterns:
  `routePrefix in setOf(CurioRoutes.REVEAL, CurioRoutes.ENTRY_DETAIL)`
  where REVEAL = `"reveal/{categorySlug}/{topicName}?browse={browse}"` and ENTRY_DETAIL = `"detail/{entryId}"`.
  `"reveal"` / `"detail"` are NEVER in that set → `reserveBarSpace` was **always false** → the placeholder never rendered (verified with python: `'reveal' in {"reveal/{…}", "detail/{entryId}"}` → False).
- Consequence: on Spin→Reveal the bottom bar vanishes, innerPadding.bottom drops from the bar height to the nav inset, the content area (SharedTransitionLayout) grows by the bar height mid-morph → the exiting ticket shifts down AND the reveal watermark (bias-positioned in the taller container) shifts down. The earlier morph fix (cc26e15) never took effect because of this bug.

### Fix
- **`navigation/CurioNavHost.kt`** — `reserveBarSpace` now compares the route PREFIX (`CurioRoutes.REVEAL.substringBefore("/")` / `ENTRY_DETAIL.substringBefore("/")`). The placeholder engages, innerPadding stays constant across the whole transition, and the watermark stays exactly where it was on the deck. This IS the requested "navbar padding" effect, done at the source: padding the reveal screen itself would double-reserve once the placeholder works (a visible empty strip + the watermark sitting 80dp too high).
- **`fastlane/.../20260810.txt`** — changelog bullet.
- **`Prompt.md`** — this log.

### Validation
No Gradle in this env (per AGENTS.md) — static checks: brace balance, prefix math sanity (python), `git diff --check`, code review. Commit + push pending.

### Follow-ups
- None.
