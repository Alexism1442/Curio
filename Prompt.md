# Prompt.md — Current Request Log

## Request (2026-08-07, 13th): Mood-board pixelation on zoom — DONE (pushed)

**User request:** "the moodboard saved image still gets pixel crack on zoom make it clear so that the imported images and the after saving it doesnt gets pixeleted"

### Analysis
- `MoodBoardZoom.kt` decodes zoomed tiles at only **2048px** (`MoodBoardZoomDecodePx`) — the pinch can reach **8x**, so the zoomed bitmap was upscaled several times → visible "pixel crack".
- Every `Image` in the mood-board pipeline (zoom overlay, board tiles, editor, gallery, export) used the Compose **default `FilterQuality.Low`**, which leaves blocky pixels when a layout outgrows its decoded bitmap (most visible during the zoom glide and on big tiles).
- The export preloaded tile bitmaps at FULL original size with no cap — a 48MP photo could allocate a multi-hundred-MB bitmap per tile (OOM risk on a full board) while the output canvas never exceeds 4096px.
- Compose BOM is 2026.05.01 — `Image(filterQuality = …)` is fully supported.

### Changes
- **`ui/components/MoodBoardZoom.kt`** — `MoodBoardZoomDecodePx` 2048 → **4096** (supports the full 8x pinch at ~1:1, matches the export cap); `FilterQuality.High` on the zoom overlay's base + hi-res layers AND the board tile images.
- **`ui/components/MoodBoardExport.kt`** — preload `ImageRequest` now `.size(4096, 4096)` (memory-safe full-res; output never exceeds it); `FilterQuality.High` on exported tile images.
- **`features/capture/formats/GalleryWallFormat.kt`** — `FilterQuality.High` on the editor's tile images (pinched-bigger tiles stay clean).
- **`ui/components/AdaptiveImageGallery.kt`** — `FilterQuality.High` on the gallery grid tiles (smooth during the zoom overlay glide).
- **`fastlane/.../20260810.txt`** — changelog bullet.
- **`Prompt.md`** — this log.

### Validation
No Gradle in this env (per AGENTS.md) — static checks: brace balance, unused-import grep, `git diff --check`, code review. Commit + push pending.

### Follow-ups
- None.
