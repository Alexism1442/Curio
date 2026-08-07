package com.curio.app.features.quests

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import com.curio.app.data.AppPreferences
import com.curio.app.data.CategoryId
import com.curio.app.data.CurioCategories
import com.curio.app.data.CurioQuests
import com.curio.app.data.CurioQuests.DailyQuest
import com.curio.app.data.CurioQuests.JourneyQuest
import com.curio.app.data.PromoMode
import com.curio.app.navigation.CurioRoutes
import com.curio.app.navigation.navigateToTab
import com.curio.app.features.settings.SettingsHeroHeader
import com.curio.app.features.settings.SettingsHeroTotalHeight
import com.curio.app.ui.theme.isCurioDarkTheme
import com.curio.app.ui.components.CurioCardHeader
import com.curio.app.ui.components.CurioForwardArrow
import com.curio.app.ui.components.CurioSettingsCard
import com.curio.app.ui.components.CurioWatermarkBackdrop
import com.curio.app.ui.components.ScreenEntrance
import com.curio.app.ui.theme.CurioColors
import com.curio.app.ui.theme.CurioGradients
import com.curio.app.ui.theme.CurioIcon
import com.curio.app.ui.theme.CurioIcons

/**
 * Quests & levels — Curio's gamification home (v7.40).
 *
 * Its own page, styled like the settings family: a compact torn rose hero
 * header on a watermark backdrop, then three quest cards and the badge
 * shelf. Reads live reactive state from [CurioQuests], so badges pop the
 * moment they unlock and the current journey quest updates in place.
 *
 * Layout:
 *  1. Hero — the shared settings torn-banner header.
 *  2. Level card — the XP bar and current rank.
 *  3. Your journey — the guided beginner tour; the current quest is
 *     highlighted with a jump-to-it button.
 *  4. Today's quests — the three daily quests with mini progress bars.
 *  5. Achievements — the badge shelf in a two-column grid.
 */
@Composable
fun QuestsScreen(navController: NavController) {
    // v7.107 — promo/demo-content mode shows the promotional sample XP (top
    // rank, Grand Curator) while ON; only the level card is demoed here.
    val promoOn = AppPreferences.promoModeState
    val xp = if (promoOn) PromoMode.DEMO_XP else CurioQuests.xpState
    val level = CurioQuests.levelForXp(xp)
    val (progress, nextThreshold) = CurioQuests.xpProgress(xp)

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(MaterialTheme.colorScheme.background)
    ) {
        // ── Watermark backdrop — muted category glyphs behind the content
        // (the settings/profile language). Quests are category-neutral, so
        // the wildcard sparkle leads the collage.
        CurioWatermarkBackdrop(
            activeCat = CurioCategories.byId(CategoryId.WILDCARD)
        )
        // The hero is drawn LAST (on top of the scroll content): the quest
        // cards scroll UP and disappear behind the ragged tear instead of
        // clipping at a straight line — the same overlay construction as
        // every settings screen.
        ScreenEntrance {
            LazyColumn(
                modifier = Modifier.fillMaxSize(),
                contentPadding = PaddingValues(start = 16.dp, end = 16.dp, top = SettingsHeroTotalHeight + 10.dp, bottom = 24.dp),
                verticalArrangement = Arrangement.spacedBy(10.dp)
            ) {
                item {
                    LevelCard(
                        level = level,
                        xp = xp,
                        nextThreshold = nextThreshold,
                        progress = progress,
                        isMaxLevel = level >= CurioQuests.maxLevel
                    )
                }
                item {
                    JourneyCard(
                        current = CurioQuests.currentJourneyQuest(),
                        onNavigate = { route -> navigateToQuest(navController, route) }
                    )
                }
                item {
                    DailyCard(
                        quests = CurioQuests.dailyQuestsFor(CurioQuests.todayEpochDay())
                    )
                }
                item {
                    AchievementsCard()
                }
            }
        }
        // Drawn on top of the scroll content — cards slide under the ragged
        // tear as they scroll up.
        SettingsHeroHeader(
            title = "Quests & levels",
            subtitle = "Grow your curiosity, one quest at a time",
            onBack = { navController.popBackStack() }
        )
    }
}

