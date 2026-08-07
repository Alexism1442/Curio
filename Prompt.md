# Prompt — onboarding intro spacing and scale refinement

## Request
Move the intro Skip/Next controls farther down, make the buttons slightly larger, and increase the Curio wordmark size.

## Implementation
- Use the existing `displaySmall` typography for the Curio wordmark, increasing it from the prior 32sp headline treatment to the established 36sp display treatment.
- Increase the gap before the controls from 20dp to 26dp.
- Increase bottom-row vertical padding from 24dp to 26dp.
- Give Skip and Next roomier content padding while preserving their existing click behavior and navigation flow.
- Keep the 70%-height torn hero, tagline, pager, dots, and permission/theme steps unchanged.

## Validation plan
- Run non-Gradle static Kotlin structure and whitespace checks.
- Review the visual/layout diff for fit and accessibility touch-target sizing.
- Do not run Gradle build, compile, lint, or test commands locally per repository policy.
