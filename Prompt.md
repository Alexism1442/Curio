# Prompt.md — Current Request Log

## Request (2026-08-07, 8th): Tablet / landscape / desktop adaptive-layout polish — DONE (committed, NOT pushed)

**User request:** "the landscape layout and tablet layout still needs fixing — many things are not properly connected and have huge gaps etc. so properly fix them and they should properly adjust in desktop and tablets with a beautiful layout — choose one on your own, you should not ask me about anything. And it should not affect the current layout." (Design decisions were mine; all changes gated on `isWide` so the phone/portrait layout is untouched.)

### Design decision
One **continuous full-bleed watermark collage** fills the tablet/desktop gutters behind the centered content column (the NavHost renders it once), and every screen's content caps at a comfortable **640dp** column inside the 720dp shell so rows/cards never stretch into disconnected, gap-filled plates.

### Changes
- **`ui/adaptive/CurioAdaptiveLayout.kt`** — added `WideContentMaxWidth = 640.dp` and `@Composable wideContentEdgePadding()` (40dp on wide, 16dp on phone) for LazyColumn contentPadding capping.
- **`navigation/CurioNavHost.kt`** — on wide only, a single `CurioWatermarkBackdrop` (wildcard, alphaScale 0.55) renders full-bleed behind the 720dp `SharedTransitionLayout` column (gutter collage).
- **17 feature screens** — their own `CurioWatermarkBackdrop` is now wrapped in `if (!windowWidthSizeClass().isWide)` so there is ONE collage, not a double: Home, Spin, Cabinet, TopicReveal, Recent, Profile, SettingsHub, SettingsSection, BackupTools, Experiments, Onboarding, ManageCategories, TopicDatabase, Quests, Support, PromoMode, EntryDetail.
- **12 list screens capped to the 640dp column on wide** via `contentPadding start/end = wideContentEdgePadding()`: SettingsHub, SettingsSection, BackupTools, Experiments, ManageCategories, TopicDatabase, Support, PromoMode, Quests, TopicHistory, Recent, + Profile's 4 settings-card rows (hero left full-bleed).
- **Home** — 4 sections capped with `.widthIn(max = if (isWide) WideContentMaxWidth else Dp.Infinity).align(CenterHorizontally)`.
- **Deliberate scope note:** the TopicReveal content column was NOT capped — it's the shared-element morph target, and changing its width on wide would alter the reveal hero bounds mid-morph. The reveal stack is already a cohesive centered column.

### Status
- Statically validated (no Gradle in this env per AGENTS.md): all 17 backdrops gated 1:1, all imports used (TopicHistory trims to `wideContentEdgePadding` only), Home sections' `.align()` in Column scopes, `git diff --check` clean, code review passed.
- Committed locally. **Not pushed** — branch is ahead of origin/main by `cc26e15` (reveal morph), `e9f46de` (README), and this commit, all awaiting the user's go-ahead to push.
