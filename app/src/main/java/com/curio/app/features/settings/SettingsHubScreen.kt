package com.curio.app.features.settings

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.BoxScope
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.BiasAlignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.curio.app.data.AppPreferences
import com.curio.app.data.CategoryFamily
import com.curio.app.data.CurioQuests
import com.curio.app.data.CategoryId
import com.curio.app.data.CurioCategories
import com.curio.app.navigation.CurioRoutes
import com.curio.app.ui.components.CurioBackButton
import com.curio.app.ui.components.CurioCardHeader
import com.curio.app.ui.components.CurioSectionLabel
import com.curio.app.ui.components.CurioSettingsCard
import com.curio.app.ui.components.CurioSettingsDivider
import com.curio.app.ui.components.CurioSettingsRow
import com.curio.app.ui.components.CurioWatermarkBackdrop
import com.curio.app.ui.components.ScreenEntrance
import com.curio.app.ui.components.SoftTornBottomShape
import com.curio.app.ui.components.SoftTornSheetShape
import com.curio.app.ui.theme.CurioColors
import com.curio.app.ui.theme.CurioIcon
import com.curio.app.ui.theme.CurioIcons
import com.curio.app.ui.theme.fromHsl
import com.curio.app.ui.theme.isCurioDarkTheme
import com.curio.app.ui.theme.pastelFillInk
import com.curio.app.ui.theme.toHsl

/** Fixed tear seed — every settings header tears in the SAME bold pattern
 *  (Settings's own pattern; Profile wears 0xC0FEE). Never re-rolls. */
private const val SETTINGS_HERO_TEAR_SEED = 0x5EED
/** The hero header's solid body height — compact ("just at the header"):
 *  back pill on top, title + subtitle pinned just above the tear. Held
 *  with flex slack so the title block clears the tear even at large font
 *  scales. */
private val SettingsHeroBannerHeight = 180.dp
/** Extra layout space reserved for the under-sheet below the torn banner. */
private val SettingsHeroSheetExtent = 24.dp
/** Total header footprint — the torn banner plus its under-sheet extent. */
private val SettingsHeroTotalHeight = SettingsHeroBannerHeight + SettingsHeroSheetExtent

/** One mirrored hero watermark pair — the left glyph mirrors the right
 *  (the Profile/Home quest hero construction, adapted for Settings). */
private data class SettingsHeroPair(
    val biasX: Float,
    val biasY: Float,
    val size: Dp,
    val rotation: Float,
    val alpha: Float
)

/**
 * The Settings hero header — the PROFILE hero's style, compact: a solid
 * rose torn banner (the same bold SoftTorn tear + theme under-sheet as
 * Profile/Home), the mirrored watermark collage of the wildcard family's
 * symbols, a back pill over the banner, and the title + subtitle pinned
 * just above the tear. Shared by every settings screen so the whole
 * Settings family wears the same hero-style header.
 */
