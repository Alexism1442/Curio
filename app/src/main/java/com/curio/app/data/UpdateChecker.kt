package com.curio.app.data

import kotlinx.coroutines.CancellationException
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import org.json.JSONArray
import org.json.JSONObject
import java.net.HttpURLConnection
import java.net.URL

/**
 * The latest published Curio release (or newest git tag), as reported by the
 * GitHub API.
 */
data class UpdateInfo(
    val tagName: String,
    /** Page to open when an update is available (release page / tag page). */
    val htmlUrl: String,
    /** Release notes body — present only when a real release exists. */
    val releaseNotes: String? = null
)

/**
 * Checks the latest published Curio release on GitHub.
 *
 * Releases are published from git tags (`v*` — see `.github/workflows/release.yml`),
 * so the latest release's tag (e.g. "v1.0.1") is the authoritative build tag
 * for the newest version. The installed version is `BuildConfig.VERSION_NAME`
 * (e.g. "1.0.0") — exactly the tag the APK was built from, minus the leading
 * "v" — so the comparison is a straight version-component compare.
 *
 * The latest-release endpoint 404s until the FIRST release is actually
 * published, so [fetchLatestRelease] falls back to the newest git tag — the
 * checker works from day one instead of showing a failure state.
 *
 * No new dependencies: a plain [HttpURLConnection] GET against the public
 * GitHub API (no auth needed; the unauthenticated rate limit is plenty for a
 * manual, user-initiated check).
 */
object UpdateChecker {
    private const val REPO = "firefly-sylestia/Curio"
    private const val LATEST_RELEASE_URL = "https://api.github.com/repos/$REPO/releases/latest"
    private const val TAGS_URL = "https://api.github.com/repos/$REPO/tags"

    /**
     * Fetches the latest release (or tag). Returns null on ANY failure —
     * offline, HTTP error, or a parse problem — so the UI can show a neutral
     * "couldn't check" state instead of crashing.
     */
    suspend fun fetchLatestRelease(): UpdateInfo? = withContext(Dispatchers.IO) {
        // try/catch (not runCatching) so coroutine CancellationException is
        // rethrown — a cancelled check (user left the screen) must propagate
        // instead of being swallowed into a misleading "failed" state.
        try {
            // 1) Latest published release — carries release notes + release page.
            val release = fetch(LATEST_RELEASE_URL) { raw ->
                val obj = JSONObject(raw)
                UpdateInfo(
                    tagName = obj.optString("tag_name"),
                    htmlUrl = obj.optString("html_url"),
                    releaseNotes = obj.optString("body").takeIf { it.isNotBlank() }
                )
            }
            if (release != null && release.tagName.isNotBlank()) return@withContext release
            // 2) No release published yet — fall back to the newest git tag
            //    (the authoritative build tag), so the check reports "up to
            //    date" once a matching tag exists instead of failing.
            fetch(TAGS_URL) { raw ->
                val arr = JSONArray(raw)
                if (arr.length() == 0) return@fetch null
                val tag = arr.optJSONObject(0)?.optString("name").orEmpty()
                if (tag.isBlank()) null
                else UpdateInfo(
                    tagName = tag,
                    htmlUrl = "https://github.com/$REPO/releases/tag/$tag",
                    releaseNotes = null
                )
            }
        } catch (e: CancellationException) {
            throw e
        } catch (e: Exception) {
            null
        }
    }

    /** True when [latestTag] ("v1.0.1") is newer than [currentVersion] ("1.0.0"). */
    fun isNewer(latestTag: String, currentVersion: String): Boolean {
        val a = latestTag.removePrefix("v").trim().split('.').mapNotNull { it.toIntOrNull() }
        val b = currentVersion.trim().split('.').mapNotNull { it.toIntOrNull() }
        // Unparseable versions fall back to a plain string inequality so a
        // differently-named tag still surfaces as "different".
        if (a.isEmpty() || b.isEmpty()) return latestTag != currentVersion
        val len = maxOf(a.size, b.size)
        for (i in 0 until len) {
            val x = a.getOrElse(i) { 0 }
            val y = b.getOrElse(i) { 0 }
            if (x != y) return x > y
        }
        return false
    }

    /** GETs [url] and parses the 200 body with [parse]; null on any non-200. */
    private fun fetch(url: String, parse: (String) -> UpdateInfo?): UpdateInfo? {
        val conn = URL(url).openConnection() as HttpURLConnection
        try {
            conn.connectTimeout = 8_000
            conn.readTimeout = 8_000
            conn.requestMethod = "GET"
            conn.setRequestProperty("Accept", "application/vnd.github+json")
            if (conn.responseCode != HttpURLConnection.HTTP_OK) return null
            val raw = conn.inputStream.bufferedReader().use { it.readText() }
            return parse(raw)
        } finally {
            conn.disconnect()
        }
    }
}
