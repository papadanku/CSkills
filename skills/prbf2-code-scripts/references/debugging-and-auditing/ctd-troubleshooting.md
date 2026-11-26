# PR:BF2 Common CTD & Logic Failure Troubleshooting

## Crash or silent property no-op in `.tweak`

- **Root Cause**: Wrong or missing active template context
- **Diagnostic & Fix**: Ensure `ObjectTemplate.activeSafe <Class> <Name>` is placed at the top of `.tweak` and before every child sub-template block (`Bundle`, `RotationalBundle`, `EntryPoint`, `Camera`, `GenericFireArm`).

## `ObjectTemplate` not found / broken child

- **Root Cause**: `ObjectTemplate.addTemplate <child>` references a template never created or loaded later
- **Diagnostic & Fix**: Verify `<child>.con` is executed before or within the parent's load order, or `ObjectTemplate.create <Class> <child>` exists in `.con`/`.tweak`.

## `v_arg1` or caller `v_*` is empty/undefined

- **Root Cause**: Confused `include` vs `run`
- **Diagnostic & Fix**: `include` shares caller `v_*` scope and takes **no** args; `run` isolates scope and passes `v_arg1..N`.

## `CRD_EXPONENTIAL` always returns `0`

- **Root Cause**: `Number1` (mean) set to `0`, e.g. `CRD_EXPONENTIAL/0/180/1`
- **Diagnostic & Fix**: `Number2` is ignored by `CRD_EXPONENTIAL`. Set `Number1` to desired non-zero mean, or use `CRD_UNIFORM/min/max/sym`.

## Missing mesh, collision, or sound crash

- **Root Cause**: Relative path or `_bf2` copy still points to deleted local folder
- **Diagnostic & Fix**: Verify `GeometryTemplate.create`, `CollisionManager.createTemplate`, `ObjectTemplate.sound.soundFilename`, and `run .../animationSystem.inc` paths resolve in the mod's virtual archives (`objects_server.zip`, `objects_vehicles_server.zip`, etc.).

## Static object missing lightmaps or wrong collision

- **Root Cause**: `StaticMesh` lightmap/material flags misconfigured
- **Diagnostic & Fix**: Check `GeometryTemplate.doNotGenerateLightmaps`, `ObjectTemplate.physicsType Mesh`, and `ObjectTemplate.mapMaterial` indices against `material/materialmanagerdefine.con`.

## HUD element missing or overlapping

- **Root Cause**: Wrong `GuiIndex` or parent node in `hudBuilder.*`
- **Diagnostic & Fix**: Verify `hudBuilder.setNodeLogicShowVariable EQUAL GuiIndex <id>` matches `VehicleHud`/`WeaponHud.guiIndex` and atlas textures exist in `atlas/atlaslist.con`.

## Network desync / ghosting error in MP

- **Root Cause**: Missing or mismatched `NetworkableInfo` on `PlayerControlObject`, `RotationalBundle`, `GenericFireArm`, or `SpawnPoint`
- **Diagnostic & Fix**: Set `ObjectTemplate.setNetworkableInfo <InfoName>` (e.g. `BasicInfo`, `SpringInfo`, `NoGhostingInfo`) consistently on networked templates.

## AI bot ignores weapon/vehicle or crashes SAI

- **Root Cause**: Missing `ObjectTemplate.aiTemplate`, broken `weaponTemplate`, or legacy BF1942 SAI conditional
- **Diagnostic & Fix**: Link `ObjectTemplate.aiTemplate <Name>` in `.tweak`; verify `weaponTemplate.setStrength` and `maxRange`; avoid non-working SAI conditionals (`AverageStrategicStrength`, `Security`, etc.) and `v_arg3 < 13`.

## Multi-line `beginRem` fails in console

- **Root Cause**: Executed via interactive in-game console
- **Diagnostic & Fix**: `beginRem ... endRem` only works when parsed from `.con`/`.tweak`/`.inc` files by the engine.