/** Jump to the screen a journey quest points at (tabs navigate like tabs). */
private fun navigateToQuest(navController: NavController, route: String) {
    if (route == CurioRoutes.SPIN) {
        navController.navigateToTab(route)
    } else {
        navController.navigate(route) { launchSingleTop = true }
    }
}

/** The rank card — big level badge, title, and the XP progress bar. */
@Composable
private fun LevelCard(level: Int, xp: Int, nextThreshold: Int, progress: Float, isMaxLevel: Boolean) {
    CurioSettingsCard {
        Row(
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(14.dp)
        ) {
            Box(
                modifier = Modifier
                    .size(64.dp)
                    .clip(RoundedCornerShape(22.dp))
                    .background(Brush.linearGradient(CurioGradients.WildcardGradientStops.take(3))),
                contentAlignment = Alignment.Center
            ) {
                Text(
                    "$level",
                    style = MaterialTheme.typography.headlineMedium.copy(fontWeight = FontWeight.ExtraBold),
                    color = Color.White
                )
            }
            Column(modifier = Modifier.weight(1f)) {
                Text(
                    "Level $level · ${CurioQuests.levelTitle(level)}",
                    style = MaterialTheme.typography.titleMedium.copy(fontWeight = FontWeight.ExtraBold),
                    maxLines = 1,
                    overflow = TextOverflow.Ellipsis
                )
                Text(
                    "Earning XP with every explore",
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant
                )
            }
            CurioIcon(
                name = CurioIcons.WorkspacePremium,
                contentDescription = null,
                // Gold trophy — an earned rank reads better in warm gold
                // than the coral used everywhere else (v7.103).
                tint = CurioColors.ButterYellow,
                size = 30.dp
            )
        }
        Spacer(Modifier.height(12.dp))
        LinearProgressIndicator(
            progress = { progress.coerceIn(0f, 1f) },
            modifier = Modifier
                .fillMaxWidth()
                .height(8.dp)
                .clip(RoundedCornerShape(50)),
            color = CurioColors.CoralBlush,
            trackColor = CurioColors.CoralBlush.copy(alpha = 0.14f)
        )
        Spacer(Modifier.height(6.dp))
        Text(
            text = if (isMaxLevel) "Grand Curator — the whole shelf is yours."
            else "$xp / $nextThreshold XP · ${(nextThreshold - xp).coerceAtLeast(0)} XP to Level ${level + 1}",
            style = MaterialTheme.typography.labelSmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant
        )
    }
}

