---
name: prbf2-code-scripts
description: Process, generate, edit, analyze, and debug Project Reality Battlefield 2 (PR:BF2) modding scripts (.ai, .con, .tweak, .inc). Use whenever working with BF2 or PR:BF2 ObjectTemplate configs, static buildings and destructibles, terrain and overgrowth, vehicles, command posts, deployables, soldiers and kits, weapons, HUD/menu scripts, materials, animationSystem .inc fragments, or AI/co-op bot definitions.
---

# prbf2-code-scripts

Comprehensive workflow for authoring, parsing, auditing, and debugging Project Reality: Battlefield 2 (PR:BF2) `.con`, `.tweak`, `.inc`, and `.ai` scripts across the full static and dynamic object ecosystem.

## When to Use

Use this skill when the user asks to:

- Create, edit, or refactor `.con`, `.tweak`, `.inc`, or `.ai` files for PR:BF2 or BF2 mods.
- Work with static buildings, destructibles/wrecks, terrain/overgrowth/water, vehicles (`PlayerControlObject`), command posts/deployables, soldiers/kits, weapons, HUD/menus (`hudBuilder.*`, `swiffHost.*`), or materials.
- Trace `ObjectTemplate` inheritance, `include` / `run` execution chains, or active template context.
- Audit scripts for multiplayer/co-op parity, LOD/lightmap/collision issues, dead code, or path errors.
- Debug PR:BF2 crashes (CTDs), broken objects/vehicles/HUDs, or bot/co-op AI behavior.

## File Roles and Ecosystem Coverage

Distinguish each extension's role before reading or modifying files:

