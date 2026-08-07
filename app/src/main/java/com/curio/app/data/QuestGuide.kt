package com.curio.app.data

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue

/**
 * Curio's quest guided tour (v8.1) — a small, tap-along walkthrough that
 * auto-navigates through the app's screens so a new user sees where
 * everything lives. Started by tapping the FIRST quest ("First Spin") on the
 * Quests page, or the guide overlay's Go button while that quest is current.
 *
 * Presentation is an IN-APP OVERLAY (not a system Toast, not a dialog): a
 * compact floating pill at the bottom of the screen with a title, a one-line
 * message, a step counter and a Next button. Every tap advances one step and
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

    data class Step(
        /** Raw route name — empty means "no navigation": the final step. */
        val route: String,
        val title: String,
        val message: String,
        val waitFor: Wait? = null
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

    private fun buildTourSteps(): List<Step> = listOf(
        Step(
            "home", "Welcome to Curio",
            "This is Home — your Today's Quest, the shuffle button, and your recent activity all live here."
        ),
        Step(
            "spin", "Spin the deck",
            "Tap the big Spin button to shuffle a random topic. That's your first quest — give it a spin!",
            Wait.SPIN
        ),
        Step(
            "cabinet", "The Cabinet",
            "Every capture you save lands here — your Keepsakes chain grows as you fill it."
        ),
        Step(
            "profile", "Your profile",
            "Your streak, level, and the lanes you've explored all live on your profile."
        ),
        Step(
            "quests", "Quests & levels",
            "Back to Quests — chains, badges, and three fresh daily quests every day."
        ),
        Step(
            "settings", "Make it yours",
            "Appearance, reminders, recording quality, and backup — every setting lives here."
        ),
        Step(
            "", "You're all set",
            "Every curious act earns XP: spin, explore, save, pin, and like. Enjoy the tour!"
        )
    )
}
