
# PR:BF2 Map, Terrain, Overgrowth & Water Scripts (`server.zip`)

- **`init.con`**: Entry point for a level. Uses `if v_arg1 == BF2Editor` to branch between editor mode (`run Terrain.con BF2Editor`, `run StaticObjects.con BF2Editor`, `UndergrowthEditable.create`, `Overgrowth.editorEnable 1`) and runtime mode (`run Terrain.con v_arg2`, `run CompiledRoads.con`, `run tmp.con v_arg1`, `run Overgrowth/OvergrowthCollision.con`).
- **`heightdata.con`**: Configures `heightmapcluster.create HeighmapCluster`, `setClusterSize`, `setHeightmapSize`, primary 16-bit and secondary 8-bit `heightmap.loadHeightData` / `loadMaterialData`.
- **`terrain.con`**: Branches on `if v_arg1 == BF2Editor` (`TerrainEditable`, `patchSize`, `detailmapBaseName`, `colormapBaseName`, `lightmapBaseName`) vs runtime (`terrain.create Terrain`, `terrain.load .../terraindata.raw`).
- **`water.con`**: Sets `renderer.waterScroll`, `waterAnimSpeed`, `waterColor`, `waterSpecularColor`, `waterSpecularPower`, `waterFogColor`, `waterFogStartEndAndBase`, `terrain.waterSunIntensity`.
- **`overgrowth/overgrowth.con` & `overgrowthcollision.con`**: Sets `Overgrowth.viewDistance`, `viewDistanceScale`, `closeDistPercentage`, `Overgrowth.path`, `Overgrowth.preLoad`, and per-patch overgrowth collision placements.
- **`ambientobjects.con`**: Defines ambient `Trigger` templates (`ObjectTemplate.triggerId`, `radius`, `events`, `chance`, `minimumTimeBetweenTriggering`).
