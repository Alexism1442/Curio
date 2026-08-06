package com.curio.app.data

import android.content.Context
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import org.json.JSONArray
import org.json.JSONObject
import java.util.Calendar

/**
 * Curio's quests & levels system (v7.40).
 *
 * A light gamification layer that runs ALWAYS-ON (no settings toggle):
 *
 *  - **XP & levels** — every curious act earns XP (spin +2, explore +5,
 *    save +10, pin/quote +3, like +2…). XP is cumulative; the level curve
 *    climbs from "First Spark" to "Grand Curator".
 *  - **Journey** — a guided beginner quest sequence that walks the user
 *    through the whole app (spin → explore → save → settings → profile →
 *    pin → quote → daily → five saves → achievement). Each quest pays XP
 *    once when its target is reached; the UI always points at the next
 *    incomplete quest.
 *  - **Daily quests** — three quests picked per day from a rotating pool
 *    (seeded by the calendar day, so they stay stable all day and change
 *    at midnight). Progress resets daily; completing one auto-awards XP.
 *  - **Achievements** — eighteen one-time badges across spins, explores,
 *    saves, formats, quotes, pins, streaks, likes, the journey and level
 *    milestones. Unlocking one auto-awards XP.
 *
 * Persistence mirrors the other data objects: one SharedPreferences file
 * (`curio_quests`, listed in [CurioBackupManager] so it ships with the
 * user's backup) with JSON values, plus reactive Compose state seeded by
 * [seed] from MainActivity. All event hooks are fire-and-forget and
 * cheap — they may be called from any thread.
 */
object CurioQuests {

    private const val PREFS_NAME = "curio_quests"

    private const val KEY_XP = "xp"
    private const val KEY_LIFETIME = "lifetime"
    private const val KEY_FORMATS = "formats"
    private const val KEY_CATEGORIES = "categories"
    private const val KEY_JOURNEY_AWARDED = "journey_awarded"
    private const val KEY_DAILY_DATE = "daily_date"
    private const val KEY_DAILY_PROGRESS = "daily_progress"
    private const val KEY_DAILY_AWARDED = "daily_awarded"
    private const val KEY_ACHIEVEMENTS = "achievements"
    private const val KEY_BEST_STREAK = "best_streak"

    // ── Reactive state (seeded by [seed], kept in sync by every hook) ──
    var xpState by mutableIntStateOf(0)
        private set
    var lifetimeState by mutableStateOf(LifetimeCounters())
        private set
    var formatsState by mutableStateOf<Set<String>>(emptySet())
        private set
    var categoriesState by mutableStateOf<Set<String>>(emptySet())
        private set
    var journeyAwardedState by mutableStateOf<Set<String>>(emptySet())
        private set
    var dailyDateState by mutableIntStateOf(-1)
        private set
    var dailyProgressState by mutableStateOf<Map<String, Int>>(emptyMap())
        private set
    var dailyAwardedState by mutableStateOf<Set<String>>(emptySet())
        private set
    var achievementsState by mutableStateOf<Set<String>>(emptySet())
        private set
    var bestStreakState by mutableIntStateOf(0)
        private set

    /** One-time cumulative counters that drive journey + achievements. */
    data class LifetimeCounters(
        val spins: Int = 0,
        val explores: Int = 0,
        val saves: Int = 0,
        val quotes: Int = 0,
        val pins: Int = 0,
        val likes: Int = 0,
        val dislikes: Int = 0,
        val profileVisits: Int = 0,
        val settingsVisits: Int = 0,
        val dailyCompleted: Int = 0
    )

    // ── Level curve — cumulative XP needed to REACH each level ─────────
    // 1 at 0 XP; the curve climbs a little faster than saves-only, so a
    // new user sees Level 2 within a couple of actions and the high levels
    // stay a long-term goal.
    private val XP_THRESHOLDS = listOf(0, 15, 40, 80, 135, 205, 290, 390, 505, 635, 780, 940)

    fun levelForXp(xp: Int): Int {
        var level = 1
        XP_THRESHOLDS.forEachIndexed { index, threshold -> if (xp >= threshold) level = index + 1 }
        return level.coerceIn(1, XP_THRESHOLDS.size)
    }

