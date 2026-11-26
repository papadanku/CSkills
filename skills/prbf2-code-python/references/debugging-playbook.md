
# Debugging & Memory Safety Playbook - Project Reality Python

This playbook addresses common bugs, server crashes, and edge cases encountered when developing PR:BF2 Python scripts.

## 1. Common Pitfalls & Errors

### A. Unchecked `None` References

- **Symptom:** `AttributeError: 'NoneType' object has no attribute ...` in server logs.
- **Cause:** Accessing methods or attributes on players, vehicles, weapons, or components without verifying they exist.
- **Solution:** Always validate return values from `player.getVehicle()`, `rmemory.getWeaponsDeviationComponent(...)`, etc.

### B. Windows Listen Server vs Dedicated Server Discrepancies

- **Symptom:** Memory hook or virtual table pointer (`vptr`) failure on Windows listen servers.
- **Solution:** Wrap memory-dependent or low-level native hooks with safety guards:

    ```python
    if rmemory.isWindowsListenServer:
        return  # TODO - needs vptr
    ```

### C. Callback Synchronization Issues

- **Symptom:** Race conditions or crashes when calling engine functions (like `sendGameEvent`) inside synchronous event callbacks (`PlayerConnect`).
- **Solution:** Defer actions or assume safe defaults during connection callbacks, performing periodic checks via `rtimer` instead of reacting instantly inside synchronous hooks where appropriate.

## 2. Debug Logging

Use `rdebug.debugMessage()` with category tags to isolate subsystems during testing:

```python
rdebug.debugMessage("Weapon deviation modified: %s" % newDeviation, "deviation")
```
