package com.curio.app.features.cabinet

import androidx.compose.animation.animateColorAsState
import androidx.compose.animation.core.FastOutSlowInEasing
import androidx.compose.animation.core.tween
import androidx.compose.foundation.BorderStroke
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
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.TextButton
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyGridState
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.items
import androidx.compose.foundation.lazy.grid.rememberLazyGridState
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.OutlinedTextFieldDefaults
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.derivedStateOf
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.produceState
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.Saver
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.Alignment
import androidx.compose.ui.BiasAlignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.focus.FocusRequester
import androidx.compose.ui.focus.focusRequester
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.graphics.lerp
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import kotlinx.coroutines.launch
import com.curio.app.data.CategoryFamily
import com.curio.app.data.CategoryId
import com.curio.app.data.CurioCategories
import com.curio.app.data.CurioEntry
import com.curio.app.data.CurioRepositoryHolder
import com.curio.app.data.AudioStorageManager
import com.curio.app.data.ImageStorageManager
import com.curio.app.features.settings.settingsReadableInk
import com.curio.app.features.settings.settingsRoseAccent
import com.curio.app.navigation.CurioRoutes
import com.curio.app.navigation.navigateToTab
import com.curio.app.ui.components.CurioBackButton
import com.curio.app.ui.components.CurioEmptyState
import com.curio.app.ui.components.CurioNavTint
import com.curio.app.ui.components.CurioWatermarkBackdrop
import com.curio.app.ui.components.CurioEntryCard
import com.curio.app.ui.components.MorphEntrance
import com.curio.app.ui.components.SoftTornBottomShape
import com.curio.app.ui.components.SoftTornSheetShape
import com.curio.app.ui.theme.CurioIcon
import com.curio.app.ui.theme.CurioIcons
import com.curio.app.ui.theme.CurioMotion
import com.curio.app.ui.theme.isCurioDarkTheme
import com.curio.app.ui.theme.categoryBackgroundWash
import com.curio.app.ui.theme.categoryBorder
import com.curio.app.ui.theme.categoryChipSurface
import com.curio.app.ui.theme.categoryInk
import com.curio.app.ui.theme.themedAccent

/**
 * The Cabinet — see Curio design contract. Library of saved captures.
 *
 * Upgraded with:
 *  - Entry cards render at once (no per-item stagger)
 *  - MorphEntrance for empty state content
 */
/**
 * Process-local identity for Cabinet filter state. The object remains stable
 * through recomposition, rotation and in-session tab restoration, but a fresh
 * app process receives a new identity so rememberSaveable intentionally
 * discards the previous filter and opens on "All".
 */
private object CabinetSessionToken

/**
 * Saves the active Cabinet filter chip by enum name; "All" (null) stays
 * null through an empty-string sentinel, surviving rotation and navigation
 * within the current app process.
 */
private val CategoryIdSaver = Saver<CategoryId?, String>(
    save = { it?.name ?: "" },
    restore = { name ->
        name.takeIf { it.isNotEmpty() }
            ?.let { n -> CategoryId.values().firstOrNull { it.name == n } }
    }
)

