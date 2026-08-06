package com.curio.app.features.settings

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.curio.app.data.CategoryId
import com.curio.app.data.CurioCategories
import com.curio.app.navigation.CurioRoutes
import com.curio.app.ui.components.CurioBackButton
import com.curio.app.ui.components.CurioCardHeader
import com.curio.app.ui.components.CurioSectionLabel
import com.curio.app.ui.components.CurioSettingsDivider
import com.curio.app.ui.components.CurioSettingsRow
import com.curio.app.ui.components.CurioTornCard
import com.curio.app.ui.components.CurioWatermarkBackdrop
import com.curio.app.ui.components.ScreenEntrance
import com.curio.app.ui.theme.CurioIcons

/** Fixed tear seed for the shared settings header — its torn seam never
 *  re-rolls, so every settings screen's header tears identically. */
private const val SETTINGS_HEADER_TEAR_SEED = 0x5EED

/** Compact hub for the redesigned settings experience — the tear family's
 *  watermark backdrop behind everything, a small torn-card header, and torn
 *  paper section cards. */
@Composable
fun SettingsHubScreen(navController: NavController) {
    Box(modifier = Modifier.fillMaxSize()) {
        // ── Watermark backdrop — muted category glyphs behind the content
        // (the Home/Spin language). Settings is category-neutral, so the
        // wildcard sparkle leads the collage.
        CurioWatermarkBackdrop(
            activeCat = CurioCategories.byId(CategoryId.WILDCARD)
        )
        Column(
            modifier = Modifier
                .fillMaxSize()
                .statusBarsPadding()
        ) {
            SettingsHeader(
                title = "Settings",
                subtitle = "Tune Curio your way",
                onBack = { navController.popBackStack() }
            )
            ScreenEntrance {
                LazyColumn(
                    modifier = Modifier.fillMaxSize(),
                    contentPadding = PaddingValues(start = 16.dp, end = 16.dp, top = 8.dp, bottom = 24.dp),
                    verticalArrangement = Arrangement.spacedBy(10.dp)
                ) {
                    item { CurioSectionLabel("Personalize") }
                    item {
                        CurioTornCard(seed = 0x11) {
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
                        CurioTornCard(seed = 0x12) {
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
                        CurioTornCard(seed = 0x13) {
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

/**
 * The settings top bar — a SMALL TORN CARD (the family's tear language):
 * a cream slip with rounded top corners and a soft torn bottom seam, with
 * the back button, title and subtitle inside. Shared by every settings
 * screen so the whole Settings family wears the same torn-card header.
 */
@Composable
fun SettingsHeader(
    title: String,
    subtitle: String,
    onBack: () -> Unit
) {
    CurioTornCard(
        seed = SETTINGS_HEADER_TEAR_SEED,
        modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 16.dp, vertical = 4.dp),
        contentPadding = PaddingValues(horizontal = 14.dp, vertical = 10.dp)
    ) {
        Row(
            modifier = Modifier.fillMaxWidth(),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(10.dp)
        ) {
            CurioBackButton(onClick = onBack)
            Column(modifier = Modifier.weight(1f)) {
                Text(title, style = MaterialTheme.typography.headlineSmall.copy(fontWeight = FontWeight.ExtraBold))
                Text(subtitle, style = MaterialTheme.typography.labelMedium, color = MaterialTheme.colorScheme.onSurfaceVariant)
            }
        }
    }
}
