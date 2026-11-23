---
name: prbf2-draft-changelog
description: Draft structured, versioned Project Reality BF2 changelogs and hotfix notes in BBCode for the RealityMod Changelogs forum. Use when the user asks to write, format, or organize a PR:BF2 changelog, patch notes, hotfix list, or release notes from commit logs or developer notes.
---

# PR:BF2 Changelog Drafter

Draft clean, standardized changelogs for Project Reality: Battlefield 2 (PR:BF2) major releases and hotfixes formatted in phpBB BBCode for the RealityMod Changelogs forum.

## When to Use

- Compiling a full major-version changelog (e.g., `PR:BF2 vX.Y.0.0 Changelog`).
- Drafting a hotfix or incremental patch changelog (e.g., `PR:BF2 vX.Y.0.1 Changelog`) to prepend to an existing release thread.
- Converting raw Git/SVN commit messages, QA notes, or developer bullet lists into formatted PR:BF2 patch notes.

## Workflow

1. **Gather Inputs**: Collect the exact 4-part version number (`vX.Y.Z.W`), release date (`YYYY/MM/DD`), whether it is a major release or a hotfix, and the raw list of changes.
2. **Load References & Template**:
    - Read `references/changelog-spec.md` for category order, verb conventions, and level/layer formatting rules.
    - Read `references/bbcode-syntax-reference.md` for valid BBCode tag syntax.
    - Read `assets/changelog-template.md` for the exact BBCode structural layout.
3. **Categorize & Normalize Entries**:
    - Sort changes into the canonical top-level categories (`General`, `COOP`, `Effects`, `Menu`, `Soldiers`, `Statics`, `Sounds`, `Vehicles`, `Weapons`, `Kits`, `Shaders`, `Levels`). Omit any category that has no changes.
    - Start every line with a capitalized past-tense verb (`Added`, `Updated`, `Improved`, `Fixed`, `Removed`, `Replaced`, `Reduced`, `Increased`, `Reverted`, `Optimized`) and end with a period.
    - Under `Levels:`, place global map additions/removals under `General:`, followed by affected maps in alphabetical order. Prefix layer-specific changes with the layer tag (e.g., `AAS16:`, `AAS32 & AAS64:`, `INS64:`, `COOP32:`).
    - Format headings with `[b]` or `[size=...][b]` and lists with `[list]` and `[*]` according to `references/bbcode-syntax-reference.md`.
4. **Add Framing & Footer (Major Releases)**:
    - For major `.0.0` releases, include a brief intro paragraph summarizing headline content and inviting QA Tester applications, plus a `[b]KEY FEATURES:[/b]` block if appropriate.
    - For hotfixes, prepend the new `PR:BF2 vX.Y.Z.W Changelog (YYYY/MM/DD)` block cleanly without repeating the full major-release intro.
    - Close major release posts with the standard `Support Project Reality!` and `- The Project Reality Team` footer.
5. **Output Format**:
    - Present the entire changelog inside a **single fenced code block** (```` ```bbcode ````) so developers can copy and paste it directly into the RealityMod forum.

## Gotchas

- Never output raw Markdown formatting inside the BBCode snippet; use `[b]`, `[url=...]`, `[list]`, and `[*]` per `references/bbcode-syntax-reference.md`.
- Never invent map names, layer sizes, vehicle variants, or bug fixes not present in the user's notes.
- Group multiple changes on the same map layer under that map's subsection rather than scattering them under `General:`.