/** The guided journey — current quest highlighted, the rest as a checklist. */
@Composable
private fun JourneyCard(
    current: CurioQuests.JourneyQuest?,
    onNavigate: (String) -> Unit
) {
    CurioSettingsCard {
        CurioCardHeader(CurioIcons.Flag, "Your journey", "A guided tour of Curio")
        Spacer(Modifier.height(4.dp))
        if (current != null) {
            // ── The current quest — the hero of this card ─────────────
            val done = CurioQuests.journeyProgress(current)
            val roseHero = if (isCurioDarkTheme()) {
                CurioColors.HomeRosewoodDark
            } else {
                CurioColors.HomeRosewood
            }
            Surface(
                shape = RoundedCornerShape(18.dp),
                color = roseHero.copy(alpha = 0.10f),
                border = BorderStroke(1.dp, roseHero.copy(alpha = 0.28f)),
                modifier = Modifier.fillMaxWidth()
            ) {
                Column(modifier = Modifier.padding(14.dp)) {
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.spacedBy(8.dp)
                    ) {
                        Box(
                            modifier = Modifier
                                .size(22.dp)
                                .clip(CircleShape)
                                .background(CurioColors.CoralBlush),
                            contentAlignment = Alignment.Center
                        ) {
                            CurioIcon(
                                name = CurioIcons.TaskAlt,
                                contentDescription = null,
                                tint = Color.White,
                                size = 14.dp
                            )
                        }
                        Text(
                            "CURRENT QUEST",
                            style = MaterialTheme.typography.labelSmall.copy(
                                fontWeight = FontWeight.ExtraBold,
                                letterSpacing = 1.2.sp
                            ),
                            color = roseHero
                        )
                    }
                    Spacer(Modifier.height(8.dp))
                    Text(
                        current.title,
                        style = MaterialTheme.typography.titleMedium.copy(fontWeight = FontWeight.ExtraBold)
                    )
                    Text(
                        current.description,
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                    Spacer(Modifier.height(6.dp))
                    Text(
                        current.hint,
                        style = MaterialTheme.typography.labelMedium,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                    Spacer(Modifier.height(10.dp))
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.spacedBy(10.dp)
                    ) {
                        Surface(
                            onClick = { current.navRoute?.let(onNavigate) },
                            shape = RoundedCornerShape(50),
                            color = CurioColors.CoralBlush,
                            enabled = current.navRoute != null,
                            modifier = Modifier.weight(1f)
                        ) {
                            Text(
                                if (current.navRoute != null) "Start · +${current.xpReward} XP"
                                else "In progress · ${done.coerceAtMost(current.target)}/${current.target}",
                                style = MaterialTheme.typography.labelLarge.copy(fontWeight = FontWeight.Bold),
                                color = Color.White,
                                modifier = Modifier.padding(vertical = 9.dp),
                                textAlign = androidx.compose.ui.text.style.TextAlign.Center
                            )
                        }
                        Text(
                            "Hint: ${current.hint}",
                            style = MaterialTheme.typography.labelSmall,
                            color = MaterialTheme.colorScheme.onSurfaceVariant,
                            maxLines = 1,
                            overflow = TextOverflow.Ellipsis,
                            modifier = Modifier.weight(1.2f)
                        )
                    }
                }
            }
            Spacer(Modifier.height(8.dp))
        }
        // ── The full checklist ────────────────────────────────────────
        CurioQuests.Journey.forEachIndexed { index, quest ->
            val done = CurioQuests.journeyProgress(quest) >= quest.target
            val isCurrent = quest.id == current?.id
            JourneyRow(
                index = index,
                quest = quest,
                done = done,
                isCurrent = isCurrent,
                onNavigate = { quest.navRoute?.let(onNavigate) }
            )
        }
        if (CurioQuests.isJourneyComplete()) {
            Spacer(Modifier.height(6.dp))
            Surface(
                shape = RoundedCornerShape(16.dp),
                color = CurioColors.Sage.copy(alpha = 0.14f),
                modifier = Modifier.fillMaxWidth()
            ) {
                Row(
                    modifier = Modifier.padding(horizontal = 12.dp, vertical = 10.dp),
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(8.dp)
                ) {
                    CurioIcon(
                        name = CurioIcons.EmojiEvents,
                        contentDescription = null,
                        tint = CurioColors.Sage,
                        size = 20.dp
                    )
                    Text(
                        "Journey complete — the whole app is yours to roam.",
                        style = MaterialTheme.typography.labelMedium.copy(fontWeight = FontWeight.Bold),
                        color = MaterialTheme.colorScheme.onSurface
                    )
                }
            }
        }
    }
}

