---
name: prbf2-draft-announcement
description: Draft Project Reality BF2 release announcements, update highlights, and community news posts in BBCode for the RealityMod Announcements & Highlights forum. Use when the user asks to write a game update post, major version release announcement, patch highlights, seasonal update, or community announcement for PR:BF2.
---

# PR:BF2 Announcement & Update Highlights Drafter

Draft community-facing release announcements, patch highlights, and seasonal or milestone updates for Project Reality: Battlefield 2 (PR:BF2) formatted in phpBB BBCode for the RealityMod Announcements & Highlights forum.

## When to Use

- Announcing a major version release (e.g., `Project Reality: BF2 vX.Y Released!`).
- Drafting a minor patch or seasonal update showcase (e.g., `vX.Y.Z - Update Highlights`).
- Writing a community milestone, Q&A, or multi-part pre-release teaser ("Road to..." series).

## Workflow

1. **Determine Post Type**:
    - **Major Release**: Full celebration post with community milestones, release trailer, thematic feature spotlights, `KEY FEATURES` list, changelog link, and full download/support/server/donation footer.
    - **Update Highlights / Seasonal**: Focused spotlight on new maps, weapons, vehicles, or seasonal changes, followed by a standard closing and social/forum call to action.
2. **Gather Inputs**: Collect version number, release date, headline factions/maps (with sizes and gamemodes), notable vehicles/weapons, key bug fixes or shader/QoL changes, trailer URL, and changelog thread URL. Ask only for missing core facts.
3. **Load References & Template**:
    - Read `references/announcement-guidelines.md` for tone, title conventions, and required footer sections.
    - Read `references/bbcode-syntax-reference.md` for valid BBCode tag syntax.
    - Use `assets/major-release-template.md` for major releases or `assets/update-highlights-template.md` for minor/seasonal updates.
4. **Draft in BBCode & Verify**:
    - Keep highlight sections player-oriented and engaging, pairing each new faction, map, or vehicle group with `[img]<SCREENSHOT_URL>[/img]` placeholders.
    - Keep the `[b]KEY FEATURES:[/b]` block scannable using `[list]` and `[*]` with concise `Added ...` / `Implemented ...` lines.
    - Format all links with `[url=<URL>]<Label>[/url]` and headings with `[size=...][b]...[/b][/size]`.
    - Include all required resource links and the team sign-off (`- The Project Reality Team`).
5. **Output Format**:
    - Present the entire announcement inside a **single fenced code block** (```` ```bbcode ````) so developers can copy and paste it directly into the RealityMod forum.

## Gotchas

- Never output raw Markdown formatting inside the BBCode snippet; use `[b]`, `[i]`, `[size]`, `[url=...]`, `[img]`, `[youtube]`, and `[list]` per `references/bbcode-syntax-reference.md`.
- Never omit the link to the full Changelog thread on major release posts.
- Always state clearly in the donation section that contributions cover infrastructure and website costs only, never team member pay.
- Credit individual contributors or developers by handle with their `[R-DEV]` / `[R-CON]` / `[R-COM]` tags when provided.
