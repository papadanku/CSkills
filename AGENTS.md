# CSkills Repository Guide

Specialized skills and automation scripts for OpenCode and AI coding assistants.

## Architecture & Structure

- **`plugin.json`**: OpenCode plugin manifest pointing to `./skills`.
- **`skills/`**: Collection of domain-specific skills (`SKILL.md`, `references/`, `assets/`, `scripts/`).
  - **Project Reality: BF2**: Python 2.7.18 (`prbf2-code-python`), C# CS-Script (`prbf2-code-csharp`), HLSL Shaders (`prbf2-code-shaders`), Web (`prbf2-code-webapp`), Brand (`prbf2-manage-brand`), and drafting (`prbf2-draft-*`).
  - **Shaders / Docs / Tools**: ReShadeFX (`reshade-code-fx`), Sphinx reStructuredText (`sphinx-code-rst`), YouTube video projects (`youtube-create-project`), and git diff summarization (`git-summarize-diff`).

## Development & Utility Commands

- **No build step required**: Static markdown skill repository.
- **YouTube Project Automation**:
  - Create project: `node skills/youtube-create-project/scripts/create_project.cjs <NewProjectName> [upload-template.md]`
  - Edit script: `node skills/youtube-create-project/scripts/edit_script.cjs <ProjectName> "<NewScriptContent>"`