- **`.con` (Definition and Entry Point)**: Instantiates geometry (`GeometryTemplate.create StaticMesh|BundledMesh`), collision (`CollisionManager.createTemplate`), network info (`NetworkableInfo.createNewInfo`), and templates (`ObjectTemplate.create <Class> <Name>`), then loads `.tweak` via `include` and `.inc` via `run`. Also used for level/terrain (`init.con`, `terrain.con`, `heightdata.con`, `water.con`, `overgrowth.con`), HUD (`hudBuilder.*`), flash menus (`swiffHost.*`), and materials (`Material.*`, `materialManager.*`).
- **`.tweak` (Property and Component Tuning)**: Tunes an already-created template. Always begins with `ObjectTemplate.activeSafe <Class> <Name>` and wraps components in `rem ---BeginComp:<Comp> ---` / `ObjectTemplate.createComponent <Comp>` / `rem ---EndComp ---`. Covers static lightmap/LODs, `Armor` destruction/damage states (`e_dstate_*`, `e_vexp_*`, `e_mexp_*`), vehicles, deployables, spawnkits (`*_init.tweak`), weapons, and HUD tweaks.
- **`.inc` (Reusable Script Fragment)**: Shared blocks such as `animationsystem*.inc` (`.ske`/`.baf` references) or shared sub-configs. Invoked via `run <path> [args]` (isolated scope, args in `v_arg1..N`) or `include <path>` (shares caller's `v_*` / `c_*` variables).
- **`.ai` (AI and Co-Op Logic)**: Defines `weaponTemplate.*` (for `GenericFireArm`), `aiTemplate.*` / `aiTemplatePlugIn.*` (for vehicles/units), and map/strategy configs (`aiPathfinding.*`, `aiStrategy.*`, `aiSettings.*`).

Note on paths: paths like `objects_server.zip`, `objects_common_server.zip`, `objects_vehicles_server.zip`, `objects_weapons_server.zip`, `menu_server.zip`, `common_server.zip`, `server.zip`, and `mods/pr/...` refer to PR:BF2 virtual game/mod archives, not files bundled inside this skill.

## Core Workflows

### 1. Processing (Parsing and Tracing)

1. Start from the entry `.con` file and record every `GeometryTemplate.create`, `CollisionManager.createTemplate`, and `ObjectTemplate.create` (whether `SimpleObject`, `PlayerControlObject`, `DestroyableObject`, `GenericFireArm`, `Kit`, `Soldier`, or `Sound`).
2. Follow `include` and `run` directives in execution order, noting scope boundaries (`include` shares `v_*`/`c_*`; `run` isolates scope and binds `v_arg1..N`, such as `if v_arg1 == BF2Editor` in level scripts).
3. Track the active `ObjectTemplate` cursor across every `create`, `activeSafe`, `active`, and `addTemplate` call so each property is attributed to the correct parent or child sub-template (`RotationalBundle`, `EntryPoint`, `Camera`, `Engine`, etc.).
4. Consult `references/con-tweak-inc-grammar.md`, `references/object-types-and-archives.md`, and `references/udl-commands-and-tokens.md` for exact command namespaces, `CRD_*` distributions, and component types.

### 2. Editing (Safe, Targeted Modifications)

1. Preserve original casing, `rem` / `beginRem ... endRem` comments, and `rem ---BeginComp:<Comp> ---` / `rem ---EndComp ---` folding markers.
2. Verify `ObjectTemplate.activeSafe <Class> <Name>` precedes any property edits in `.tweak` files, especially before child sub-templates (`RotationalBundle`, `Bundle`, `Camera`, `EntryPoint`).
3. Keep multiplayer and co-op parity in sync: check `setNetworkableInfo`, `_bf2` one-man co-op vehicle variants, and linked `.ai` (`Weapons.ai` / `Objects.ai`) files when modifying vehicles or weapons.
4. Do not hand-edit `material/materialmanagerdefine.con` out of sync with PRMaterials.
5. Use `assets/` templates as structural baselines when creating new files.

### 3. Analyzing (Auditing and Optimization)

1. Check active template context on every `ObjectTemplate.*` block and verify all `addTemplate` targets exist.
2. Validate asset paths for `StaticMesh`/`BundledMesh`, `.collisionmesh`, `.ssc`/`.ogg` sounds, `.ske`/`.baf` animations, and HUD `.tga`/`.dds` icons.
3. Audit performance and gameplay flags: `GeometryTemplate` LOD/lightmap settings (`setSubGeometryLodDistance`, `doNotGenerateLightmaps`, `maxSkip3pLods`, `cullRadiusScale`), `col3` presence for AI navmeshing, `NetworkableInfo` on synced parts, and dead or duplicate property lines.
4. For HUDs, verify `GuiIndex` links between `VehicleHud`/`WeaponHud` and `hudBuilder.setNodeLogicShowVariable` plus atlas registration. For `.ai` files, verify `IT*` flags and absence of broken legacy BF1942 SAI conditionals (`references/ai-coop-scripting.md`).

### 4. Debugging (CTDs and Runtime Failures)

1. Reproduce using the PR Debugger in windowed mode and inspect `mods/pr/logs/` (check both BFLog and Debug log, scanning earlier `Error`/`Assert` lines for collision or template faults rather than only the final line).
2. Walk through `references/debugging-and-audit-checklist.md` to diagnose context mismatches, `include` vs `run` scope bugs, `CRD_EXPONENTIAL` zero-mean traps, broken relative paths in `_bf2` copies, static lightmap/material errors, HUD `GuiIndex` mismatches, or missing `aiTemplate` links.
3. Provide exact line-level fixes and explain the engine rule behind each change.

## Handling Ambiguity and Missing Context

- If a `.tweak` or `.inc` file is provided without its parent `.con` (or vice versa), state which parent `ObjectTemplate` or child template definitions are missing and ask for them or note any unverified assumptions explicitly.
- Never guess undocumented engine commands or invent asset paths. Cross-check tokens against `references/udl-commands-and-tokens.md`, `references/object-types-and-archives.md`, and `references/ai-coop-scripting.md`.

## Bundled References and Assets

- `references/con-tweak-inc-grammar.md` - Syntax, `include` vs `run` scoping, `CRD_*`, and active template context.
- `references/object-types-and-archives.md` - Static buildings/destructibles, map/terrain/overgrowth, vehicles, command posts/deployables, soldiers/kits, HUD/menus, materials, and virtual archive layout.
- `references/udl-commands-and-tokens.md` - Complete catalog of 139 command namespaces, 44 components, 188 object/enum tokens, and AI/Atlas tokens.
- `references/ai-coop-scripting.md` - `.ai` structure, `TTN*`/`CST*`/`IT*` flags, non-working `AIDLL.dll` conditionals, and `_bf2` co-op conversion.
- `references/debugging-and-audit-checklist.md` - PR Debugger workflow, CTD table, and pre-commit audit checklist.
- `assets/static-destructible.con.txt`, `assets/static-destructible.tweak.txt` - Static building and destructible `Armor` templates.
- `assets/vehicle-pco.con.txt`, `assets/vehicle-pco.tweak.txt` - Vehicle `PlayerControlObject` templates.
- `assets/hud-and-material.con.txt` - `hudBuilder.*`, `Sound`, and `materialManager.*` templates.
- `assets/weapon-template.con.txt`, `assets/weapon-template.tweak.txt`, `assets/animationsystem1p.inc.txt`, `assets/weapon-and-vehicle.ai.txt` - Weapon, 1P animation, and AI templates.

## Gotchas

- `beginRem ... endRem` works in files loaded by the engine, not in the interactive console.
- `CRD_EXPONENTIAL/0/180/1` always returns `0` because `Number2` is ignored and `Number1` (mean) is `0`.
- `include` shares `v_*` variables and accepts no arguments; `run` isolates scope and passes `v_arg1..N`.
- Legacy BF1942 SAI conditionals (`AverageStrategicStrength`, `Security`, etc.) and `v_arg3 < 13` fail or return `0` in BF2 `AIDLL.dll`.