    /** Fraction toward the next level (1f at max) + the next threshold's XP. */
    fun xpProgress(xp: Int): Pair<Float, Int> {
        val level = levelForXp(xp)
        val lastIndex = XP_THRESHOLDS.lastIndex
        if (level >= XP_THRESHOLDS.size) return 1f to XP_THRESHOLDS[lastIndex]
        val from = XP_THRESHOLDS[level - 1]
        val to = XP_THRESHOLDS[level]
        return ((xp - from).toFloat() / (to - from).coerceAtLeast(1)) to to
    }

    fun levelTitle(level: Int): String = when (level) {
        1 -> "First Spark"
        2 -> "Curious Newcomer"
        3 -> "Tuned Ear"
        4 -> "Pattern Spotter"
        5 -> "Comparator"
        6 -> "Synthesizer"
        7 -> "Curator"
        8 -> "Master Curator"
        9 -> "Lore Keeper"
        10 -> "Lane Walker"
        11 -> "Archive Scholar"
        else -> "Grand Curator"
    }

    /** The highest achievable level — UI uses this for the max-level state. */
    val maxLevel: Int get() = XP_THRESHOLDS.size

    // ── Journey quests — the guided beginner tour through the app ──────
    // Displayed in order; the "current" quest is the first incomplete one.
    // Progress is derived from the counters (no per-quest map), and XP is
    // awarded exactly once per quest when its target is reached.
    enum class JourneyKind { SPIN, EXPLORE, SAVE, SETTINGS, PROFILE, PIN, QUOTE, DAILY, ACHIEVEMENT }

    data class JourneyQuest(
        val id: String,
        val title: String,
        val description: String,
        val hint: String,
        val xpReward: Int,
        val kind: JourneyKind,
        val target: Int,
        /** Optional route to jump straight to the quest's screen. */
        val navRoute: String? = null
    )

    val Journey: List<JourneyQuest> = listOf(
        JourneyQuest(
            id = "take-the-wheel", title = "Spin the deck",
            description = "Shuffle a random deck and let curiosity pick the topic.",
            hint = "Tap the Shuffle button on the Spin tab.",
            xpReward = 10, kind = JourneyKind.SPIN, target = 1,
            navRoute = "spin"
        ),
        JourneyQuest(
            id = "first-look", title = "Explore a topic",
            description = "Open a topic and tap Explore to go find it in the world.",
            hint = "Spin, then tap the landed card and choose Explore.",
            xpReward = 15, kind = JourneyKind.EXPLORE, target = 1
        ),
        JourneyQuest(
            id = "first-keepsake", title = "Save your first capture",
            description = "Turn what you found into a note, sound bite, or mood board.",
            hint = "After exploring, write it down and save it to the Cabinet.",
            xpReward = 20, kind = JourneyKind.SAVE, target = 1
        ),
        JourneyQuest(
            id = "settle-in", title = "Look around Settings",
            description = "Appearance, reminders, recording, backup — make Curio yours.",
            hint = "Open Settings and browse the sections.",
            xpReward = 10, kind = JourneyKind.SETTINGS, target = 1,
            navRoute = "settings"
        ),
        JourneyQuest(
            id = "raise-the-flag", title = "Visit your profile",
            description = "See your stats, level, and lanes.",
            hint = "Open Profile from Home's avatar pill.",
            xpReward = 10, kind = JourneyKind.PROFILE, target = 1,
            navRoute = "profile"
        ),
        JourneyQuest(
            id = "pin-it", title = "Pin a topic for later",
            description = "Bookmark a topic you want to come back to.",
            hint = "On any topic reveal, tap the pin button.",
            xpReward = 10, kind = JourneyKind.PIN, target = 1
        ),
        JourneyQuest(
            id = "collect-a-thought", title = "Bookmark a quote",
            description = "Save a line from a capture to your Saved shelf.",
            hint = "Open a saved capture and tap the bookmark on a quote.",
            xpReward = 10, kind = JourneyKind.QUOTE, target = 1
        ),
        JourneyQuest(
            id = "daily-driver", title = "Complete a daily quest",
            description = "Finish one of today's three quests.",
            hint = "Check Today's quests below and knock one out.",
            xpReward = 15, kind = JourneyKind.DAILY, target = 1
        ),
        JourneyQuest(
            id = "five-keepsakes", title = "Save five captures",
            description = "Fill your Cabinet with keepsakes.",
            hint = "Keep writing things down as you explore.",
            xpReward = 25, kind = JourneyKind.SAVE, target = 5
        ),
        JourneyQuest(
            id = "badge-of-honor", title = "Unlock an achievement",
            description = "Earn a badge from the achievements shelf.",
            hint = "Every milestone below unlocks a badge.",
            xpReward = 25, kind = JourneyKind.ACHIEVEMENT, target = 1
        )
    )