/** One checklist row — number circle, title, and a done/current state. */
@Composable
private fun JourneyRow(
    index: Int,
    quest: JourneyQuest,
    done: Boolean,
    isCurrent: Boolean,
    onNavigate: () -> Unit
) {
    val accent = if (done) CurioColors.Sage else CurioColors.CoralBlush
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 6.dp),
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        Box(
            modifier = Modifier
                .size(30.dp)
                .clip(CircleShape)
                .background(accent.copy(alpha = if (done || isCurrent) 1f else 0.12f)),
            contentAlignment = Alignment.Center
        ) {
            if (done) {
                CurioIcon(CurioIcons.Check, null, tint = Color.White, size = 16.dp)
            } else {
                Text(
                    "${index + 1}",
                    style = MaterialTheme.typography.labelMedium.copy(fontWeight = FontWeight.ExtraBold),
                    color = if (isCurrent) Color.White else MaterialTheme.colorScheme.onSurfaceVariant
                )
            }
        }
        Column(modifier = Modifier.weight(1f)) {
            Text(
                quest.title,
                style = MaterialTheme.typography.bodyLarge.copy(
                    fontWeight = if (isCurrent || done) FontWeight.ExtraBold else FontWeight.Medium
                ),
                color = if (done) MaterialTheme.colorScheme.onSurfaceVariant
                else MaterialTheme.colorScheme.onSurface,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
            Text(
                if (done) "Done · +${quest.xpReward} XP"
                else "+${quest.xpReward} XP",
                style = MaterialTheme.typography.labelSmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
        }
        if (isCurrent && quest.navRoute != null) {
            Surface(
                onClick = onNavigate,
                shape = RoundedCornerShape(50),
                color = CurioColors.CoralBlush.copy(alpha = 0.16f)
            ) {
                Row(
                    modifier = Modifier.padding(horizontal = 10.dp, vertical = 6.dp),
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(4.dp)
                ) {
                    Text(
                        "Go",
                        style = MaterialTheme.typography.labelMedium.copy(fontWeight = FontWeight.Bold),
                        color = CurioColors.CoralBlush
                    )
                    CurioForwardArrow(
                        "Go to quest",
                        tint = CurioColors.CoralBlush,
                        size = 14.dp
                    )
                }
            }
        }
    }
}

/** Today's three quests with mini progress bars. */
@Composable
private fun DailyCard(quests: List<DailyQuest>) {
    CurioSettingsCard {
        CurioCardHeader(CurioIcons.EmojiEvents, "Today's quests", "Resets at midnight")
        Spacer(Modifier.height(2.dp))
        quests.forEach { quest ->
            val progress = CurioQuests.dailyProgressState[quest.kind.name] ?: 0
            val done = quest.id in CurioQuests.dailyAwardedState
            val fraction = (progress.toFloat() / quest.target).coerceIn(0f, 1f)
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(vertical = 7.dp),
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                Box(
                    modifier = Modifier
                        .size(34.dp)
                        .clip(RoundedCornerShape(11.dp))
                        .background(
                            if (done) CurioColors.Sage.copy(alpha = 0.18f)
                            else CurioColors.CoralBlush.copy(alpha = 0.14f)
                        ),
                    contentAlignment = Alignment.Center
                ) {
                    CurioIcon(
                        name = if (done) CurioIcons.Check else CurioIcons.TaskAlt,
                        contentDescription = null,
                        tint = if (done) CurioColors.Sage else CurioColors.CoralBlush,
                        size = 18.dp
                    )
                }
                Column(modifier = Modifier.weight(1f)) {
                    Text(
                        quest.title,
                        style = MaterialTheme.typography.bodyLarge.copy(
                            fontWeight = if (done) FontWeight.ExtraBold else FontWeight.SemiBold
                        ),
                        color = if (done) MaterialTheme.colorScheme.onSurfaceVariant
                        else MaterialTheme.colorScheme.onSurface,
                        maxLines = 1,
                        overflow = TextOverflow.Ellipsis
                    )
                    Spacer(Modifier.height(5.dp))
                    LinearProgressIndicator(
                        progress = { fraction },
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(4.dp)
                            .clip(RoundedCornerShape(50)),
                        color = if (done) CurioColors.Sage else CurioColors.CoralBlush,
                        trackColor = MaterialTheme.colorScheme.surfaceVariant
                    )
                }
                Spacer(Modifier.width(6.dp))
                Text(
                    if (done) "Done" else "+${quest.xpReward} XP",
                    style = MaterialTheme.typography.labelSmall.copy(fontWeight = FontWeight.Bold),
                    color = if (done) CurioColors.Sage else CurioColors.CoralBlush
                )
            }
        }
    }
}