@Composable
fun CabinetScreen(navController: NavController) {
    var selectedFilter by rememberSaveable(CabinetSessionToken, stateSaver = CategoryIdSaver) {
        mutableStateOf<CategoryId?>(null)
    }
    var showLegacyOnly by rememberSaveable(CabinetSessionToken) { mutableStateOf(false) }
    // Saveable-backed scroll state — the grid keeps its position on rotation.
    val gridState = rememberLazyGridState()

    // Search + sort — the search button expands into a real filter bar
    // (matches by topic name or custom title, case-insensitive), and the
    // sort button toggles newest-first / oldest-first by capture time.
    var searchActive by rememberSaveable { mutableStateOf(false) }
    var searchQuery by rememberSaveable { mutableStateOf("") }
    var sortNewestFirst by rememberSaveable { mutableStateOf(true) }
    var selectionMode by rememberSaveable { mutableStateOf(false) }
    var selectedEntryIds by rememberSaveable { mutableStateOf<Set<String>>(emptySet()) }
    var showBulkDeleteConfirm by rememberSaveable { mutableStateOf(false) }
    val deleteScope = rememberCoroutineScope()
    val context = androidx.compose.ui.platform.LocalContext.current
    val searchFocus = remember { FocusRequester() }
    LaunchedEffect(searchActive) {
        if (searchActive) {
            searchFocus.requestFocus()
        }
    }

    val entries by produceState<List<CurioEntry>>(initialValue = emptyList()) {
        try {
            CurioRepositoryHolder.repo.observeAll().collect { value = it }
        } catch (_: Exception) {
            value = emptyList()
        }
    }

    val visibleEntries = remember(entries, selectedFilter, showLegacyOnly, searchQuery, sortNewestFirst) {
        val q = searchQuery.trim()
        var result = if (selectedFilter == null) entries
            else entries.filter { it.topic.categoryId == selectedFilter }
        // Legacy captures live in their own Cabinet section. The normal
        // Cabinet never mixes restored FieldMind records with native Curio
        // captures; selecting Legacy is the explicit opt-in view.
        result = if (showLegacyOnly) result.filter { it.isLegacy }
                 else result.filterNot { it.isLegacy }
        if (q.isNotEmpty()) {
            result = result.filter {
                it.topic.name.contains(q, ignoreCase = true) ||
                    it.title?.contains(q, ignoreCase = true) == true ||
                    // v7.17 — custom tags are searchable too.
                    it.tags.any { tag -> tag.contains(q, ignoreCase = true) }
            }
        }
        if (sortNewestFirst) result.sortedByDescending { it.capturedAtMillis }
        else result.sortedBy { it.capturedAtMillis }
    }

    val categorySelectionIds = visibleEntries.map { it.id }.toSet()
    LaunchedEffect(selectedFilter, showLegacyOnly, searchQuery) {
        selectedEntryIds = selectedEntryIds.intersect(categorySelectionIds)
        if (selectedEntryIds.isEmpty()) selectionMode = false
    }
    val allVisibleSelected = categorySelectionIds.isNotEmpty() &&
        categorySelectionIds.all { it in selectedEntryIds }

    if (showBulkDeleteConfirm) {
        AlertDialog(
            onDismissRequest = { showBulkDeleteConfirm = false },
            title = { Text("Delete selected captures?", fontWeight = FontWeight.Bold) },
            text = { Text("This permanently deletes ${selectedEntryIds.size} selected capture(s), including their attached media.") },
            confirmButton = {
                TextButton(onClick = {
                    showBulkDeleteConfirm = false
                    val ids = selectedEntryIds.toList()
                    deleteScope.launch {
                        val selectedEntries = entries.filter { it.id in ids }
                        val deleted = runCatching {
                            CurioRepositoryHolder.repo.deleteByIds(ids)
                        }.isSuccess
                        if (deleted) {
                            selectedEntries.forEach { entry ->
                                entry.captureData.audioFilePaths().forEach { path ->
                                    AudioStorageManager.deleteAudio(context, path)
                                }
                                ImageStorageManager.deleteImagesForEntry(context, entry.id)
                            }
                            selectedEntryIds = emptySet()
                            selectionMode = false
                        }
                    }
                }) { Text("Delete", color = MaterialTheme.colorScheme.error, fontWeight = FontWeight.Bold) }
            },
            dismissButton = {
                TextButton(onClick = { showBulkDeleteConfirm = false }) { Text("Cancel") }
            }
        )
    }

    // The Cabinet wears the active filter's category wash — the same tinted
    // background as the filters page — ONLY while a category filter is
    // active. The "All" page stays on the plain theme background (like Home),
    // and the search button keeps its neutral look in every state.
    val filterCat = selectedFilter?.let { CurioCategories.byId(it) }
    // Publish the active filter's wash so the Scaffold-level bottom bar can
    // blend with the tinted Cabinet page (mirrors Spin's CurioNavTint
    // handoff — the bar lives outside the NavHost and can't read this
    // screen's state directly). Null on "All" so the bar stays plain.
    val cabinetWash = filterCat?.categoryBackgroundWash()
    LaunchedEffect(cabinetWash) {
        CurioNavTint.publishCabinetWash(cabinetWash)
    }
    // Hygiene: clear the handoff when the Cabinet leaves composition so a
    // stale wash never lingers for another tab.
    DisposableEffect(Unit) {
        onDispose { CurioNavTint.publishCabinetWash(null) }
    }

    // The hero banner runs up BEHIND the status bar (it applies its own
    // status-bar inset), so the root Box carries no status-bar padding.
    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(filterCat?.categoryBackgroundWash() ?: MaterialTheme.colorScheme.background)
    ) {
        // Muted category-glyph watermark behind the grid — the same
        // backdrop language as Home / Spin / the saved-entry page, so the
        // Cabinet reads as part of the app's paper-and-glyph world. The
        // backdrop is deliberately STATIC (always the wildcard scatter): if
        // the emphasis followed the active filter, the highlighted glyph
        // would jump to a different position on every page switch — the
        // "shifting watermark". Fixed, so switching All / categories /
        // Legacy never moves a glyph; the active category is already
        // carried by the page wash, the chip row and the card tints.
        // v7.77 — the flat grid sits directly on this backdrop, so the
        // glyphs stay a faint whisper and the cards always read first.
        CurioWatermarkBackdrop(
            activeCat = CurioCategories.byId(CategoryId.WILDCARD),
            modifier = Modifier.fillMaxSize(),
            alphaScale = 0.45f
        )
        Column(
            modifier = Modifier.fillMaxSize()
        ) {
        // ── Grid or empty state — the scroll content fills the screen and
        // runs UNDER the torn hero banner and the sticky chip bar (both are
        // drawn on top in this root Box), so cards disappear under the
        // ragged tear and the pinned chips as they scroll — the settings
        // overlay pattern.
        if (visibleEntries.isEmpty()) {
            Box(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(top = CabinetContentTop)
            ) {
            MorphEntrance {
                if (searchActive && searchQuery.isNotBlank()) {
                    // Live search came up empty — tell the user what didn't
                    // match (and that the keyboard is still up, ready to edit).
                    CurioEmptyState(
                        glyph = CurioIcons.SearchOff,
                        headline = "No captures match",
                        subtext = "Nothing in the Cabinet matches \"${searchQuery.trim()}\". Try a different name.",
                        tint = MaterialTheme.colorScheme.tertiary.copy(alpha = 0.4f),
                        ctaLabel = "Clear search",
                        onCtaClick = {
                            searchQuery = ""
                            searchActive = false
                        }
                    )
                } else if (showLegacyOnly) {
                    CurioEmptyState(
                        glyph = CurioIcons.History,
                        headline = "No legacy captures yet",
                        subtext = "Restore a FieldMind archive from Settings to keep old observations separate from Curio.",
                        tint = MaterialTheme.colorScheme.tertiary.copy(alpha = 0.4f),
                        ctaLabel = "Open settings",
                        onCtaClick = { navController.navigate(CurioRoutes.SETTINGS) { launchSingleTop = true } }
                    )
                } else if (selectedFilter == null && !showLegacyOnly) {
                    CurioEmptyState(
                        glyph = CurioIcons.Inventory2,
                        headline = "Your Cabinet is empty",
                        subtext = "Everything you save will live here. Shuffle to find your first one.",
                        tint = MaterialTheme.colorScheme.tertiary.copy(alpha = 0.4f),
                        ctaLabel = "Discover something",
                        onCtaClick = {
                            // Tab switch (not a plain push): Cabinet is itself
                            // a tab, so pushing spin on top of it would leave a
                            // hybrid back stack — back would walk into Cabinet
                            // and tab switches would pile up duplicates. Anchor
                            // to HOME like every other Spin launch in the app.
                            navController.navigateToTab(CurioRoutes.SPIN)
                        }
                    )
                } else {
                    val filterId = selectedFilter ?: CategoryId.WILDCARD
                    val cat = CurioCategories.byId(filterId)
                    CurioEmptyState(
                        glyph = CurioIcons.SearchOff,
                        headline = "No ${cat.displayName} captures yet",
                        subtext = "Shuffle for ${cat.displayName} to find your first one.",
                        tint = cat.categoryInk().copy(alpha = 0.4f),
                        ctaLabel = "Shuffle for ${cat.displayName}",
                        onCtaClick = {
                            // Same tab-switch contract as the "All" empty state
                            // (and Home's quest cards): anchor to HOME so the
                            // Shuffle tab replaces Cabinet instead of stacking
                            // a spin/… entry on top of the Cabinet tab entry.
                            navController.navigateToTab(
                                CurioRoutes.spinWithCategory(cat.id.routeSlug)
                            )
                        }
                    )
                }
            }
            }
        } else {
            LazyVerticalGrid(
                state = gridState,
                columns = GridCells.Fixed(2),
                contentPadding = PaddingValues(
                    start = 16.dp,
                    end = 16.dp,
                    top = CabinetContentTop,
                    bottom = 24.dp
                ),
                horizontalArrangement = Arrangement.spacedBy(12.dp),
                verticalArrangement = Arrangement.spacedBy(12.dp),
                modifier = Modifier.fillMaxSize()
            ) {
                items(visibleEntries, key = { it.id }) { entry ->
                    CurioEntryCard(
                        entry = entry,
                        selected = entry.id in selectedEntryIds,
                        onLongClick = {
                            selectionMode = true
                            selectedEntryIds = selectedEntryIds + entry.id
                        },
                        onClick = {
                            if (selectionMode) {
                                selectedEntryIds = if (entry.id in selectedEntryIds) {
                                    selectedEntryIds - entry.id
                                } else {
                                    selectedEntryIds + entry.id
                                }
                            } else {
                                navController.navigate(
                                    CurioRoutes.entryDetail(entry.id)
                                ) { launchSingleTop = true }
                            }
                        }
                    )
                }
            }
        }
        }

        // ── Sticky filter chip bar — drawn ON TOP of the scroll content.
        // As the grid scrolls the bar lifts, pops (0.97 → 1.0) and frosts in
        // (Profile's pill mechanism), pinning just below the ragged tear
        // while the entry cards pass underneath it.
        CabinetStickyChipBar(
            gridState = gridState,
            entries = entries,
            selectedFilter = selectedFilter,
            showLegacyOnly = showLegacyOnly,
            onSelectAll = { selectedFilter = null; showLegacyOnly = false },
            onSelectCategory = { selectedFilter = it; showLegacyOnly = false },
            onToggleLegacy = { selectedFilter = null; showLegacyOnly = !showLegacyOnly }
        )

        // ── Torn rose hero banner — drawn ON TOP of the scroll content; the
        // search field expands INSIDE the banner when search is active. The
        // title + subtitle sit pinned just above the tear and the
        // search/sort/select pills ride the banner's top row as ink-glass
        // pills (replaced by a Cancel pill while searching).
        val cabinetTitle = when {
            selectionMode -> "${selectedEntryIds.size} selected"
            showLegacyOnly -> "Legacy Cabinet"
            else -> "The Cabinet"
        }
        val cabinetSubtitle = when {
            selectionMode -> "Long-press cards to select · ${if (showLegacyOnly) "legacy" else "current filter"}"
            showLegacyOnly -> "Restored FieldMind records"
            else -> selectedFilter?.let { "Showing ${CurioCategories.byId(it).displayName}" } ?: "Your saved captures"
        }
        CabinetHeroHeader(
            title = cabinetTitle,
            subtitle = cabinetSubtitle,
            sheetColor = filterCat?.categoryBackgroundWash() ?: MaterialTheme.colorScheme.background,
            backVisible = selectedFilter != null || showLegacyOnly,
            onBack = { selectedFilter = null; showLegacyOnly = false },
            searchActive = searchActive,
            searchQuery = searchQuery,
            onSearchQueryChange = { searchQuery = it },
            onCloseSearch = { searchActive = false; searchQuery = "" },
            searchFocus = searchFocus
        ) { ink ->
            if (selectionMode) {
                CabinetHeroActionPill(
                    onClick = {
                        selectedEntryIds = if (allVisibleSelected) {
                            selectedEntryIds - categorySelectionIds
                        } else {
                            selectedEntryIds + categorySelectionIds
                        }
                    },
                    label = if (allVisibleSelected) "Clear" else "Select all",
                    ink = ink,
                    emphasized = true
                )
                CabinetHeroActionPill(
                    onClick = {
                        if (selectedEntryIds.isNotEmpty()) showBulkDeleteConfirm = true
                    },
                    label = "Delete (${selectedEntryIds.size})",
                    ink = ink,
                    emphasized = true,
                    destructive = true
                )
                CabinetHeroActionPill(
                    onClick = { selectionMode = false; selectedEntryIds = emptySet() },
                    glyph = CurioIcons.Close,
                    contentDescription = "Cancel selection",
                    ink = ink
                )
            } else {
                CabinetHeroActionPill(
                    onClick = {
                        selectionMode = true
                        selectedEntryIds = emptySet()
                    },
                    label = "Select",
                    ink = ink
                )
                CabinetHeroActionPill(
                    onClick = { sortNewestFirst = !sortNewestFirst },
                    glyph = if (sortNewestFirst) CurioIcons.ArrowDownward else CurioIcons.ArrowUpward,
                    contentDescription = if (sortNewestFirst) "Newest first — tap for oldest" else "Oldest first — tap for newest",
                    ink = ink,
                    emphasized = sortNewestFirst
                )
                CabinetHeroActionPill(
                    onClick = { searchActive = true },
                    glyph = CurioIcons.Search,
                    contentDescription = "Search captures",
                    ink = ink
                )
            }
        }
    }
}