@Composable
fun SettingsHeroHeader(
    title: String,
    subtitle: String,
    onBack: () -> Unit
) {
    val heroTornShape = remember(SETTINGS_HERO_TEAR_SEED) { SoftTornBottomShape(SETTINGS_HERO_TEAR_SEED, bold = true) }
    val sheetShape = remember(SETTINGS_HERO_TEAR_SEED) {
        SoftTornSheetShape(SETTINGS_HERO_TEAR_SEED, lip = 10.dp, baseline = 14.dp, bold = true)
    }
    val fill = settingsRoseAccent()
    val ink = settingsReadableInk(fill)
    Box(
        modifier = Modifier
            .fillMaxWidth()
            .height(SettingsHeroTotalHeight)
    ) {
        // ── Under-sheet — the theme's own background, so the tear sits on
        // the page color in every theme (the Profile construction).
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(42.dp)
                .offset(y = SettingsHeroBannerHeight - 18.dp)
                .clip(sheetShape)
                .background(MaterialTheme.colorScheme.background)
        )
        // ── Torn-edge shadow — hairline dark rim under the seam.
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(SettingsHeroBannerHeight)
                .offset(y = 1.dp)
                .clip(heroTornShape)
                .background(Color.Black.copy(alpha = 0.20f))
        )
        // ── Solid rose banner, torn bottom edge ────────────────────────
        Surface(
            shape = heroTornShape,
            color = fill,
            shadowElevation = 0.dp,
            modifier = Modifier
                .fillMaxWidth()
                .height(SettingsHeroBannerHeight)
        ) {
            Box(modifier = Modifier.fillMaxSize()) {
                // Mirrored watermark collage — the wildcard family's symbols
                // pop around the banner edges (settings is category-neutral;
                // the Profile hero's exact collage construction).
                val symbols = CurioIcons.heroWatermarkSymbols(CategoryFamily.WILDCARD)
                val pairs = listOf(
                    SettingsHeroPair(biasX = 0.93f, biasY = -0.85f, size = 44.dp, rotation = 12f, alpha = 0.11f),
                    SettingsHeroPair(biasX = 0.55f, biasY = -0.64f, size = 48.dp, rotation = 8f, alpha = 0.13f),
                    SettingsHeroPair(biasX = 0.94f, biasY = -0.12f, size = 56.dp, rotation = 14f, alpha = 0.14f),
                    SettingsHeroPair(biasX = 0.56f, biasY = 0.54f, size = 50.dp, rotation = 10f, alpha = 0.13f),
                    SettingsHeroPair(biasX = 0.94f, biasY = 0.80f, size = 44.dp, rotation = 6f, alpha = 0.11f)
                )
                pairs.forEachIndexed { i, pair ->
                    SettingsHeroSymbol(symbols[i * 2], BiasAlignment(-pair.biasX, pair.biasY), pair.size, -pair.rotation, pair.alpha, ink)
                    SettingsHeroSymbol(symbols[i * 2 + 1], BiasAlignment(pair.biasX, pair.biasY), pair.size, pair.rotation, pair.alpha, ink)
                }
                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .statusBarsPadding()
                        .padding(start = 20.dp, end = 20.dp, top = 10.dp, bottom = 16.dp)
                ) {
                    // ── Back pill over the banner ───────────────────────
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.SpaceBetween
                    ) {
                        CurioBackButton(
                            onClick = onBack,
                            containerColor = ink.copy(alpha = 0.18f),
                            contentColor = ink,
                            disableRipple = true
                        )
                        // Decorative echo of the back pill — a plain settings
                        // glyph floats on the opposite corner (Profile's
                        // top-bar symmetry). Deliberately NOT a Surface:
                        // no circle, no press, just a quiet ink glyph so it
                        // never reads as a button.
                        CurioIcon(
                            name = CurioIcons.Settings,
                            contentDescription = null,
                            tint = ink.copy(alpha = 0.55f),
                            size = 24.dp
                        )
                    }
                    // Flex spacer — pins the title block just above the tear.
                    Spacer(Modifier.weight(1f))
                    // ── Title + subtitle — the header's identity ───────
                    Column {
                        Text(
                            title,
                            style = MaterialTheme.typography.headlineSmall.copy(fontWeight = FontWeight.ExtraBold),
                            color = ink,
                            maxLines = 1
                        )
                        Text(
                            subtitle,
                            style = MaterialTheme.typography.labelMedium,
                            color = ink.copy(alpha = 0.82f),
                            maxLines = 1
                        )
                    }
                }
            }
        }
    }
}

/** One mirrored watermark glyph on the hero header — the banner's readable
 *  ink at a soft alpha (the Profile/Home collage construction). */
@Composable
private fun BoxScope.SettingsHeroSymbol(
    glyph: String,
    alignment: Alignment,
    size: Dp,
    rotation: Float,
    alpha: Float,
    tint: Color
) {
    CurioIcon(
        name = glyph,
        contentDescription = null,
        tint = tint.copy(alpha = alpha),
        size = size,
        modifier = Modifier
            .align(alignment)
            .padding(10.dp)
            .graphicsLayer { rotationZ = rotation }
    )
}

/** The settings hero's rose-wood fill — the SAME treatment as Home/Profile
 *  (the muted rose-wood base, its airy pastel twin in pastel mode) so
 *  Settings reads as part of the same torn-banner family. */
@Composable
private fun settingsRoseAccent(): Color {
    val base = toHsl(CurioColors.HomeRosewood)
    return if (AppPreferences.pastelColorsState) {
        val pinkHue = (base.h - 15f + 360f) % 360f
        if (isCurioDarkTheme()) {
            fromHsl(pinkHue, (base.s * 0.55f).coerceIn(0f, 0.55f), 0.42f)
        } else {
            fromHsl(pinkHue, (base.s * 0.90f).coerceIn(0f, 0.80f), 0.82f)
        }
    } else {
        fromHsl(base.h, (base.s * 0.80f).coerceAtMost(0.40f), (base.l * 1.06f).coerceAtMost(0.70f))
    }
}

