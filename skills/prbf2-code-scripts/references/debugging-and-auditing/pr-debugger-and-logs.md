# PR:BF2 Debugger & Log Inspection

Grounded in PR:BF2 debugger documentation, `.con` grammar rules, `AIDLL.dll` findings, and LOD/collision guidelines.

## Launching & Using the PR:BF2 Debugger

- Launch in **windowed mode** via PR Launcher (`Right-click PLAY -> Launch Debugger`) with an offline/converted debugger profile. Fullscreen mode only writes logs; windowed mode surfaces modal assert/error dialogs for critical failures.
- Ignore benign texture-coordinate warnings during map load (click Continue).

## Inspecting `mods/pr/logs/`

Inspect `mods/pr/logs/` (in the game/mod installation):

- **BFLog**: Standard error messages (missing files, template errors, assert failures).
- **Debug log**: Detailed trace (`Debug`, `Warning`, `Error`, `Assert`). Collision mesh and template-context errors often appear **earlier** than the final crash line - search for `Error` and `Assert` near recently modified objects.
