# Prompt.md — Current Request Log

## Request (2026-08-07, 10th): Overlay permission — stop re-asking + Settings toggle — DONE (pushed)

**User request:** "for the overlay permission dont ask it again when the user says no also add a toggle in settings to give the permission."

### Changes
- **`data/AppPreferences.kt`** — new persisted `overlay_ask_declined` flag (`isOverlayAskDeclined` / `setOverlayAskDeclined`, reactive `overlayAskDeclinedState`, seeded in `initThemeMode`). Once the user declines "Display over other apps", all AUTOMATIC prompts are suppressed until they explicitly use the Settings toggle (which always opens the system page and clears the flag).
- **`features/reveal/TopicRevealScreen.kt`** — the explore-start bubble prompt no longer fires when the permission was declined (explore proceeds without the bubble). "Not now" / dialog-dismiss records the decline; returning from system settings WITHOUT granting records it too; a fresh grant clears it.
- **`features/settings/SettingsSectionScreen.kt`** (Notifications) — new **"Display over other apps" permission toggle** showing the live grant state; toggling opens the system special-access page (grant OR revoke) and clears the declined flag; returning without granting records the decline. The existing "Floating explore bubble" toggle now clears the declined flag when it opens the system page (explicit intent) and relies on the ON_RESUME observer (not the premature result callback) for the grant/decline decision. Dialog text updated to tell the user it won't ask again until they enable it in Settings.
- **`features/onboarding/OnboardingScreen.kt`** — returning from the overlay settings page without granting during setup records the decline; a grant clears it.

### Status
- Statically validated (no Gradle in this env): all references consistent, `git diff --check` clean, code review passed.
- Committed and **pushed** (branch in sync with origin/main after the `bf932c0` CI-fix push).
