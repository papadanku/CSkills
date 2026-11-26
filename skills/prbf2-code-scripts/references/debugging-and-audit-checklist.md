
# PR:BF2 Debugging & Script Audit Checklist

Grounded in PR:BF2 debugger documentation, `.con` grammar rules, `AIDLL.dll` findings, and LOD/collision guidelines.

## 1. Using the PR:BF2 Debugger

- Launch in **windowed mode** via PR Launcher (`Right-click PLAY -> Launch Debugger`) with an offline/converted debugger profile. Fullscreen mode only writes logs; windowed mode surfaces modal assert/error dialogs for critical failures.
- Ignore benign texture-coordinate warnings during map load (click Continue).
- Inspect `mods/pr/logs/` (in the game/mod installation):
  - **BFLog**: Standard error messages (missing files, template errors, assert failures).
  - **Debug log**: Detailed trace (`Debug`, `Warning`, `Error`, `Assert`). Collision mesh and template-context errors often appear **earlier** than the final crash line - search for `Error` and `Assert` near recently modified objects.

## 2. Common CTD & Logic Failure Patterns

| Symptom / Error | Root Cause | Diagnostic & Fix |
| :--- | :--- | :--- |
| Crash or silent property no-op in `.tweak` | Wrong or missing active template context | Ensure `ObjectTemplate.activeSafe <Class> <Name>` is placed at the top of `.tweak` and before every child sub-template block (`Bundle`, `RotationalBundle`, `EntryPoint`, `Camera`, `GenericFireArm`). |
| `ObjectTemplate` not found / broken child | `ObjectTemplate.addTemplate <child>` references a template never created or loaded later | Verify `<child>.con` is executed before or within the parent's load order, or `ObjectTemplate.create <Class> <child>` exists in `.con`/`.tweak`. |
| `v_arg1` or caller `v_*` is empty/undefined | Confused `include` vs `run` | `include` shares caller `v_*` scope and takes **no** args; `run` isolates scope and passes `v_arg1..N`. |
| `CRD_EXPONENTIAL` always returns `0` | `Number1` (mean) set to `0`, e.g. `CRD_EXPONENTIAL/0/180/1` | `Number2` is ignored by `CRD_EXPONENTIAL`. Set `Number1` to desired non-zero mean, or use `CRD_UNIFORM/min/max/sym`. |
| Missing mesh, collision, or sound crash | Relative path or `_bf2` copy still points to deleted local folder | Verify `GeometryTemplate.create`, `CollisionManager.createTemplate`, `ObjectTemplate.sound.soundFilename`, and `run .../animationSystem.inc` paths resolve in the mod's virtual archives (`objects_server.zip`, `objects_vehicles_server.zip`, etc.). |
| Static object missing lightmaps or wrong collision | `StaticMesh` lightmap/material flags misconfigured | Check `GeometryTemplate.doNotGenerateLightmaps`, `ObjectTemplate.physicsType Mesh`, and `ObjectTemplate.mapMaterial` indices against `material/materialmanagerdefine.con`. |
| HUD element missing or overlapping | Wrong `GuiIndex` or parent node in `hudBuilder.*` | Verify `hudBuilder.setNodeLogicShowVariable EQUAL GuiIndex <id>` matches `VehicleHud`/`WeaponHud.guiIndex` and atlas textures exist in `atlas/atlaslist.con`. |
| Network desync / ghosting error in MP | Missing or mismatched `NetworkableInfo` on `PlayerControlObject`, `RotationalBundle`, `GenericFireArm`, or `SpawnPoint` | Set `ObjectTemplate.setNetworkableInfo <InfoName>` (e.g. `BasicInfo`, `SpringInfo`, `NoGhostingInfo`) consistently on networked templates. |
| AI bot ignores weapon/vehicle or crashes SAI | Missing `ObjectTemplate.aiTemplate`, broken `weaponTemplate`, or legacy BF1942 SAI conditional | Link `ObjectTemplate.aiTemplate <Name>` in `.tweak`; verify `weaponTemplate.setStrength` and `maxRange`; avoid non-working SAI conditionals (`AverageStrategicStrength`, `Security`, etc.) and `v_arg3 < 13`. |
| Multi-line `beginRem` fails in console | Executed via interactive in-game console | `beginRem ... endRem` only works when parsed from `.con`/`.tweak`/`.inc` files by the engine. |

## 3. Script Audit Checklist (Before Committing Changes)

1. **Template Context Safety**: Every `.tweak` file starts with `ObjectTemplate.activeSafe <Class> <Name>` matching `.con`'s `ObjectTemplate.create <Class> <Name>`.
2. **Component Integrity**: Every `ObjectTemplate.createComponent <Comp>` is wrapped in matching `rem ---BeginComp:<Comp> ---` and `rem ---EndComp ---` comments.
3. **Multiplayer & Co-Op Parity**:
   - Networked objects (`PlayerControlObject`, `RotationalBundle`, `GenericFireArm`, deployables) have valid `setNetworkableInfo`.
   - If a vehicle or weapon is used in Co-op, check whether a `_bf2` variant or `.ai` file (`Weapons.ai` / `Objects.ai`) needs matching updates.
4. **Asset & Path Hygiene**:
   - No broken `GeometryTemplate`, `CollisionManager`, `.ssc`/`.ogg` sound, HUD `.tga`/`.dds`, or `.ske`/`.baf` animation paths.
   - `materialmanagerdefine.con` is not hand-edited out of sync with PRMaterials.
   - Remove dead/redundant duplicate property lines and unreferenced child templates.
5. **Performance & LODs**:
   - Check `GeometryTemplate.setSubGeometryLodDistance`, `maxSkip3pLods`, `cullRadiusScale`, and collision mesh assignments (`col0`-`col3`, with `col3` required for AI navmesh generation).
