
# C# Coding Conventions & Identifier Naming Rules

This document outlines the coding standards for Project Reality BF2 CS-Script (`.csx`) files, synthesizing repository idioms with the bundled [Microsoft C# Coding Style Guide](microsoft-csharp-style-guide.md).

## 1. Readability & Anti-Code-Golfing Rules

- **No Code Golfing**: Never write compressed, clever one-liners, nested ternary expressions, or single-line control-flow statements. Clarity and maintainability always take precedence over brevity.
- **Indentation**: Use **4 spaces per indentation level** (tabs saved as spaces, no hard tabs). Indent continuation lines by 4 spaces.
- **Detailed Variable Names**: Always choose descriptive, English-readable names that express intent (e.g., `soundFilePath`, `missingSoundCount`, `processedFileCount`). Avoid abbreviations, acronyms, and single-letter identifiers outside simple loop counters.

## 2. Identifier Naming Guidelines

| Construct | Case Style | Example | Rules |
| :--- | :--- | :--- | :--- |
| **Classes, Structs, Enums, Interfaces** | `PascalCase` | `ConFileParser`, `ObjectTemplate`, `ScriptResult` | Nouns or noun phrases. Interfaces start with `I`. |
| **Methods** | `PascalCase` | `ReadCon`, `ValidateFile`, `GenerateScriptResult` | Verbs or verb phrases describing actions. |
| **Public Properties & Constants** | `PascalCase` | `Success`, `MaxDegreeOfParallelism` | Clear nouns representing data or state. |
| **Parameters & Local Variables** | `camelCase` | `soundFilePath`, `missingSoundCount`, `templateFiles` | Descriptive nouns/adjectives starting with lowercase. |
| **Private / Internal Fields** | `camelCase` or `_camelCase` | `regexOptions`, `_processedCounter`, `errorMessage` | Descriptive names; follow Microsoft's `_camelCase` for private instance fields when appropriate. |

## 3. Layout, Formatting & Organization

- **One Statement & Declaration per Line**: Write only one statement per line and one variable declaration per line.
- **Braces (`{ }`)**:
    - Follow Microsoft's Allman brace style: place opening `{` and closing `}` braces on their own new lines for namespaces, classes, methods, and all control-flow statements (`if`, `else`, `for`, `foreach`, `while`, `try`, `catch`).
    - Always use curly braces even for single-statement `if` blocks to prevent maintenance errors.
- **Blank Lines**: Add at least one blank line between method definitions and property definitions.
- **Using Directives**: Place framework namespace imports (`System.*`) first, followed by external libraries, and mod-specific namespaces (`Reality.BF2.*`).
- **File Header Documentation**: Every `.csx` script should feature an introductory block comment (`/* ... */`) detailing its purpose, utility methods, parsing logic, and output contract.

## 4. Defensive Programming & Error Handling

- **Null Checks**: Always check file existence (`File.Exists`) and validate parser return values before invoking members.
- **Exception Isolation**: In parallel loops (`Parallel.ForEach`), catch exceptions locally, store them in a shared reference variable (thread-safely or under lock), and call `loopState.Break()` to terminate gracefully without crashing the build process.
- **Resource Cleanup**: Ensure output files from previous runs are safely deleted or overwritten (`File.Delete`, `File.WriteAllText`).
