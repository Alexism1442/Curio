# Prompt.md — Current Request Log

## Request (2026-08-07, 19th): Restore the shuffle main-card morph — the glyph rides the card again — DONE (pushed)

**User request:** "why did u remove the morph animatio n of the main card bruh and place that placeholder behind evrything else and with adaptive color according to the theme and category etc also there is no need of that placeholder in cabinet detail screen" → clarified: "the shuffle main card morph animation"

### Analysis — root cause
- The v8.3 "hero watermark" fix pulled the 150dp category glyph OUT of the shared element on both sides, so the morph animates a bare gradient — the user read the empty gradient as a "placeholder" and missed the glyph riding the card as it expands.
- Why the glyph was removed in v8.3: inside the card-bounds shared element it scales non-uniformly (ticket 286×310 ⇄ hero ~392×260) → a stretched oval mid-morph.
- The Entry Detail route was ALSO in the bottom-bar reserve set (v8.2), leaving a bar-height placeholder on the cabinet detail screen — the user said it isn't needed there.

### Fix — a dedicated glyph shared element; detail route drops the reserve
- **`ui/adaptive/RevealSharedScopes.kt`** — new `RevealGlyphSharedElementKey = "reveal-glyph"`.
- **`features/spin/SpinScreen.kt` / `features/reveal/TopicRevealScreen.kt`** — the glyph now has its OWN shared element. It is the same 150dp on both sides (same CenterEnd + 6dp position, same ink@0.16 theme-adaptive tint), so its morph is a **pure translation**: it rides the expanding card with zero squash. The reveal-side late bloom (`HeroPillEntrance` 250ms) is gone — the glyph arrives WITH the card, so the morphing card reads as the real card (adaptive gradient + glyph), not a placeholder. The card face (gradient + rim-light) keeps its own "reveal-hero" element; text stays outside both elements.
- **`navigation/CurioNavHost.kt`** — `ENTRY_DETAIL` dropped from `reserveBarSpace`: no bottom-bar placeholder on the cabinet detail screen. The Reveal route keeps the reserve (the watermark-shift fix from v8.2 stays intact).

### Validation
No Gradle in this env (per AGENTS.md) — static checks: brace balance (RevealSharedScopes 3/3, SpinScreen 397/397, TopicReveal 202/202, NavHost 150/150), key wired on both sides (decl + import + `rememberSharedContentState` in each file), 2 `Modifier.sharedElement` sites per file (face + glyph), no leftover 250ms glyph bloom, reserve set = Reveal only, `git diff --check` clean. Code review ran. CI on the pushed HEAD is the compile gate.

### Follow-ups
- None.