// ══════════════════════════════════════════════════════════════════════════════════════════════════════════
// Torn rose hero banner — the Profile/Settings hero-card language, with
// the Cabinet's own fixed tear seed. Title + subtitle pinned just above
// the tear; the top row carries the back pill (when a filter/legacy view
// is active) and the search/sort/select action pills as ink-glass pills.
// ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

/** The hero banner's solid body height — compact, like the settings hero. */
private val CabinetHeroBannerHeight = 180.dp
/** Extra layout space reserved for the under-sheet below the torn banner. */
private val CabinetHeroSheetExtent = 24.dp
/** Total header footprint — the torn banner plus its under-sheet extent. */
private val CabinetHeroTotalHeight = CabinetHeroBannerHeight + CabinetHeroSheetExtent
/** Fixed tear seed — the Cabinet tears in its own bold pattern, never re-rolls. */
private const val CABINET_TEAR_SEED = 0xCAB1E

// ── Sticky filter chip bar ──────────────────────────────────────────────
// The chip row is a scroll-reactive overlay (like Profile's pinned pills):
// it rests below the hero, then lifts, pops (0.97 → 1.0) and frosts in as
// the grid scrolls, pinning just below the ragged tear while the entry
// cards pass underneath it.
/** Where the chip bar rests below the hero (its unpinned spot). */
private val CabinetChipBarRestTop = CabinetHeroTotalHeight + 10.dp
/** Where the chip bar pins when scrolled — just below the ragged tear. */
private val CabinetChipBarPinnedTop = CabinetHeroTotalHeight + 2.dp
/** Scroll distance (dp) before the chip bar fully pins (Profile pill style). */
private val CabinetChipStickyThreshold = 56.dp
/** The chip bar's layout height — scroll content starts below it. */
private val CabinetChipBarHeight = 52.dp
/** Top content padding — hero + chip bar + breathing room. */
private val CabinetContentTop = CabinetHeroTotalHeight + CabinetChipBarHeight + 18.dp