    // ── Daily quests — three picked per day from a rotating pool ───────
    enum class DailyKind { SPIN, EXPLORE, SAVE, QUOTE, PIN, PROFILE, LIKE }

    data class DailyQuest(
        val id: String,
        val title: String,
        val xpReward: Int,
        val kind: DailyKind,
        val target: Int
    )

    private val DailyPool: List<DailyQuest> = listOf(
        DailyQuest("d-spin-1", "Spin the deck once", 10, DailyKind.SPIN, 1),
        DailyQuest("d-spin-3", "Spin the deck 3 times", 15, DailyKind.SPIN, 3),
        DailyQuest("d-explore-1", "Explore a topic", 15, DailyKind.EXPLORE, 1),
        DailyQuest("d-save-1", "Save a capture", 15, DailyKind.SAVE, 1),
        DailyQuest("d-quote-1", "Bookmark a quote", 10, DailyKind.QUOTE, 1),
        DailyQuest("d-pin-1", "Pin a topic for later", 10, DailyKind.PIN, 1),
        DailyQuest("d-profile-1", "Visit your profile", 10, DailyKind.PROFILE, 1),
        DailyQuest("d-like-1", "Like a topic", 10, DailyKind.LIKE, 1)
    )

    private const val DAILY_COUNT = 3

    /** The three quests live for [epochDay] — stable all day, new at midnight. */
    fun dailyQuestsFor(epochDay: Long): List<DailyQuest> {
        val base = (epochDay % DailyPool.size).toInt().let { if (it < 0) it + DailyPool.size else it }
        return (0 until DAILY_COUNT).map { i -> DailyPool[(base + i * 2) % DailyPool.size] }
    }

    // ── Achievements — one-time badges with XP payouts ─────────────────
    enum class AchievementKind {
        SPIN, EXPLORE, LANES, SAVE, FORMATS, QUOTE, PIN, STREAK, LIKE, JOURNEY, XP
    }

    data class Achievement(
        val id: String,
        val glyph: String,
        val title: String,
        val description: String,
        val xpReward: Int,
        val kind: AchievementKind,
        val target: Int
    )

    val Achievements: List<Achievement> = listOf(
        Achievement("spin-1", "casino", "First Spin", "Spin the deck once", 10, AchievementKind.SPIN, 1),
        Achievement("spin-25", "casino", "Deck Regular", "Spin 25 times", 15, AchievementKind.SPIN, 25),
        Achievement("spin-100", "casino", "Deck Master", "Spin 100 times", 25, AchievementKind.SPIN, 100),
        Achievement("explore-1", "explore", "First Discovery", "Explore your first topic", 10, AchievementKind.EXPLORE, 1),
        Achievement("explore-25", "explore", "Globe Trotter", "Explore 25 topics", 20, AchievementKind.EXPLORE, 25),
        Achievement("lanes-all", "palette", "All Lanes", "Explore in every lane", 30, AchievementKind.LANES, CurioCategories.visible.size),
        Achievement("save-1", "inventory_2", "First Keepsake", "Save your first capture", 10, AchievementKind.SAVE, 1),
        Achievement("save-25", "inventory_2", "Notebook Keeper", "Save 25 captures", 20, AchievementKind.SAVE, 25),
        Achievement("save-100", "inventory_2", "Archivist", "Save 100 captures", 35, AchievementKind.SAVE, 100),
        Achievement("formats-all", "auto_awesome", "Every Format", "Save one capture in every format", 30, AchievementKind.FORMATS, CaptureFormat.entries.size),
        Achievement("quote-5", "format_quote", "Quote Collector", "Bookmark 5 quotes", 15, AchievementKind.QUOTE, 5),
        Achievement("pin-5", "bookmark", "Pin Cushion", "Pin 5 topics", 15, AchievementKind.PIN, 5),
        Achievement("streak-3", "local_fire_department", "Spark Streak", "Keep a 3-day streak", 15, AchievementKind.STREAK, 3),
        Achievement("streak-7", "local_fire_department", "Week of Wonder", "Keep a 7-day streak", 25, AchievementKind.STREAK, 7),
        Achievement("streak-30", "local_fire_department", "Month of Mystery", "Keep a 30-day streak", 40, AchievementKind.STREAK, 30),
        Achievement("like-10", "thumb_up", "Curator's Taste", "Like 10 topics", 20, AchievementKind.LIKE, 10),
        Achievement("journey-done", "flag", "Journey Complete", "Finish every journey quest", 50, AchievementKind.JOURNEY, Journey.size),
        Achievement("xp-505", "workspace_premium", "Lore Keeper", "Reach Level 10", 25, AchievementKind.XP, 505)
    )

