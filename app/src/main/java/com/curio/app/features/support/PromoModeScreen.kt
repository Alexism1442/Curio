package com.curio.app.features.support

import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.BiasAlignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.DpSize
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import com.curio.app.data.CategoryId
import com.curio.app.data.CurioCategories
import com.curio.app.features.settings.SettingsHeroHeader
import com.curio.app.features.settings.SettingsHeroTotalHeight
import com.curio.app.ui.components.CurioSectionLabel
import com.curio.app.ui.components.CurioWatermarkBackdrop
import com.curio.app.ui.components.ScreenEntrance
import com.curio.app.ui.components.SoftTornBottomShape
import com.curio.app.ui.components.SoftTornSheetShape
import com.curio.app.ui.components.shareComposableCard
import com.curio.app.ui.theme.CurioColors
import com.curio.app.ui.theme.CurioIcon
import com.curio.app.ui.theme.CurioIcons

/**
 * Promo mode — the hidden, share-ready promo page unlocked by tapping the
 * Version row in Support & diagnostics five times.
 *
 * Shows the app's torn-rose promo poster as a live preview (WYSIWYG — the
 * exact art the share sheet sends) plus one Share action that renders the
 * poster off-screen at 360×480 dp via [shareComposableCard] and opens the
 * Android share sheet, so screenshots for the store are one tap away.
 *
 * The [PromoShareCard] poster is fully self-contained (explicit colors, no
 * app-theme dependency) so the off-screen export renders identically on any
 * device.
 */
@Composable
fun PromoModeScreen(navController: NavController) {
    val context = LocalContext.current
    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(MaterialTheme.colorScheme.background)
    ) {
        // ── Watermark backdrop — muted category glyphs (settings family).
        CurioWatermarkBackdrop(
            activeCat = CurioCategories.byId(CategoryId.WILDCARD),
            alphaScale = 0.45f
        )
        // ── Scroll content — fills the screen, runs under the ragged tear.
        ScreenEntrance {
            LazyColumn(
                modifier = Modifier.fillMaxSize(),
                contentPadding = PaddingValues(
                    start = 16.dp,
                    end = 16.dp,
                    top = SettingsHeroTotalHeight + 10.dp,
                    bottom = 32.dp
                ),
                verticalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                item { CurioSectionLabel("Promo card") }
                item {
                    // Live preview — the exact poster the share sheet sends.
                    Box(
                        modifier = Modifier
                            .fillMaxWidth()
                            .aspectRatio(3f / 4f)
                            .shadow(10.dp, RoundedCornerShape(22.dp))
                            .clip(RoundedCornerShape(22.dp))
                    ) {
                        PromoShareCard()
                    }
                }
                item {
                    Surface(
                        onClick = {
                            shareComposableCard(
                                context = context,
                                cardSize = DpSize(360.dp, 480.dp),
                                authority = "${context.packageName}.fileprovider",
                                card = { PromoShareCard() }
                            )
                        },
                        shape = RoundedCornerShape(50),
                        color = CurioColors.HomeRosewood,
                        contentColor = Color(0xFFFDFCF9),
                        modifier = Modifier.fillMaxWidth()
                    ) {
                        Row(
                            modifier = Modifier.padding(horizontal = 18.dp, vertical = 14.dp),
                            verticalAlignment = Alignment.CenterVertically,
                            horizontalArrangement = Arrangement.Center
                        ) {
                            CurioIcon(CurioIcons.Share, null, tint = Color(0xFFFDFCF9), size = 18.dp)
                            Spacer(Modifier.width(8.dp))
                            Text(
                                "Share promo card",
                                style = MaterialTheme.typography.labelLarge.copy(fontWeight = FontWeight.Bold)
                            )
                        }
                    }
                }
                item {
                    Text(
                        "Reopen anytime: in Support & diagnostics, tap the Version row five times.",
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                        textAlign = TextAlign.Center,
                        modifier = Modifier.fillMaxWidth()
                    )
                }
            }
        }
        // ── Torn rose hero on top — rows disappear under the tear (the
        // settings overlay pattern).
        SettingsHeroHeader(
            title = "Promo mode",
            subtitle = "Store-ready promo art",
            onBack = { navController.popBackStack() }
        )
    }
}