/** One mirrored hero watermark pair (the settings/profile collage). */
private data class CabinetHeroPair(
    val biasX: Float,
    val biasY: Float,
    val size: Dp,
    val rotation: Float,
    val alpha: Float
)

/**
 * The Cabinet's torn rose hero banner — the shared Profile/Settings
 * construction: a solid rose banner with the same bold SoftTorn tear and a
 * theme-matched under-sheet, the mirrored wildcard watermark collage, the
 * back pill (when a filter/legacy view is active) and the caller-provided
 * action pills riding the top row, and the title + subtitle pinned just
 * above the tear. Runs up behind the status bar; [sheetColor] lets the
 * under-sheet match the page (the category tint wash when a filter is on).
 */
@Composable
private fun CabinetHeroHeader(
    title: String,
    subtitle: String,
    sheetColor: Color,
    backVisible: Boolean,
    onBack: () -> Unit,
    searchActive: Boolean,
    searchQuery: String,
    onSearchQueryChange: (String) -> Unit,
    onCloseSearch: () -> Unit,
    searchFocus: FocusRequester,
    trailing: @Composable (ink: Color) -> Unit
) {
    val heroTornShape = remember(CABINET_TEAR_SEED) { SoftTornBottomShape(CABINET_TEAR_SEED, bold = true) }
    val sheetShape = remember(CABINET_TEAR_SEED) {
        SoftTornSheetShape(CABINET_TEAR_SEED, lip = 10.dp, baseline = 14.dp, bold = true)
    }
    val fill = settingsRoseAccent()
    val ink = settingsReadableInk(fill)
    Box(
        modifier = Modifier
            .fillMaxWidth()
            .height(CabinetHeroTotalHeight)
    ) {
        // ── Under-sheet — the page's own color (tint wash when a filter is
        // active), so the tear sits on the page in every state.
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(42.dp)
                .offset(y = CabinetHeroBannerHeight - 18.dp)
                .clip(sheetShape)
                .background(sheetColor)
        )
        // ── Torn-edge shadow — hairline dark rim under the seam.
        Box(
            modifier = Modifier
                .fillMaxWidth()
                .height(CabinetHeroBannerHeight)
                .offset(y = 1.dp)
                .clip(heroTornShape)
                .background(Color.Black.copy(alpha = 0.20f))
        )
        // ── Solid rose banner, torn bottom edge — shares the exact rose
        // family as Profile/Settings (settingsRoseAccent).
        Surface(
            shape = heroTornShape,
            color = fill,
            shadowElevation = 0.dp,
            modifier = Modifier
                .fillMaxWidth()
                .height(CabinetHeroBannerHeight)
        ) {
            Box(modifier = Modifier.fillMaxSize()) {
                // Mirrored watermark collage — the wildcard family's symbols
                // pop around the banner edges (the settings/profile collage).
                val symbols = CurioIcons.heroWatermarkSymbols(CategoryFamily.WILDCARD)
                val pairs = listOf(
                    CabinetHeroPair(biasX = 0.93f, biasY = -0.85f, size = 44.dp, rotation = 12f, alpha = 0.11f),
                    CabinetHeroPair(biasX = 0.55f, biasY = -0.64f, size = 48.dp, rotation = 8f, alpha = 0.13f),
                    CabinetHeroPair(biasX = 0.94f, biasY = -0.12f, size = 56.dp, rotation = 14f, alpha = 0.14f),
                    CabinetHeroPair(biasX = 0.56f, biasY = 0.54f, size = 50.dp, rotation = 10f, alpha = 0.13f),
                    CabinetHeroPair(biasX = 0.94f, biasY = 0.80f, size = 44.dp, rotation = 6f, alpha = 0.11f)
                )
                pairs.forEachIndexed { i, pair ->
                    CabinetHeroSymbol(symbols[i * 2], BiasAlignment(-pair.biasX, pair.biasY), pair.size, -pair.rotation, pair.alpha, ink)
                    CabinetHeroSymbol(symbols[i * 2 + 1], BiasAlignment(pair.biasX, pair.biasY), pair.size, pair.rotation, pair.alpha, ink)
                }
                Column(
                    modifier = Modifier
                        .fillMaxSize()
                        .statusBarsPadding()
                        .padding(start = 20.dp, end = 20.dp, top = 10.dp, bottom = 16.dp)
                ) {
                    // ── Top row — back pill (when needed) + action pills ──
                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        verticalAlignment = Alignment.CenterVertically,
                        horizontalArrangement = Arrangement.SpaceBetween
                    ) {
                        if (backVisible) {
                            CurioBackButton(
                                onClick = onBack,
                                containerColor = ink.copy(alpha = 0.18f),
                                contentColor = ink,
                                disableRipple = true
                            )
                        } else {
                            // Balance the row when there's no back pill.
                            Spacer(Modifier.size(42.dp))
                        }
                        if (searchActive) {
                            // Search is open — the top row holds just the
                            // Cancel pill (the action pills are hidden).
                            CabinetHeroActionPill(
                                onClick = onCloseSearch,
                                label = "Cancel",
                                glyph = CurioIcons.Close,
                                contentDescription = "Close search",
                                ink = ink
                            )
                        } else {
                            Row(
                                horizontalArrangement = Arrangement.spacedBy(8.dp),
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                trailing(ink)
                            }
                        }
                    }
                    // Flex spacer — pins the title block just above the tear.
                    Spacer(Modifier.weight(1f))
                    // ── Search field (open inside the hero) or the Cabinet's
                    // title + subtitle, pinned just above the tear ──
                    if (searchActive) {
                        OutlinedTextField(
                            value = searchQuery,
                            onValueChange = onSearchQueryChange,
                            placeholder = { Text("Search captures…") },
                            leadingIcon = {
                                CurioIcon(CurioIcons.Search, null, tint = ink, size = 20.dp)
                            },
                            trailingIcon = {
                                if (searchQuery.isNotEmpty()) {
                                    IconButton(onClick = { onSearchQueryChange("") }) {
                                        CurioIcon(
                                            CurioIcons.Close,
                                            "Clear search",
                                            tint = ink.copy(alpha = 0.85f),
                                            size = 20.dp
                                        )
                                    }
                                }
                            },
                            singleLine = true,
                            shape = RoundedCornerShape(50),
                            textStyle = MaterialTheme.typography.bodyLarge.copy(color = ink),
                            keyboardOptions = KeyboardOptions(imeAction = ImeAction.Search),
                            keyboardActions = KeyboardActions(onSearch = {}),
                            colors = OutlinedTextFieldDefaults.colors(
                                focusedContainerColor = ink.copy(alpha = 0.16f),
                                unfocusedContainerColor = ink.copy(alpha = 0.16f),
                                focusedBorderColor = ink.copy(alpha = 0.55f),
                                unfocusedBorderColor = ink.copy(alpha = 0.30f),
                                cursorColor = ink,
                                focusedTextColor = ink,
                                unfocusedTextColor = ink,
                                focusedPlaceholderColor = ink.copy(alpha = 0.72f),
                                unfocusedPlaceholderColor = ink.copy(alpha = 0.72f),
                                focusedLeadingIconColor = ink,
                                unfocusedLeadingIconColor = ink,
                                focusedTrailingIconColor = ink.copy(alpha = 0.85f),
                                unfocusedTrailingIconColor = ink.copy(alpha = 0.85f)
                            ),
                            modifier = Modifier
                                .fillMaxWidth()
                                .focusRequester(searchFocus)
                        )
                    } else {
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
}

/**
 * The Cabinet's filter chip row, drawn ON TOP of the scroll content.
 *
 * Scroll-reactive, like Profile's pinned pills: as the grid scrolls, the
 * row pops (scale 0.97 → 1.0, eased), lifts a few dp, and a frosted pill
 * surface morphs in behind the chips (transparent → frosted with a hairline
 * rim + shadow). It pins just below the hero's ragged tear, and the entry
 * cards scroll underneath it.
 */
@Composable
private fun BoxScope.CabinetStickyChipBar(
    gridState: LazyGridState,
    entries: List<CurioEntry>,
    selectedFilter: CategoryId?,
    showLegacyOnly: Boolean,
    onSelectAll: () -> Unit,
    onSelectCategory: (CategoryId) -> Unit,
    onToggleLegacy: () -> Unit
) {
    // Scroll-reactive lift — the chips pop + frost as the first card row
    // approaches them and pin once it reaches the bar, so the lift is tied
    // to the cards actually arriving (not raw scroll offset, which would
    // include the grid's large top content padding). Progress reads the
    // first visible card row's top edge inside the viewport: it starts at
    // the content top (~274dp) and falls as the user scrolls.
    val thresholdPx = with(LocalDensity.current) { CabinetChipStickyThreshold.toPx() }
    val barBottomPx = with(LocalDensity.current) { (CabinetChipBarRestTop + CabinetChipBarHeight).toPx() }
    val progress by remember {
        derivedStateOf {
            val first = gridState.layoutInfo.visibleItemsInfo.firstOrNull()
            if (first == null) 0f
            else ((barBottomPx - first.offset) / thresholdPx).coerceIn(0f, 1f)
        }
    }
    val frostShift = FastOutSlowInEasing.transform(progress)
    val popScale = androidx.compose.ui.util.lerp(0.97f, 1f, frostShift)
    val stickyDark = isCurioDarkTheme()
    // Resting state = no bar (the chips float on the page wash); scrolled
    // state = a solid frosted pill bar — the Profile pill morph.
    val restBg = Color.Transparent
    val frostBg = if (stickyDark) Color(0xFF23242C).copy(alpha = 0.94f) else Color.White.copy(alpha = 0.94f)
    val restRim = Color.Transparent
    val frostRim = if (stickyDark) Color.White.copy(alpha = 0.16f) else Color(0xFFD9DEE6)
    // Resolve solid target colors from scroll, then animate the paint.
    val targetBarBg = lerp(restBg, frostBg, frostShift)
    val targetBarRim = lerp(restRim, frostRim, frostShift)
    val barBg by animateColorAsState(
        targetValue = targetBarBg,
        animationSpec = tween(CurioMotion.Durations.Quick),
        label = "cabinetChipBarBackground"
    )
    val barRim by animateColorAsState(
        targetValue = targetBarRim,
        animationSpec = tween(CurioMotion.Durations.Quick),
        label = "cabinetChipBarRim"
    )
    val liftPx = with(LocalDensity.current) { (CabinetChipBarRestTop - CabinetChipBarPinnedTop).toPx() }

    Surface(
        shape = RoundedCornerShape(50),
        color = barBg,
        border = if (frostShift > 0.02f) BorderStroke(1.dp, barRim) else null,
        shadowElevation = 8.dp * frostShift,
        modifier = Modifier
            .align(Alignment.TopStart)
            .fillMaxWidth()
            .padding(horizontal = 16.dp)
            .offset(y = CabinetChipBarRestTop)
            .graphicsLayer {
                translationY = -liftPx * frostShift
                scaleX = popScale
                scaleY = popScale
            }
    ) {
        val hasLegacyEntries = entries.any { it.isLegacy }
        LazyRow(
            contentPadding = PaddingValues(horizontal = 10.dp),
            horizontalArrangement = Arrangement.spacedBy(8.dp),
            modifier = Modifier.padding(vertical = 6.dp)
        ) {
            item("all") {
                FilterChipLite(
                    label = "All",
                    accent = MaterialTheme.colorScheme.primary,
                    tint = MaterialTheme.colorScheme.primaryContainer,
                    ink = MaterialTheme.colorScheme.onPrimaryContainer,
                    chipSurface = MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.6f),
                    chipBorder = BorderStroke(1.dp, MaterialTheme.colorScheme.outlineVariant),
                    selected = selectedFilter == null && !showLegacyOnly,
                    onClick = onSelectAll
                )
            }
            items(CurioCategories.visible) { cat ->
                FilterChipLite(
                    label = cat.displayName,
                    accent = cat.themedAccent(),
                    tint = cat.tint,
                    // The button (label text) never adapts to the category —
                    // it stays on the neutral theme ink in every state, so
                    // only the background carries the tint.
                    ink = MaterialTheme.colorScheme.onSurfaceVariant,
                    chipSurface = cat.categoryChipSurface(MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.6f)),
                    chipBorder = cat.categoryBorder(
                        fallback = BorderStroke(1.dp, MaterialTheme.colorScheme.outlineVariant)
                    ),
                    selected = selectedFilter == cat.id && !showLegacyOnly,
                    onClick = { onSelectCategory(cat.id) }
                )
            }
            // Legacy sits LAST, after every native category — and only when
            // there's something to show (or the legacy view is currently
            // open, so the active chip stays visible/deselectable).
            if (hasLegacyEntries || showLegacyOnly) {
                item("legacy") {
                    FilterChipLite(
                        label = "Legacy",
                        accent = MaterialTheme.colorScheme.tertiary,
                        tint = MaterialTheme.colorScheme.tertiaryContainer,
                        ink = MaterialTheme.colorScheme.onTertiaryContainer,
                        chipSurface = MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.6f),
                        chipBorder = BorderStroke(1.dp, MaterialTheme.colorScheme.outlineVariant),
                        selected = showLegacyOnly,
                        onClick = onToggleLegacy
                    )
                }
            }
        }
    }
}

