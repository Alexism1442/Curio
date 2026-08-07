# Prompt.md — Current Request Log

## Request (2026-08-07, 7th): README — design-identity reframe + stale-fact fixes — DONE (committed, NOT pushed)

**User request:** "update the readme and also change material design to material inspired custom design — not hand crafted but like scraped from the internet." Clarified via ask_user: **NOT a redesign** — this is README wording only. Reframe the design identity as a *Material-inspired custom design language* assembled from the established design language of the web (Material 3 foundation + editorial/tactile web aesthetic), not a hand-invented look. Also fix stale facts (selected option "Design + fix stale facts").

### Changes (README.md only)
- **Design Identity / Design & Privacy / Themes sections** — reframed from "Material 3 with Curio's warm-cream paper world" to "Material-inspired custom design language — not a hand-invented look, but one assembled from the established design language of the modern web" (Material 3 open design system as foundation + warm-cream paper world drawn from today's editorial app aesthetics).
- **Stale facts fixed** (verified against repo):
  - Topics: 2,500+/2,312+ → **3,133** (validator-summed across the 11 JSON files: 3133).
  - Level system (1–9) → **50-level quest system** with XP ranks, titles, quest chains.
  - Kotlin 1.9+ → **Kotlin 2.3+** (actual 2.3.21); Gradle 8.0+ → **Gradle 9.4+** (wrapper 9.4.1); removed "or Canary".
  - Target OS: "Android 15+ (API 37)" → **Android 17 (API 37)**.
- Also noticed: `docs/v1.0-launch.md` + `app/AGENTS.md` still carry the old "Material 3 with Curio's warm-cream" framing — left untouched (out of scope; flag if wanted).

### Status
- Committed locally. **Not pushed** (branch is ahead of origin/main by the reveal-morph commit `cc26e15` too — awaiting user's go-ahead to push).
