
# C# Coding Conventions & Identifier Naming Rules

This document outlines the coding standards for Project Reality BF2 CS-Script (`.csx`) files, synthesizing repository idioms with [Microsoft's C# Coding Conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions) and [Identifier Names Guidelines](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/identifier-names).

## 1. Identifier Naming Guidelines

| Construct | Case Style | Example | Rules |
| :--- | :--- | :--- | :--- |
| **Classes, Structs, Enums, Interfaces** | `PascalCase` | `ConFileParser`, `ObjectTemplate`, `ScriptResult` | Nouns or noun phrases. Interfaces start with `I`. |
| **Methods** | `PascalCase` | `ReadCon`, `ValidateFile`, `GenerateScriptResult` | Verbs or verb phrases describing actions. |
| **Public Properties & Constants** | `PascalCase` | `Success`, `MaxDegreeOfParallelism` | Clear nouns representing data or state. |
| **Parameters & Local Variables** | `camelCase` | `soundFilePath`, `numMissing`, `templateFiles` | Descriptive nouns/adjectives starting with lowercase. |
| **Private / Internal Fields** | `camelCase` | `rxOptions`, `counter`, `error` | Avoid leading underscores unless necessary for disambiguation. |

## 2. Layout, Formatting & Organization

- **Indentation**: Use 4 spaces per indentation level (no hard tabs).
- **Braces (`{ }`)**:
    - Place opening braces on the same line for classes, methods, and control flow statements (`if`, `for`, `foreach`, `while`, `try-catch`).
    - Always use curly braces even for single-statement `if` blocks to prevent maintenance errors.
- **Using Directives**: Place framework namespace imports (`System.*`) first, followed by external libraries, and mod-specific namespaces (`Reality.BF2.*`).
- **File Header Documentation**: Every `.csx` script should feature an introductory block comment (`/* ... */`) detailing its purpose, utility methods, parsing logic, and output contract.

## 3. Defensive Programming & Error Handling

- **Null Checks**: Always check file existence (`File.Exists`) and validate parser return values before invoking members.
- **Exception Isolation**: In parallel loops (`Parallel.ForEach`), catch exceptions locally, store them in a shared reference variable (thread-safely or under lock), and call `loopState.Break()` to terminate gracefully without crashing the build process.
- **Resource Cleanup**: Ensure output files from previous runs are safely deleted or overwritten (`File.Delete`, `File.WriteAllText`).
