
# PR:BF2 Object Types & Virtual Archive Reference

In PR:BF2, modding scripts live inside virtual game/mod archives (`objects_server.zip`, `objects_common_server.zip`, `objects_vehicles_server.zip`, `objects_weapons_server.zip`, `menu_server.zip`, `common_server.zip`, and map-level `server.zip` under `mods/pr/...`). These are **game/mod archive paths**, not files bundled in this skill.

## 1. Static Objects & Map/Terrain (`objects_server.zip`, `server.zip`)

### Static Buildings, Props & Destructibles (`staticobjects/...`)

- **Geometry**: `GeometryTemplate.create StaticMesh <name>` + `CollisionManager.createTemplate <name>`.
- **Object Class**: Usually `ObjectTemplate.create SimpleObject <name>` with `ObjectTemplate.physicsType Mesh` (or `3` in `.con` before `.tweak` override) and `ObjectTemplate.hasMobilePhysics 0`.
- **Lightmaps & LODs** (in `.tweak`):
    - `GeometryTemplate.doNotGenerateLightmaps <0|1>`, `GeometryTemplate.lightmapOverride <0|1>`, `GeometryTemplate.compressVertexData 1`, `GeometryTemplate.maxTextureRepeat <int>`
    - `GeometryTemplate.setSubGeometryLodDistance <subGeom> <lod> <dist>`
- **Destructible / Wreck / Construction Variants** (`*_wreck_*`, `*_block`, `hq_wall_*`, `framework_construction*`):
    - Use `PlayerControlObject` or `DestroyableObject` with `ObjectTemplate.isDestructable 1`, `ObjectTemplate.setNetworkableInfo BasicInfo`, and `rem ---BeginComp:Armor ---`:
        - `ObjectTemplate.armor.maxHitPoints`, `hitPoints`, `wreckHitPoints`, `timeToStayAsWreck`, `timeToStayAfterDestroyed`, `hideChildrenOnSpectacularDeath 1`
        - Damage & explosion effects: `ObjectTemplate.armor.addArmorEffect <hpThreshold> <effectTemplate> <pos> <rot>` (e.g., `e_dstate_land_mediumsmoke`, `e_vexp_*`, `e_mexp_*`, `e_sAmb_wreckfire`).

### Map & Terrain Scripts (`server.zip`)

- **`init.con`**: Entry point for a level. Uses `if v_arg1 == BF2Editor` to branch between editor mode (`run Terrain.con BF2Editor`, `run StaticObjects.con BF2Editor`, `UndergrowthEditable.create`, `Overgrowth.editorEnable 1`) and runtime mode (`run Terrain.con v_arg2`, `run CompiledRoads.con`, `run tmp.con v_arg1`, `run Overgrowth/OvergrowthCollision.con`).
- **`heightdata.con`**: Configures `heightmapcluster.create HeighmapCluster`, `setClusterSize`, `setHeightmapSize`, primary 16-bit and secondary 8-bit `heightmap.loadHeightData` / `loadMaterialData`.
- **`terrain.con`**: Branches on `if v_arg1 == BF2Editor` (`TerrainEditable`, `patchSize`, `detailmapBaseName`, `colormapBaseName`, `lightmapBaseName`) vs runtime (`terrain.create Terrain`, `terrain.load .../terraindata.raw`).
- **`water.con`**: Sets `renderer.waterScroll`, `waterAnimSpeed`, `waterColor`, `waterSpecularColor`, `waterSpecularPower`, `waterFogColor`, `waterFogStartEndAndBase`, `terrain.waterSunIntensity`.
- **`overgrowth/overgrowth.con` & `overgrowthcollision.con`**: Sets `Overgrowth.viewDistance`, `viewDistanceScale`, `closeDistPercentage`, `Overgrowth.path`, `Overgrowth.preLoad`, and per-patch overgrowth collision placements.
- **`ambientobjects.con`**: Defines ambient `Trigger` templates (`ObjectTemplate.triggerId`, `radius`, `events`, `chance`, `minimumTimeBetweenTriggering`).

