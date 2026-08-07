# Prompt — Profile level and progress rearrangement

## Request
On Profile, replace the hero stats-grid Streak slot with Level. Show the level title (for example, "Synthesizer") in a pill beside the streak pill and Edit profile. Remove the standalone bottom level card, while keeping XP/progress with quests and achievements. The level title pill should show only the title because the numeric level is already visible in the hero stats grid. Do not push; commit locally only.

## Implementation
- Profile hero stats now show `Level · Saved · Lanes`; the numeric level remains in the Level stat.
- The hero action row now contains Edit profile, the displayed streak, and a title-only level pill (`CurioQuests.levelTitle(level)`). The action row uses `FlowRow` for narrow screens and uses the promo display streak consistently.
- Replaced the standalone Profile level card with a compact XP progress card.
- Added a compact achievements preview with unlocked count, progress, and up to three earned badge chips; the full achievement shelf remains on the Quests page.
- Existing Quests navigation, lanes, Settings, and Support behavior remain unchanged.

## Validation
- `git diff --check` passed.
- Comment-aware Kotlin structural checks passed for ProfileScreen.kt.
- Confirmed the title-only level pill and numeric level stat.
- Code review found no blockers.
- No Gradle build, compile, lint, or test commands were run because repository policy forbids them locally.
- No release-note update was made because this change is intentionally being held for the user's every-third-commit push cadence.
