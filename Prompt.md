# Prompt — tablet & landscape adaptive redesign

## Request
Redesign the whole app's placements for tablet and landscape mode. User decisions (ask_user):
- **NavigationRail on the left** for medium/expanded windows; bottom bar stays on phones.
- **Centered max-width column** (~720dp) for page content; theme background fills the gutters.
- **Always-on** (automatic) — no Settings toggle.

## Analysis
- Curio is a single-Activity Compose app: one NavHost, 3 bottom-nav tabs (Home / Spin / Cabinet), edge-to-edge, no orientation lock, no size-class awareness today.
- `material3-window-size-class-android 1.5.0-alpha20` is already in the version catalog but not wired in. Verified from the artifact sources: the only public API is
  `@ExperimentalMaterial3WindowSizeClassApi @Composable fun calculateWindowSizeClass(activity: Activity): WindowSizeClass`
  (Compact < 600dp / Medium 600–839 / Expanded ≥ 840). `LocalActivity` is available from activity-compose 1.13.0.
- M3 1.5.0-alpha20 `NavigationRail(modifier, containerColor, contentColor, header, windowInsets = NavigationRailDefaults.windowInsets, content)` and
  `NavigationRailItem(selected, onClick, icon, modifier, enabled, label, alwaysShowLabel, colors, interactionSource)` confirmed in the artifact.
  Default rail insets = `systemBarsForVisualComponents.only(Vertical + Start)` — correct for a full-height rail at the window edge.
- `widthIn(max=…)` uses `enforceIncoming = true` (verified in foundation-layout 1.11.2 sources): a cap only engages when the incoming constraint is looser,
  so `fillMaxHeight().widthIn(max = 720.dp)` inside a centered Box yields exactly min(available, 720) with no constraint conflict.

## Plan
1. Add `implementation(libs.androidx.material3.window.size)` to `app/build.gradle.kts`.
2. New `ui/adaptive/CurioAdaptiveLayout.kt`: `CurioContentMaxWidth = 720.dp`, `windowWidthSizeClass()` helper, `WindowWidthSizeClass.isWide`.
3. `CurioBottomNav.kt`: add `CurioNavigationRail` (shares destinations + page-wash tint logic with the bottom bar).
4. `CurioNavHost.kt`: wide windows render the rail in a Row + center the NavHost content at the max width; bottom bar only in compact.
5. Adaptive grids: Cabinet (Fixed 2 → Adaptive 176 when wide), Category picker + Spin picker sheet (Fixed 2 → Adaptive 160 when wide); center both picker sheets at 720 on wide windows.
6. Update Prompt.md, app/AGENTS.md (adaptive contract), fastlane changelog for the current versionCode.

## Validation
- No local Gradle builds (repo policy). Static checks: import/reference deltas, `git diff --check`, delimiter balance.
- Spawn code-reviewer-glm after implementation.
- Commit + push on completion.

## Follow-up fixes (same session, same commit)
1. **Reveal morph** — the topic reveal now EXPANDS out of the landed card via a real shared-element transition (`SharedTransitionLayout` wraps the NavHost in CurioNavHost; Spin front ticket + Reveal hero are matched `"reveal-hero"` shared elements; scopes threaded via `ui/adaptive/RevealSharedScopes.kt` composition locals, since this Compose version has no built-in `LocalSharedTransitionScope`). Removed the competing `MorphEntrance` wrapper on the reveal hero.
2. **Shuffle double-open** — tab taps compared the FULL route, so a category-launched deck (`spin/artists`) re-navigated when tapping the already-selected Shuffle tab. Both bottom bar and rail now guard on the route PREFIX.
3. **Profile stat alignment** — Level · Saved · Lanes labels had `fillMaxWidth` without `textAlign` (left-hugging under centered values); added `TextAlign.Center`.
4. **Detail scroll lag** — two per-frame `blur(18.dp)` RenderEffect passes over flat/gradient colors (visual no-ops, GPU-costly each scroll frame) replaced with static glows; removed the now-unused `androidx.compose.ui.draw.blur` import.

## Follow-up: adaptive reach into detail / settings / capture (same commit wave)
- **Settings hub** → `LazyVerticalGrid`: `GridCells.Adaptive(300.dp)` on wide windows (2-up cards), `Fixed(1)` on compact (identical to the old list); search, section labels and no-results span full width via `GridItemSpan(maxLineSpan)`.
- **Capture editor** → the six format chips render through a new `FormatChip` composable; wide windows use `FlowRow` (all six visible, wrapping) instead of the compact horizontal scroll.
- **Detail page** → new `detailBodyGutter()` helper widens the reading column's three body gutters (quick-fact column, FormatBody box, category label row) from 20dp to 28dp on wide windows; hero badge and paper-card internals untouched.
