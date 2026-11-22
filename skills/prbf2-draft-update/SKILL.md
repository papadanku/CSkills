---
name: prbf2-draft-update
description: Draft Project Reality BF2 Developer Blogs and technical development updates for the RealityMod Development Blogs forum. Use when the user asks to write a dev blog, development update, feature deep-dive, multi-part technical showcase, or behind-the-scenes post for PR:BF2.
---

# PR:BF2 Developer Blog Drafter

Draft technical, behind-the-scenes Developer Blogs for Project Reality: Battlefield 2 (PR:BF2) matching the style of the RealityMod Development Blogs forum.

## When to Use

- Writing a new Developer Blog post (single-part or multi-part series such as "Part 1/3").
- Turning developer notes, PRs, design docs, or technical experiments into a community-facing dev blog.
- Drafting a showcase for new mechanics, shaders, animations, maps, vehicles, or open-source tooling.

## Workflow

1. **Gather Inputs**: Identify the topic, target audience (players vs. modders), author handle/role, whether it is part of a multi-part series, and any media placeholders (YouTube embeds, screenshots, diagrams). Ask the user only for missing core technical details or design rationale.
2. **Load References & Template**:
    - Read `references/style-and-structure.md` for tone, technical depth, and PR branding rules.
    - Read `references/bbcode-syntax-reference.md` when drafting or converting posts to BBCode for direct phpBB forum posting.
    - Read `assets/dev-blog-template.md` (or `assets/dev-blog-bbcode-template.md` if the user wants phpBB BBCode for direct forum posting).
3. **Draft the Post**:
    - Open with a friendly greeting (`Hello, everyone!` or `Hey everyone,`) and brief context on the feature or series.
    - State the core problem or motivation clearly before diving into the solution.
    - Include an upfront `Acknowledgements` or `Scope & Caveats` subsection if there are known limitations, temporary behaviors, or deferred changes.
    - Break the technical explanation into scannable subsections that connect implementation details (algorithms, parameters, asset pipelines) directly to gameplay impact.
    - Place clear `[IMAGE: ...]` or `[VIDEO: ...]` media markers where screenshots, comparisons, or clips belong (or `[img]` / `[youtube]` tags when using BBCode).
    - Close with a brief thank-you and personal or team sign-off (`- <Author>` or `- The Project Reality Team`).
4. **Verify**: Check against `references/style-and-structure.md` (and `references/bbcode-syntax-reference.md` when outputting BBCode) before presenting the draft.

## Gotchas

- Avoid vague marketing hype; PR:BF2 readers expect concrete mechanical explanations, trade-offs, and honest caveats.
- Do not dump raw code or changelogs verbatim. Summarize *why* a system was built and *how* it changes player experience.
- Keep media placeholders descriptive so colleagues know which screenshots or clips to capture.
