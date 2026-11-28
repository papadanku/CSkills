---
name: prbf2-code-scripts
description: Comprehensive Project Reality (BF2 engine) modding reference and script engineering suite. Combines the full RealityDocs reference catalog (AI code, CON script grammar, command-line options, console commands, ObjectTemplate properties, Vars.set variables, and asset guidelines) with workflows and tools for authoring, editing, auditing, converting, and debugging .con, .tweak, .inc, and .ai scripts. Use whenever working with BF2 or PR:BF2 ObjectTemplate configs, static buildings, destructibles, terrain, vehicles, command posts, deployables, soldiers, kits, weapons, HUD/menus, materials, console commands, or AI/co-op bots.
---

# prbf2-code-scripts

Unified reference documentation and script engineering workflow for modding Project Reality (Refractor 2 / BF2 engine), combining the complete RealityDocs reference catalog under `references/` with domain guides (`guides/`), starter templates (`assets/`), and PEP-8 Python utilities (`scripts/`).

## System Requirements

These are general guidelines for the minimum requirements for a server.

### Linux & Windows

- **CPU**: 3Ghz Processor (PR uses a lot of CPU, so get the fastest one you can afford).
- **RAM**: 2GB (at least 1GB per server instance plus 1GB for overhead).
- **Disk**: 40GB (about 15GB for server files and installation, plus space for battlerecorder files).

## When to Use

Use this skill when the user asks to:

- Look up Project Reality / BF2 console commands, `ObjectTemplate.*` properties, `Vars.set` engine variables, `ai*` commands, command-line flags, or polycount/LOD guidelines.
- Create, edit, or refactor `.con`, `.tweak`, `.inc`, or `.ai` files for static buildings, destructibles, terrain/overgrowth, vehicles (`PlayerControlObject`), deployables, soldiers/kits, weapons, HUD/menus (`hudBuilder.*`, `swiffHost.*`), or materials.
- Trace `ObjectTemplate` inheritance, `include` / `run` execution chains, or active template context.
- Audit scripts for multiplayer/co-op parity, LOD/lightmap/collision issues, dead code, or path errors.
- Debug PR:BF2 crashes (CTDs), broken objects/vehicles/HUDs, or bot/co-op AI behavior.

## References (`references/`)

Load only the specific slice needed for the current task:

