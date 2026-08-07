# Prompt — request log (DOX)

This file is the running log per the DOX framework (see root `AGENTS.md` — Prompt.md).

## Current request — "fix shuffle button sizing + home pill icons + CI errors"

**Reported problems:**
1. The Spin page's shuffle button doesn't shrink on small screens and looks bad.
2. The Home top-bar profile/menu pills: the icon inside the pill sits a little low
   (not the pill itself).
3. CI compile errors (from the last push):

   - `SpinScreen.kt:935/972` — Unresolved reference `fillMaxHeight` (used but never imported).
   - `SpinScreen.kt:943` — `maxWidth` "cannot be called with an implicit receiver" inside the
     nested `Row { Column { } }` of the wide layout (BoxWithConstraintsScope receiver lost).
   - `CabinetScreen.kt:476-522` — `CabinetHeroHeader(...)` call: "No value passed for parameter
     'trailing'" + "Too many arguments" + "Cannot infer type for value parameter 'ink'" +
     six "@Composable invocations can only happen from the context of a @Composable function".
     Root cause: the `trailing: @Composable (ink: Color) -> Unit` slot is NOT the last parameter
     (`compact` follows it), so K2 fails to bind the trailing-lambda syntax `) { ink -> }`.

**Fixes (committed in one commit):**
1. `SpinScreen.kt`
   - Added `import androidx.compose.foundation.layout.fillMaxHeight`.
   - Hoisted the `wideFit` computation out of the wide-branch `Row/Column` into the
     `BoxWithConstraints` scope (where `widthFit` already resolves `maxWidth` fine).
   - `SpinButton` now takes `fitScale: Float = 1f`; the button + orbit ring scale with the
     deck's continuous fit (`sizeScale = fitScale.coerceIn(0.75f, 1f)`), so on small screens
     the CTA shrinks in proportion to the deck instead of staying full-size. `SpinDeckSection`
     passes its `fitScale` through. NOTE: on normal 360dp phones fitScale ≈ 0.93, so the button
     is now ~7% smaller there too (matching the deck's existing 0.93 render scale).
2. `CabinetScreen.kt` — the action-pill slot is now passed as a named argument
   `trailing = { ink -> ... }` (the K2-safe form the rest of the codebase uses), with the
   lambda body re-indented. Clears all six Cabinet CI errors.
3. `HomeScreen.kt` — `TopBarPill` icons get a `(-0.5f).dp` upward optical offset (same
   correction the casino glyph wears on top of the shared 1dp CurioIcon lift).

**Validation:** Local Gradle builds are forbidden in this environment (AGENTS.md), so the
compile fix is verified by code review + CI on push. `git diff`/grep verified: import present,
single `wideFit` declaration, brace balance in the Cabinet call, single `SpinButton` call site.

**State:** fixes committed to `main` and pushed. Working tree still holds the user's
in-progress `authors.json`/`books.json` + scripts (left untouched, not part of this commit).
