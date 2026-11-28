---
name: prbf2-code-python
description: Expert assistant for debugging, drafting, documenting, and consulting on Project Reality BF2's Python 2.7.18 scripts. Use this skill whenever the user mentions working with Project Reality Python code in mods/pr_repo/python, writing game logic handlers, interacting with BF2 server/host APIs, debugging server crashes or logic errors, or following PR coding standards.
---

# Project Reality Python Coder (`prbf2-code-python`)

This skill provides expert guidance for developing, debugging, documenting, and testing Python scripts in the **Project Reality: Battlefield 2 (PR:BF2)** modification codebase (`mods/pr_repo/python`).

## 1. Core Environment & Constraints

- **Python Version:** **Python 2.7.18**. All code must be compatible with Python 2.7 syntax and semantics (e.g., standard print statements, old-style division rules unless `__future__` division is imported, `xrange` over `range` for large loops).
- **Engine Context:** Code runs inside the BF2 dedicated/listen server Python environment managed by the game engine (`host`, `bf2`, and native C extension modules like `_realitycore`).
- **Platform Considerations:** Scripts must respect platform differences between Windows and Linux server builds (e.g., checking `rmemory.isWindowsListenServer` where virtual table pointers or memory hooks differ).

## 2. Code Style, Readability & Anti-Code-Golfing Rules

- **No Code Golfing:** Never write compressed, clever one-liners, deeply nested comprehensions, chained ternaries, or single-line `if`/`for` statements to save lines. Prioritize clarity and maintainability over brevity.
- **Proper Indentation:** Always use **4 spaces per indentation level** (never tabs, and never mix tabs and spaces). Break long expressions cleanly across lines using parentheses.
- **Detailed Variable Names:** Always use clear, descriptive variable names that communicate intent (e.g., `targetPlayer`, `vehiclePosition`, `distanceSquared`, `remainingSupplyCount`). Avoid cryptic abbreviations or single-letter names (e.g., `p`, `v`, `x`, `d`, `tmp`).
- **Follow PEP-8:** Follow the bundled [PEP-8 Style Guide](references/pep8-style-guide.md) for indentation, 79-character line limits, blank lines, whitespace around operators, import grouping, and `is None` / `is not None` comparisons, harmonized with PR:BF2's repository naming conventions below.

## 3. Naming & Coding Conventions

Adhere strictly to the established Project Reality codebase patterns (following PEP-8 formatting with PR naming idioms):

- **Classes:** Use `PascalCase` (e.g., `ReportSupplies`, `DeviationOnSwitch`, `ProjectileHandler`).
- **Functions & Methods:** Use `camelCase` (e.g., `playerConnect`, `playerChangeWeapon`, `calcDistanceSquared`, `sendRoundStatistics`).
- **Global Variables & Constants:** Use `g_` prefix followed by camelCase or snake_case (e.g., `g_maxPlayers`, `g_serverName`, `g_supply_objects`), and `UPPER_SNAKE_CASE` for module-level constants.
- **Module Aliasing:** When importing internal PR modules, use standard short `r` aliases for namespacing clarity:

    ```python
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

## 4. Core Architectural Patterns

### A. Static Class / Namespace Pattern (`@classmethod`)

Rather than instantiating heavy stateful objects everywhere, feature handlers and utility systems are structured as classes containing `@classmethod` methods (`init`, `refresh`, `send`, `stop`, etc.):

```python
class FeatureHandler:
    trackedPlayers = set()

    @classmethod
    def init(cls):
        if rmemory.isWindowsListenServer:
            return

        rtimer.repeatingTask(cls.refresh, 1.0)
        host.registerHandler('PlayerConnect', cls.playerConnect, 1)

    @classmethod
    def playerConnect(cls, connectingPlayer):
        cls.trackedPlayers.add(connectingPlayer)

    @classmethod
    def refresh(cls, args=None):
        for activePlayer in bf2.playerManager.getPlayers():
            if activePlayer not in cls.trackedPlayers:
                continue
            # Handler logic here
```

### B. Event Handling & Priorities

- Register engine event callbacks using `host.registerHandler('EventName', callback, priority)`.
- Common events: `'PlayerConnect'`, `'PlayerDisconnect'`, `'PlayerChangeWeapon'`, `'PlayerDeath'`, `'Chat'`, etc.

### C. Timers & Asynchronous Tasks

- Use `rtimer.repeatingTask(callback, intervalSeconds)` for periodic polling or updates.
- Use `rtimer.callLater(delaySeconds, callback, *args)` for delayed execution.

### D. Debugging & Logging

- Use `rdebug.debugMessage(message, category)` for targeted runtime diagnostics.

## 5. Reference Documentation Index

All reference material is stored locally within this skill:

- [PEP-8 Style Guide](references/pep8-style-guide.md)
- [Coding Standards](references/coding-standards.md)
- [Common Architectural Patterns](references/common-patterns.md)
- [Debugging & Memory Safety Playbook](references/debugging-playbook.md)
- [Unit Testing & Mocking Guide](references/testing-guide.md)
