package com.curio.app.data

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue

/**
 * Curio's quest guided tour (v8.1) — a small, tap-along walkthrough that
 * auto-navigates through the app's screens so a new user sees where
 * everything lives. Offered ONCE from the Quests page when the user taps the
 * first quest ("First Spin") and accepts the one-time prompt (v8.2) — it is
 * never auto-shown from other screens.
 *
 * Presentation is an IN-APP OVERLAY (not a system Toast, not a dialog): a
 * compact floating pill that MOVES WITH THE SCREEN (v8.3) — bottom for the
 * tab screens, below the hero on the settings-family screens, centered on
 * the final step — with a pointer arrow toward the content it describes, a
 * progress-dot indicator and a Next button. Every tap advances one step and
 * auto-navigates to that step's screen. Some steps WAIT for the real action
 * (the Spin step advances the moment the user actually spins —
 * [CurioQuests.onSpin] reports it via [onWait]), so the walkthrough hands
 * over to the user mid-flow.
 *
 * Routes use the same raw names as [QuestStage.navRoute] ("home", "spin",
 * "cabinet", "profile", "quests", "settings"); the NavHost maps them onto
 * real navigation (tabs via navigateToTab, the rest pushed).
 */
object QuestGuide {

    /** The real-world event a step can wait for before auto-advancing. */
    enum class Wait { SPIN, EXPLORE, SAVE, PROFILE, SETTINGS }

    /** Where the overlay floats on the current screen (v8.3). */
    enum class Position {
        /** Bottom of the screen, pointer up at the content above. */
        BOTTOM,
        /** Just below the settings-family hero, pointer down. */
        TOP,
        /** Mid-screen with no pointer — the final step. */
        CENTER
    }

    data class Step(
        /** Raw route name — empty means "no navigation": the final step. */
        val route: String,
        val title: String,
        val message: String,
        val waitFor: Wait? = null,
        val position: Position = Position.BOTTOM
    )

    // ── Reactive state (mirrors CurioQuests' pattern) ──
    var active by mutableStateOf(false)
        private set
    var steps by mutableStateOf<List<Step>>(emptyList())
        private set
    var index by mutableIntStateOf(0)
        private set

    /** The step the tour is currently showing, or null when idle. */
    val current: Step? get() = steps.getOrNull(index)

    /** True on the final step — the overlay's button reads "Finish". */
    val isLast: Boolean get() = active && index >= steps.lastIndex

    /** The very first quest a new user sees — tapping it launches the tour. */
    val firstQuestId: String? get() = CurioQuests.allStages().firstOrNull()?.id

    /** Starts the full walkthrough from the first step. */
    fun start() {
        steps = buildTourSteps()
        index = 0
        active = true
    }

    /** Advances one step; the final step's Finish ends the tour. */
    fun next() {
        if (!active) return
        if (index >= steps.lastIndex) stop() else index += 1
    }

    /** Ends the tour (Finish button or the overlay's close X). */
    fun stop() {
        active = false
        steps = emptyList()
        index = 0
    }

    /** Event-driven advance — reported by the [CurioQuests] hooks. */
    fun onWait(wait: Wait) {
        if (!active) return
        val step = current ?: return
        if (step.waitFor == wait) next()
    }

    // v8.3 — one-line messages (the pill shows at most two lines) and a
    // per-step position so the pill never floats over the thing it explains.
    private fun buildTourSteps(): List<Step> = listOf(
        Step(
            "home", "Welcome to Curio",
            "Your daily quest, shuffle, and recent activity live here."
        ),
        Step(
            "spin", "Spin the deck",
            "Tap Spin to shuffle a topic — that's your first quest!",
            Wait.SPIN
        ),
        Step(
            "cabinet", "The Cabinet",
            "Every capture you save lands here."
        ),
        Step(
            "profile", "Your profile",
            "Streak, level, and explored lanes live here."
        ),
        Step(
            "quests", "Quests & levels",
            "Chains, badges, and fresh daily quests — right here.",
            position = Position.TOP
        ),
        Step(
            "settings", "Make it yours",
            "Appearance, reminders, and backup all live here.",
            position = Position.TOP
        ),
        Step(
            "", "You're all set",
            "Spin, explore, save — every curious act earns XP!",
            position = Position.CENTER
        )
    )
}