// ═══════════════════════════════════════════════════════════════════════
// The promo poster — the torn-rose family's share card.
// ═══════════════════════════════════════════════════════════════════════

/** Fixed promo-poster tear seed — the seam never re-rolls across preview
 *  and export. */
private const val PROMO_TEAR_SEED = 0x50AC0

/** The poster's rose banner gradient — soft pink melting into a deeper
 *  rose at the tear. */
private val PromoRoseTop = Color(0xFFF9CDD8)
private val PromoRoseDeep = Color(0xFFE493A8)
/** Readable deep plum-rose ink for text on the banner. */
private val PromoBannerInk = Color(0xFF54242F)
/** Warm paper cream — the under-sheet and the poster's lower half. */
private val PromoPaper = Color(0xFFFDFCF9)
/** Deep warm body ink for the promise rows. */
private val PromoBodyInk = Color(0xFF3A262B)
private val PromoBodyMuted = Color(0xFF8A6870)

/**
 * The self-contained promo poster: a rose banner (wordmark + tagline +
 * category chips) torn onto a paper body (the three promises + the die),
 * all drawn with explicit colors so the off-screen export and the on-screen
 * preview match.
 */
@Composable
fun PromoShareCard() {
    val bannerTorn = remember(PROMO_TEAR_SEED) { SoftTornBottomShape(PROMO_TEAR_SEED, bold = true) }
    val sheetShape = remember(PROMO_TEAR_SEED) {
        SoftTornSheetShape(PROMO_TEAR_SEED, lip = 10.dp, baseline = 14.dp, bold = true)
    }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .background(PromoPaper)
    ) {
        // ── Banner (top 60%) — rose gradient with a torn bottom seam ──
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .weight(0.60f)
        ) {
            // Cream sheet peeking up through the tear bites.
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .height(40.dp)
                    .align(Alignment.BottomCenter)
                    .offset(y = 10.dp)
                    .clip(sheetShape)
                    .background(PromoPaper)
            )
            // The rose banner, clipped to the seeded torn bottom edge.
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .fillMaxHeight()
                    .clip(bannerTorn)
                    .background(Brush.verticalGradient(listOf(PromoRoseTop, PromoRoseDeep)))
            ) {
                // Watermark glyphs — white at a soft alpha (banner family).
                val glyphs = listOf(
                    Triple(CurioIcons.AutoAwesome, BiasAlignment(-0.92f, -0.92f), 30f),
                    Triple(CurioIcons.Casino, BiasAlignment(0.92f, -0.82f), 26f),
                    Triple(CurioIcons.Star, BiasAlignment(-0.84f, 0.20f), 22f),
                    Triple(CurioIcons.AutoAwesome, BiasAlignment(0.90f, 0.14f), 24f)
                )
                glyphs.forEach { (glyph, bias, glyphSize) ->
                    CurioIcon(
                        name = glyph,
                        contentDescription = null,
                        tint = Color.White.copy(alpha = 0.28f),
                        size = glyphSize.dp,
                        modifier = Modifier
                            .align(bias)
                            .padding(12.dp)
                    )
                }
                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .padding(horizontal = 22.dp, vertical = 24.dp),
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Spacer(Modifier.weight(0.10f))
                    // Wordmark
                    Text(
                        text = "C U R I O",
                        style = MaterialTheme.typography.headlineMedium.copy(
                            fontWeight = FontWeight.ExtraBold,
                            letterSpacing = 6.sp
                        ),
                        color = PromoBannerInk,
                        textAlign = TextAlign.Center
                    )
                    Spacer(Modifier.height(10.dp))
                    Text(
                        text = "Discover something new,\nexplore it your way.",
                        style = MaterialTheme.typography.titleMedium.copy(
                            fontWeight = FontWeight.SemiBold,
                            lineHeight = 22.sp
                        ),
                        color = PromoBannerInk.copy(alpha = 0.92f),
                        textAlign = TextAlign.Center
                    )
                    Spacer(Modifier.weight(0.12f))
                    // Category chips
                    Row(
                        horizontalArrangement = Arrangement.spacedBy(8.dp),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        PromoChip(CurioIcons.Movies, "Films", PromoBannerInk)
                        PromoChip(CurioIcons.Music, "Albums", PromoBannerInk)
                    }
                    Spacer(Modifier.height(8.dp))
                    Row(
                        horizontalArrangement = Arrangement.spacedBy(8.dp),
                        verticalAlignment = Alignment.CenterVertically
                    ) {
                        PromoChip(CurioIcons.Books, "Books", PromoBannerInk)
                        PromoChip(CurioIcons.Science, "Discoveries", PromoBannerInk)
                    }
                    Spacer(Modifier.weight(0.10f))
                }
            }
        }
        // ── Paper body (bottom 40%) — the three promises + the die ──
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .weight(0.40f)
                .padding(horizontal = 24.dp, vertical = 18.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            PromoPromise(CurioIcons.Star, "Shuffle the deck", "Films, albums, books & discoveries")
            Spacer(Modifier.height(12.dp))
            PromoPromise(CurioIcons.MoodInspired, "Explore it your way", "Your pace, your notes, your words")
            Spacer(Modifier.height(12.dp))
            PromoPromise(CurioIcons.Bookmark, "Keep what moves you", "Quotes & entries in your Cabinet")
            Spacer(Modifier.height(16.dp))
            // The die — the wildcard shuffle mark.
            Box(
                modifier = Modifier
                    .size(50.dp)
                    .clip(CircleShape)
                    .background(PromoRoseDeep),
                contentAlignment = Alignment.Center
            ) {
                CurioIcon(CurioIcons.Casino, null, tint = Color.White, size = 25.dp)
            }
            Spacer(Modifier.height(8.dp))
            Text(
                text = "CURIO · FREE · ON-DEVICE · NO ADS",
                style = MaterialTheme.typography.labelSmall.copy(
                    fontWeight = FontWeight.ExtraBold,
                    letterSpacing = 1.4.sp
                ),
                color = PromoBodyMuted,
                textAlign = TextAlign.Center
            )
        }
    }
}

