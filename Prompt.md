# Prompt — approved security hardening

## Request
Implement security findings 1–3 from the Curio audit:

1. Prevent audio restore path traversal.
2. Prevent FieldMind JSON imports from reading arbitrary local filesystem paths while preserving supported `content://` media imports.
3. Restrict backup restore to the app's known user preference namespaces.

Also explain finding 9 (network/release hardening) for approval, but do not implement it yet.

## Completed
- Added shared storage path validation and canonical containment helpers.
- Hardened audio persistence and backup restore against unsafe capture IDs.
- Backup restore now clears source-device audio paths and only reassigns paths for bundled recordings restored into app-private storage.
- Backup restore rejects duplicate capture IDs and unknown SharedPreferences namespaces.
- FieldMind JSON media import now accepts `content://` sources and importer-temp files only; arbitrary local paths and unsupported schemes are rejected.
- Tightened audio deletion containment to avoid path-prefix boundary mistakes.

## Validation
- `git diff --check` passed.
- Static Kotlin brace/string balance checks passed for all changed Kotlin files.
- Code review found no blockers.
- No Gradle compile/build/lint/test command was run because the repository forbids those commands locally; CI remains the compilation source of truth.

## Pending approval — finding 9
Item 9 is defense-in-depth rather than a confirmed exploit in the current HTTPS-only code:

- Add `android:usesCleartextTraffic="false"` and an explicit Network Security Config to prevent future accidental HTTP traffic.
- Separately consider enabling R8/minification for production releases to make reverse engineering harder; this is not a substitute for keeping secrets out of the APK and may require keep-rule/CI validation.

Do not implement item 9 until the user approves its scope.
