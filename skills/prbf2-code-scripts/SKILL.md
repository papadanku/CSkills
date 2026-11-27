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

## Navigating `references/` on Demand

The `references/` directory is organized into focused topic folders so you can search/browse by domain and load **only** the specific slice needed for the current task:

- **`references/grammar/`** — Core syntax, scoping, distributions, and template context:
    - `references/grammar/file-roles-and-lifecycle.md`: `.con` -> `.tweak` -> `.inc` lifecycle and typical file contents.
    - `references/grammar/syntax-and-scoping.md`: Comments (`rem`, `beginRem`), variables (`v_*`/`c_*`), conditionals/loops, and `include` vs `run` vs `return` scoping.
    - `references/grammar/crd-and-template-context.md`: `CRD_*` distributions, `ObjectTemplate.create` / `activeSafe` / `active`, and `BeginComp`/`EndComp` blocks.
- **`references/properties/`** — Complete documented command catalogs, `ObjectTemplate.*` properties, components, and UDL tokens:
    - **`references/properties/ai/`** — AI command tree split by subsystem:
        - `references/properties/ai/core/ai-and-iai.md`: `iai.*` and `ai.*` properties.
        - `references/properties/ai/core/it-flags.md`: `IT*` AI type flags.
        - `references/properties/ai/core/settings-and-bots.md`: `aisettings.*` and `aibotmanager.*`.
        - `references/properties/ai/strategy/aistrategy.md`: `aistrategy.*` properties.
        - `references/properties/ai/strategy/aistrategicarea.md`: `aistrategicarea.*` properties.
        - `references/properties/ai/navigation/aipathfinding.md`: `aipathfinding.*` properties.
        - `references/properties/ai/navigation/ailandingzone.md`: `ailandingzone.*` properties.
        - `references/properties/ai/templates/aitemplate.md`: `aitemplate.*` properties.
        - `references/properties/ai/templates/aitemplateplugin.md`: `aitemplateplugin.*` properties.
        - `references/properties/ai/templates/weapontemplate.md`: `weaponTemplate.*` properties.
        - `references/properties/ai/templates/object-and-objecttemplate.md`: AI-side `objecttemplate.*` and `object.*` properties.
        - `references/properties/ai/scripting-and-debug/debug-random-radio-cheats-script.md`: `aidebug.*`, `airandom.*`, `airadio.*`, `aicheats.*`, `aiscript.*`.
    - **`references/properties/objecttemplate/`** — Top-level `ObjectTemplate.*` properties split by domain:
        - `references/properties/objecttemplate/components/components.md`: All 44 `ObjectTemplate.createComponent` blocks.
        - `references/properties/objecttemplate/components/weapons-and-hud.md`: `ObjectTemplate` component sub-properties for `ammo.*`, `detonation.*`, `deviation.*`, `fire.*`, `follow.*`, `helpHud.*`, `ik.*`, `penetrate.*`, `recoil.*`, `seek.*`, `target.*`, `warningHud.*`, `weaponHud.*`, `zoom.*`.
        - `references/properties/objecttemplate/components/vehicles-and-core.md`: `ObjectTemplate` component sub-properties for `ability.*`, `abilityHud.*`, `animation.*`, `antenna.*`, `armor.*`, `audio.*`, `collision.*`, `geometry.*`, `newCar2.*`, `postProcess.*`, `radio.*`, `sound.*`, `strategicObject.*`, `vehicleHud.*`.
        - `references/properties/objecttemplate/core/template-lifecycle-and-hierarchy.md`: Lifecycle, hierarchy, geometry, LODs, and networkables.
        - `references/properties/objecttemplate/effects/particles-emitters-decals-and-lights.md`: Particles, emitters, decals, lights, and shadows.
        - `references/properties/objecttemplate/misc/general-a-to-l.md` & `references/properties/objecttemplate/misc/general-m-to-z.md`: Remaining general `ObjectTemplate.*` properties (A-L and M-Z).
        - `references/properties/objecttemplate/physics/collision-physics-and-materials.md`: Collision, physics, mass, drag, gravity, and materials.
        - `references/properties/objecttemplate/vehicles/engines-rotors-wings-and-controls.md`: Engines, rotors, wings, wheels, gears, and controls.
        - `references/properties/objecttemplate/vehicles/cameras-seats-and-entry.md`: Cameras, FOV, seats, entry points, and soldier movement.
        - `references/properties/objecttemplate/weapons/firearms-ammo-and-projectiles.md`: Firearms, ammo, projectiles, damage, recoil, deviation, and zoom.
        - `references/properties/objecttemplate/world/sound-triggers-spawners-and-controlpoints.md`: Sound, triggers, spawners, control points, ladders, ziplines, and destructibles.
    - `references/properties/namespaces-internal-and-undocumented.md`: Engine/internal namespaces with 0 documented properties in RealityDocs (`rhooks.`, `admin.`, `BitStream.`, `kitTemplate.`, `aiComm.`, etc.).
    - `references/properties/tokens-objects-and-enums.md`: All 188 `.con`/`.tweak`/`.inc` object classes, inputs, networkables, armor/vehicle enums, `IT*` flags, and `.tac`/`.tai` Atlas tokens.
    - `references/properties/tokens-ai-behaviors-and-types.md`: AI behaviors (`BB*`/`BBP*`), `BAPST*` wrappers, movement properties, and `.ai` unit/armor/kit/input tokens.
