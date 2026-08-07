package com.curio.app.ui.components

import androidx.compose.animation.core.Animatable
import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.tween
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.widthIn
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import com.curio.app.ui.theme.CurioColors
import com.curio.app.ui.theme.CurioIcon
import com.curio.app.ui.theme.CurioIcons
import com.curio.app.ui.theme.CurioMotion

/**
 * The quest guide's compact IN-APP OVERLAY — a small floating pill near the
 * bottom of the screen (not a system Toast, not a dialog). Carries a flag
 * marker, a bold title, a one-to-two line message, a footer (step count or
 * XP), and a Next / Go / Finish action. Tap the pill to advance the
 * walkthrough; the optional [onClose] X ends it.
 */
@Composable
fun QuestGuideToast(
    title: String,
    message: String,
    footer: String?,
    actionLabel: String,
    onClick: () -> Unit,
    onClose: (() -> Unit)? = null,
    modifier: Modifier = Modifier
) {
    // Gentle pop-in (fade + slight scale) so the pill doesn't slam in.
    val pop = remember { Animatable(0f) }
    LaunchedEffect(Unit) {
        pop.animateTo(1f, tween(CurioMotion.Durations.Quick, easing = FastOutSlowInEasing))
    }
    Surface(
        onClick = onClick,
        shape = RoundedCornerShape(20.dp),
        color = MaterialTheme.colorScheme.surfaceContainerHigh,
        contentColor = MaterialTheme.colorScheme.onSurface,
        shadowElevation = 10.dp,
        tonalElevation = 3.dp,
        border = BorderStroke(1.dp, MaterialTheme.colorScheme.outlineVariant.copy(alpha = 0.4f)),
        modifier = modifier
            .widthIn(max = 430.dp)
            .graphicsLayer {
                val t = pop.value
                scaleX = 0.94f + 0.06f * t
                scaleY = 0.94f + 0.06f * t
                alpha = t
            }
    ) {
        Row(
            modifier = Modifier.padding(start = 12.dp, top = 10.dp, bottom = 10.dp, end = 6.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(10.dp)
        ) {
            Box(
                modifier = Modifier
                    .size(36.dp)
                    .clip(RoundedCornerShape(12.dp))
                    .background(CurioColors.CoralBlush),
                contentAlignment = Alignment.Center
            ) {
                CurioIcon(CurioIcons.Flag, null, tint = Color.White, size = 20.dp)
            }
            Column(modifier = Modifier.weight(1f)) {
                Text(
                    title,
                    style = MaterialTheme.typography.titleSmall.copy(fontWeight = FontWeight.ExtraBold),
                    maxLines = 1,
                    overflow = TextOverflow.Ellipsis
                )
                Text(
                    message,
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )
            }
            if (footer != null) {
                Text(
                    footer,
                    style = MaterialTheme.typography.labelSmall.copy(fontWeight = FontWeight.Bold),
                    color = CurioColors.CoralBlush
                )
            }
            // The visible action label (Go / Next / Finish) — the whole pill
            // is tappable, so this is the affordance cue.
            Text(
                actionLabel,
                style = MaterialTheme.typography.labelLarge.copy(fontWeight = FontWeight.ExtraBold),
                color = CurioColors.CoralBlush
            )
            CurioIcon(
                name = CurioIcons.ChevronRight,
                contentDescription = actionLabel,
                tint = CurioColors.CoralBlush,
                size = 18.dp
            )
            if (onClose != null) {
                Box(
                    modifier = Modifier
                        .size(26.dp)
                        .clip(CircleShape)
                        .clickable(onClick = onClose),
                    contentAlignment = Alignment.Center
                ) {
                    CurioIcon(
                        name = CurioIcons.Close,
                        contentDescription = "Close guide",
                        tint = MaterialTheme.colorScheme.onSurfaceVariant,
                        size = 16.dp
                    )
                }
            }
        }
    }
}
