---
name: prbf2-draft-update
description: Draft Project Reality BF2 Developer Blogs and technical development updates in BBCode for the RealityMod Development Blogs forum. Use when the user asks to write a dev blog, development update, feature deep-dive, multi-part technical showcase, or behind-the-scenes post for PR:BF2.
---

# PR:BF2 Developer Blog Drafter

Draft technical, behind-the-scenes Developer Blogs for Project Reality: Battlefield 2 (PR:BF2) formatted in phpBB BBCode for the RealityMod Development Blogs forum.

## When to Use

- Writing a new Developer Blog post (single-part or multi-part series such as "Part 1/3").
- Turning developer notes, PRs, design docs, or technical experiments into a community-facing dev blog.
- Drafting a showcase for new mechanics, shaders, animations, maps, vehicles, or open-source tooling.

## Workflow

1. **Gather Inputs**: Identify the topic, target audience (players vs. modders), author handle/role, whether it is part of a multi-part series, and any media placeholders (YouTube embeds, screenshots, diagrams). Ask the user only for missing core technical details or design rationale.
2. **Load References & Template**:
    - Read `references/style-and-structure.md` for tone, technical depth, and PR branding rules.
    - Read `references/bbcode-syntax-reference.md` for valid BBCode tag syntax.
    - Read `assets/dev-blog-template.md` for the BBCode post structure.
3. **Draft the Post in BBCode**:
    - Open with a friendly greeting (`Hello, everyone!` or `Hey everyone,`) and brief context on the feature or series.
    - State the core problem or motivation clearly before diving into the solution.
    - Include an upfront `[b]Acknowledgements[/b]` or `[b]Scope & Caveats[/b]` section if there are known limitations, temporary behaviors, or deferred changes.
    - Break the technical explanation into scannable `[b]` or `[size=...][b]` sections that connect implementation details directly to gameplay impact, using `[list]` and `[*]` for bullet points.
    - Use `[img]<URL_OR_PLACEHOLDER>[/img]` and `[youtube]<VIDEO_ID>[/youtube]` tags where screenshots, comparisons, or clips belong.
    - Close with a brief thank-you and personal or team sign-off (`- <Author>` or `- The Project Reality Team`).
4. **Output Format**:
    - Present the entire drafted post inside a **single fenced code block** (```` ```bbcode ````) so developers can copy and paste it directly into the RealityMod forum without extra editing.
    - Verify all tags against `references/bbcode-syntax-reference.md` and tone against `references/style-and-structure.md`.

## Gotchas

- Never output raw Markdown formatting (such as `#` headings, `**bold**`, or `[text](url)`) inside the BBCode snippet; use `[b]`, `[i]`, `[size]`, `[url=...]`, `[img]`, and `[list]` instead.
- Avoid vague marketing hype; PR:BF2 readers expect concrete mechanical explanations, trade-offs, and honest caveats.
- Keep media placeholders descriptive so colleagues know which screenshots or clips to capture.
