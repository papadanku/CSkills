---
name: prbf2-branding-manager
description: Audit, review, and apply Project Reality brand guidelines across software GUIs, UI themes, desktop launchers, web documentation, promotional images, screenshots, and videos. Use when the user asks to review an app interface or promotional media for Project Reality brand compliance, check colors/fonts/logos against Project Reality standards, or restyle/theme software UIs (CSS, Tailwind, Qt, Electron, React, Sphinx, HonKit, etc.) using Project Reality's official visual identity.
---

# Project Reality Branding

Maintain, audit, and apply the official Project Reality visual identity across desktop software, web platforms, and promotional media, grounded in the developer branding guidelines (https://forum.realitymod.org/viewtopic.php?t=156071) and official Project Reality properties (https://www.realitymod.org/, https://www.realitymod.org/manual/en/, and https://realitymod.gitlab.io/public/RealityDocs/).

## When to Use

- Reviewing desktop applications (such as launchers, options dialogs, or overlays) and web apps/docs for Project Reality brand alignment.
- Reviewing visual content such as promotional images, screenshots, thumbnails, trailers, and videos for watermark, typography, logo, and color compliance.
- Changing or building graphical interface themes for software to match Project Reality's official dark-first palette, surface hierarchy, and typography.

## Official Brand Tokens

### Typography

- **Primary Display Font:** `Bebas Neue` (sans-serif, neo-grotesque). Use for launcher menus (e.g., `PLAY`, `MANUAL`, `OPTIONS`), promotional titles, watermarks, and uppercase display headers. Source: https://fonts.google.com/specimen/Bebas+Neue
- **Alternative / Multilingual Font:** `League Gothic`. Use whenever lowercase characters or broader language/diacritic support are needed, since Bebas Neue is uppercase-focused. Source: https://fonts.google.com/specimen/League+Gothic
- **UI Body and Documentation Font:** Use a clean, neutral sans-serif for settings labels, navigation links, and long-form documentation prose (as seen in the PR Options dialog, HonKit Manual, and RealityDocs). Use monospace for file paths, code pills, and keyboard shortcuts.

### Core Brand and Surface Palette

- **Reality Gray:** `#171717` - Primary dark background for web pages, HonKit manual, and screenshot watermarks.
- **Deep Doc Canvas:** `#111113` (with `#1E1F24` top nav/cards) - Optional ultra-dark surface tier for dense technical documentation (RealityDocs).
- **Desktop Dialog Surfaces:** `#111111` titlebar, `#222222` outer window frame, and `#333333` inner tabbed panel with 1px muted-gray borders and horizontal section dividers (PR:BF2 Options pattern).
- **Reality White:** `#FFFFFF` - Primary headings, foreground text, watermark lettering, and high-contrast desktop input/dropdown/checkbox backgrounds.
- **Reality Blue:** `#3DA0EC` - Primary brand accent, links, header titles, and description callouts.
- **Action / Active Blue:** `#2A90C3` to `#206694` (and `#2D789F` active sidebar pills) - Used for primary action buttons (`Apply`, `Close`, `Reset All Profiles`) and active navigation highlights.
- **Inline Code Pill (Dark Docs):** `#102746` background tint with light blue/white monospace text.

### Team Member Role Colors

Use these colors strictly for role badges, contributor tags, author labels, and credits:

- **Lead Developer Blue:** `#206694`
- **Developer Blue:** `#3498DB`
- **Retired Cyan:** `#11806A`
- **Tech Support Orange:** `#A84300`
- **Contributor Violet:** `#9B59B6`
- **Tester Orange:** `#A08536`
- **Community Green:** `#1F8B4C`

### Logo and Iconography

- Use the official Project Reality logo (`Project_Reality_logo_256.png`) or the metallic PR dog-tag/shield icon for desktop window titlebars.
- Preserve the original aspect ratio without stretching, skewing, or recoloring.
- Place the logo over `#171717`, `#111111`, or clean dark/neutral regions with clear padding around the mark.

## Workflows

### 1. Reviewing Software Graphical Interfaces (Desktop and Web)

1. **Inspect Surface Hierarchy:**
    - Web and documentation apps should anchor on `#171717` (or `#111113` / `#1E1F24` for Sphinx/technical docs) with `#FFFFFF` headings and `#3DA0EC` links/nav accents.
    - Desktop utility dialogs should follow the `#111111` titlebar, `#222222` frame, `#333333` panel pattern with subtle 1px borders and clean section dividers.
2. **Audit Interactive Controls:**
    - Check that primary action buttons and active sidebar items use `#3DA0EC` or `#2A90C3`–`#2D789F` steel-blue tones.
    - In desktop settings dialogs, verify inputs/dropdowns/checkboxes maintain strong contrast (such as `#FFFFFF` controls with dark text, or high-contrast dark inputs with crisp borders).
3. **Audit Launcher Key-Art Layouts:**
    - If reviewing a full-bleed launcher screen, verify right-aligned `Bebas Neue` uppercase menu items (`PLAY` emphasized larger), top-left dark square social icon buttons, and a bottom-left condensed news ticker.
    - Flag rendering bugs such as unescaped HTML entities (e.g., `&amp;`) in news tickers or feeds.
4. **Audit Role and Status Colors:** Check that `#206694`, `#3498DB`, `#11806A`, `#A84300`, `#9B59B6`, `#A08536`, and `#1F8B4C` are used accurately for team roles rather than arbitrary decorative accents.
5. **Verify Typography and Contrast:** Confirm display headers use `Bebas Neue` (or `League Gothic` for lowercase/multilingual), while dense settings/docs use readable sans-serif/monospace. Render dark role colors (`#206694`, `#11806A`, `#A84300`, `#1F8B4C`) as solid pills with `#FFFFFF` text.
6. **Report Findings:** Present a concise findings table with columns: `Component`, `Current Value`, `Guideline`, `Severity`, and `Recommended Fix`.

### 2. Reviewing Visual Content (Images, Screenshots, Videos)

1. **Check Watermark and Overlay Palette:** Confirm watermarks, title cards, lower-thirds, and description bars use `#171717` backgrounds, `#FFFFFF` primary text, and `#3DA0EC` accents.
2. **Audit Typeface Usage:** Verify `Bebas Neue` is used for uppercase titles/watermarks and `League Gothic` is used where lowercase or extended character sets are required.
3. **Inspect Logo Placement:** Confirm the Project Reality logo is uncropped, undistorted, and legible against its background.
4. **Check Role Attributions:** If developers, testers, or contributors are credited on-screen, verify their names or badges use the matching Team Member Role color.
5. **Assess Visual Tone:** Ensure overlays look clean, sharp, and grounded in Project Reality's combined-arms tactical aesthetic ("Realistic Gaming Redefined") rather than cluttered or neon-arcade styles.

### 3. Changing Software GUI Themes

1. **Detect the Theme System:** Locate the project's styling layer (CSS custom properties, Tailwind config, SCSS variables, Qt QSS, GTK CSS, Sphinx/HonKit CSS, React theme object, or ImGui palette).
2. **Map Core Tokens:**
    - Web / Media base background: `#171717` (or `#111113` with `#1E1F24` header for Sphinx/technical docs)
    - Desktop dialog surfaces: `#111111` titlebar, `#222222` frame, `#333333` inner panel, `#555555` 1px borders
    - Primary foreground/text: `#FFFFFF`
    - Muted secondary text: `#B3B3B3`
    - Primary accent, links, and highlights: `#3DA0EC`
    - Primary buttons and active nav pills: `#2A90C3` to `#206694` (or `#2D789F` solid fill)
    - Inline code badge (dark docs): `#102746` background
3. **Map Role Tokens:** Expose all seven role colors (`--pr-role-lead-dev: #206694`, `--pr-role-dev: #3498DB`, `--pr-role-retired: #11806A`, `--pr-role-support: #A84300`, `--pr-role-contributor: #9B59B6`, `--pr-role-tester: #A08536`, `--pr-role-community: #1F8B4C`) for user/staff badges.
4. **Configure Fonts:** Import or bundle `Bebas Neue` (and `League Gothic` for lowercase/multilingual support) for display headers/launcher menus, and pair with a clean neutral sans-serif for body/settings text and monospace for code.
5. **Validate Changes:** Build or run the UI check, verify there are no broken font imports, unescaped HTML entities, or unreadable text-on-background pairs, and summarize the updated tokens.

## Gotchas

- **Bebas Neue Case and Language Limits:** Standard Bebas Neue lacks lowercase letters and extended diacritics. Switch to `League Gothic` instead of forcing faux-lowercase or mismatched fallback fonts.
- **Display Font vs. Body Readability:** Do not apply `Bebas Neue` or `League Gothic` to long-form documentation prose or dense settings forms; reserve them for display headers, launcher menus, and watermarks.
- **Role Blue vs. Brand Blue:** Do not mix up Developer Blue (`#3498DB`) or Lead Developer Blue (`#206694`) with Reality Blue (`#3DA0EC`). Use `#3DA0EC` for general brand accents and `#2A90C3`–`#2D789F` for active buttons/pills.
- **Dark-on-Dark Contrast:** Role colors like `#11806A`, `#206694`, and `#A84300` can lose legibility as thin text on `#171717`. Prefer solid role pills with `#FFFFFF` label text.
- **Unescaped Ticker Text:** Always sanitize/decode HTML entities (such as `&amp;`) in news tickers fed from web RSS/blog endpoints.