- [AI Code: Bots, Strategy, and Pathfinding](references/ai-bots-strategy-and-pathfinding.md): AI bot manager, strategic areas, landing zones, and pathfinding commands.
- [AI Code: Scripts, Debug, and Templates](references/ai-scripts-and-templates.md): AI debug, radio, script hooks, `aitemplate`, `aitemplateplugin`, and `weaponTemplate` AI properties.
- [AI Code: Types, Flags, and Settings](references/ai-types-and-settings.md): AI `IT` target flags, core `ai.*` commands, and `aisettings.*` configuration.
- [Assets: Polycounts, LOD Guidelines, and Destroyables](references/assets-polycounts-lod-and-destroyables.md): 3D asset polygon budgets, LOD distance guidelines, and converting destroyable objects.
- [Command Line Options](references/command-line-options.md): Project Reality launcher and engine command-line flags and parameters.
- [CON Script Grammar](references/con-script-grammar.md): Syntax, tokens, variables, and structure rules for `.con` and `.tweak` script files.
- [Console: Animation System](references/console-animation-system.md): Animation system console commands, states, and blending parameters.
- [Console: Audio, Sound, and Sample Rates](references/console-audio-and-samplerates.md): Audio engine console commands, sound playback, and sample rate settings.
- [Console Gameplay: Combat Area, Ingame, Spawn Manager, and Physics](references/console-gameplay-combatarea-spawn-physics.md): Console commands for combat areas, ingame HUD/actions, spawn manager, and physics.
- [Console Gameplay: Game Commands](references/console-gameplay-game.md): Core `game.*` console commands for match rules, tickets, teams, and server gameplay.
- [Console Gameplay: Player, Squad, Commander, and Radio](references/console-gameplay-player-squad-commander.md): Console commands for commander assets, player state, squads, and radio messages.
- [Console Graphics: Lighting, Shadows, Shaders, and Environment Maps](references/console-graphics-lighting-shadows-shaders.md): Console commands for lightmanager, shadowmanager, shadermanager, envmaps, and hemimaps.
- [Console Graphics: Collision, Mesh Renderer, Decals, and Textures](references/console-graphics-meshes-collisions-decals.md): Console commands for collision meshes, mesh renderer, decals, and texture manager.
- [Console Graphics: Renderer](references/console-graphics-renderer.md): `renderer.*` console commands for rendering pipeline, post-processing, and draw flags.
- [Console Graphics: Skydome, Weather, Particles, and Effects](references/console-graphics-sky-weather-effects.md): Console commands for skydome, weather, particle systems, and effect tweaking.
- [Console Graphics: Terrain, Heightmap, Overgrowth, and Undergrowth](references/console-graphics-terrain-and-vegetation.md): Console commands for terrain rendering, heightmaps, overgrowth, and undergrowth.
- [Console Matchmaking: Local, Maplist, Profile, and Scoring](references/console-matchmaking-and-scoring.md): Console commands for local server, maplist rotation, player profiles, and scoring.
- [Console Menu: HUD Builder](references/console-menu-hud-builder.md): `hudBuilder.*` console commands for constructing HUD nodes, bars, buttons, and minimaps.
- [Console Menu: Interface, HUD Items, and HUD Manager](references/console-menu-interface-and-hud-items.md): `hudItems.*`, `hudManager.*`, and `menu.*` console commands.
- [Console Objects: Object, Networkables, and Ragdolls](references/console-objects-and-ragdolls.md): `object.*`, `networkableInfo`, and `ragdoll.*` console commands.
- [Console Objects: Geometry Templates and Materials](references/console-objects-geometry-and-materials.md): `geometryTemplate.*` and `material.*` console commands.
- [Console ObjectTemplate (3dMapIcon to animationSystem1P)](references/console-objecttemplate-part-01.md): `objectTemplate.*` properties: (3dMapIcon to animationSystem1P).
- [Console ObjectTemplate (animationSystem3P to cockpitSubGeom)](references/console-objecttemplate-part-02.md): `objectTemplate.*` properties: (animationSystem3P to cockpitSubGeom).
- [Console ObjectTemplate (cockpitSubGeom to detonation.flashbangAdditiveGlowMaxHoldTime)](references/console-objecttemplate-part-03.md): `objectTemplate.*` properties: (cockpitSubGeom to detonation.flashbangAdditiveGlowMaxHoldTime).
- [Console ObjectTemplate (detonation.flashbangAdditiveGlowMaxRampTime to engineName)](references/console-objecttemplate-part-04.md): `objectTemplate.*` properties: (detonation.flashbangAdditiveGlowMaxRampTime to engineName).
- [Console ObjectTemplate (engineType to healSpeed)](references/console-objecttemplate-part-05.md): `objectTemplate.*` properties: (engineType to healSpeed).
- [Console ObjectTemplate (healStorageSize to maxNrOfObjectSpawned)](references/console-objecttemplate-part-06.md): `objectTemplate.*` properties: (healStorageSize to maxNrOfObjectSpawned).
- [Console ObjectTemplate (maxResetSpeed to QualityLevel)](references/console-objecttemplate-part-07.md): `objectTemplate.*` properties: (maxResetSpeed to QualityLevel).
- [Console ObjectTemplate (radialDirection to setSkeletonCollisionBone)](references/console-objecttemplate-part-08.md): `objectTemplate.*` properties: (radialDirection to setSkeletonCollisionBone).
- [Console ObjectTemplate (setSoldierExitLocation to templateHasBeenUsed)](references/console-objecttemplate-part-09.md): `objectTemplate.*` properties: (setSoldierExitLocation to templateHasBeenUsed).
- [Console ObjectTemplate (textureName to weaponHud.deviationFactor)](references/console-objecttemplate-part-10.md): `objectTemplate.*` properties: (textureName to weaponHud.deviationFactor).
- [Console ObjectTemplate (weaponHud.disableOnSprint to zRotationSnap)](references/console-objecttemplate-part-11.md): `objectTemplate.*` properties: (weaponHud.disableOnSprint to zRotationSnap).
- [Console Other: Editor, Console, Demo, and Runtime Hosts](references/console-other-editor-and-runtime.md): BF2 editor, console, demo playback, filemanager, swiffhost, pythonhost, and portal commands.
- [Console Other: Server Commands (sv)](references/console-other-server-commands.md): `sv.*` server configuration and administration console commands.
- [Console Settings: Controls, Video, General, and Manager](references/console-settings-controls-video-general.md): Console commands for control maps, general/global settings, settings manager, and video settings.
- [Console Haptic Settings (Part 1: hapticSettings.addWeaponClassMap to hapticSettings.setPhysicsSEASmoothTimeZHigh)](references/console-settings-haptic-part-1.md): `hapticSettings.*` commands: (Part 1).
- [Console Haptic Settings (Part 2: hapticSettings.setPhysicsSEASmoothTimeZLow to hapticSettings.setTurnSensitivitySOLDIER)](references/console-settings-haptic-part-2.md): `hapticSettings.*` commands: (Part 2).
- [Console Vars.set (Vars.set to demo-fspeed)](references/console-vars-part-01.md): `Vars.set` engine variables: (Vars.set to demo-fspeed).
- [Console Vars.set (demo-slomo-cam to phy-fri-wheel2)](references/console-vars-part-02.md): `Vars.set` engine variables: (demo-slomo-cam to phy-fri-wheel2).
- [Console Vars.set (phy-gas to ragdoll_legForwardAngle)](references/console-vars-part-03.md): `Vars.set` engine variables: (phy-gas to ragdoll_legForwardAngle).
- [Console Vars.set (ragdoll_legForwardFactor to zipline-soldier-height)](references/console-vars-part-04.md): `Vars.set` engine variables: (ragdoll_legForwardFactor to zipline-soldier-height).

