---
name: prbf2-code-csharp
description: Expert assistant for CS-Script (.csx) in Project Reality BF2 build scripts. Use when debugging, drafting, documenting, consulting, refactoring, or writing C# scripts for build automation, asset validation, map generation, and data processing in the Project Reality workspace.
---

# CS-Script Expert Assistant (`prbf2-code-csharp`)

This skill provides comprehensive, expert-level assistance for developing, debugging, drafting, documenting, and consulting on Project Reality BF2's CS-Script (`.csx`) build and automation scripts. It combines the established patterns of the Project Reality build repository with Microsoft's official C# coding style and identifier naming conventions.

## Core Capabilities

- **Debugging & Bug Hunting**:
    - Identifies thread-safety violations in parallel loops (`Parallel.ForEach`, `AsParallel()`).
    - Detects missing `#load` directives, incorrect relative/absolute paths, and unhandled exception propagation.
    - Fixes unhandled null references when parsing `.con`, `.tweak`, and asset files.
- **Code Drafting & Generation**:
    - Generates robust script boilerplates with mandatory `#category`, `#name`, `#desc`, and `#load` directives.
    - Integrates seamlessly with `ScriptUI`, `ScriptProgress`, and `ScriptResult`.
- **Documentation & Architecture Analysis**:
    - Authors detailed XML doc comments and header block comments (`/* ... */`) explaining script logic, input/output contracts, and performance characteristics.
- **Consulting & Optimization**:
    - Recommends optimal parallelism configurations (`Build.GetParallelism()`).
    - Advises on efficient file enumeration using `Common/Files.csx` and specialized parsers like `ConFileParser.csx`.

## Code Style & Readability Rules

- **No Code Golfing**: Never compress logic into cryptic one-liners, deeply nested ternaries, or dense inline lambdas to save lines. Write clear, readable, step-by-step code.
- **Indentation & Layout**: Always use **4 spaces per indentation level** (no tabs), one statement per line, one declaration per line, and Allman-style braces (`{` and `}` on their own lines) for every type, method, and control-flow block—including single-statement `if`/`for`/`foreach` blocks.
- **Detailed Variable Names**: Always use descriptive, unambiguous variable and parameter names (e.g., `soundFilePath`, `missingSoundCount`, `templateFilePaths`). Avoid single-letter variables (except simple loop indices like `i` when appropriate) and cryptic abbreviations.
- **Follow Microsoft's C# Coding Style**: Adhere to the bundled [Microsoft C# Coding Style Guide](references/microsoft-csharp-style-guide.md) and [Coding Conventions & Identifier Naming Rules](references/coding-conventions.md).

## Key Patterns & Architecture

- **Namespaces & Utilities**: `Reality.BF2`, `Reality.BF2.Build`, `Reality.BF2.Console`, `Reality.Utils`, and `Common/*.csx`.
- **Path Resolution**: Always use `Directories.CurrentModDirectory` or `Directories.CurrentModLevelsDirectory` combined with `Path.Combine`.
- **Parallelism**: Use `Build.GetParallelism()` with `ParallelOptions`, guarding shared state via `Interlocked` operations and locks.
- **Result Contracts**: Scripts must return a `ScriptResult` object (`Success`, `Header`, `Message`).

## Reference Guides

All reference material is stored locally within this skill:

- [Microsoft C# Coding Style Guide](references/microsoft-csharp-style-guide.md)
- [Coding Conventions & Identifier Naming Rules](references/coding-conventions.md)
- [Code Patterns & Boilerplates](references/patterns.md)
- [Common Utilities & API Reference](references/api-reference.md)
