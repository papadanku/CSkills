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

## 2. Naming & Coding Conventions

Adhere strictly to the established Project Reality codebase patterns (blending PEP8 with PR idioms):

- **Classes:** Use `PascalCase` (e.g., `ReportSupplies`, `DeviationOnSwitch`, `ProjectileHandler`).
- **Functions & Methods:** Use `camelCase` (e.g., `playerConnect`, `playerChangeWeapon`, `calcDistanceSquared`, `sendRoundStatistics`).
- **Global Variables & Constants:** Use `g_` prefix followed by camelCase or snake_case (e.g., `g_maxPlayers`, `g_serverName`, `g_supply_objects`).
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

## 3. Core Architectural Patterns

### A. Static Class / Namespace Pattern (`@classmethod`)

Rather than instantiating heavy stateful objects everywhere, feature handlers and utility systems are structured as classes containing `@classmethod` methods (`init`, `refresh`, `send`, `stop`, etc.):

```python
class FeatureHandler:
    trackedItems = set()

    @classmethod
    def init(cls):
        if rmemory.isWindowsListenServer:
            return
        rtimer.repeatingTask(cls.refresh, 1.0)
        host.registerHandler('PlayerConnect', cls.playerConnect, 1)

    @classmethod
    def playerConnect(cls, player):
        cls.trackedItems.add(player)

    @classmethod
    def refresh(cls, args=None):
        for player in bf2.playerManager.getPlayers():
            if player not in cls.trackedItems:
                continue
            # Logic here
```

### B. Event Handling & Priorities

- Register engine event callbacks using `host.registerHandler('EventName', callback, priority)`.
- Common events: `'PlayerConnect'`, `'PlayerDisconnect'`, `'PlayerChangeWeapon'`, `'PlayerDeath'`, `'Chat'`, etc.

### C. Timers & Asynchronous Tasks

- Use `rtimer.repeatingTask(callback, intervalSeconds)` for periodic polling or updates.
- Use `rtimer.callLater(delaySeconds, callback, *args)` for delayed execution.

### D. Debugging & Logging

- Use `rdebug.debugMessage(message, category)` for targeted runtime diagnostics.

## 4. Reference Documentation Index

For deeper diving, consult the bundled reference files:

- [Coding Standards](references/coding-standards.md)
- [Common Architectural Patterns](references/common-patterns.md)
- [Debugging & Memory Safety Playbook](references/debugging-playbook.md)
- [Unit Testing & Mocking Guide](references/testing-guide.md)