## Workflow & Domain Guides (`guides/`)

Supplementary domain, debugging, grammar, and token guides:

- `guides/grammar/` (`guides/grammar/file-roles-and-lifecycle.md`, `guides/grammar/syntax-and-scoping.md`, `guides/grammar/crd-and-template-context.md`)
- `guides/objects/` (`guides/objects/archives-overview.md`, `guides/objects/static-and-destructibles.md`, `guides/objects/terrain-and-level-scripts.md`, `guides/objects/vehicles.md`, `guides/objects/props-deployables-and-spawners.md`, `guides/objects/soldiers-and-kits.md`, `guides/objects/hud-menus-and-materials.md`)
- `guides/ai-and-coop/` (`guides/ai-and-coop/weapon-and-unit-ai.md`, `guides/ai-and-coop/strategic-ai-and-aidll.md`, `guides/ai-and-coop/coop-navmesh-and-vehicles.md`)
- `guides/debugging-and-auditing/` (`guides/debugging-and-auditing/pr-debugger-and-logs.md`, `guides/debugging-and-auditing/ctd-troubleshooting.md`, `guides/debugging-and-auditing/pre-commit-audit-checklist.md`)
- `guides/properties/` (`guides/properties/namespaces-internal-and-undocumented.md`, `guides/properties/tokens-objects-and-enums.md`, `guides/properties/tokens-ai-behaviors-and-types.md`)

## Core Workflows

### 1. Processing (Parsing and Tracing)

1. Start from the entry `.con` file and record every `GeometryTemplate.create`, `CollisionManager.createTemplate`, and `ObjectTemplate.create`.
2. Follow `include` (shared `v_*`/`c_*` scope, no args) and `run` (isolated scope, `v_arg1..N`) directives in execution order.
3. Track the active `ObjectTemplate` cursor across every `create`, `activeSafe`, `active`, and `addTemplate` call so each property is attributed to the right parent or child sub-template.
4. Consult `references/` and `guides/` for exact command namespaces, `CRD_*` distributions, and component types.

### 2. Editing (Safe, Targeted Modifications)

