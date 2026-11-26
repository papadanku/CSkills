# CSkills Repository Guide

Specialized skills and automation scripts for AI coding assistants and OpenCode (`plugin.json`).

## Architecture & Structure

- **Plugin Manifest**: `plugin.json` maps `./skills` as an OpenCode plugin source.
- **Skill Structure**: Each skill directory contains a `SKILL.md` file along with optional `references/`, `assets/`, and `scripts/`.
- **Domain Modules**:
  - **Project Reality: BF2**: Python 2.7.18 (`prbf2-code-python`), C# CS-Script (`prbf2-code-csharp`), HLSL Shaders (`prbf2-code-shaders`), modding scripts (`prbf2-code-scripts`), web/branding (`prbf2-code-webapp`, `prbf2-manage-brand`), and drafting (`prbf2-draft-*`).
  - **Other Tooling**: ReShadeFX shaders (`reshade-code-fx`), Sphinx reStructuredText (`sphinx-code-rst`), YouTube video projects (`youtube-create-project`), and git diff summarization (`git-summarize-diff`).

## Development & Utility Commands

- **Build / Compilation**: None required (static markdown & script repository).
- **YouTube Project Automation**:
  - Create project: `node skills/youtube-create-project/scripts/create_project.cjs <NewProjectName> [upload-template.md]`
  - Edit script: `node skills/youtube-create-project/scripts/edit_script.cjs <ProjectName> "<NewScriptContent>"`
