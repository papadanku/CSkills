---
name: prbf2-cs-coder
description: Expert assistant for CS-Script (.csx) in Project Reality BF2 build scripts. Use when debugging, drafting, documenting, consulting, refactoring, or writing C# scripts for build automation, asset validation, map generation, and data processing in the Project Reality workspace.
---

# CS-Script Expert Assistant (`prbf2-cs-coder`)

This skill provides comprehensive, expert-level assistance for developing, debugging, drafting, documenting, and consulting on Project Reality BF2's CS-Script (`.csx`) build and automation scripts. It combines the rigorous patterns of the Project Reality build repository with Microsoft's official C# coding conventions and identifier naming rules.

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

## Key Patterns & Architecture

- **Namespaces & Utilities**: `Reality.BF2`, `Reality.BF2.Build`, `Reality.BF2.Console`, `Reality.Utils`, and `Common/*.csx`.
- **Path Resolution**: Always use `Directories.CurrentModDirectory` or `Directories.CurrentModLevelsDirectory` combined with `Path.Combine`.
- **Parallelism**: Use `Build.GetParallelism()` with `ParallelOptions`, guarding shared state via `Interlocked` operations and locks.
- **Result Contracts**: Scripts must return a `ScriptResult` object (`Success`, `Header`, `Message`).

## Reference Guides

- [Coding Conventions & Style Rules](references/coding-conventions.md)
- [Code Patterns & Boilerplates](references/patterns.md)
- [Common Utilities & API Reference](references/api-reference.md)
