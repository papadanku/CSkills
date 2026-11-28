# Console Graphics: Terrain, Heightmap, Overgrowth, and Undergrowth

## Terrain

### terrain

- `terrain.ambientColor <Vec3>`
    - Returns: `Vec3`
- `terrain.create <std::string>`
    - Returns: `void`
- `terrain.forceRenderStyle <int>`
    - Returns: `int`
- `terrain.GIColor <Vec3>`
    - Returns: `Vec3`
- `terrain.GIColorHigh <Vec3>`
    - Returns: `Vec3`
- `terrain.GIColorLow <Vec3>`
    - Returns: `Vec3`
- `terrain.init`
    - Returns: `void`
- `terrain.load <std::string>`
    - Returns: `void`
- `terrain.refreshTerrainSampling`
    - Returns: `void`
- `terrain.sunColor <Vec3>`
    - Returns: `Vec3`
- `terrain.terrainWaterColor <Vec3>`
    - Returns: `Vec3`
- `terrain.waterAlphaAdd <float>`
    - Returns: `float`
- `terrain.waterAlphaHeightMul <float>`
    - Returns: `float`
- `terrain.waterAnimSpeed <float>`
    - Returns: `float`
- `terrain.waterColor <Vec3>`
    - Returns: `Vec3`
- `terrain.waterNormalMap <std::string>`
    - Returns: `std::string`
- `terrain.waterQuality <int>`
    - Returns: `int`
- `terrain.waterReflectivity <float>`
    - Returns: `float`
- `terrain.waterScroll <Vec2>`
    - Returns: `Vec2`
- `terrain.waterSpecularColor <Vec4>`
    - Returns: `Vec4`
- `terrain.waterSpecularPower <float>`
    - Returns: `float`
- `terrain.waterSunIntensity <float>`
    - Returns: `float`
- `terrain.waterTransparency <float>`
    - Returns: `float`

### terrainCuller

- `terrainCuller.baseCellSize <int>`
    - Returns: `int`
- `terrainCuller.checkInside <bool>`
    - Returns: `bool`
- `terrainCuller.cullerType <int>`
    - Returns: `int`
- `terrainCuller.detailCullMaxLevel <int>`
    - Returns: `int`
- `terrainCuller.lod0SwitchStart <float>`
    - Returns: `float`
- `terrainCuller.lod0SwitchStop <float>`
    - Returns: `float`
- `terrainCuller.lod1SwitchStart <float>`
    - Returns: `float`
- `terrainCuller.lod1SwitchStop <float>`
    - Returns: `float`
- `terrainCuller.lod2Start <float>`
    - Returns: `float`
- `terrainCuller.lodSwitchDistance <int>`
    - Returns: `int`
- `terrainCuller.updateLodLevel <bool>`
    - Returns: `bool`
- `terrainCuller.useStitchedLods <bool>`
    - Returns: `bool`

## Heightmap

### heightmapcluster

- `heightmapcluster.addHeightmap <std::string int int>`
    - Returns: `void`
- `heightmapcluster.compileWaterMeshesIntoHeightmap`
    - Returns: `void`
- `heightmapcluster.create <std::string>`
    - Returns: `void`
- `heightmapcluster.importSurroundingRawHeightMap <std::string>`
    - Returns: `bool`
- `heightmapcluster.intersectCameraRay`
    - Returns: `void`
- `heightmapcluster.setClusterSize <int>`
    - Returns: `void`
- `heightmapcluster.setHeightmapSize <int>`
    - Returns: `void`
- `heightmapcluster.setSeaWaterLevel <float>`
    - Returns: `void`
- `heightmapcluster.smoothEdges <int float float>`
    - Returns: `void`
- `heightmapcluster.stitchEdges`
    - Returns: `void`

### heightmap

- `heightmap.loadHeightData <std::string>`
    - Returns: `void`
- `heightmap.loadMaterialData <std::string>`
    - Returns: `void`
- `heightmap.setBitResolution <int>`
    - Returns: `void`
- `heightmap.setMaterialScale <int>`
    - Returns: `void`
- `heightmap.setModified <bool>`
    - Returns: `void`
- `heightmap.setScale <Vec3>`
    - Returns: `void`
- `heightmap.setSize <int int>`
    - Returns: `void`

## Overgrowth

- `overgrowth.addMaterial <std::string uint>`
    - Returns: `bool`
- `overgrowth.addType <std::string>`
    - Returns: `bool`
- `overgrowth.closeDistFade <float>`
    - Returns: `float`
- `overgrowth.closeDistPercentage <float>`
    - Returns: `float`
- `overgrowth.editorEnable <float>`
    - Returns: `float`
- `overgrowth.exportToTerrainTexture`
    - Returns: `void`
- `overgrowth.generateAll`
    - Returns: `void`
- `overgrowth.generateAtlas`
    - Returns: `void`
- `overgrowth.getActiveMaterialName`
    - Returns: `std::string`
- `overgrowth.getGeometryList`
    - Returns: `std::string`
- `overgrowth.getLodDistance`
    - Returns: `float`
- `overgrowth.getMaterialList`
    - Returns: `std::string`
- `overgrowth.getTypeList`
    - Returns: `std::string`
- `overgrowth.lodTimer <float>`
    - Returns: `float`
- `overgrowth.paintMaterial <float float float>`
    - Returns: `void`
- `overgrowth.paintShadowmap <float float float>`
    - Returns: `void`
- `overgrowth.path <std::string>`
    - Returns: `std::string`
- `overgrowth.postLoad`
    - Returns: `void`
- `overgrowth.preLoad`
    - Returns: `void`
- `overgrowth.removeActiveMaterial`
    - Returns: `bool`
- `overgrowth.removeActiveType`
    - Returns: `bool`
- `overgrowth.save`
    - Returns: `void`
- `overgrowth.setActiveMaterial <std::string>`
    - Returns: `void`
- `overgrowth.setActiveType <std::string>`
    - Returns: `void`
- `overgrowthType.density <float>`
    - Returns: `float`
- `overgrowthType.geometry <std::string>`
    - Returns: `std::string`
- `overgrowthType.minRadiusToOthers <float>`
    - Returns: `float`
- `overgrowthType.minRadiusToSame <float>`
    - Returns: `float`
- `overgrowthType.normalScale <float>`
    - Returns: `float`
- `overgrowthType.randomScale <Vec2>`
    - Returns: `Vec2`
- `overgrowthType.rotationScale <float>`
    - Returns: `float`
- `overgrowth.viewDistance <float>`
    - Returns: `float`
- `overgrowth.viewDistanceScale <float>`
    - Returns: `float`

## Undergrowth

- `undergrowth.dynamicShadowsEnable <bool>`
    - Returns: `bool`
- `undergrowth.enabled <bool>`
    - Returns: `bool`
- `undergrowth.load <std::string>`
    - Returns: `void`
- `undergrowth.reload`
    - Returns: `void`
- `undergrowth.simpleShaderEnable <bool>`
    - Returns: `bool`
- `undergrowth.test <uint>`
    - Returns: `uint`
- `undergrowth.test2 <float>`
    - Returns: `float`
- `undergrowth.viewDistanceFade <float>`
    - Returns: `float`
- `undergrowth.viewDistanceScale <float>`
    - Returns: `float`
- `undergrowth.zPassPatchCount <uint>`
    - Returns: `uint`
