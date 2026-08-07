# Prompt.md — Current Request Log

## Request (2026-08-07, 11th): Music topics open YouTube — DONE (pushed)

**User request:** "for albums it still says we will open google search soo fix tht and also opeen youtube for music artists too."

### Analysis
- `data/ExploreSearch.kt` `buildExploreSearchUrl` already opened YouTube for **albums** (`CategoryId.ALBUMS`); **artists** still built a Google URL.
- The only user-visible "Google search" copy was the hardcoded explore-confirmation dialog in `features/reveal/TopicRevealScreen.kt` (line ~901): "We'll open a Google search to get you started." — wrong for music. Remaining mentions are code comments (reveal screen ×2, HomeScreen resume handler, ExploreSearch KDoc).
- Artist topics carry `subtype "Artist"` (354/354 entries) — the existing query builder (name + year + subtype) works cleanly for YouTube, no artist extraction needed (the topic IS the artist).

### Changes
- **`data/ExploreSearch.kt`** — YouTube results page now for `ALBUMS || ARTISTS` (Google for everything else); KDoc updated.
- **`features/reveal/TopicRevealScreen.kt`** — new `exploreOpenCopy(cat)` helper (albums/artists → "We'll open YouTube to get you started.", else Google); dialog text now uses it; the two code comments corrected.
- **`features/home/HomeScreen.kt`** — resume-handler comment corrected (comment-only, rides along with the behavior change).
- **`fastlane/.../20260810.txt`** — changelog bullet added.
- **`Prompt.md`** — this log.

### Validation
No Gradle in this env (per AGENTS.md) — static checks: no other user-visible "Google search" copy remains (only the intentional Google-branch strings), `git diff --check` clean, brace balance re-checked in the reveal screen. Code review + push pending.

### Follow-ups
- None. Reminder/notification copy had no Google references.
