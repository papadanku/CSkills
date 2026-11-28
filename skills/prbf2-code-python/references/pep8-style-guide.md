
# PEP-8 Style Guide (Local Reference)

This document provides a self-contained reference to Python's PEP-8 style conventions for use within this skill. Note that where Project Reality's existing codebase uses `camelCase` for functions/methods and `g_` prefixes for globals (as documented in [Coding Standards](coding-standards.md)), preserve those established repository naming idioms while applying all PEP-8 formatting, layout, whitespace, and readability rules below.

## 1. Code Layout & Indentation

- **4 Spaces per Indentation Level:** Use 4 consecutive spaces for every indentation level. Never use tabs, and never mix tabs and spaces.
- **Continuation Lines:** Align wrapped elements vertically inside parentheses, brackets, or braces, or use a hanging indent with 4 spaces (ensuring arguments are distinguishable from the block body):

    ```python
    # Aligned with opening delimiter
    result = calculateDamage(
        attackerPlayer, targetVehicle,
        impactVelocity, armorMultiplier
    )

    # Hanging indent (4 extra spaces, nothing on first line)
    def handleVehicleDamage(
            targetVehicle, attackerPlayer,
            damageAmount, hitMaterial):
        pass
    ```

- **Maximum Line Length:**
    - Limit code lines to **79 characters**.
    - Limit docstrings and comments to **72 characters**.
    - Wrap long lines using implied line continuation inside parentheses `()`, brackets `[]`, or braces `{}` rather than backslashes `\`.
- **Line Breaks & Binary Operators:** Break before binary operators so operators align cleanly with their operands:

    ```python
    totalDamage = (
        baseWeaponDamage
        + splashDamageBonus
        - armorMitigation
    )
    ```

- **Blank Lines:**
    - Surround top-level function and class definitions with **2 blank lines**.
    - Surround method definitions inside a class with **1 blank line**.
    - Use single blank lines sparingly inside functions to separate logical sections.
- **Source File Encoding:** Use UTF-8 (no BOM).

## 2. Imports

- Place imports at the top of the file, on **separate lines**:

    ```python
    # Correct
    import math
    import os

    # Wrong
    import math, os
    ```

- Group imports in the following order, separated by a blank line:
    1. Standard library imports
    2. Related third-party / engine imports (`bf2`, `host`)
    3. Local application / Project Reality module imports (`reality*`)
- Avoid wildcard imports (`from module import *`) as they obscure which names are in scope.

## 3. Whitespace in Expressions & Statements

- **No Extraneous Whitespace:**
    - Inside parentheses, brackets, or braces: `spam(ham[1], {'eggs': 2})`, not `spam( ham[ 1 ], { 'eggs': 2 } )`.
    - Immediately before a comma, semicolon, or colon: `if x == 4: print x, y`, not `if x == 4 : print x , y`.
    - Before the open parenthesis of a function call or indexing bracket: `func(arg)` and `items[index]`, not `func (arg)` or `items [index]`.
- **Operators:** Always surround binary operators (`=`, `+=`, `==`, `<`, `>`, `!=`, `in`, `not in`, `is`, `is not`, `and`, `or`) with a single space on each side.
- **Keyword Arguments & Defaults:** Do not put spaces around `=` when indicating a keyword argument or default parameter value:

    ```python
    def registerTimer(callback, intervalSeconds=1.0):
        pass
    ```

- **Trailing Whitespace:** Remove trailing spaces at the end of lines.

## 4. Compound Statements & Anti-Code-Golfing

- **One Statement per Line:** Never combine multiple statements on the same line with semicolons (`;`).
- **Separate Suite Lines:** Never place an `if`, `for`, or `while` body on the same line as the header:

    ```python
    # Correct
    if targetPlayer is None:
        return

    # Wrong (code golfing)
    if targetPlayer is None: return
    ```

- **Avoid Overly Clever One-Liners:** Prefer explicit loops and named intermediate variables over deeply nested comprehensions or chained ternary operators.

## 5. Comments & Docstrings

- **Block Comments:** Apply to the code that follows them, indented to the same level. Start each line with `# ` (hash followed by a single space).
- **Inline Comments:** Use sparingly, separated by at least **two spaces** from the statement, starting with `# `. Explain *why*, not *what*.
- **Docstrings:** Use triple double-quotes `"""Summary line."""` for public modules, classes, functions, and methods. Keep single-line docstrings on one line; for multi-line docstrings, place a blank line after the summary line.

## 6. Programming Recommendations

- **Comparisons to `None`:** Always use `is` or `is not`, never `==` or `!=`:

    ```python
    if activeVehicle is not None:
        processVehicle(activeVehicle)
    ```

- **Boolean Comparisons:** Do not compare boolean values to `True` or `False` using `==`:

    ```python
    # Correct
    if isRoundActive:
        pass

    # Wrong
    if isRoundActive == True:
        pass
    ```

- **Empty Sequences:** Test empty lists, strings, and sets by truthiness (`if not pendingPlayers:`) rather than `len(pendingPlayers) == 0`.
- **Exceptions:** Always catch specific exceptions (`except ValueError:`) rather than bare `except:` clauses.
- **Return Consistency:** Be consistent in `return` statements: either all return paths in a function return an explicit value (`return None`), or none do.
- **Detailed Naming:** Prefer descriptive, unambiguous names (`remainingAmmoCount`, `spawnPointPosition`) over single-letter or abbreviated identifiers.
