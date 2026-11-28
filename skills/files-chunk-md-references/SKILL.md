---
name: files-chunk-md-references
description: Chunk large Markdown files into smaller, focused, kebab-case reference files one level deep for Agent Skills. Use when splitting large Markdown documentation, organizing a skill's references/ directory, or refactoring oversized reference files to reduce agent context usage.
---

# files-chunk-md-references

Split large Markdown files into focused, self-contained reference files placed one level deep in `references/` with detailed, consistent kebab-case filenames.

## When to Use

- Converting a large Markdown document or knowledge base into a skill's `references/` directory.
- Refactoring an oversized `SKILL.md` or reference file that consumes too much context when loaded at once.
- Standardizing reference filenames to descriptive, consistent kebab-case so a model can infer file contents from the filename alone.
- Flattening nested reference subdirectories into a single level (`references/<file>.md`).

## Core Principles

1. **One level deep from `SKILL.md`**: Place all chunked files directly inside `references/` (for example, `references/api-auth-oauth2.md`). Never create nested subdirectories like `references/api/auth/oauth2.md` or chain references from one reference file to another.
2. **Focused, bounded chunks**: Aim for one coherent topic per file (typically 50 to 300 lines, and under 500 lines max). Split oversized sections at subheadings rather than cutting mid-paragraph, mid-table, or mid-code-block.
3. **Detailed, consistent kebab-case names**: Use lowercase alphanumeric words separated by single hyphens (`a-z`, `0-9`, `-`). Name files after their specific domain and topic so the model knows what is inside before reading (for example, `billing-webhook-events.md` instead of `part-2.md` or `webhooks.md`).
4. **Self-contained and script-less**: Perform all analysis and file creation directly without relying on scripts or external sources.

## Steps

### 1. Inspect the Source File

Read the target Markdown file's heading hierarchy (`#`, `##`, `###`) and approximate line counts per section to choose the right split boundary:

- If `##` sections are each 50 to 300 lines, split at `##`.
- If a `##` section is very large (over 300 lines) and has clear `###` subsections, split at `###` and carry the parent `##` title into both the filename prefix and the chunk's `#` heading for context.
- If multiple consecutive `##` sections are very short (under 30 lines each) and tightly related, group them into a single coherent topic file rather than creating fragmented micro-files.
- If the file has an introductory overview before the first split heading, save it as `<topic>-overview.md` if substantive, or merge it into `SKILL.md` if short.

### 2. Design Consistent Kebab-Case Filenames

Before writing files, establish a naming pattern for the entire set so related chunks sort and scan predictably:

- Pattern: `<domain-or-category>-<specific-topic>.md` (for example, `stripe-webhooks-signature-verification.md`, `stripe-webhooks-retry-schedule.md`).
- Strip leading section numbers (turn `2.1 Rate Limits` into `rate-limits.md`, not `2-1-rate-limits.md`).
- Replace spaces, underscores, slashes, and punctuation with single hyphens, collapse consecutive hyphens, and trim leading or trailing hyphens.
- Avoid vague names (`section-1.md`, `misc.md`, `details.md`, `notes.md`). Every filename should clearly indicate what the model will find when loading it.

### 3. Write the Chunked Reference Files

Create each chunk directly under `references/` while preserving content integrity:

- Start each file with a clear `# Title` reflecting its full context (for example, `# API: Rate Limits`).
- Adjust subheading levels inside the chunk if needed so headings descend cleanly (`#` -> `##` -> `###`).
- Never split inside a fenced code block (` ``` ` or `~~~`) or a Markdown table; ignore `#` lines that appear inside code blocks.
- Keep each file self-contained: do not link from `references/a.md` to `references/b.md` in a way that forces multi-hop loading.

### 4. Wire References into `SKILL.md`

Add a concise `## References` section in `SKILL.md` listing each file one level deep with a one-line description of when to load it:

```markdown
## References

- [API Authentication](references/api-authentication-oauth2.md): OAuth2 token flows, scopes, and refresh handling.
- [API Rate Limits](references/api-rate-limits-quotas.md): Per-endpoint quotas, headers, and backoff rules.
```

### 5. Validate the Output

Verify every generated file before finishing:

- All reference files live directly under `references/` (depth 1 from `SKILL.md`, no nested directories).
- Every filename uses only lowercase letters, numbers, and single hyphens ending in `.md`.
- Every link in `SKILL.md` resolves to an existing file in `references/`.
- No individual reference file is unnecessarily bloated, empty, or truncated mid-code-block.

## Gotchas

- **Splitting inside code blocks**: Lines starting with `#` inside Bash, Python, or YAML code blocks are comments, not Markdown headings. Always track fenced code block boundaries when identifying split points.
- **Over-fragmentation**: Splitting every 10-line `###` subsection creates dozens of tiny files and clutters `SKILL.md`. Keep related short subsections together under their parent topic.
- **Generic filenames**: Filenames like `overview.md` or `configuration.md` become ambiguous when a skill covers multiple topics. Always include the subject prefix (for example, `postgres-configuration.md`).
- **Nested reference chains**: Avoid putting links inside one reference file that require reading another reference file to understand. Keep all navigation anchored in `SKILL.md`.
