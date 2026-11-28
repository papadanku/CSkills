# Console Graphics: Collision, Mesh Renderer, Decals, and Textures

## Collision

- `CollisionCheck.checkStaticCollisionMeshes <int>`
    - Returns: `void`
- `collisionManager.buildDebugCollisionMeshes`
    - Returns: `void`
- `collisionManager.create <std::string>`
    - Returns: `void`
- `collisionManager.createTemplate <std::string>`
    - Returns: `void`
    - Description: Creates a Collision Mesh template from the collision mesh name so it can be used in other files without creating a duplicate mesh
    - Used in: `.con` files for collision meshes
- `collisionManager.drawBoundingBoxes <bool>`
    - Returns: `void`
- `collisionManager.drawForces <bool>`
    - Returns: `void`
- `collisionManager.drawIntersectFaces <bool>`
    - Returns: `void`
- `collisionManager.drawMeshes <bool>`
    - Returns: `void`
- `collisionManager.drawNormals <bool>`
    - Returns: `void`
- `collisionManager.drawOnlyRoot <float>`
    - Returns: `void`
- `collisionManager.drawPivots <bool>`
    - Returns: `void`
- `collisionManager.drawPrimitives <bool>`
    - Returns: `void`
- `collisionManager.drawSoldierMesh <bool>`
    - Returns: `void`
- `collisionManager.drawTestedFaces <bool>`
    - Returns: `void`
- `collisionManager.getNameOfObjectInFocus`
    - Returns: `void`
- `collisionManager.identityRotateObjectInFocus`
    - Returns: `void`
- `collisionManager.rotateObjectInFocusAroundAxis <uint float>`
    - Returns: `void`
- `collisionManager.rotateObjectInFocusAroundVector <Vec3 float>`
    - Returns: `void`
- `collisionManager.setActiveLod <int>`
    - Returns: `void`
- `collisionManager.setDrawDistance <float>`
    - Returns: `void`
- `collisionManager.setGeometry <bool>`
    - Returns: `void`
- `collisionManager.setSleepinessOfObjectInFocus <int>`
    - Returns: `void`
    - `.con` presumably
    - Effect Unknown. Causes a game crash during loading when using `collisionManager.setSleepinessOfObjectInFocus 0` in a `.con` of a `GenericFirearm`
- `collisionManager.updateFlagsOfObjectInFocus <U32 U32>`
    - Returns: `void`
- `collisionManager.useDeferredLoading <bool>`
    - Returns: `bool`

## Mesh Renderer

### skinnedMeshRenderer

- `skinnedMeshRenderer.shaderQuality <ShaderQuality>`
    - Returns: `ShaderQuality`

### staticMeshRenderer

- `staticMeshRenderer.allowAnisoFiltering <bool>`
    - Returns: `bool`
- `staticMeshRenderer.convertLightmapName <std::string>`
    - Returns: `std::string`
- `staticMeshRenderer.enableLightIndexes <bool>`
    - Returns: `bool`
- `staticMeshRenderer.enableLightMapAtlas <bool>`
    - Returns: `bool`
- `staticMeshRenderer.enableNewLightmapNames <bool>`
    - Returns: `bool`
- `staticMeshRenderer.enableRendering <bool>`
    - Returns: `bool`
- `staticMeshRenderer.enableUnifiedIndexlist <bool>`
    - Returns: `bool`
- `staticMeshRenderer.loadAllLightMapFiles <std::string std::string>`
    - Returns: `bool`
- `staticMeshRenderer.loadAllLightMapFilesDLL <std::string std::string>`
    - Returns: `bool`
- `staticMeshRenderer.materialCullingEnabled <bool>`
    - Returns: `bool`
- `staticMeshRenderer.maxLightMappedLod <int>`
    - Returns: `int`
- `staticMeshRenderer.noLods <bool>`
    - Returns: `bool`

## Decal

- `decalManager.decalGeomClipAngle <float>`
    - Returns: `float`
- `decalManager.decalNormalOffset <float>`
    - Returns: `float`
- `decalManager.drawStats <bool>`
    - Returns: `bool`
- `decalManager.fadeDistance <float>`
    - Returns: `float`

    Set the View Distance of the Decals to start to fade. Works in level .con files

- `decalManager.fadeOutAtPercentageOfTimeToLive <float>`
    - Returns: `float`
- `decalManager.generateTexture`
    - Returns: `bool`
- `decalManager.startFadePercentageOfFadeDistancel <float>`
    - Returns: `float`
- `decalManager.timeToLive <float>`
    - Returns: `float`

    Time in seconds of how long will a vehicle, effect or projectile will last. For vehicles, if it has been exited for a time, it will blow up. Uses CRD Arguments.

    http://bfmods.com/mdt/scripting/ObjectTemplate/Properties/TimeToLive.html

## Texture Manager

- `texturemanager.customTextureSuffix <std::string>`
    - Returns: `std::string`
