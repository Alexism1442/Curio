package com.curio.app.features.onboarding

import android.Manifest
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Build
import android.provider.Settings
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.BoxScope
import androidx.compose.foundation.layout.BoxWithConstraints
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ColumnScope
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.foundation.pager.HorizontalPager
import androidx.compose.foundation.pager.rememberPagerState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Switch
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.BiasAlignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.scale
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.core.content.ContextCompat
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleEventObserver
import androidx.lifecycle.compose.LocalLifecycleOwner
import androidx.navigation.NavController
import com.curio.app.R
import com.curio.app.data.AppPreferences
import com.curio.app.data.CategoryFamily
import com.curio.app.data.CategoryId
import com.curio.app.data.CurioCategories
import com.curio.app.features.settings.settingsReadableInk
import com.curio.app.features.settings.settingsRoseAccent
import com.curio.app.navigation.CurioRoutes
import com.curio.app.ui.components.CurioSettingsCard
import com.curio.app.ui.components.CurioSettingsDivider
import com.curio.app.ui.components.CurioWatermarkBackdrop
import com.curio.app.ui.components.MorphEntrance
import com.curio.app.ui.components.SoftTornBottomShape
import com.curio.app.ui.components.SoftTornSheetShape
import com.curio.app.ui.theme.CurioColors
import com.curio.app.ui.theme.CurioIcon
import com.curio.app.ui.theme.CurioIcons
import com.curio.app.ui.theme.isCurioDarkTheme
import com.curio.app.ui.theme.pastelFillInk
import kotlinx.coroutines.launch

/**
 * First-launch onboarding — the torn-rose family redesign.
 *
 * The screen wears the SAME hero language as Settings/Profile/Home: a solid
 * rose banner torn with the shared [SoftTornBottomShape] seam (mirrored
 * wildcard watermark collage, brand title + tagline pinned above the tear),
 * a muted watermark backdrop behind the slides, and torn-PAPER illustration
 * tiles (calm rose ink on a paper slip) instead of the old colorful gradient
 * blocks. The setup step's permission cards are borderless
 * [CurioSettingsCard] boxes with coral icon chips.
 */