- **`references/objects/`** — Domain patterns, polycount/LOD standards, and virtual archive paths:
    - `references/objects/archives-overview.md`: Virtual archive-to-domain mapping (`objects_*.zip`, `menu_server.zip`, `common_server.zip`, `server.zip`).
    - `references/objects/static-and-destructibles.md`: Static buildings (`StaticMesh`, `SimpleObject`), lightmaps/LODs, and destructible/wreck `Armor` setups.
    - `references/objects/polycounts-and-lods.md`: Weapon/vehicle polycount & LOD guidelines and converting destroyable objects to `_nondest`.
    - `references/objects/terrain-and-level-scripts.md`: `init.con`, `heightdata.con`, `terrain.con`, `water.con`, `overgrowth*.con`, `ambientobjects.con`.
    - `references/objects/vehicles.md`: `PlayerControlObject` hierarchy (`RotationalBundle`, `Engine`, `EntryPoint`, `Camera`, `GenericFireArm`), HUDs, and `_bf2` summary.
    - `references/objects/props-deployables-and-spawners.md`: Command posts/ACVs, deployables/ammo caches, spawners, and props.
    - `references/objects/soldiers-and-kits.md`: `Soldier`, ragdolls, `animationsystem*.inc`, `Kit`, and `*_init.tweak` spawnkits.
    - `references/objects/hud-menus-and-materials.md`: `hudBuilder.*`, `swiffHost.*`, `atlaslist.con`, and `materialmanagerdefine.con` / `impactsounds.con`.
- **`references/ai-and-coop/`** — `.ai` scripting, Strategic AI, and Co-Op:
    - `references/ai-and-coop/weapon-and-unit-ai.md`: `weaponTemplate.*` (`Weapons.ai`) and `aiTemplate.*` / `aiTemplatePlugIn.*` (`Objects.ai`).
    - `references/ai-and-coop/strategic-ai-and-aidll.md`: Broken legacy BF1942 `AIDLL.dll` conditionals, `v_arg3` mapping, comparison aliases, Strategic AI DB variables, and `TTN*`/`CST*`/`IT*` flags.
    - `references/ai-and-coop/coop-navmesh-and-vehicles.md`: `AI/AI.ai` navmesh setup and `_bf2` one-man co-op vehicle conversion.
- **`references/debugging-and-auditing/`** — Troubleshooting, CLI flags, and verification:
    - `references/debugging-and-auditing/pr-debugger-and-logs.md`: Windowed PR Debugger workflow and `mods/pr/logs/` inspection.
    - `references/debugging-and-auditing/ctd-troubleshooting.md`: Common CTD & logic failure root causes and fixes.
    - `references/debugging-and-auditing/pre-commit-audit-checklist.md`: Pre-commit template context, component, MP/co-op parity, asset path, and LOD/collision checklist.
    - `references/debugging-and-auditing/command-line-options.md`: `BF2.exe` / `BF2_r.exe` command-line options (`+multi`, `+wx`, `+loadLevel`, etc.).

## Core Workflows

### 1. Processing (Parsing and Tracing)

1. Start from the entry `.con` file and record every `GeometryTemplate.create`, `CollisionManager.createTemplate`, and `ObjectTemplate.create` (whether `SimpleObject`, `PlayerControlObject`, `DestroyableObject`, `GenericFireArm`, `Kit`, `Soldier`, or `Sound`).
2. Follow `include` and `run` directives in execution order, noting scope boundaries (`include` shares `v_*`/`c_*`; `run` isolates scope and binds `v_arg1..N`, such as `if v_arg1 == BF2Editor` in level scripts).
3. Track the active `ObjectTemplate` cursor across every `create`, `activeSafe`, `active`, and `addTemplate` call so each property is attributed to the correct parent or child sub-template (`RotationalBundle`, `EntryPoint`, `Camera`, `Engine`, etc.).
4. Load only the relevant `references/grammar/`, `references/objects/`, and `references/properties/` files for exact command namespaces, `CRD_*` distributions, and component types.

### 2. Editing (Safe, Targeted Modifications)

