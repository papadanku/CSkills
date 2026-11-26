
# Welcome to CSkills!

CSkills is a repository of specialized skills designed to extend the capabilities of various AI development tools that support agent skills.

- **Who is CSkills for?**

    CSkills was created and is maintained for developers and AI tool users looking to extend their CLI and desktop agent capabilities with domain-specific expertise.

- **What is CSkills?**

    CSkills is a collection of specialized skills designed to help AI agents perform specific tasks, generate content, or interact with various systems more effectively.

- **Where was CSkills created?**

    CSkills originated in the developer workspace.

- **When was CSkills created?**

    CSkills was developed to address evolving needs in multi-agent and CLI-based development tooling.

- **Why CSkills?**

    CSkills aims to provide a **free, open-source framework** to help create **streamlined, efficient, specialized AI agent workflows** accessible to all developers.

## Features

The **Skills** directory contains expert instructions and automation tools for diverse technical domains:

- **git-summarize-diff**: Summarizes staged changes concisely using the Conventional Commits format or objective plain English.
- **prbf2-code-csharp**: Assistant for finding bugs, generating, and optimizing CS-Script (.csx) build scripts in Project Reality BF2.
- **prbf2-code-python**: Assistant for debugging, generating, and optimizing Python 2.7.18 game logic for Project Reality: BF2.
- **prbf2-code-scripts**: Assistant for processing, generating, editing, analyzing, and debugging .ai, .con, .tweak, and .inc modding scripts in Project Reality: BF2.
- **prbf2-code-shaders**: Expert HLSL assistant for finding bugs, generating, and optimizing shaders for RealityShaders in Project Reality: BF2.
- **prbf2-code-webapp**: Expert assistant for web development tasks in Project Reality: BF2.
- **prbf2-draft-announcement**: Assistant for drafting release announcements, update highlights, and community news posts for Project Reality: BF2.
- **prbf2-draft-changelog**: Assistant for compiling structured, versioned release and hotfix changelogs for Project Reality: BF2.
- **prbf2-draft-update**: Assistant for drafting technical Developer Blogs and behind-the-scenes development updates for Project Reality: BF2.
- **prbf2-manage-brand**: Assistant for managing branding assets and configurations in Project Reality: BF2.
- **reshade-code-fx**: Expert ReShadeFX (HLSL) assistant for finding bugs, generating shader code, and suggesting optimized revisions.
- **sphinx-code-rst**: Multi-tool for reStructuredText (RST) and Sphinx documentation management and generation.
- **youtube-create-project**: Facilitates the creation and management of YouTube video projects, including scripts and assets.

## Installation Instructions - Plugin

### Prerequisite: Download Plugin

You need to download the repository as a `.zip` file from either method below.

- Clicking the **Download ZIP** button on GitHub's green **<> Code** button.
- Clicking the **Download .zip** button on CSkills' project page (https://papadanku.github.io/CSkills/)

### ChatGPT (OpenAI)

1. **Install the Plugin in ChatGPT Desktop App**:
    1. Open the ChatGPT desktop app.
    1. Click on the plugin icon on the top-left corner.
    1. Click the **Add** button on the top-right corner.
    1. On the **Add** menu, select the **Upload plugin archive** option.
    1. Drag and drop the downloaded `.zip` file into the upload box.
    1. Click the **Install plugin** button.
1. **Enable the Plugin**:
    1. Once installed, the plugin will appear in your list of available plugins.
    1. Enable the plugin to make the skills available for use in ChatGPT.

### Claude (Anthropic)

1. **Install the Plugin in Claude Desktop App**:
    1. Open the Claude desktop app.
    1. Click on the **Plugins** icon on the top-left corner.
    1. Click the **Add** button in the top-right corner.
    1. Choose the **Upload plugin** option.
    1. Drag the `.zip` file you created from the `/plugin` folder into the **Plugin file** box.
    1. Click the **Upload** button.
    1. Wait for the installation to complete.