/** One mirrored watermark glyph on the Cabinet hero (settings/profile style). */
@Composable
private fun BoxScope.CabinetHeroSymbol(
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

/** One ink-glass action pill on the Cabinet hero — the banner's readable
 *  ink at a soft alpha (the Profile edit-pill language), so the Select /
 *  Sort / Search / selection buttons read on the rose in every theme.
 *  [emphasized] deepens the fill for the active/primary state;
 *  [destructive] deepens it further for the delete action. */
@Composable
private fun CabinetHeroActionPill(
    onClick: () -> Unit,
    ink: Color,
    label: String? = null,
    glyph: String? = null,
    contentDescription: String? = null,
    emphasized: Boolean = false,
    destructive: Boolean = false
) {
    val fill = when {
        destructive -> ink.copy(alpha = 0.55f)
        emphasized -> ink.copy(alpha = 0.42f)
        else -> ink.copy(alpha = 0.18f)
    }
    Surface(
        onClick = onClick,
        shape = RoundedCornerShape(50),
        color = fill,
        border = BorderStroke(1.dp, ink.copy(alpha = 0.28f)),
        shadowElevation = 0.dp
    ) {
        Row(
            modifier = Modifier.padding(horizontal = 11.dp, vertical = 8.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(5.dp)
        ) {
            if (glyph != null) {
                CurioIcon(
                    name = glyph,
                    contentDescription = contentDescription,
                    tint = ink,
                    size = 18.dp
                )
            }
            if (label != null) {
                Text(
                    label,
                    style = MaterialTheme.typography.labelLarge.copy(fontWeight = FontWeight.Bold),
                    color = ink
                )
            }
        }
    }
}

@Composable
private fun FilterChipLite(
    label: String,
    accent: Color,
    tint: Color,
    ink: Color,
    chipSurface: Color = MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.6f),
    chipBorder: BorderStroke? = null,
    selected: Boolean,
    onClick: () -> Unit
) {
    Surface(
        onClick = onClick,
        shape = RoundedCornerShape(50),
        color = if (selected) tint else chipSurface,
        border = if (selected) null else chipBorder
    ) {
        Text(
            text = label,
            style = MaterialTheme.typography.labelLarge,
            color = if (selected) ink else MaterialTheme.colorScheme.onSurfaceVariant,
            modifier = Modifier.padding(horizontal = 16.dp, vertical = 8.dp)
        )
    }
}
