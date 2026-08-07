# Prompt — GitHub Actions lint artifact warning

## Request
CI reports the Node 20 deprecation notice while running `actions/upload-artifact@v5`, followed by:

`Warning: No files were found with the provided path: app/build/reports/lint-results*.*`

## Findings
- The Node message is an informational runtime transition from GitHub-hosted runners. The workflow must not set `ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true`, because that opts into the deprecated Node 20 runtime.
- `actions/upload-artifact@v5` remains the configured modern artifact action; no runtime downgrade is needed.
- Lint reports are optional diagnostics when the Gradle step fails before generating them. The Gradle command remains the authoritative CI failure signal.

## Completed
- Changed the lint-report artifact upload to `if-no-files-found: ignore`, removing the misleading warning when no report exists while preserving Gradle failure behavior.
- Updated `.github/AGENTS.md` to document that lint reports are best-effort and may be absent after an early Gradle failure.
- Ran workflow/static validation only; no local Gradle commands are allowed by repository policy.