/** The badge shelf — every achievement in a two-column grid. */
@Composable
private fun AchievementsCard() {
    val unlockedCount = CurioQuests.achievementsState.size
    CurioSettingsCard {
        CurioCardHeader(
            CurioIcons.EmojiEvents,
            "Achievements",
            "$unlockedCount of ${CurioQuests.Achievements.size} badges"
        )
        Spacer(Modifier.height(4.dp))
        CurioQuests.Achievements.chunked(2).forEach { row ->
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(vertical = 5.dp),
                horizontalArrangement = Arrangement.spacedBy(10.dp)
            ) {
                row.forEach { achievement ->
                    AchievementTile(
                        achievement = achievement,
                        modifier = Modifier.weight(1f)
                    )
                }
                if (row.size == 1) Spacer(Modifier.weight(1f))
            }
        }
    }
}

/** One badge tile — glyph, title, and a tiny progress line. */
@Composable
private fun AchievementTile(
    achievement: CurioQuests.Achievement,
    modifier: Modifier = Modifier
) {
    val unlocked = achievement.id in CurioQuests.achievementsState
    val progress = CurioQuests.achievementProgressFor(achievement)
    val accent = if (unlocked) CurioColors.Sage else CurioColors.CoralBlush
    Surface(
        shape = RoundedCornerShape(18.dp),
        color = if (unlocked) CurioColors.Sage.copy(alpha = 0.12f)
        else MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.45f),
        border = BorderStroke(
            1.dp,
            if (unlocked) CurioColors.Sage.copy(alpha = 0.35f)
            else MaterialTheme.colorScheme.outlineVariant.copy(alpha = 0.5f)
        ),
        modifier = modifier
    ) {
        Column(modifier = Modifier.padding(horizontal = 12.dp, vertical = 12.dp)) {
            Row(
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                Box(
                    modifier = Modifier
                        .size(34.dp)
                        .clip(RoundedCornerShape(11.dp))
                        .background(accent.copy(alpha = if (unlocked) 1f else 0.14f)),
                    contentAlignment = Alignment.Center
                ) {
                    CurioIcon(
                        name = if (unlocked) achievement.glyph else CurioIcons.StarOutline,
                        contentDescription = null,
                        tint = if (unlocked) Color.White else accent,
                        size = 18.dp
                    )
                }
                Text(
                    if (unlocked) "Unlocked" else "+${achievement.xpReward} XP",
                    style = MaterialTheme.typography.labelSmall.copy(fontWeight = FontWeight.Bold),
                    color = if (unlocked) CurioColors.Sage else accent
                )
            }
            Spacer(Modifier.height(8.dp))
            Text(
                achievement.title,
                style = MaterialTheme.typography.titleSmall.copy(
                    fontWeight = if (unlocked) FontWeight.ExtraBold else FontWeight.SemiBold
                ),
                color = if (unlocked) MaterialTheme.colorScheme.onSurface
                else MaterialTheme.colorScheme.onSurfaceVariant,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
            Text(
                achievement.description,
                style = MaterialTheme.typography.labelSmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                maxLines = 2,
                overflow = TextOverflow.Ellipsis
            )
            Spacer(Modifier.height(8.dp))
            LinearProgressIndicator(
                progress = { (progress.toFloat() / achievement.target.coerceAtLeast(1)).coerceIn(0f, 1f) },
                modifier = Modifier
                    .fillMaxWidth()
                    .height(4.dp)
                    .clip(RoundedCornerShape(50)),
                color = if (unlocked) CurioColors.Sage else accent,
                trackColor = MaterialTheme.colorScheme.surfaceVariant
            )
            Spacer(Modifier.height(4.dp))
            Text(
                if (unlocked) "Badge earned" else "$progress / ${achievement.target}",
                style = MaterialTheme.typography.labelSmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
        }
    }
}
