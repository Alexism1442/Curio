package com.curio.app.data

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import org.json.JSONObject
import java.net.HttpURLConnection
import java.net.URL

/**
 * The latest published Curio release, as reported by the GitHub API.
 */
data class UpdateInfo(
    val tagName: String,
    val htmlUrl: String
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
 * No new dependencies: a plain [HttpURLConnection] GET against the public
 * GitHub API (no auth needed; the unauthenticated rate limit is plenty for a
 * manual, user-initiated check).
 */
object UpdateChecker {
    private const val LATEST_RELEASE_URL =
        "https://api.github.com/repos/firefly-sylestia/Curio/releases/latest"

    /**
     * Fetches the latest release. Returns null on ANY failure — offline,
     * HTTP error, 404 (no release published yet), or a parse problem — so the
     * UI can show a neutral "couldn't check" state instead of crashing.
     */
    suspend fun fetchLatestRelease(): UpdateInfo? = withContext(Dispatchers.IO) {
        // try/catch (not runCatching) so coroutine CancellationException is
        // rethrown — a cancelled check (user left the screen) must propagate
        // instead of being swallowed into a misleading "failed" state.
        try {
            val conn = URL(LATEST_RELEASE_URL).openConnection() as HttpURLConnection
            try {
                conn.connectTimeout = 8_000
                conn.readTimeout = 8_000
                conn.requestMethod = "GET"
                conn.setRequestProperty("Accept", "application/vnd.github+json")
                if (conn.responseCode != HttpURLConnection.HTTP_OK) return@withContext null
                val raw = conn.inputStream.bufferedReader().use { it.readText() }
                val obj = JSONObject(raw)
                UpdateInfo(
                    tagName = obj.optString("tag_name"),
                    htmlUrl = obj.optString("html_url")
                )
            } finally {
                conn.disconnect()
            }
        } catch (e: kotlinx.coroutines.CancellationException) {
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
}