@Composable
fun OnboardingScreen(navController: NavController) {
    // Intro slides + theme step + permission setup (v7.100 adds the theme
    // picker between the intros and the permissions).
    val pagerState = rememberPagerState(pageCount = { OnboardingSlides.size + 2 })
    val scope = rememberCoroutineScope()
    val context = LocalContext.current
    val isLastSlide = pagerState.currentPage == OnboardingSlides.size + 1

    // ── Setup-step permission state ───────────────────────────────────
    var notificationGranted by remember { mutableStateOf(hasNotificationPermission(context)) }
    var micGranted by remember { mutableStateOf(hasMicPermission(context)) }
    // "Display over other apps" — special access for the floating explore
    // bubble. No runtime dialog on Android 10+, so "Allow" opens the system
    // settings page; the ON_RESUME observer picks up the grant on return.
    // v7.35 — [AppPreferences.overlayActuallyUsable] (not raw canDrawOverlays):
    // an Android 15+ first-time grant can sit in the system's PENDING state
    // where canDrawOverlays() lies and no overlay ever shows — the card
    // stays "Allow" until the AppOps state actually settles (toggle off/on
    // in the system page resolves it).
    var overlayGranted by remember { mutableStateOf(AppPreferences.overlayActuallyUsable(context)) }
    // "Want the daily shuffle reminder on?" — only reachable once
    // notifications are granted; applied to prefs the moment it flips.
    var reminderWanted by rememberSaveable { mutableStateOf(false) }

    val requestNotifications = rememberLauncherForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { granted ->
        notificationGranted = granted
        // If they asked for the reminder before granting, it lands now.
        if (granted && reminderWanted) {
            AppPreferences.setReminderEnabled(context, true)
        }
    }
    val requestMic = rememberLauncherForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { granted -> micGranted = granted }
    // The result callback is empty on purpose: `StartActivityForResult`
    // fires while the settings page is still open (permission not yet
    // granted), so the ON_RESUME observer above is the real source of truth.
    val requestOverlay = rememberLauncherForActivityResult(
        ActivityResultContracts.StartActivityForResult()
    ) { _ -> }

    fun openOverlaySettings() {
        runCatching {
            requestOverlay.launch(
                Intent(
                    Settings.ACTION_MANAGE_OVERLAY_PERMISSION,
                    Uri.parse("package:${context.packageName}")
                )
            )
        }
    }

    // Re-read permission state when returning from the system Settings
    // screen — users can flip grants mid-session and the cards should
    // reflect reality the moment they come back.
    val lifecycleOwner = LocalLifecycleOwner.current
    DisposableEffect(lifecycleOwner) {
        val observer = LifecycleEventObserver { _, event ->
            if (event == Lifecycle.Event.ON_RESUME) {
                notificationGranted = hasNotificationPermission(context)
                micGranted = hasMicPermission(context)
                overlayGranted = AppPreferences.overlayActuallyUsable(context)
            }
        }
        lifecycleOwner.lifecycle.addObserver(observer)
        onDispose { lifecycleOwner.lifecycle.removeObserver(observer) }
    }

    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(MaterialTheme.colorScheme.background)
    ) {
        // ── Watermark backdrop — muted category glyphs behind the slides
        // (the Home/Profile language; the wildcard sparkle leads because
        // onboarding is category-neutral).
        CurioWatermarkBackdrop(
            activeCat = CurioCategories.byId(CategoryId.WILDCARD),
            alphaScale = 0.45f
        )
        Column(modifier = Modifier.fillMaxSize()) {
            // ── Torn-rose brand hero — the Settings/Profile family's banner:
            // solid rose, torn seam, mirrored watermark collage, and the
            // brand title + tagline pinned above the tear.
            OnboardingHero()

            // ── Slide area ─────────────────────────────────────────────
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .weight(1f)
            ) {
                HorizontalPager(
                    state = pagerState,
                    modifier = Modifier.fillMaxSize()
                ) { pageIndex ->
                    when (pageIndex) {
                        OnboardingSlides.size -> {
                            // Theme step: light / dark / system + pastel toggle.
                            MorphEntrance {
                                ThemeSlide()
                            }
                        }
                        OnboardingSlides.size + 1 -> {
                            // Final step: permission setup, not an intro slide.
                            SetupSlide(
                                notificationGranted = notificationGranted,
                                micGranted = micGranted,
                                overlayGranted = overlayGranted,
                                reminderWanted = reminderWanted,
                                onReminderChange = { wanted ->
                                    reminderWanted = wanted
                                    AppPreferences.setReminderEnabled(context, wanted)
                                },
                                onRequestNotifications = {
                                    requestNotifications.launch(Manifest.permission.POST_NOTIFICATIONS)
                                },
                                onRequestMic = {
                                    requestMic.launch(Manifest.permission.RECORD_AUDIO)
                                },
                                onRequestOverlay = { openOverlaySettings() }
                            )
                        }
                        else -> {
                            MorphEntrance {
                                OnboardingSlide(slide = OnboardingSlides[pageIndex])
                            }
                        }
                    }
                }
            }

            // ── Page dots (empty on the final setup step — keeps layout stable) ─
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(vertical = 14.dp),
                horizontalArrangement = Arrangement.Center
            ) {
                if (!isLastSlide) {
                    // One dot per intro slide + one for the theme step.
                    (0..OnboardingSlides.size).forEach { index ->
                        val selected = pagerState.currentPage == index
                        PageDot(
                            selected = selected,
                            onClick = { scope.launch { pagerState.animateScrollToPage(index) } }
                        )
                    }
                }
            }

            // ── Bottom controls ────────────────────────────────────────────────
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .navigationBarsPadding()
                    .padding(horizontal = 24.dp, vertical = 12.dp),
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.SpaceBetween
            ) {
                TextButton(onClick = { finishOnboarding(context, navController) }) {
                    Text(
                        text = "Skip",
                        style = MaterialTheme.typography.labelLarge,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                }
                Button(
                    onClick = {
                        if (isLastSlide) {
                            finishOnboarding(context, navController)
                        } else {
                            scope.launch {
                                pagerState.animateScrollToPage(pagerState.currentPage + 1)
                            }
                        }
                    },
                    shape = RoundedCornerShape(24.dp),
                    colors = ButtonDefaults.buttonColors(
                        containerColor = MaterialTheme.colorScheme.primary,
                        contentColor = MaterialTheme.colorScheme.onPrimary
                    )
                ) {
                    Text(
                        text = if (isLastSlide) "Let's go" else "Next",
                        style = MaterialTheme.typography.labelLarge
                    )
                }
            }
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// Torn-rose brand hero — the Settings/Profile banner construction, compact
// and back-button-free: the solid rose banner tears with the shared bold
// seam, a mirrored wildcard watermark collage floats on the edges, and the
// brand name + tagline are pinned just above the tear.
// ─────────────────────────────────────────────────────────────────────────────

/** Fixed tear seed — the onboarding hero always tears in the SAME pattern
 *  (its own seed; Settings wears 0x5EED, Profile 0xC0FEE). Never re-rolls. */
private const val ONBOARDING_TEAR_SEED = 0x0B0A5EED
/** Fixed tear seed for the setup slide's paper tile (same rule: stable,
 *  never re-rolls). */
private const val ONBOARDING_SETUP_TEAR_SEED = 0xACE0
/** The hero's solid body height — brand-only, so a touch slimmer than the
 *  Settings banner (which also holds the back pill). */
private val OnboardingHeroBannerHeight = 170.dp
/** Extra layout space reserved for the under-sheet below the torn banner. */
private val OnboardingHeroSheetExtent = 24.dp
/** Total hero footprint — the torn banner plus its under-sheet extent; the
 *  pager content starts just below it. */
private val OnboardingHeroTotalHeight = OnboardingHeroBannerHeight + OnboardingHeroSheetExtent

/** One mirrored hero watermark pair — the left glyph mirrors the right
 *  (the Settings/Profile hero construction). */
private data class OnboardingHeroPair(
    val biasX: Float,
    val biasY: Float,
    val size: Dp,
    val rotation: Float,
    val alpha: Float
)

@Composable
private fun OnboardingHero() {
    val heroTornShape = remember(ONBOARDING_TEAR_SEED) {
        SoftTornBottomShape(ONBOARDING_TEAR_SEED, bold = true)
    }
    val sheetShape = remember(ONBOARDING_TEAR_SEED) {
        SoftTornSheetShape(ONBOARDING_TEAR_SEED, lip = 10.dp, baseline = 14.dp, bold = true)
    }
    val fill = settingsRoseAccent()
    val ink = settingsReadableInk(fill)
    Box(
        modifier = Modifier
            .fillMaxWidth()
            .height(OnboardingHeroTotalHeight)
    ) {
        // ── Under-sheet — the theme's own background, so the tear sits on
        // the page color in every theme (the Profile construction).
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(42.dp)
                .offset(y = OnboardingHeroBannerHeight - 18.dp)
                .clip(sheetShape)
                .background(MaterialTheme.colorScheme.background)
        )
        // ── Torn-edge shadow — hairline dark rim under the seam.
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(OnboardingHeroBannerHeight)
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
                .height(OnboardingHeroBannerHeight)
        ) {
            Box(modifier = Modifier.fillMaxSize()) {
                // Mirrored watermark collage — the wildcard family's symbols
                // pop around the banner edges (Settings' exact construction).
                val symbols = CurioIcons.heroWatermarkSymbols(CategoryFamily.WILDCARD)
                val pairs = listOf(
                    OnboardingHeroPair(biasX = 0.93f, biasY = -0.82f, size = 40.dp, rotation = 10f, alpha = 0.11f),
                    OnboardingHeroPair(biasX = 0.57f, biasY = -0.60f, size = 44.dp, rotation = 8f, alpha = 0.13f),
                    OnboardingHeroPair(biasX = 0.95f, biasY = -0.10f, size = 50.dp, rotation = 14f, alpha = 0.14f),
                    OnboardingHeroPair(biasX = 0.60f, biasY = 0.44f, size = 44.dp, rotation = 10f, alpha = 0.13f),
                    OnboardingHeroPair(biasX = 0.95f, biasY = 0.80f, size = 40.dp, rotation = 6f, alpha = 0.11f)
                )
                pairs.forEachIndexed { i, pair ->
                    OnboardingHeroSymbol(
                        glyph = symbols[i * 2],
                        alignment = BiasAlignment(-pair.biasX, pair.biasY),
                        size = pair.size,
                        rotation = -pair.rotation,
                        alpha = pair.alpha,
                        tint = ink
                    )
                    OnboardingHeroSymbol(
                        glyph = symbols[i * 2 + 1],
                        alignment = BiasAlignment(pair.biasX, pair.biasY),
                        size = pair.size,
                        rotation = pair.rotation,
                        alpha = pair.alpha,
                        tint = ink
                    )
                }
                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .statusBarsPadding()
                        .padding(start = 20.dp, end = 20.dp, top = 8.dp, bottom = 14.dp)
                ) {
                    // Flex spacer — pins the brand block just above the tear.
                    Spacer(Modifier.weight(1f))
                    // ── Brand name + tagline — the onboarding identity ──
                    Column {
                        Text(
                            text = "Curio",
                            style = MaterialTheme.typography.headlineMedium.copy(fontWeight = FontWeight.ExtraBold),
                            color = ink,
                            maxLines = 1
                        )
                        Text(
                            text = stringResource(R.string.app_tagline),
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

/** One mirrored watermark glyph on the hero banner — the banner's readable
 *  ink at a soft alpha (the Settings/Profile collage construction). */
@Composable
private fun BoxScope.OnboardingHeroSymbol(
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

// ─────────────────────────────────────────────────────────────────────────────
// Torn-paper illustration tile — replaces the old colorful gradient block
// with the app's PAPER language: a soft paper slip (the theme's low surface,
// like the settings boxes) torn with the hero's seeded bottom seam, the
// slide's glyph in calm rose ink, and a whisper of watermark glyphs at the
// corners. No more loud rainbow gradient + white icon.
// ─────────────────────────────────────────────────────────────────────────────

@Composable
private fun OnboardingTile(
    glyph: String,
    seed: Int,
    size: Dp = 172.dp
) {
    val heroTornShape = remember(seed) { SoftTornBottomShape(seed, bold = true) }
    val sheetShape = remember(seed) { SoftTornSheetShape(seed, lip = 8.dp, baseline = 12.dp, bold = true) }
    val fill = settingsRoseAccent()
    // The glyph ink: the rose itself in light mode (soft pink on cream
    // paper), its readable light twin over the dark surface in dark mode.
    val glyphTint = if (isCurioDarkTheme()) pastelFillInk(fill) else fill
    Box(
        modifier = Modifier
            .size(size)
            .graphicsLayer { rotationZ = 1.5f }
    ) {
        // ── Under-sheet — the page color behind the tear.
        Box(
            modifier = Modifier
                .matchParentSize()
                .clip(sheetShape)
                .background(MaterialTheme.colorScheme.background)
        )
        // ── Torn-edge shadow — hairline dark rim under the seam.
        Box(
            modifier = Modifier
                .matchParentSize()
                .offset(y = 1.dp)
                .clip(heroTornShape)
                .background(Color.Black.copy(alpha = 0.14f))
        )
        // ── The paper slip — cream in light, soft dark in dark mode.
        Surface(
            shape = heroTornShape,
            color = MaterialTheme.colorScheme.surfaceContainerLow,
            shadowElevation = 0.dp,
            modifier = Modifier.matchParentSize()
        ) {
            Box(modifier = Modifier.fillMaxSize()) {
                // Faint watermark whispers at the corners — the collage
                // language, barely there so the main glyph reads first.
                val symbols = CurioIcons.heroWatermarkSymbols(CategoryFamily.WILDCARD)
                OnboardingTileGlyph(
                    glyph = symbols[0],
                    alignment = BiasAlignment(-0.92f, -0.92f),
                    size = size * 0.22f,
                    rotation = -8f,
                    tint = glyphTint.copy(alpha = 0.08f)
                )
                OnboardingTileGlyph(
                    glyph = symbols[2],
                    alignment = BiasAlignment(0.92f, -0.92f),
                    size = size * 0.20f,
                    rotation = 10f,
                    tint = glyphTint.copy(alpha = 0.08f)
                )
                OnboardingTileGlyph(
                    glyph = symbols[4],
                    alignment = BiasAlignment(0.94f, 0.86f),
                    size = size * 0.26f,
                    rotation = 12f,
                    tint = glyphTint.copy(alpha = 0.07f)
                )
                // ── The slide's glyph — calm rose ink on paper.
                CurioIcon(
                    name = glyph,
                    contentDescription = null,
                    tint = glyphTint,
                    size = size * 0.40f,
                    modifier = Modifier
                        .align(Alignment.Center)
                        .graphicsLayer { rotationZ = -2f }
                )
            }
        }
    }
}

/** One faint watermark glyph on the paper tile — ink at a whisper. */
@Composable
private fun BoxScope.OnboardingTileGlyph(
    glyph: String,
    alignment: Alignment,
    size: Dp,
    rotation: Float,
    tint: Color
) {
    CurioIcon(
        name = glyph,
        contentDescription = null,
        tint = tint,
        size = size,
        modifier = Modifier
            .align(alignment)
            .padding(6.dp)
            .graphicsLayer { rotationZ = rotation }
    )
}

@Composable
private fun OnboardingSlide(slide: OnboardingSlideData) {
    // The pager area sits below the torn hero, so on compact screens the
    // centered column would clip with a fixed-size tile — the tile (and
    // spacing) shrink under a height threshold to always fit.
    BoxWithConstraints(
        modifier = Modifier
            .fillMaxSize()
            .padding(horizontal = 32.dp, vertical = 8.dp),
        contentAlignment = Alignment.Center
    ) {
        val compact = maxHeight < 480.dp
        val tileSize = if (compact) 136.dp else 168.dp
        Column(
            modifier = Modifier.fillMaxWidth(),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            // ── Illustration — torn-paper tile (no more colorful gradient block) ─
            OnboardingTile(glyph = slide.glyph, seed = slide.seed, size = tileSize)

            Spacer(Modifier.height(if (compact) 16.dp else 24.dp))

            Text(
                text = slide.headline,
                style = MaterialTheme.typography.headlineMedium,
                color = MaterialTheme.colorScheme.onBackground,
                textAlign = TextAlign.Center
            )

            Spacer(Modifier.height(if (compact) 8.dp else 10.dp))

            Text(
                text = slide.subtext,
                style = MaterialTheme.typography.bodyLarge,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                textAlign = TextAlign.Center
            )
        }
    }
}

@Composable
private fun SetupSlide(
    notificationGranted: Boolean,
    micGranted: Boolean,
    overlayGranted: Boolean,
    reminderWanted: Boolean,
    onReminderChange: (Boolean) -> Unit,
    onRequestNotifications: () -> Unit,
    onRequestMic: () -> Unit,
    onRequestOverlay: () -> Unit
) {
    // Centered when the content fits, scrollable on very small screens —
    // the Box centers the scrollable column as a whole, so short content
    // stays vertically centered like the intro slides.
    Box(
        modifier = Modifier
            .fillMaxSize()
            .padding(horizontal = 24.dp, vertical = 12.dp),
        contentAlignment = Alignment.Center
    ) {
        Column(
            modifier = Modifier.verticalScroll(rememberScrollState()),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            // ── Illustration — the same torn-paper tile, smaller ──────
            OnboardingTile(
                glyph = CurioIcons.Settings,
                seed = ONBOARDING_SETUP_TEAR_SEED,
                size = 118.dp
            )

            Spacer(Modifier.height(18.dp))

            Text(
                text = "Make Curio yours",
                style = MaterialTheme.typography.headlineMedium,
                color = MaterialTheme.colorScheme.onBackground,
                textAlign = TextAlign.Center
            )

            Spacer(Modifier.height(8.dp))

            Text(
                text = "Grant what you like — you can change it anytime in Settings.",
                style = MaterialTheme.typography.bodyLarge,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                textAlign = TextAlign.Center
            )

            Spacer(Modifier.height(20.dp))

            // ── Notifications ─────────────────────────────────────────
            PermissionCard(
                glyph = CurioIcons.Notifications,
                title = "Notifications",
                subtitle = "Explore-session timer & reminders, plus the daily shuffle nudge",
                granted = notificationGranted,
                onRequest = onRequestNotifications
            ) {
                // Ask whether the daily shuffle reminder should be on —
                // only once notifications are actually granted (it can't
                // work without them). Rides INSIDE the notifications card
                // behind a divider.
                if (notificationGranted) {
                    CurioSettingsDivider()
                    ReminderRow(
                        reminderWanted = reminderWanted,
                        onReminderChange = onReminderChange
                    )
                }
            }

            Spacer(Modifier.height(10.dp))

            // ── Microphone ────────────────────────────────────────────
            PermissionCard(
                glyph = CurioIcons.Mic,
                title = "Microphone",
                subtitle = "Voice notes (Sound Bite) & voice attachments in your journal",
                granted = micGranted,
                onRequest = onRequestMic
            )

            Spacer(Modifier.height(10.dp))

            // ── Display over other apps (floating explore bubble) ─────
            PermissionCard(
                glyph = CurioIcons.BubbleChart,
                title = "Display over other apps",
                subtitle = "Floating explore bubble while you research a topic",
                granted = overlayGranted,
                onRequest = onRequestOverlay
            )
        }
    }
}

/** A borderless settings-box permission card — coral icon chip + label +
 *  Allow/Granted, the torn-family language of the Settings hub. */
@Composable
private fun PermissionCard(
    glyph: String,
    title: String,
    subtitle: String,
    granted: Boolean,
    onRequest: () -> Unit,
    extraContent: @Composable ColumnScope.() -> Unit = {}
) {
    val accent = MaterialTheme.colorScheme.primary
    CurioSettingsCard(border = null) {
        Row(
            modifier = Modifier.fillMaxWidth(),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            // ── Coral icon chip (the CurioCardHeader construction) ─────
            Box(
                modifier = Modifier
                    .size(38.dp)
                    .clip(RoundedCornerShape(14.dp))
                    .background(CurioColors.CoralBlush.copy(alpha = 0.16f)),
                contentAlignment = Alignment.Center
            ) {
                CurioIcon(
                    name = glyph,
                    contentDescription = null,
                    tint = CurioColors.CoralBlush,
                    size = 20.dp
                )
            }
            Column(modifier = Modifier.weight(1f)) {
                Text(
                    title,
                    style = MaterialTheme.typography.titleSmall.copy(fontWeight = FontWeight.SemiBold),
                    color = MaterialTheme.colorScheme.onSurface
                )
                Text(
                    subtitle,
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    maxLines = 2,
                    overflow = TextOverflow.Ellipsis
                )
            }
            if (granted) {
                Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(4.dp)
                ) {
                    CurioIcon(
                        name = CurioIcons.Check,
                        contentDescription = null,
                        tint = accent,
                        size = 16.dp
                    )
                    Text(
                        "Granted",
                        style = MaterialTheme.typography.labelMedium.copy(fontWeight = FontWeight.Bold),
                        color = accent
                    )
                }
            } else {
                Button(
                    onClick = onRequest,
                    shape = RoundedCornerShape(18.dp),
                    contentPadding = PaddingValues(horizontal = 18.dp, vertical = 10.dp),
                    colors = ButtonDefaults.buttonColors(
                        containerColor = accent,
                        contentColor = MaterialTheme.colorScheme.onPrimary
                    )
                ) {
                    Text(
                        "Allow",
                        style = MaterialTheme.typography.labelLarge
                    )
                }
            }
        }
        extraContent()
    }
}

@Composable
private fun ReminderRow(
    reminderWanted: Boolean,
    onReminderChange: (Boolean) -> Unit
) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(top = 6.dp),
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(10.dp)
    ) {
        CurioIcon(
            name = CurioIcons.Schedule,
            contentDescription = null,
            tint = MaterialTheme.colorScheme.onSurfaceVariant,
            size = 18.dp
        )
        Column(modifier = Modifier.weight(1f)) {
            Text(
                "Daily shuffle reminder",
                style = MaterialTheme.typography.bodyMedium.copy(fontWeight = FontWeight.Medium),
                color = MaterialTheme.colorScheme.onSurface
            )
            Text(
                "A gentle nudge to discover something new",
                style = MaterialTheme.typography.bodySmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
        }
        Switch(checked = reminderWanted, onCheckedChange = onReminderChange)
    }
}

/** POST_NOTIFICATIONS is a no-op below API 33 — treated as granted. */
private fun hasNotificationPermission(context: Context): Boolean =
    Build.VERSION.SDK_INT < 33 ||
        ContextCompat.checkSelfPermission(context, Manifest.permission.POST_NOTIFICATIONS) ==
        PackageManager.PERMISSION_GRANTED

private fun hasMicPermission(context: Context): Boolean =
    ContextCompat.checkSelfPermission(context, Manifest.permission.RECORD_AUDIO) ==
        PackageManager.PERMISSION_GRANTED

@Composable
private fun PageDot(selected: Boolean, onClick: () -> Unit) {
    val size = if (selected) 12.dp else 8.dp
    val color = if (selected) {
        MaterialTheme.colorScheme.primary
    } else {
        MaterialTheme.colorScheme.onSurfaceVariant.copy(alpha = 0.35f)
    }
    Box(
        modifier = Modifier
            .padding(horizontal = 4.dp)
            .size(size)
            .scale(if (selected) 1.2f else 1f)
            .background(color, shape = CircleShape)
            .clickable(onClick = onClick)
    )
}

private fun finishOnboarding(context: Context, navController: NavController) {
    CurioOnboardingState.markComplete(context)
    navController.navigate(CurioRoutes.HOME) {
        popUpTo(CurioRoutes.ONBOARDING) { inclusive = true }
        // launchSingleTop dedups the replay path: onboarding is pushed on
        // top of an existing HOME, so without it [HOME, ONBOARDING] → pops
        // onboarding → pushes a second HOME and back walks Home twice.
        launchSingleTop = true
    }
}

private data class OnboardingSlideData(
    val glyph: String,
    val headline: String,
    val subtext: String,
    val seed: Int
)

// v7.100 — intro copy rewritten around the three beats of the loop:
// shuffle → explore → keep.
private val OnboardingSlides = listOf(
    OnboardingSlideData(
        glyph = CurioIcons.Casino,
        headline = "Something new, every shuffle",
        subtext = "Spin the deck and Curio deals a topic you didn't know you'd love — a film, an album, a book, a discovery.",
        seed = 0xBEEF
    ),
    OnboardingSlideData(
        glyph = CurioIcons.AutoAwesome,
        headline = "Explore it your way",
        subtext = "Listen, read, watch, or scroll. Your explore is timed, never rushed — wander wherever curiosity leads.",
        seed = 0xF00D
    ),
    OnboardingSlideData(
        glyph = CurioIcons.Inventory2,
        headline = "Keep what moves you",
        subtext = "Voice notes, reviews, moodboards, journal pages — save what stays with you in the format that fits.",
        seed = 0xCAFE
    )
)

/** Fixed tear seed for the theme step's paper tile (stable, never re-rolls). */
private const val ONBOARDING_THEME_TEAR_SEED = 0x7E57E

/** The theme step — a simple Light / Dark / System picker and one pastel
 *  toggle, nothing else (v7.100). Applies instantly via the reactive
 *  [AppPreferences] theme state, so picking Dark flips the whole app while
 *  you look. */
@Composable
private fun ThemeSlide() {
    val context = LocalContext.current
    val mode = AppPreferences.themeModeState
    val pastel = AppPreferences.pastelColorsState
    BoxWithConstraints(
        modifier = Modifier
            .fillMaxSize()
            .padding(horizontal = 32.dp, vertical = 8.dp),
        contentAlignment = Alignment.Center
    ) {
        val compact = maxHeight < 520.dp
        val tileSize = if (compact) 100.dp else 120.dp
        Column(
            // Scrollable like the setup step — the theme row is taller than
            // the intro slides, so short screens must never clip the pastel
            // card (the Box centers the scrollable column as a whole).
            modifier = Modifier
                .fillMaxWidth()
                .verticalScroll(rememberScrollState()),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            // ── Illustration — the torn-paper tile with a palette glyph ──
            OnboardingTile(glyph = CurioIcons.Palette, seed = ONBOARDING_THEME_TEAR_SEED, size = tileSize)

            Spacer(Modifier.height(if (compact) 14.dp else 20.dp))

            Text(
                text = "Pick your look",
                style = MaterialTheme.typography.headlineMedium,
                color = MaterialTheme.colorScheme.onBackground,
                textAlign = TextAlign.Center
            )

            Spacer(Modifier.height(if (compact) 6.dp else 10.dp))

            Text(
                text = "Light, dark, or follow your phone — and keep Curio's soft pastel colors?",
                style = MaterialTheme.typography.bodyLarge,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                textAlign = TextAlign.Center
            )

            Spacer(Modifier.height(if (compact) 18.dp else 24.dp))

            // ── Mode chips — Light / Dark / System (and nothing else) ──
            Row(
                horizontalArrangement = Arrangement.spacedBy(10.dp),
                verticalAlignment = Alignment.CenterVertically
            ) {
                ThemeModeChip(
                    label = "Light",
                    glyph = CurioIcons.LightMode,
                    selected = mode == AppPreferences.THEME_LIGHT,
                    onClick = { AppPreferences.setThemeMode(context, AppPreferences.THEME_LIGHT) }
                )
                ThemeModeChip(
                    label = "Dark",
                    glyph = CurioIcons.DarkMode,
                    selected = mode == AppPreferences.THEME_DARK,
                    onClick = { AppPreferences.setThemeMode(context, AppPreferences.THEME_DARK) }
                )
                ThemeModeChip(
                    label = "System",
                    glyph = CurioIcons.Contrast,
                    selected = mode == AppPreferences.THEME_SYSTEM,
                    onClick = { AppPreferences.setThemeMode(context, AppPreferences.THEME_SYSTEM) }
                )
            }

            Spacer(Modifier.height(if (compact) 14.dp else 18.dp))

            // ── Pastel toggle — borderless box, the setup-card language ──
            CurioSettingsCard(border = null) {
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(12.dp)
                ) {
                    CurioIcon(
                        name = CurioIcons.Palette,
                        contentDescription = null,
                        tint = MaterialTheme.colorScheme.onSurfaceVariant,
                        size = 20.dp
                    )
                    Column(modifier = Modifier.weight(1f)) {
                        Text(
                            "Pastel colors",
                            style = MaterialTheme.typography.bodyMedium.copy(fontWeight = FontWeight.SemiBold),
                            color = MaterialTheme.colorScheme.onSurface
                        )
                        Text(
                            "Soft pastel accents instead of deep tones",
                            style = MaterialTheme.typography.bodySmall,
                            color = MaterialTheme.colorScheme.onSurfaceVariant
                        )
                    }
                    Switch(
                        checked = pastel,
                        onCheckedChange = { AppPreferences.setPastelColorsEnabled(context, it) }
                    )
                }
            }
        }
    }
}

/** One mode chip in the theme picker — filled with the primary color when
 *  selected, a soft surface with a hairline rim otherwise. */
@Composable
private fun ThemeModeChip(
    label: String,
    glyph: String,
    selected: Boolean,
    onClick: () -> Unit
) {
    Surface(
        onClick = onClick,
        shape = RoundedCornerShape(50),
        color = if (selected) MaterialTheme.colorScheme.primary else MaterialTheme.colorScheme.surfaceContainerLow,
        border = if (selected) null else BorderStroke(1.dp, MaterialTheme.colorScheme.outlineVariant)
    ) {
        Row(
            modifier = Modifier.padding(horizontal = 14.dp, vertical = 10.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(6.dp)
        ) {
            CurioIcon(
                name = glyph,
                contentDescription = null,
                tint = if (selected) MaterialTheme.colorScheme.onPrimary else MaterialTheme.colorScheme.onSurfaceVariant,
                size = 16.dp
            )
            Text(
                text = label,
                style = MaterialTheme.typography.labelLarge.copy(fontWeight = FontWeight.Bold),
                color = if (selected) MaterialTheme.colorScheme.onPrimary else MaterialTheme.colorScheme.onSurface
            )
        }
    }
}

object CurioOnboardingState {
    private const val PREFS = "curio_onboarding"
    private const val KEY_COMPLETE = "complete"

    fun isComplete(context: Context): Boolean =
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            .getBoolean(KEY_COMPLETE, false)

    fun markComplete(context: Context) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            .edit()
            .putBoolean(KEY_COMPLETE, true)
            .apply()
    }

    fun reset(context: Context) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            .edit()
            .putBoolean(KEY_COMPLETE, false)
            .apply()
    }
}