/** A white-glass category chip on the rose banner — glyph + label. */
@Composable
private fun PromoChip(glyph: String, label: String, ink: Color) {
    Row(
        modifier = Modifier
            .clip(RoundedCornerShape(50))
            .background(Color.White.copy(alpha = 0.28f))
            .border(BorderStroke(1.dp, Color.White.copy(alpha = 0.55f)), RoundedCornerShape(50))
            .padding(horizontal = 12.dp, vertical = 6.dp),
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(5.dp)
    ) {
        CurioIcon(glyph, null, tint = ink, size = 14.dp)
        Text(
            label,
            style = MaterialTheme.typography.labelMedium.copy(fontWeight = FontWeight.Bold),
            color = ink
        )
    }
}

/** One of the poster's three promise rows — tinted glyph chip + title +
 *  subtitle. */
@Composable
private fun PromoPromise(glyph: String, title: String, subtitle: String) {
    Row(
        modifier = Modifier.fillMaxWidth(),
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        Box(
            modifier = Modifier
                .size(30.dp)
                .clip(CircleShape)
                .background(CurioColors.HomeRosewood.copy(alpha = 0.16f)),
            contentAlignment = Alignment.Center
        ) {
            CurioIcon(glyph, null, tint = CurioColors.HomeRosewood, size = 15.dp)
        }
        Column {
            Text(
                title,
                style = MaterialTheme.typography.titleSmall.copy(fontWeight = FontWeight.Bold),
                color = PromoBodyInk
            )
            Text(
                subtitle,
                style = MaterialTheme.typography.bodySmall,
                color = PromoBodyMuted,
                maxLines = 1
            )
        }
    }
}
