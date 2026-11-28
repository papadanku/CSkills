
# Microsoft C# Coding Style Guide (Local Reference)

This document provides a self-contained reference to Microsoft's official C# coding conventions and identifier naming rules for use within this skill.

## 1. Identifier Naming Rules & Conventions

### Capitalization Styles

- **`PascalCase`**: Capitalize the first letter of every word (e.g., `SoundUtilities`, `ValidateFile`, `MaxDegreeOfParallelism`). Use for:
    - Namespaces, classes, structs, records, and enums
    - Interfaces (prefixed with `I`, e.g., `IAssetValidator`)
    - Methods, properties, events, and delegates
    - Constants (both fields and local constants, including `private` and `internal` constants)
- **`camelCase`**: Lowercase first letter, capitalize subsequent words (e.g., `soundFilePath`, `templateFiles`). Use for:
    - Method parameters and local variables
    - Private and internal non-constant fields (prefix instance fields with `_`, e.g., `_missingCount`, and static fields with `s_` if following Microsoft's `s_` convention, or consistent repository field style)

### Naming Best Practices

- **Prefer Clarity Over Brevity**: Choose easily readable identifier names (`HorizontalAlignment`, `CanScrollHorizontally`, `missingSoundCount`) rather than terse or cryptic abbreviations (`HorzAlign`, `ScrollX`, `cnt`).
- **No Single-Letter Names**: Avoid single-letter variable names except for simple loop counters (`i`, `j`) or standard lambda/generic type parameters (`T`).
- **No Hungarian Notation**: Do not encode types into variable names (e.g., use `soundFilePath`, not `strSoundFilePath`; use `fileCount`, not `iFileCount`).
- **Word Choice**:
    - Use nouns or noun phrases for classes, structs, and properties.
    - Use verbs or verb phrases for methods (`ReadCon`, `GenerateScriptResult`).
    - Use singular names for standard enums and plural names for `[Flags]` enums; do not add an `Enum` or `Flags` suffix.
    - Avoid abbreviations or acronyms unless universally understood (e.g., `Id`, `Xml`, `IO`).

## 2. Layout & Formatting Conventions

- **Indentation**: Use **4-space indentation** (smart indenting, tabs saved as spaces). Never use hard tabs.
- **Line Discipline**:
    - Write only **one statement per line**.
    - Write only **one declaration per line**.
    - Indent continuation lines by one tab stop (4 spaces).
- **Bracing Style (Allman)**:
    - Place opening `{` and closing `}` braces on their own separate lines, aligned with the containing statement.
    - Always include braces for `if`, `else`, `for`, `foreach`, `while`, and `using` blocks, even when the body contains only a single statement.
- **Spacing & Parentheses**:
    - Add at least one blank line between method definitions and property definitions.
    - Use parentheses to make operator precedence and clauses in complex expressions explicit:

        ```csharp
        if ((startX > endX) && (startX > previousX))
        {
            // Take appropriate action.
        }
        ```

    - Use single spaces around binary operators (`=`, `+`, `==`, `&&`) and after commas, with no spaces immediately inside parentheses.

## 3. Commenting Conventions

- Place comments on a **separate line**, not at the end of a line of code.
- Begin comment text with an uppercase letter and end with a period.
- Insert one space between the comment delimiter (`//`) and the comment text:

    ```csharp
    // Validate that the referenced audio file exists on disk.
    ```

- Use XML documentation comments (`/// <summary>...</summary>`) for public classes, methods, and properties.

## 4. Language & Type Usage Guidelines

- **String Interpolation & Formatting**: Use string interpolation (`$"Validating {current} of {total}"`) or `string.Format` for short strings; use `StringBuilder` or `StringWriter` when appending in loops.
- **Type Inference (`var`)**: Use `var` when the type of the variable is obvious from the right-hand side of the assignment (e.g., `var parser = new ConFileParser();`). Use explicit types when the type is not obvious from the initializer (e.g., `int missingSoundCount = 0;`).
- **Language Keywords over BCL Types**: Use C# language keywords (`string`, `int`, `bool`, `object`) rather than BCL type names (`String`, `Int32`, `Boolean`, `Object`), except when calling static members where appropriate.
- **Object Initializers**: Use object initializers to simplify object creation cleanly across multiple indented lines:

    ```csharp
    var parallelOptions = new ParallelOptions
    {
        MaxDegreeOfParallelism = Build.GetParallelism()
    };
    ```

- **Exception Handling**: Use `try-catch` only for conditions you can handle or log meaningfully, and use `using` statements (or blocks) to ensure `IDisposable` resources are always disposed.
- **LINQ & Lambdas**: Break chained LINQ queries across multiple lines with clear indentation; never compress complex multi-step LINQ pipelines into a single unreadable line.
