#!/usr/bin/env python3
"""Fix four factual slips in the batch 10/11 film entries.

Reviewer-flagged fixes (applied to films.json AND the reusable scripts so a
future re-run can't reintroduce them):
1. Marcel the Shell — voiced by Jenny Slate, not director Dean Fleischer Camp.
2. Zero Dark Thirty — the Abbottabad raid is ~20 minutes, not 40.
3. Nightcrawler — Gyllenhaal dropped ~30 lbs, not 20.
4. Godzilla Minus One — 1954 to 2023 is ~69 years, not 70.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FIXES = [
    (
        "Marcel (voiced by director Dean Fleischer Camp, who created the viral shorts with Jenny Slate) lives in an Airbnb and narrates his tiny life: the tennis ball, the lint, the search for his family.",
        "Marcel (voiced by Jenny Slate, in a feature spun off from the viral shorts she created with director Dean Fleischer Camp) lives in an Airbnb and narrates his tiny life: the tennis ball, the lint, the search for his family.",
    ),
    (
        "The film's final act, the Abbottabad raid, is a 40-minute, night-vision reconstruction that plays like a real-time documentary, and the film's opening (the 9/11 audio-only black screen) is the most audacious cold open of the decade.",
        "The film's final act, the Abbottabad raid, is a twenty-minute, night-vision reconstruction that plays like a real-time documentary, and the film's opening (the 9/11 audio-only black screen) is the most audacious cold open of the decade.",
    ),
    (
        "Jake Gyllenhaal (who dropped 20 pounds and studied real crime-scene photographers)",
        "Jake Gyllenhaal (who dropped 30 pounds and studied real crime-scene photographers)",
    ),
    (
        "70 years after the original, this Japanese entry took Best Visual Effects with a team of just 35 artists",
        "nearly 70 years after the original, this Japanese entry took Best Visual Effects with a team of just 35 artists",
    ),
]

TARGETS = [
    ROOT / "app/src/main/assets/topics/films.json",
    ROOT / "scripts/batch_films_add_10.py",
    ROOT / "scripts/batch_films_add_11.py",
]


def main() -> int:
    total = 0
    for path in TARGETS:
        text = path.read_text(encoding="utf-8")
        for old, new in FIXES:
            count = text.count(old)
            if count:
                text = text.replace(old, new)
                total += count
                print(f"  fixed {count}x in {path.name}: {old[:60]}...")
        path.write_text(text, encoding="utf-8")
    print(f"total replacements: {total}")
    return 0 if total == 4 else 1


if __name__ == "__main__":
    raise SystemExit(main())
