
# Common Architectural Patterns - Project Reality Python

This document outlines the recurrent design patterns used throughout Project Reality game logic scripts.

## 1. Class-Based Static Utility Pattern

Instead of heavy instantiation or standalone procedural spaghetti, feature modules group functionality inside classes utilizing `@classmethod`:

```python
class WeaponDeviationHandler:
    activeModifier = 1.0

    @classmethod
    def init(cls):
        if rmemory.isWindowsListenServer:
            return
        host.registerHandler('PlayerChangeWeapon', cls.playerChangeWeapon, 1)

    @classmethod
    def playerChangeWeapon(cls, player, oldWeapon, newWeapon):
        if newWeapon is None:
            return
        # Handler logic
```

## 2. Engine Event Registration

Events from the BF2 server engine are hooked via `host.registerHandler`:

- **Syntax:** `host.registerHandler(eventName, callbackFunction, priority)`
- **Common Events:**
    - `'PlayerConnect'` / `'PlayerDisconnect'`
    - `'PlayerSpawn'` / `'PlayerDeath'`
    - `'PlayerChangeWeapon'`
    - `'Chat'`
    - `'ServerGameStatus'`

## 3. Timers and Repeating Tasks

For periodic tasks (e.g., checking player positions, updating custom UI/launchers, scanning objects):

```python
# Repeating task every 0.8 seconds
rtimer.repeatingTask(cls.refresh, 0.8)

# Delayed execution
rtimer.callLater(3.0, cls.delayedCallback, player)
```

## 4. Entity Access and Null Checks

BF2 player and vehicle references can become `None` unexpectedly (e.g., during disconnects or death transitions). Always guard entity access:

```python
player = bf2.playerManager.getPLAYER(playerId)
if player is None:
    return

sol = player.getDefaultVehicle()
veh = player.getVehicle()
if sol is None or (veh is not sol):
    return
```
