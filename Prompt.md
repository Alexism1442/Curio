# Prompt.md — Current Request Log

## Request (2026-08-07, 15th): Quest guide indicators + claim buttons + Go buttons — DONE (pushed)

**User request:** "improve the turtorial with proper indicators etc and the texts gets short too and also move the according to the screen etc also add claim button per quest box and also add go button next to a quest which will guide the user." (plus a CI compile fix pasted mid-work: `filterQuality` on `Image(painter = …)`)

### Analysis
- **CI compile error first:** foundation 1.4+ REMOVED the `filterQuality` parameter from the `Image(painter: Painter, …)` overload (it only remains on `Image(bitmap: ImageBitmap, …)`). The v8.2 mood-board crispness commit added `filterQuality = FilterQuality.High` to 5 painter-overload call sites (MoodBoardZoom ×3, GalleryWallFormat, AdaptiveImageGallery) → CI failed. MoodBoardExport was fine (bitmap overload).
- **Tour overlay:** was a bottom-centered pill with a numeric footer, long multi-clause messages, no pointer, no position variation — the user wanted proper indicators, short copy, and screen-relative placement.
- **Daily quests:** XP was auto-awarded inside `bumpDaily` the instant a target was hit — no reward moment, no claim tap.
- **Go buttons:** only the globally current quest row had a Go chip; other chains' next quests and in-progress dailies had no jump affordance.

### Fix
1. **`ui/components/MoodBoardZoom.kt`** — `moodBoardPainter` now sets `.filterQuality(FilterQuality.High)` on the Coil `ImageRequest` (import `coil.request.filterQuality`); the 3 painter-overload `filterQuality` params removed. **`features/capture/formats/GalleryWallFormat.kt`** + **`ui/components/AdaptiveImageGallery.kt`** — same: request-level filtering, painter-overload params removed (gallery builds its own `ImageRequest` with `.filterQuality(High)`). Pushed first as `ef1052e` to unblock CI.
2. **`data/QuestGuide.kt`** — every step's message shortened to one line; new `Position` enum (`BOTTOM` / `TOP` / `CENTER`) per step: Quests & Settings → TOP (below the hero), final step → CENTER, rest BOTTOM.
3. **`ui/components/QuestGuideToast.kt`** — full redesign: `GuidePointer.UP/DOWN` arrow in a small coral circle floats above/below the pill aimed at the content; progress-dot row under the message (current step filled); `footer` text replaced by `stepIndex`/`stepCount`.
4. **`navigation/CurioNavHost.kt`** — overlay alignment now follows the step (`BottomCenter` / `TopCenter` / `Center`); TOP steps pad down by `SettingsHeroTotalHeight + 8.dp` so the pill sits under the Quests/Settings hero; pointer derived from position; imports `GuidePointer` + `SettingsHeroTotalHeight`.
5. **`data/CurioQuests.kt`** — `bumpDaily` no longer grants XP (progress only); new `claimDaily(context, questId)` marks the quest awarded, bumps `dailyCompleted`, persists and grants XP.
6. **`features/quests/QuestsScreen.kt`** — DailyCard takes `onClaim`/`onGo`; complete-but-unclaimed dailies show a solid **"Claim +XP"** pill; in-progress dailies show "+XP" + a **Go** chip via new `dailyGoRoute(kind)` (SPIN→spin, EXPLORE→spin, PROFILE→profile, rest null); ChainCard computes `nextIndex` and ChainStageRow shows a Go/Start chip on every chain's NEXT actionable stage (solid coral "Go" for the current quest, muted "Start" otherwise).

### Validation
No Gradle in this env (per AGENTS.md) — static checks: brace balance, no leftover `footer =`/painter-overload `filterQuality`, claim/Go/Position wiring greps, `git diff --check`, code review. Changelog + Prompt.md updated. CI on the pushed HEAD is the compile gate.

### Follow-ups
- None.