/** Readable ink for content sitting on the settings rose banner (Home's
 *  helper, replicated for this file). */
@Composable
private fun settingsReadableInk(fill: Color): Color = if (
    !AppPreferences.pastelColorsState && !isCurioDarkTheme()
) {
    MaterialTheme.colorScheme.onSurface
} else {
    pastelFillInk(fill)
}

/** Compact hub for the redesigned settings experience — the Profile-style
 *  hero header on a watermark backdrop, with clean settings cards. */
@Composable
fun SettingsHubScreen(navController: NavController) {
    val context = LocalContext.current
    // Feed the quests system — opening Settings completes the journey quest.
    LaunchedEffect(Unit) { CurioQuests.onSettingsVisited(context) }
    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(MaterialTheme.colorScheme.background)
    ) {
        // ── Watermark backdrop — muted category glyphs behind the content
        // (the Home/Profile language). Settings is category-neutral, so the
        // wildcard sparkle leads the collage.
        CurioWatermarkBackdrop(
            activeCat = CurioCategories.byId(CategoryId.WILDCARD)
        )
        Column(
            modifier = Modifier
                .fillMaxSize()
                .statusBarsPadding()
        ) {
            SettingsHeroHeader(
                title = "Settings",
                subtitle = "Tune Curio your way",
                onBack = { navController.popBackStack() }
            )
            ScreenEntrance {
                LazyColumn(
                    modifier = Modifier.fillMaxSize(),
                    contentPadding = PaddingValues(start = 16.dp, end = 16.dp, top = 10.dp, bottom = 24.dp),
                    verticalArrangement = Arrangement.spacedBy(10.dp)
                ) {
                    item { CurioSectionLabel("Personalize") }
                    item {
                        CurioSettingsCard {
                            CurioCardHeader(CurioIcons.AutoAwesome, "How Curio feels", "Appearance and color")
                            CurioSettingsRow(CurioIcons.DarkMode, "Appearance", "Theme, tint, and pastel color") {
                                navController.navigate(CurioRoutes.SETTINGS_APPEARANCE) { launchSingleTop = true }
                            }
                            CurioSettingsDivider()
                            CurioSettingsRow(CurioIcons.Notifications, "Notifications", "Reminders and explore controls") {
                                navController.navigate(CurioRoutes.SETTINGS_NOTIFICATIONS) { launchSingleTop = true }
                            }
                            CurioSettingsDivider()
                            CurioSettingsRow(CurioIcons.Mic, "Recording", "Voice-note quality and dictation") {
                                navController.navigate(CurioRoutes.SETTINGS_RECORDING) { launchSingleTop = true }
                            }
                        }
                    }
                    item { CurioSectionLabel("Explore") }
                    item {
                        CurioSettingsCard {
                            CurioCardHeader(CurioIcons.ScienceGlyph, "Experiments", "Try visual ideas before they ship")
                            CurioSettingsRow(CurioIcons.Layers, "Card & deck experiments", "Main card, peek deck, and Spin tests") {
                                navController.navigate(CurioRoutes.EXPERIMENTS) { launchSingleTop = true }
                            }
                            CurioSettingsDivider()
                            CurioSettingsRow(CurioIcons.DragHandle, "Manage categories", "Show, hide, or reorder lanes") {
                                navController.navigate(CurioRoutes.MANAGE_CATEGORIES) { launchSingleTop = true }
                            }
                            CurioSettingsDivider()
                            CurioSettingsRow(CurioIcons.History, "Topic history", "Revisit what you explored") {
                                navController.navigate(CurioRoutes.TOPIC_HISTORY) { launchSingleTop = true }
                            }
                        }
                    }
                    item { CurioSectionLabel("Safety & support") }
                    item {
                        CurioSettingsCard {
                            CurioCardHeader(CurioIcons.Backup, "Your data", "Backups and restore")
                            CurioSettingsRow(CurioIcons.Backup, "Backup & restore", "Keep captures and settings safe") {
                                navController.navigate(CurioRoutes.SETTINGS_DATA) { launchSingleTop = true }
                            }
                            CurioSettingsDivider()
                            CurioSettingsRow(CurioIcons.Info, "About Curio", "Replay intro and app details") {
                                navController.navigate(CurioRoutes.SETTINGS_ABOUT) { launchSingleTop = true }
                            }
                        }
                    }
                }
            }
        }
    }
}