1. **Enable the Plugin**:
    1. Once installed, the plugin will appear in your list of available plugins.
    1. Enable the plugin to make the skills available for use in Claude.

## Installation Instructions - Skills

### Gemini (Google)

1. Open the Gemini desktop app.
1. Click the settings gear icon in the bottom-left corner.
1. In the settings menu, select **Skills**.
1. Click the **Create** button in the top-right corner.
1. Choose **Upload** from the options.
1. Drag and drop the entire skill folder (e.g., `skills/git-summarize-diff/`) into the upload box.
1. Once the upload completes, click **Create** to add the skill.

### Vibe (Mistral AI)

1. Open the Vibe desktop app.
1. Click the **Context** icon in the top-left corner.
1. In the Context menu, select **Skills**.
1. Click the **Import** button in the top-right corner (next to the **+ New skill** button).
1. Choose **Upload skill folder** from the options.
1. Select an entire skill folder (e.g., `skills/git-summarize-diff/`).
1. Click the **Upload** button.
1. Once the upload completes, click the **Create skill** button on the top-left corner to add the skill.

## Installation Instructions - CLI Agents

**Copy** CSkills' `skills` folder into the following paths:

- **Antigravity (Google)**
    - `~/.gemini/config/skills/` (global)
    - `<workspace-root>/.agents/skills/` (workspace)
- **Claude Code (Anthropic)**
    - `~/.claude/skills/` (global)
    - `<workspace-root>/.claude/skills/` (workspace)
- **Codex (OpenAI)**
    - `~/.agents/skills/` (global)
    - `<workspace-root>/.agents/skills/` (workspace)
- **OpenCode**
    - `~/.config/opencode/skills/` (global)
    - `<workspace-root>/.opencode/skills/` (workspace)
- **Vibe (Mistral AI)**
    - `~/.vibe/skills/` (global)
    - `<workspace-root>/.vibe/skills/` (workspace)

## Supported Platforms Reference

CSkills is supported in the following products:

- **ChatGPT (OpenAI)**:
    - Download ChatGPT: https://chatgpt.com/download/
    - Download Codex: https://openai.com/codex/
    - Docs (Skills): https://developers.openai.com/plugins/concepts/skills
    - Docs (Plugins): https://developers.openai.com/plugins/concepts/plugins
- **Claude (Anthropic)**: https://claude.com/product/claude-code
    - Download Claude: https://claude.com/download
    - Docs (Skills): https://support.claude.com/en/articles/12512180-use-skills-in-claude
    - Docs (Plugins): https://support.claude.com/en/articles/13837440-use-plugins-in-claude
- **Gemini (Google)**
    - Download Antigravity: https://antigravity.google/
    - Download Gemini: https://gemini.google/desktop/
    - Docs (Skills): https://docs.cloud.google.com/gemini/enterprise/docs/skills
- **Vibe (Mistral AI)**:
    - Download Vibe: https://mistral.ai/products/vibe/
    - Docs (Skills): https://docs.mistral.ai/getting-started/quickstarts/vibe-work/create-first-skill
- **OpenCode**: https://opencode.ai/
- And more... https://agentskills.io/clients

# AI Diligence Statement

While developing and maintaining CSkills, I used AI models as tools to streamline documentation, version control, and technical research. **Mistral AI's Ministral** model helped draft commit messages and write project documentation. **Google's Gemini Flash-Lite** served as a skill creator, helping me build and structure the skills CSkills relies on.

I affirm that all AI-assisted content, documentation, and frameworks have undergone human review, evaluation, and adaptation. The final implementation, architecture, and output reflect my decisions, expertise, and intended design. While these AI models provided valuable assistance throughout development, I remain responsible for the project's codebase, accuracy, and overall direction. This disclosure is provided in the spirit of transparency, open-source integrity, and a commitment to acknowledging the collaborative tools utilized in CSkills's creation.
