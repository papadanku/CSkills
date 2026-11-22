---
name: prbf2-web-coder
description: Build clean, dependency-conservative HTML, CSS, and vanilla JavaScript web applications and developer tools for Project Reality (PR:BF2) development, styled with Project Reality brand guidelines and compliant with Google's HTML/CSS style guide. Use when the user asks to build a PR:BF2 web tool, calculator, `.con`/`.desc` generator, map/kit viewer, server utility, or dashboard in HTML/CSS/JS.
---

# PR:BF2 Web Coder

Build clean, dependency-conservative modern HTML and CSS (with vanilla JavaScript when interactivity is needed) web applications and utilities to aid Project Reality (PR:BF2) development, adhering strictly to Project Reality's visual identity and Google's HTML/CSS style guide.

## When to Use

- Building web-based developer tools for Project Reality (such as `.con` or `.desc` generators, ticket/layer calculators, vehicle/kit reference tools, localization editors, or RCon/server dashboards).
- Creating lightweight HTML5 and CSS3 interfaces—whether static/markup-and-style-focused or script-driven—while keeping external dependencies minimal and conservative.

## Reference Files

Read these bundled reference files before writing code:

- `references/project-reality-branding-spec.md` - Official typography, surface hierarchy, brand colors (`#171717`, `#FFFFFF`, `#3DA0EC`), action blues (`#2A90C3` to `#206694`, `#2D789F`), and team role color tokens.
- `references/general-guide.md` - Google HTML/CSS general rules (HTTPS, 2-space indentation, lowercase code, UTF-8 without BOM, no trailing whitespace).
- `references/html-guide.md` - Google HTML rules (`<!doctype html>`, semantic elements, separation of concerns, no unnecessary `id` attributes, double quotes for attributes, no `type` attributes on CSS/JS, no entity references).
- `references/css-guide.md` - Google CSS rules (valid CSS, hyphenated semantic class names, avoid ID selectors and `!important`, shorthand properties, `0` without units, leading `0`s, 3-char hex where possible, single quotes in CSS, alphabetized declarations).

## Core Principles

### 1. HTML, CSS, and Conservative Dependencies

- **Default to Native HTML & CSS:** Use semantic HTML5 (`<dialog>`, `<details>`, `<datalist>`, `<template>`, native form controls) and modern CSS (custom properties, Grid, Flexbox, `:has()`, responsive layout) first. Add vanilla ES6+ JavaScript only when dynamic behavior or interactivity adds value.
- **Be Conservative on Dependencies:** Prefer zero external runtime dependencies. Avoid heavy UI frameworks, CSS bloat, or unvetted third-party CDNs by default. If an external resource (such as a font stylesheet or small utility library) is used, keep it minimal, purposeful, and well-scoped rather than pulling in large frameworks.
- **Font Handling:** Keep core layout and readability resilient offline by defining clean system sans-serif and monospace stacks for body/code, and optionally referencing `Bebas Neue` / `League Gothic` via `https:` when web font loading is desired, with graceful local fallbacks.
- **Minimal Code Footprint:** Write only the markup, styles, and scripts needed for the tool. Avoid boilerplate wrappers, redundant div nesting, or unused CSS rules.

### 2. Google HTML/CSS Style Guide Compliance

Follow `references/general-guide.md`, `references/html-guide.md`, and `references/css-guide.md` in every generated file:

- **HTML Structure:** Start with `<!doctype html>` and `<meta charset="utf-8">`. Keep all element names, attributes, and CSS selectors/properties/values lowercase.
- **Indentation and Whitespace:** Indent by 2 spaces (never tabs) and strip all trailing whitespace.
- **Quotation Marks:** Use double quotes (`"..."`) in HTML attributes and single quotes (`'...'`) in CSS values; omit quotes inside `url()`.
- **Separation of Concerns:** Keep presentation in `<style>` or `.css` files and behavior in `<script>` or `.js` files. Avoid inline `style="..."` or `onclick="..."` attributes in HTML.
- **Selectors and IDs:** Style using short, hyphenated semantic `.class` selectors (avoid `#id` selectors in CSS and avoid qualifying classes with tag names like `div.panel`). When an `id` is strictly needed for `<label for="...">` or `aria-describedby`, include a hyphen (e.g., `map-scale`).
- **CSS Formatting:** End every declaration with `;`, put a single space after `:` and before `{`, separate rules with a blank line, use shorthand properties, omit units on `0`, include leading `0`s (e.g., `0.8rem`), and use 3-character lowercase hex where possible (e.g., `#fff`, `#111`, `#222`, `#333`, `#555`).

### 3. Project Reality Branding Integration

Apply `references/project-reality-branding-spec.md`:

- **Surfaces:** Use `#171717` (or `#111113` with `#1e1f24` top nav for dense technical tools) for web canvases, or `#111` / `#222` / `#333` with `1px solid #555` borders for utility dialog layouts.
- **Text and Accents:** Use `#fff` primary text, `#b3b3b3` muted labels, `#3da0ec` brand accents/links, `#2a90c3` to `#206694` primary action buttons, and `#102746` for inline code pills.
- **Typography:** Reserve `Bebas Neue` (or `League Gothic` for lowercase/multilingual) for uppercase display headers and titles; use clean neutral sans-serif for controls/prose and monospace for `.con`/`.desc`/code outputs.
- **Role Badges:** Use the 7 role colors strictly for role badges (`#206694`, `#3498db`, `#11806a`, `#a84300`, `#9b59b6`, `#a08536`, `#1f8b4c`) with `#fff` label text.

## Workflow

1. **Clarify Tool Scope:** Identify the exact PR:BF2 development task (inputs, outputs, file formats like `.con`, `.desc`, `.ai`, `.py`, or localization files) and keep the UI focused on that single workflow.
2. **Design Semantic HTML:** Draft minimal, valid HTML5 using semantic landmarks (`<header>`, `<main>`, `<section>`, `<footer>`), native form controls, and accessible labels.
3. **Apply Branded CSS:** Define CSS custom properties (`:root`) for Project Reality tokens in lowercase hex, using Grid/Flexbox for layout and high-contrast controls.
4. **Implement Vanilla JS (When Needed):** Write modular, minimal ES6+ event listeners (`addEventListener`) and pure helper functions when interactivity is re ired. Sanitize or escape any user/feed text via `textContent` rather than raw `innerHTML`.
5. **Audit Against Guides:** Verify conservative dependency choices, Google HTML/CSS style compliance (2-space indent, lowercase, no `!important`, no `#id` CSS selectors, no inline handlers), and Project Reality color/font accuracy before delivering.

## Gotchas

- **Uppercase Hex vs. Google Style:** The branding spec lists hex codes in uppercase (`#FFFFFF`), while Google's CSS guide requires lowercase (`#fff`, `#3da0ec`). Always write lowercase hex (and 3-char shorthand like `#fff`, `#111`, `#222`, `#333`, `#555` where possible) in CSS.
- **Entity References:** Do not use HTML entity references like `&mdash;` or `&rdquo;` in UTF-8 HTML; write the literal UTF-8 character, and only escape `<` and `&` where required.
- **Inline Event Handlers:** Never use `onclick="..."` or `oninput="..."` in HTML; attach listeners in JavaScript with `addEventListener`.
