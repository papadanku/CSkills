
# Project Reality Branding Specification

Official reference specification extracted from the `project-reality-branding` skill, grounded in the Project Reality developer branding guidelines ([Forum Thread](https://forum.realitymod.org/viewtopic.php?t=156071)) and official Project Reality properties ([Main Website](https://www.realitymod.org/), [Project Reality Manual](https://www.realitymod.org/manual/en/), and [RealityDocs](https://realitymod.gitlab.io/public/RealityDocs/)).

## 1. Typography

- **Primary Display Font (`Bebas Neue`):** Sans-serif, neo-grotesque typeface. Use for launcher menus (e.g., `PLAY`, `MANUAL`, `OPTIONS`), promotional titles, watermarks, banners, and uppercase display headers. Source: [Google Fonts: Bebas Neue](https://fonts.google.com/specimen/Bebas+Neue)
- **Alternative / Multilingual Font (`League Gothic`):** Use whenever lowercase characters or broader language/diacritic support are needed, since `Bebas Neue` is uppercase-focused and lacks lowercase glyphs and extended diacritics. Source: [Google Fonts: League Gothic](https://fonts.google.com/specimen/League+Gothic)
- **UI Body and Documentation Font (Neutral Sans-Serif):** Use a clean, neutral sans-serif for settings labels, navigation links, form inputs, and long-form documentation prose (as seen in the PR:BF2 Options dialog, HonKit Manual, and RealityDocs). Do **not** apply `Bebas Neue` or `League Gothic` to long-form prose or dense settings forms.
- **Code and Technical Font (Monospace):** Use monospace for file paths, inline code pills, logs, and keyboard shortcuts.

## 2. Core Brand and Surface Palette

### Brand and Media Colors

- **Reality Gray (`#171717`):** Primary dark background for web pages, HonKit manual, and screenshot watermarks.
- **Reality White (`#FFFFFF`):** Primary headings, foreground text, watermark lettering, and high-contrast desktop input/dropdown/checkbox backgrounds.
- **Reality Blue (`#3DA0EC`):** Primary brand accent, links, header titles, highlights, active states, and description callouts.

### Surface Hierarchy (Web, Docs, and Desktop)

- **Web / HonKit Manual Base Canvas (`#171717`):** Primary dark background.
- **Sphinx / Technical Docs Deep Doc Canvas (`#111113`):** Optional ultra-dark surface tier for dense technical documentation (RealityDocs).
- **Sphinx / Technical Docs Top Nav and Elevated Cards (`#1E1F24`):** Elevated header bar and card surfaces (RealityDocs).
- **Sphinx / Technical Docs Inline Code Pill (`#102746`):** Background tint with light blue/white monospace text (RealityDocs).
- **Desktop Utility Dialogs Titlebar (`#111111`):** Window titlebar surface (PR:BF2 Options pattern).
- **Desktop Utility Dialogs Outer Window Frame (`#222222`):** Outer dialog container background (PR:BF2 Options pattern).
- **Desktop Utility Dialogs Inner Tabbed Panel (`#333333`):** Inner panel surface with 1px muted-gray borders and horizontal section dividers (PR:BF2 Options pattern).
- **Desktop / Theme Panel Borders and Dividers (`#555555`):** 1px subtle muted-gray borders.
- **Secondary / Muted Text (`#B3B3B3`):** Muted text tier stepped down from `#FFFFFF`.

### Interactive and Action Blues

- **Action / Primary Button Blue (`#2A90C3` to `#206694`):** Primary action buttons (`Apply`, `Close`, `Reset All Profiles`) in desktop dialogs.
- **Active Navigation Pill (`#2D789F`):** Solid fill for active sidebar/navigation items (e.g., HonKit Manual active page).

## 3. Team Member Role Colors

Use these colors **strictly** for role badges, contributor tags, author labels, and on-screen/UI credits (never as arbitrary decorative UI accents):

- **Lead Developer Blue (`#206694`):** Recommended CSS token `--pr-role-lead-dev: #206694`
- **Developer Blue (`#3498DB`):** Recommended CSS token `--pr-role-dev: #3498DB`
- **Retired Cyan (`#11806A`):** Recommended CSS token `--pr-role-retired: #11806A`
- **Tech Support Orange (`#A84300`):** Recommended CSS token `--pr-role-support: #A84300`
- **Contributor Violet (`#9B59B6`):** Recommended CSS token `--pr-role-contributor: #9B59B6`
- **Tester Orange (`#A08536`):** Recommended CSS token `--pr-role-tester: #A08536`
- **Community Green (`#1F8B4C`):** Recommended CSS token `--pr-role-community: #1F8B4C`

## 4. Logo and Iconography

- **Primary Logo:** Official Project Reality logo (`Project_Reality_logo_256.png` or official high-resolution asset).
- **Desktop Titlebar Icon:** Metallic PR dog-tag / shield icon for desktop window titlebars.
- **Integrity:** Preserve the original aspect ratio without stretching, skewing, or recoloring.
- **Placement and Clear Space:** Place over `#171717`, `#111111`, or clean dark/neutral regions with clear padding around the mark.

## 5. Layout, Component, and Media Specifications

### Desktop Launcher (Key-Art Layout)

- **Background:** Full-bleed atmospheric battlefield key art.
- **Primary Menu:** Right-aligned vertical menu in uppercase `Bebas Neue`, with `PLAY` emphasized larger above secondary items (`MANUAL`, `OPTIONS`, `SUPPORT`, `CREDITS`, `DONATE`, `EXIT`).
- **Social Links:** Top-left vertical stack of dark square social icon buttons.
- **News Ticker:** Bottom-left condensed display ticker; must sanitize/decode HTML entities (e.g., `&amp;`) before rendering.

### Desktop Utility Dialogs (Options / Settings)

- **Chrome and Panels:** Layered dark charcoal (`#111111` titlebar, `#222222` frame, `#333333` tabbed panel) with 1px muted borders and horizontal section dividers.
- **Form Controls:** Maintain strong contrast, such as `#FFFFFF` rounded inputs, dropdowns, and checkboxes with dark text (or high-contrast dark inputs with crisp borders).
- **Action Buttons:** `#2A90C3` to `#206694` blue fills for primary actions (`Reset All Profiles`, `Apply`, `Close`).

### Visual Content (Promotional Images, Screenshots, and Videos)

- **Watermarks and Overlays:** Watermarks, title cards, lower-thirds, and description bars use `#171717` backgrounds, `#FFFFFF` primary text, and `#3DA0EC` accents.
- **Overlay Typography:** `Bebas Neue` for uppercase titles/watermarks; `League Gothic` where lowercase or extended character sets are required.
- **Role Attributions:** On-screen credits for developers, testers, or contributors use the corresponding Team Member Role color.
- **Visual Tone:** Clean, sharp, and grounded in Project Reality's combined-arms tactical aesthetic (*"Realistic Gaming Redefined"*) rather than cluttered or neon-arcade styles.

## 6. Contrast and Implementation Constraints

- **Role Blue vs. Brand Blue:** Do not confuse Developer Blue (`#3498DB`) or Lead Developer Blue (`#206694`) with Reality Blue (`#3DA0EC`). Reserve `#3DA0EC` for general brand accents and `#2A90C3` to `#2D789F` for active buttons/pills.
- **Dark-on-Dark Contrast:** Darker role colors (`#11806A`, `#206694`, `#A84300`, `#1F8B4C`) lose legibility as thin text on `#171717`. Render them as solid pill/badge fills with `#FFFFFF` label text.
- **Faux-Lowercase Prohibition:** Never force faux-lowercase or mismatched fallback fonts in place of `Bebas Neue`; switch to `League Gothic` when lowercase or non-ASCII characters are required.