1. Preserve original casing, `rem` / `beginRem ... endRem` comments, and `rem ---BeginComp:<Comp> ---` / `rem ---EndComp ---` folding markers.
2. Verify `ObjectTemplate.activeSafe <Class> <Name>` precedes any property edits in `.tweak` files, especially before child sub-templates.
3. Keep multiplayer and co-op parity in sync: check `setNetworkableInfo`, `_bf2` one-man co-op vehicle variants, and linked `.ai` (`Weapons.ai` / `Objects.ai`) files.
4. Do not hand-edit `material/materialmanagerdefine.con` out of sync with PRMaterials.
5. Use `assets/` templates as structural baselines when creating new files.

### 3. Analyzing (Auditing and Optimization)

1. Check active template context on every `ObjectTemplate.*` block and verify all `addTemplate` targets exist.
2. Validate asset paths for meshes, `.collisionmesh`, `.ssc`/`.ogg` sounds, `.ske`/`.baf` animations, and HUD `.tga`/`.dds` icons.
3. Audit `GeometryTemplate` LOD/lightmap settings, `col3` presence for AI navmeshing, `NetworkableInfo` on synced parts, and dead or duplicate property lines.
4. Verify HUD `GuiIndex` links and absence of broken legacy BF1942 SAI conditionals in `.ai` files.

### 4. Debugging (CTDs and Runtime Failures)

1. Reproduce using the PR Debugger in windowed mode and inspect `mods/pr/logs/`, scanning earlier `Error`/`Assert` lines rather than only the final line.
2. Walk through `guides/debugging-and-auditing/ctd-troubleshooting.md` for context mismatches, `include` vs `run` scope bugs, `CRD_EXPONENTIAL` zero-mean traps, broken `_bf2` paths, lightmap/material errors, HUD `GuiIndex` mismatches, or missing `aiTemplate` links.

## Bundled Assets (`assets/`)

- `assets/static-destructible.con.txt`, `assets/static-destructible.tweak.txt` - Static building and destructible `Armor` templates.
- `assets/vehicle-pco.con.txt`, `assets/vehicle-pco.tweak.txt` - Vehicle `PlayerControlObject` templates.
- `assets/hud-and-material.con.txt` - `hudBuilder.*`, `Sound`, and `materialManager.*` templates.
- `assets/weapon-template.con.txt`, `assets/weapon-template.tweak.txt`, `assets/animationsystem1p.inc.txt`, `assets/weapon-and-vehicle.ai.txt` - Weapon, 1P animation, and AI templates.

## Bundled Scripts (`scripts/`)

All utilities follow PEP-8 (4-space indentation, descriptive variables, no code-golfing) and support `--help` and `--json` where applicable:

- `scripts/audit_scripts.py` - Pre-commit linter and static auditor for `.con`, `.tweak`, `.inc`, and `.ai` files.
- `scripts/trace_templates.py` - Traces `ObjectTemplate` hierarchy, components, and `include`/`run` execution chains.
- `scripts/convert_nondest.py` - Converts destroyable `.con`/`.tweak` objects into `_nondest` `SimpleObject` variants.
- `scripts/convert_coop_bf2.py` - Generates `_bf2` one-man co-op vehicle `.con`/`.tweak` variants.
- `scripts/scaffold_template.py` - Scaffolds new `.con`/`.tweak`/`.inc`/`.ai` files from `assets/`.
- `scripts/parse_pr_log.py` - Parses PR Debugger logs (`mods/pr/logs/`) and maps errors to CTD hints.
- `scripts/lookup_property.py` - Searches `references/` and `guides/properties/` for command signatures and notes.

## Gotchas

- `beginRem ... endRem` works in files loaded by the engine, not in the interactive console.
- `CRD_EXPONENTIAL/0/180/1` always returns `0` because `Number2` is ignored and `Number1` (mean) is `0`.
- `include` shares `v_*` variables and accepts no arguments; `run` isolates scope and passes `v_arg1..N`.
- Legacy BF1942 SAI conditionals (`AverageStrategicStrength`, `Security`, etc.) and `v_arg3 < 13` fail or return `0` in BF2 `AIDLL.dll`.
