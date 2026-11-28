
# Coding Standards - Project Reality Python

This document details the exact formatting, naming, and structural standards observed across the Project Reality Python codebase (`mods/pr_repo/python`). For general Python formatting and layout rules, also consult the bundled [PEP-8 Style Guide](pep8-style-guide.md).

## 1. Python 2.7 Compatibility

- **Syntax:** Write valid Python 2.7.18 code. Avoid Python 3 constructs (e.g., `print "text"` statement style or `print("text", file=...)` kwargs).
- **Division:** Be mindful of integer division (`5 / 2 == 2`). Use float division explicitly when needed (`5.0 / 2` or float casting).
- **Iterators:** Prefer `xrange()` over `range()` for loops over large collections to avoid list allocations.

## 2. Readability & Anti-Code-Golfing Rules

- **No Code Golfing:** Never sacrifice readability for fewer lines or characters. Avoid dense one-liners, nested list/dict comprehensions, chained ternary expressions, or inline `if`/`for` suites (e.g., never write `if player is None: return` on one line).
- **Indentation:** Always use **4 spaces per indentation level**. Never use tabs or mix tabs and spaces.
- **Detailed Variable Names:** Choose clear, descriptive names that explain what the variable holds (e.g., `supplyCratePosition`, `minimumDistanceSquared`, `currentDistance`). Avoid single-letter names (`x`, `p`, `d`) or cryptic abbreviations.

## 3. Naming Conventions

| Construct | Case Style | Example |
| :--- | :--- | :--- |
| **Classes** | `PascalCase` | `ReportSupplies`, `DeviationOnSwitch`, `ProjectileHandler` |
| **Functions & Methods** | `camelCase` | `playerConnect`, `calcDistanceSquared`, `sendRoundStatistics` |
| **Global Variables** | `g_` + `camelCase`/`snake_case` | `g_maxPlayers`, `g_serverName`, `g_supply_objects` |
| **Constants** | `UPPER_SNAKE_CASE` | `MAX_RETRIES`, `DEFAULT_TIMEOUT` |
| **Local Variables** | `camelCase` or `snake_case` | `supplyCrate`, `minimumDistanceSquared`, `currentDistance` |

## 4. Module Import & Aliasing Conventions

To prevent namespace pollution and maintain consistency across modules, internal PR modules must be imported with standard short `r` aliases:

```python
import bf2
import host
import realityadmin as radmin
import realityconstants as rconstants
import realitycore as rcore
import realitydebug as rdebug
import realityevents as revents
import realitymemory as rmemory
import realityserver as rserver
import realityspawner as rspawner
import realitytimer as rtimer
import realityvehicles as rvehicles
import realityzones as rzones
```

## 5. Docstrings & Comments

- Use clear inline comments `#` to explain non-obvious engine interactions or assumptions (e.g., reliability of engine events or timing workarounds).
- Keep module headers clean and imports grouped logically per PEP-8: standard library first, then external/engine modules (`bf2`, `host`), followed by internal PR modules (`reality*`).