1. Preserve original casing, `rem` / `beginRem ... endRem` comments, and `rem ---BeginComp:<Comp> ---` / `rem ---EndComp ---` folding markers.
2. Verify `ObjectTemplate.activeSafe <Class> <Name>` precedes any property edits in `.tweak` files, especially before child sub-templates (`RotationalBundle`, `Bundle`, `Camera`, `EntryPoint`).
3. Keep multiplayer and co-op parity in sync: check `setNetworkableInfo`, `_bf2` one-man co-op vehicle variants (`references/ai-and-coop/coop-navmesh-and-vehicles.md`), and linked `.ai` (`Weapons.ai` / `Objects.ai`) files when modifying vehicles or weapons.
4. Do not hand-edit `material/materialmanagerdefine.con` out of sync with PRMaterials (`references/objects/hud-menus-and-materials.md`).
5. Use `assets/` templates as structural baselines when creating new files.

### 3. Analyzing (Auditing and Optimization)

1. Check active template context on every `ObjectTemplate.*` block and verify all `addTemplate` targets exist.
2. Validate asset paths for `StaticMesh`/`BundledMesh`, `.collisionmesh`, `.ssc`/`.ogg` sounds, `.ske`/`.baf` animations, and HUD `.tga`/`.dds` icons.
3. Audit performance and gameplay flags: `GeometryTemplate` LOD/lightmap settings (`setSubGeometryLodDistance`, `doNotGenerateLightmaps`, `maxSkip3pLods`, `cullRadiusScale`), `col3` presence for AI navmeshing, `NetworkableInfo` on synced parts, and dead or duplicate property lines (`references/debugging-and-auditing/pre-commit-audit-checklist.md`).
4. For HUDs, verify `GuiIndex` links between `VehicleHud`/`WeaponHud` and `hudBuilder.setNodeLogicShowVariable` plus atlas registration. For `.ai` files, verify `IT*` flags and absence of broken legacy BF1942 SAI conditionals (`references/ai-and-coop/strategic-ai-and-aidll.md`).

### 4. Debugging (CTDs and Runtime Failures)

1. Reproduce using the PR Debugger in windowed mode and inspect `mods/pr/logs/` (`references/debugging-and-auditing/pr-debugger-and-logs.md`), scanning earlier `Error`/`Assert` lines for collision or template faults rather than only the final line.
2. Walk through `references/debugging-and-auditing/ctd-troubleshooting.md` to diagnose context mismatches, `include` vs `run` scope bugs, `CRD_EXPONENTIAL` zero-mean traps, broken relative paths in `_bf2` copies, static lightmap/material errors, HUD `GuiIndex` mismatches, or missing `aiTemplate` links.
3. Provide exact line-level fixes and explain the engine rule behind each change.

## Handling Ambiguity and Missing Context

- If a `.tweak` or `.inc` file is provided without its parent `.con` (or vice versa), state which parent `ObjectTemplate` or child template definitions are missing and ask for them or note any unverified assumptions explicitly.
- Never guess undocumented engine properties or invent asset paths. Cross-check tokens against the relevant files in `references/properties/`, `references/objects/`, and `references/ai-and-coop/`.

## Bundled Assets

- `assets/static-destructible.con.txt`, `assets/static-destructible.tweak.txt` - Static building and destructible `Armor` templates.
- `assets/vehicle-pco.con.txt`, `assets/vehicle-pco.tweak.txt` - Vehicle `PlayerControlObject` templates.
- `assets/hud-and-material.con.txt` - `hudBuilder.*`, `Sound`, and `materialManager.*` templates.
- `assets/weapon-template.con.txt`, `assets/weapon-template.tweak.txt`, `assets/animationsystem1p.inc.txt`, `assets/weapon-and-vehicle.ai.txt` - Weapon, 1P animation, and AI templates.

## Bundled Scripts

Run these self-contained Python 3 utilities (each supports `--help` and `--json` where applicable):

- `scripts/audit_scripts.py` - Pre-commit linter and static auditor for `.con`, `.tweak`, `.inc`, and `.ai` files.
- `scripts/trace_templates.py` - Traces `ObjectTemplate` hierarchy, components, and `include`/`run` execution chains.
- `scripts/convert_nondest.py` - Converts destroyable `.con`/`.tweak` objects into `_nondest` `SimpleObject` variants.
- `scripts/convert_coop_bf2.py` - Generates `_bf2` one-man co-op vehicle `.con`/`.tweak` variants.
- `scripts/scaffold_template.py` - Scaffolds new `.con`/`.tweak`/`.inc`/`.ai` files from `assets/`.
- `scripts/parse_pr_log.py` - Parses PR Debugger logs (`mods/pr/logs/`) and maps errors to CTD hints.
- `scripts/lookup_property.py` - Searches `references/properties/` for command signatures, return types, and notes.

## Gotchas

- `beginRem ... endRem` works in files loaded by the engine, not in the interactive console.
- `CRD_EXPONENTIAL/0/180/1` always returns `0` because `Number2` is ignored and `Number1` (mean) is `0`.
- `include` shares `v_*` variables and accepts no arguments; `run` isolates scope and passes `v_arg1..N`.
- Legacy BF1942 SAI conditionals (`AverageStrategicStrength`, `Security`, etc.) and `v_arg3 < 13` fail or return `0` in BF2 `AIDLL.dll`.
