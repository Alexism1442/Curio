# Prompt — request log (DOX)

This file is the running log per the DOX framework (see root `AGENTS.md` — Prompt.md).

## Current request — "fix morph dip + title text morph + smoothen Cabinet animations"

**Reported problems:**
1. Tapping the Spin ticket opens Topic Reveal with the smooth shared-element morph,
   but at the START of the animation the card visibly moves DOWN before expanding
   (user suspected the bottom navbar).
2. Only the card/icon morphs; the topic TITLE text pops in after the expansion —
   make the title morph too.
3. The Cabinet animations feel somewhat janky — make them more seamless.

**Root cause of the dip (confirmed by code analysis):** `CurioNavHost` renders the
Scaffold bottom bar only for tab routes (`showBottomBar`). Navigating Spin → Reveal
removes the bar in the same frame the transition starts → `innerPadding.bottom` drops
~80dp instantly → the exiting Spin screen re-lays-out taller, and its deck stage is
**bottom-anchored** (`contentAlignment = BottomCenter` / `Arrangement.Bottom`), so the
ticket physically drops ~80dp → the morph then plays from the lowered position
("moves down, then animates").

**Fixes (one commit):**
1. `CurioNavHost.kt` — on the morph-target routes (`REVEAL`, `ENTRY_DETAIL`) the
   bottomBar slot now renders an INVISIBLE placeholder sized exactly like the bar
   (`heightIn(min = 80.dp)` + `windowInsetsPadding(navigationBars)`, mirroring the
   `CurioBottomBar` construction), so `innerPadding` never changes and the exiting
   tab screen never re-lays-out mid-morph. Fixes both Spin→Reveal and Cabinet→Detail
   (and their pop-backs). Reveal/Detail are scrollable/top-anchored, so the reserved
   space is invisible on those screens; reveal→capture stays stable (top-anchored).
2. `RevealSharedScopes.kt` — new `RevealTitleSharedElementKey = "reveal-hero-title"`.
3. `SpinScreen.kt` (`HeroTicketCard`) — the ticket's title Text is now its own shared
   element (nested inside the "reveal-hero" card element — the framework excludes the
   inner element from the outer's overlay, so the card expands while the title glides
   out separately).
4. `TopicRevealScreen.kt` — the headline below the hero is the matching shared element
   (null-guarded for secondary entry points). It deliberately has NO entrance animation
   (the hero's existing comment shows entrance animations on shared elements affect the
   overlay → would make the text invisible mid-morph).
5. `CabinetScreen.kt` (`CabinetChipPop`) — eased the per-pill pop (scale, color bloom,
   elevation) on the same FastOutSlowIn curve as the bar's lift, so the chips settle in
   sync with the bar instead of popping linearly ("janky" feel).

**Known risks to verify on-device/CI (can't run Gradle here):**
- Nested shared element (ticket title inside the card shared element) — intended
  behavior per the framework, but worth a visual check; fallback is dropping the title
  shared element and keeping only the card morph.
- The title's crossfade travels from the ticket (light ink on gradient) to the reveal
  headline (onSurface) — a brief color blend over the cream page; acceptable.
- REVEAL/ENTRY_DETAIL now render in an 80dp-shorter content area (scrollable screens,
  mostly invisible; verify reveal bottom CTA / detail bottom content when scrolled).

**Validation:** no Gradle builds allowed in this environment (root AGENTS.md); changes
were reviewed by code-reviewer-glm and verified with grep/diff. CI on push is the
compile check. Committed to `main` and pushed.