    // ── Seed / persistence ──────────────────────────────────────────────

    /** Load all persisted state (called once from MainActivity onCreate). */
    fun seed(context: Context) {
        val prefs = prefs(context)
        xpState = prefs.getInt(KEY_XP, 0)
        lifetimeState = readLifetime(prefs.getString(KEY_LIFETIME, null))
        formatsState = readStringSet(prefs.getString(KEY_FORMATS, null))
        categoriesState = readStringSet(prefs.getString(KEY_CATEGORIES, null))
        journeyAwardedState = readStringSet(prefs.getString(KEY_JOURNEY_AWARDED, null))
        dailyDateState = prefs.getInt(KEY_DAILY_DATE, -1)
        dailyProgressState = readIntMap(prefs.getString(KEY_DAILY_PROGRESS, null))
        dailyAwardedState = readStringSet(prefs.getString(KEY_DAILY_AWARDED, null))
        achievementsState = readStringSet(prefs.getString(KEY_ACHIEVEMENTS, null))
        bestStreakState = prefs.getInt(KEY_BEST_STREAK, 0)
        // A stale daily slot from a previous day rolls over on the next hook;
        // reconcile it now so reads are consistent.
        ensureDaily(context)
    }

    private fun prefs(context: Context) =
        context.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE)

    private fun readLifetime(raw: String?): LifetimeCounters {
        if (raw == null) return LifetimeCounters()
        return try {
            val o = JSONObject(raw)
            LifetimeCounters(
                spins = o.optInt("spins"),
                explores = o.optInt("explores"),
                saves = o.optInt("saves"),
                quotes = o.optInt("quotes"),
                pins = o.optInt("pins"),
                likes = o.optInt("likes"),
                dislikes = o.optInt("dislikes"),
                profileVisits = o.optInt("profileVisits"),
                settingsVisits = o.optInt("settingsVisits"),
                dailyCompleted = o.optInt("dailyCompleted")
            )
        } catch (_: Exception) {
            LifetimeCounters()
        }
    }

    private fun readStringSet(raw: String?): Set<String> {
        if (raw == null) return emptySet()
        return try {
            val arr = JSONArray(raw)
            (0 until arr.length()).map { arr.getString(it) }.toSet()
        } catch (_: Exception) {
            emptySet()
        }
    }

    private fun readIntMap(raw: String?): Map<String, Int> {
        if (raw == null) return emptyMap()
        return try {
            val o = JSONObject(raw)
            buildMap { o.keys().forEach { key -> put(key, o.optInt(key)) } }
        } catch (_: Exception) {
            emptyMap()
        }
    }

    private fun write(context: Context) {
        val counters = lifetimeState
        val lifetime = JSONObject()
            .put("spins", counters.spins)
            .put("explores", counters.explores)
            .put("saves", counters.saves)
            .put("quotes", counters.quotes)
            .put("pins", counters.pins)
            .put("likes", counters.likes)
            .put("dislikes", counters.dislikes)
            .put("profileVisits", counters.profileVisits)
            .put("settingsVisits", counters.settingsVisits)
            .put("dailyCompleted", counters.dailyCompleted)
        val dailyProgress = JSONObject()
        dailyProgressState.forEach { (k, v) -> dailyProgress.put(k, v) }
        prefs(context).edit()
            .putInt(KEY_XP, xpState)
            .putString(KEY_LIFETIME, lifetime.toString())
            .putString(KEY_FORMATS, JSONArray(formatsState.toList()).toString())
            .putString(KEY_CATEGORIES, JSONArray(categoriesState.toList()).toString())
            .putString(KEY_JOURNEY_AWARDED, JSONArray(journeyAwardedState.toList()).toString())
            .putInt(KEY_DAILY_DATE, dailyDateState)
            .putString(KEY_DAILY_PROGRESS, dailyProgress.toString())
            .putString(KEY_DAILY_AWARDED, JSONArray(dailyAwardedState.toList()).toString())
            .putString(KEY_ACHIEVEMENTS, JSONArray(achievementsState.toList()).toString())
            .putInt(KEY_BEST_STREAK, bestStreakState)
            .apply()
    }

    // ── Daily rollover — a new calendar day resets quest progress ──────
    private fun ensureDaily(context: Context) {
        val today = todayEpochDay().toInt()
        if (dailyDateState == today) return
        dailyDateState = today
        dailyProgressState = emptyMap()
        dailyAwardedState = emptySet()
        write(context)
    }

    /** Today's epoch day (midnight-normalized) — the daily reset key. */
    fun todayEpochDay(): Long {
        val cal = Calendar.getInstance()
        cal.set(Calendar.HOUR_OF_DAY, 0)
        cal.set(Calendar.MINUTE, 0)
        cal.set(Calendar.SECOND, 0)
        cal.set(Calendar.MILLISECOND, 0)
        return cal.timeInMillis / 86_400_000L
    }

    // ── XP ───────────────────────────────────────────────────────────────
    private fun addXp(context: Context, amount: Int) {
        xpState += amount
        write(context)
        checkAll(context)
    }

    // ── Event hooks — the app calls these where real actions happen ────

    /** A spin landed (SpinScreen). */
    fun onSpin(context: Context) {
        ensureDaily(context)
        lifetimeState = lifetimeState.copy(spins = lifetimeState.spins + 1)
        bumpDaily(context, DailyKind.SPIN)
        write(context)
        addXp(context, 2)
        checkJourney(context)
    }

    /** The user started exploring a topic (ExploreSessionStore.recordExplored). */
    fun onExplore(context: Context, categoryId: CategoryId) {
        ensureDaily(context)
        lifetimeState = lifetimeState.copy(explores = lifetimeState.explores + 1)
        categoriesState = categoriesState + categoryId.name
        bumpDaily(context, DailyKind.EXPLORE)
        write(context)
        addXp(context, 5)
        checkJourney(context)
    }

    /** A capture was saved (SaveCaptureScreen). [format] feeds the Every-Format achievement. */
    fun onSave(context: Context, format: CaptureFormat) {
        ensureDaily(context)
        lifetimeState = lifetimeState.copy(saves = lifetimeState.saves + 1)
        formatsState = formatsState + format.name
        bumpDaily(context, DailyKind.SAVE)
        write(context)
        addXp(context, 10)
        checkJourney(context)
    }

    /** A quote was bookmarked (AppPreferences.saveQuote). */
    fun onQuoteSaved(context: Context) {
        ensureDaily(context)
        lifetimeState = lifetimeState.copy(quotes = lifetimeState.quotes + 1)
        bumpDaily(context, DailyKind.QUOTE)
        write(context)
        addXp(context, 3)
        checkJourney(context)
    }

    /** A topic was pinned (AppPreferences.pinTopic). */
    fun onTopicPinned(context: Context) {
        ensureDaily(context)
        lifetimeState = lifetimeState.copy(pins = lifetimeState.pins + 1)
        bumpDaily(context, DailyKind.PIN)
        write(context)
        addXp(context, 3)
        checkJourney(context)
    }

    /** A topic was liked (AppPreferences.setTopicSentiment). */
    fun onTopicLiked(context: Context) {
        ensureDaily(context)
        lifetimeState = lifetimeState.copy(likes = lifetimeState.likes + 1)
        bumpDaily(context, DailyKind.LIKE)
        write(context)
        addXp(context, 2)
        checkJourney(context)
    }

    /** A topic was disliked (AppPreferences.setTopicSentiment). */
    fun onTopicDisliked(context: Context) {
        ensureDaily(context)
        lifetimeState = lifetimeState.copy(dislikes = lifetimeState.dislikes + 1)
        write(context)
        addXp(context, 1)
        checkJourney(context)
    }

    /** Profile opened (ProfileScreen) — counts for the journey + daily quests. */
    fun onProfileVisited(context: Context) {
        ensureDaily(context)
        lifetimeState = lifetimeState.copy(profileVisits = lifetimeState.profileVisits + 1)
        bumpDaily(context, DailyKind.PROFILE)
        write(context)
        checkJourney(context)
    }

    /** Settings opened (SettingsHubScreen) — counts for the journey quest. */
    fun onSettingsVisited(context: Context) {
        ensureDaily(context)
        lifetimeState = lifetimeState.copy(settingsVisits = lifetimeState.settingsVisits + 1)
        write(context)
        checkJourney(context)
    }

    /** Streak advanced (StreakTracker.recordActivity) — feeds streak badges. */
    fun onStreakRecorded(context: Context, streak: Int) {
        if (streak > bestStreakState) {
            bestStreakState = streak
            write(context)
        }
        checkAll(context)
    }

    // ── Daily quest completion (auto-awarded when a target is reached) ──
    private fun bumpDaily(context: Context, kind: DailyKind) {
        val today = todayEpochDay().toInt()
        if (dailyDateState != today) {
            dailyDateState = today
            dailyProgressState = emptyMap()
            dailyAwardedState = emptySet()
        }
        val key = kind.name
        val current = dailyProgressState[key] ?: 0
        dailyProgressState = dailyProgressState + (key to (current + 1))
        // Auto-award XP when a today quest hits its target for the first time.
        dailyQuestsFor(todayEpochDay())
            .filter { it.kind == kind && (dailyProgressState[it.kind.name] ?: 0) >= it.target }
            .forEach { quest ->
                if (quest.id !in dailyAwardedState) {
                    dailyAwardedState = dailyAwardedState + quest.id
                    dailyCompleted(context, quest.xpReward)
                }
            }
    }

    private fun dailyCompleted(context: Context, xpReward: Int) {
        lifetimeState = lifetimeState.copy(dailyCompleted = lifetimeState.dailyCompleted + 1)
        write(context)
        addXp(context, xpReward)
        checkJourney(context)
    }

    // ── Journey checks — award each quest's XP once when its target hits ──
    private fun checkJourney(context: Context) {
        val counters = lifetimeState
        var changed = false
        Journey.forEach { quest ->
            if (quest.id in journeyAwardedState) return@forEach
            if (journeyProgress(quest, counters) >= quest.target) {
                journeyAwardedState = journeyAwardedState + quest.id
                xpState += quest.xpReward
                changed = true
            }
        }
        if (changed) {
            write(context)
            checkAll(context)
        }
    }

    /** Live progress for a journey quest, derived from the counters. */
    fun journeyProgress(quest: JourneyQuest, counters: LifetimeCounters = lifetimeState): Int = when (quest.kind) {
        JourneyKind.SPIN -> counters.spins
        JourneyKind.EXPLORE -> counters.explores
        JourneyKind.SAVE -> counters.saves
        JourneyKind.SETTINGS -> counters.settingsVisits
        JourneyKind.PROFILE -> counters.profileVisits
        JourneyKind.PIN -> counters.pins
        JourneyKind.QUOTE -> counters.quotes
        JourneyKind.DAILY -> counters.dailyCompleted
        JourneyKind.ACHIEVEMENT -> achievementsState.size
    }

    /** True once every journey quest has been completed and paid out. */
    fun isJourneyComplete(): Boolean =
        Journey.all { it.id in journeyAwardedState }

    // ── Achievement checks — unlock + pay each badge exactly once ───────
    private fun checkAll(context: Context) {
        val newlyUnlocked = Achievements.filter { it.id !in achievementsState && achievementProgress(it) >= it.target }
        if (newlyUnlocked.isEmpty()) return
        newlyUnlocked.forEach {
            achievementsState = achievementsState + it.id
            // Every badge pays its own XP reward exactly once (the shelf's
            // "+N XP" labels are real, not decoration).
            xpState += it.xpReward
        }
        write(context)
        checkJourney(context)
    }

    private fun achievementProgress(achievement: Achievement): Int {
        val counters = lifetimeState
        return when (achievement.kind) {
            AchievementKind.SPIN -> counters.spins
            AchievementKind.EXPLORE -> counters.explores
            AchievementKind.LANES -> categoriesState.size
            AchievementKind.SAVE -> counters.saves
            AchievementKind.FORMATS -> formatsState.size
            AchievementKind.QUOTE -> counters.quotes
            AchievementKind.PIN -> counters.pins
            AchievementKind.STREAK -> bestStreakState
            AchievementKind.LIKE -> counters.likes
            AchievementKind.JOURNEY -> journeyAwardedState.size
            AchievementKind.XP -> xpState
        }
    }

    /** Live progress for an achievement badge (for the UI's mini-progress). */
    fun achievementProgressFor(achievement: Achievement): Int = achievementProgress(achievement)

    /** The next journey quest the UI should point the user at — null when done. */
    fun currentJourneyQuest(): JourneyQuest? =
        Journey.firstOrNull { journeyProgress(it) < it.target }
}
