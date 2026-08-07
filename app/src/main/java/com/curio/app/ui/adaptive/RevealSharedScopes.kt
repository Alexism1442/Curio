package com.curio.app.ui.adaptive

import androidx.compose.animation.AnimatedVisibilityScope
import androidx.compose.animation.BoundsTransform
import androidx.compose.animation.SharedTransitionScope
import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.tween
import androidx.compose.runtime.staticCompositionLocalOf

/**
 * Shared-element handoff between the Spin deck and the Topic Reveal page.
 *
 * The Spin front ticket and the Reveal hero are matched shared elements
 * (key [RevealSharedElementKey]), so opening a landed topic morphs the
 * reveal hero OUT of the ticket's position instead of sliding the page in.
 *
 * The scopes are created by [androidx.compose.animation.SharedTransitionLayout]
 * in CurioNavHost and provided per-destination here, because this Compose
 * version has no built-in CompositionLocal for the shared transition scope.
 * Both locals are null-guarded at the consumer sites (never null in the
 * NavHost subtree).
 */
const val RevealSharedElementKey = "reveal-hero"

/**
 * Second shared element for the topic NAME: the Spin ticket's title morphs
 * into the reveal screen's headline below the hero, so the text glides out
 * of the expanding card instead of popping in after the bounds morph ends.
 */
const val RevealTitleSharedElementKey = "reveal-hero-title"

/**
 * Bounds animation for the reveal morph — a quick, even FastOutSlowIn
 * tween (320ms) so the card expands into the hero smoothly without the
 * default spring's wobble or the earlier laggy feel.
 */
val RevealBoundsTransform = BoundsTransform { _, _ ->
    tween(320, easing = FastOutSlowInEasing)
}

/** The SharedTransitionScope instance wrapping the NavHost. */
val LocalRevealSharedScope = staticCompositionLocalOf<SharedTransitionScope?> { null }

/** The destination's AnimatedContentScope (controls the element's visibility). */
val LocalRevealVisibilityScope = staticCompositionLocalOf<AnimatedVisibilityScope?> { null }
