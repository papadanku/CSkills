# CSkills Repository Guide

Collection of specialized skills and agents for OpenCode extending AI capabilities in domains like Python 2.7, C# scripts, HLSL shaders, reStructuredText documentation, and YouTube video workflows.

## Structure & Architecture

- **`plugin.json`**: OpenCode plugin manifest referencing `./skills`.
- **`skills/`**: Houses specialized skills containing expert guidance, reference materials, and automation scripts:
  - `git-diff-summarizer`: Summarizes staged changes concisely using the Conventional Commits format or objective plain English.
  - `prbf2-python-coder`: Project Reality: BF2 Python 2.7.18 scripting guidelines, testing, and debugging playbooks.
  - `prbf2-cs-coder`: CS-Script (.csx) build automation, asset validation, map generation, and data processing.
  - `prbf2-shader-coder`: RealityShaders HLSL development, bug patterns, and optimization guides.
  - `reshadefx-coder`: ReShadeFX (HLSL) shader development and optimization within CShade.
  - `restructuredtext-book`: Sphinx documentation structure, domains, and RST syntax references.
  - `youtube-creator`: Video project management scripts (`create_project.cjs`, `edit_script.cjs`) and templates.

## Development & Conventions

- This repository is a static collection of markdown skill files, references, assets, and Node.js utility scripts.
- No build step or package manager manifest is required unless running local skill automation scripts (e.g., Node.js execution for `youtube-creator` scripts).
