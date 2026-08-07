package com.curio.app.data

import android.net.Uri

/**
 * Builds the search URL opened when the user taps "Explore now".
 *
 * Music — albums AND artists (everything in the ALBUMS and ARTISTS
 * categories) — opens a YouTube results page so the user can listen
 * directly; every other category keeps the Google search.
 *
 * The query is the topic name plus contextual search hints so the first
 * result is actually the right thing:
 *  - A year is extracted from the topic name when it carries one (films are
 *    named "Citizen Kane (1941)"), otherwise from an era tag (e.g. "1960s").
 *  - For albums (whose topic name is the album), the artist is pulled from
 *    the teaser — album teasers almost always name the artist ("1967 Beatles,
 *    recorded ..." → "Beatles"). Best-effort: no artist found → the plain
 *    album name still searches fine.
 *  - The subtype is appended as a disambiguator ("album", "film", ...).
 */
/** True for music categories — album and artist explores open a YouTube
 *  results page so the user can listen directly (everything else keeps the
 *  Google search). Single source of truth for the explore URL AND the
 *  explore-dialog copy (see TopicRevealScreen.exploreOpenCopy). */
fun categoryOpensYouTube(categoryId: CategoryId): Boolean =
    categoryId == CategoryId.ALBUMS || categoryId == CategoryId.ARTISTS

fun buildExploreSearchUrl(topic: CurioTopic): String {
    val parts = mutableListOf<String>()
    if (topic.subtype.equals("Album", ignoreCase = true)) {
        extractArtist(topic.teaser)?.let { parts += it }
    }
    parts += topic.name
    extractYear(topic)?.let { parts += it }
    parts += topic.subtype
    val query = parts.joinToString(" ").trim()
    return if (categoryOpensYouTube(topic.categoryId)) {
        "https://www.youtube.com/results?search_query=" + Uri.encode(query)
    } else {
        "https://www.google.com/search?q=" + Uri.encode(query)
    }
}

/** Year from the topic name ("Citizen Kane (1941)" → "1941"), else era tag. */
private fun extractYear(topic: CurioTopic): String? {
    val inName = Regex("\\b(18|19|20)\\d{2}\\b").find(topic.name)?.value
    if (inName != null) return inName
    val eraTag = topic.tags.firstOrNull { it.matches(Regex("\\b(18|19|20)\\d{2}s\\b")) }
    return eraTag
}

/**
 * Best-effort artist extraction from an album teaser. Album teasers name the
 * artist next to the release year ("1967 Beatles, recorded..." or "Pink Floyd
 * 1973 — ..."). Grab the word cluster that contains the year and take the
 * capitalized neighbor phrase that isn't the year itself.
 */
private fun extractArtist(teaser: String): String? {
    // Pattern 1: "<Year> <Artist>, ..." (e.g. "1967 Beatles, recorded in 6 months")
    Regex("\\b(18|19|20)\\d{2}\\s+([A-Z][\\w'.-]*(?:\\s+[A-Z][\\w'.-]*){0,2})").find(teaser)?.let { m ->
        val artist = m.groupValues[2].trim()
        // Skip when the capture is mostly a name-like sentence fragment.
        if (artist.isNotBlank() && artist.split(' ').size <= 3) return artist
    }
    // Pattern 2: "<Artist> <Year> —" (e.g. "Pink Floyd 1973 — spent 937 weeks")
    Regex("([A-Z][\\w'.-]*(?:\\s+[A-Z][\\w'.-]*){0,2})\\s+\\b(18|19|20)\\d{2}\\b").find(teaser)?.let { m ->
        val artist = m.groupValues[1].trim()
        if (artist.isNotBlank() && artist.split(' ').size <= 3) return artist
    }
    return null
}