## 2. Vehicles (`objects_vehicles_server.zip`)

- **Root Template**: `ObjectTemplate.create PlayerControlObject <vehName>` with `GeometryTemplate.create BundledMesh <vehName>`, `CollisionManager.createTemplate <vehName>`, `ObjectTemplate.hasMobilePhysics 1`, and `ObjectTemplate.setNetworkableInfo BasicInfo`.
- **Hierarchy & Sub-Templates**:
    - `RotationalBundle`: Wheels/drivetrains, steering, turrets, control surfaces (ailerons, elevators, rudders), rotors, landing gear.
    - `Bundle` / `Engine` / `Spring` / `Rotor` / `Wing`: Propulsion, suspension, and aerodynamics.
    - `EntryPoint`: Crew/passenger entry positions (`ObjectTemplate.setEntryRadius`, `setPosition`).
    - `Camera`: Pilot, driver, gunner, and commander cameras (`ObjectTemplate.worldFOV`, `insideFOV`, `CVMChase`, `CVMInside`).
    - `GenericFireArm`: Coaxial/turret/pylon weapons (`ObjectTemplate.addTemplate <weaponName>`).
- **Components**: `Armor`, `VehicleHud` (`guiIndex` linking to `hud/hudsetup/vehicles/...`), `AbilityHud`, `WarningHud`.
- **Co-Op Variants**: `_bf2` one-man variants reuse parent meshes/sounds/animations via relative paths and merge gunner turrets into the driver PCO.

## 3. Props, Command Posts & Deployables (`objects_common_server.zip`)

- **Command Posts / ACVs** (`common/command_post/...`): `PlayerControlObject`s combining vehicle mobility (`Steeringwheel`, `Drivetrain_*`, `Engine`) with command/supply abilities (`Ability`, `StrategicObject`).
- **Deployables & Ammo Caches** (`common/deployables/...`, `common/ammocache/...`): `PlayerControlObject`s with `isDestructable 1`, `setNetworkableInfo BasicInfo`, `Armor` component, and `SupplyObject` / `Ability` radius settings.
- **Spawners & Props** (`spawners/...`, `common/command_post/props/...`): `ObjectSpawner` / `SimpleObject` / `SupplyObject` templates placed in `GamePlayObjects.con` or attached via `addTemplate`.

## 4. Soldiers & Kits (`objects_common_server.zip`)

- **Soldiers & Ragdolls**: `Soldier` templates, skeleton/ragdoll setup (`ragDoll.skeleton`, `ragDoll.addParticle <boneIndex> <mass>`), and `animationsystem*.inc` fragments referencing `.ske` and `.baf` files.
- **Kits & Spawnkits**: `Kit` templates and kit initialization tweaks (`*_init.tweak`, `*_sp_init.tweak`, `*_ziptie_init.tweak`) binding weapons, equipment, and `KitInfo` networkables.

## 5. HUD, Menus & Materials (`menu_server.zip`, `common_server.zip`)

- **HUD Scripts** (`hud/hudsetup/...`): `.con` and `.tweak` files using `hudBuilder.createSplitNode`, `createTransformNode`, `createPictureNode`, `createCompassNode`, `setNodeLogicShowVariable` (`EQUAL GuiIndex <id>` / `OR GuiIndex <id>`), and `setNodeColor`.
- **Flash Menus & Atlases** (`External/flashmenu/...`, `atlas/...`): `swiffHost.*` (`addAward`, `addGameMode`, `addRank`) and `atlaslist.con` (`hudManager.addTextureAtlas "*.tai"`).
- **Materials** (`material/...`):
    - `materialmanagerdefine.con`: Generated by **PRMaterials** (do not hand-edit without regenerating; defines `Material.active`, `name`, `type`, `friction`, `elasticity`, `resistance`, `damageLoss`, `hasWaterPhysics`).
    - `materialmanagersettings.con` & `impactsounds.con`: Material interaction cells (`materialManager.createCell`, `damageMod`, `setEffectTemplate`, `setSoundTemplate`) and `ObjectTemplate.create Sound` templates.
