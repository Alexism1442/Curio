from pathlib import Path

p = Path("app/src/main/java/com/curio/app/features/cabinet/CabinetScreen.kt")
text = p.read_text(encoding="utf-8")

start_marker = "        // \u2500\u2500 Top bar"
end_marker = "        // \u2500\u2500 Filter chip row"

si = text.index(start_marker)
ei = text.index(end_marker)

new_block = """        // \u2500\u2500 Torn rose hero banner \u2014 the Profile/Settings hero-card language,
        // with the Cabinet's own fixed tear seed. The title + subtitle sit
        // pinned just above the tear and the search/sort/select pills ride
        // the banner's top row as ink-glass pills so they read on the rose.
        val cabinetTitle = when {
            selectionMode -> "${selectedEntryIds.size} selected"
            showLegacyOnly -> "Legacy Cabinet"
            else -> "The Cabinet"
        }
        val cabinetSubtitle = when {
            selectionMode -> "Long-press cards to select \u00b7 ${if (showLegacyOnly) "legacy" else "current filter"}"
            showLegacyOnly -> "Restored FieldMind records"
            else -> selectedFilter?.let { "Showing ${CurioCategories.byId(it).displayName}" } ?: "Your saved captures"
        }
        CabinetHeroHeader(
            title = cabinetTitle,
            subtitle = cabinetSubtitle,
            sheetColor = filterCat?.categoryBackgroundWash() ?: MaterialTheme.colorScheme.background,
            backVisible = selectedFilter != null || showLegacyOnly,
            onBack = { selectedFilter = null; showLegacyOnly = false }
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
            } else if (!searchActive) {
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
                    contentDescription = if (sortNewestFirst) "Newest first \u2014 tap for oldest" else "Oldest first \u2014 tap for newest",
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
        if (searchActive) {
            // Search mode \u2014 a real filter bar below the hero narrows the grid
            // by topic name / custom title. Auto-focus pulls the keyboard up
            // the moment it expands.
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(horizontal = 16.dp, top = 14.dp),
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                OutlinedTextField(
                    value = searchQuery,
                    onValueChange = { searchQuery = it },
                    placeholder = { Text("Search captures\u2026") },
                    leadingIcon = {
                        CurioIcon(CurioIcons.Search, null, size = 20.dp)
                    },
                    trailingIcon = {
                        if (searchQuery.isNotEmpty()) {
                            IconButton(onClick = { searchQuery = "" }) {
                                CurioIcon(CurioIcons.Close, "Clear search", size = 20.dp)
                            }
                        }
                    },
                    singleLine = true,
                    shape = RoundedCornerShape(50),
                    keyboardOptions = KeyboardOptions(imeAction = ImeAction.Search),
                    keyboardActions = KeyboardActions(onSearch = {}),
                    modifier = Modifier
                        .weight(1f)
                        .focusRequester(searchFocus)
                )
                Surface(
                    onClick = {
                        searchActive = false
                        searchQuery = ""
                    },
                    shape = RoundedCornerShape(50),
                    color = MaterialTheme.colorScheme.surfaceVariant,
                    border = BorderStroke(1.dp, MaterialTheme.colorScheme.outlineVariant)
                ) {
                    CurioIcon(
                        name = CurioIcons.Close,
                        contentDescription = "Close search",
                        tint = MaterialTheme.colorScheme.onSurface,
                        size = 24.dp,
                        modifier = Modifier.padding(8.dp)
                    )
                }
            }
        }

        // \u2500\u2500 Filter chip row"""

text = text[:si] + new_block + text[ei:]
p.write_text(text, encoding="utf-8")
print("cabinet top bar replaced OK")
