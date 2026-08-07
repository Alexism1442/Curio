# Prompt — CI Kotlin compilation fix

## Request
CI failed on the release/debug Kotlin compilation after the dark hero-card and Spin reveal handoff changes.

## CI diagnosis
- `EntryDetailScreen.kt:419` uses `CurioColors.CreamWhite`, but `CurioColors` was not imported. The unresolved receiver caused the follow-on `Modifier.background` type-inference errors at lines 414 and 419.
- `SpinScreen.kt:809-810` calls `openingScope.launch { delay(...) }`. `rememberCoroutineScope()` and `delay` were already present, but the `kotlinx.coroutines.launch` extension import was missing, producing both `Unresolved reference 'launch'` and the suspend-call error.
- No runtime logic or UI behavior needed changing.

## Plan
1. Add the missing `CurioColors` import to EntryDetailScreen.
2. Add the missing `kotlinx.coroutines.launch` import to SpinScreen.
3. Run static validation and inspect the final diff. Local Gradle/build/lint/test commands remain forbidden by repository policy.
4. Update this log, commit, and push the CI fix.

## Implementation
- Added `import com.curio.app.ui.theme.CurioColors`.
- Added `import kotlinx.coroutines.launch`.

## Validation
- Pending final static checks and CI verification after push.
