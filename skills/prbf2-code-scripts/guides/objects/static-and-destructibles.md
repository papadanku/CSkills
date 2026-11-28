
# PR:BF2 Static Buildings, Props & Destructibles (`objects_server.zip`)

## Static Buildings & Props (`staticobjects/...`)

- **Geometry**: `GeometryTemplate.create StaticMesh <name>` + `CollisionManager.createTemplate <name>`.
- **Object Class**: Usually `ObjectTemplate.create SimpleObject <name>` with `ObjectTemplate.physicsType Mesh` (or `3` in `.con` before `.tweak` override) and `ObjectTemplate.hasMobilePhysics 0`.
- **Lightmaps & LODs** (in `.tweak`):
    - `GeometryTemplate.doNotGenerateLightmaps <0|1>`, `GeometryTemplate.lightmapOverride <0|1>`, `GeometryTemplate.compressVertexData 1`, `GeometryTemplate.maxTextureRepeat <int>`
    - `GeometryTemplate.setSubGeometryLodDistance <subGeom> <lod> <dist>`

## Destructible / Wreck / Construction Variants

Variants include `*_wreck_*`, `*_block`, `hq_wall_*`, `framework_construction*`:

- Use `PlayerControlObject` or `DestroyableObject` with `ObjectTemplate.isDestructable 1`, `ObjectTemplate.setNetworkableInfo BasicInfo`, and `rem ---BeginComp:Armor ---`:
    - `ObjectTemplate.armor.maxHitPoints`, `hitPoints`, `wreckHitPoints`, `timeToStayAsWreck`, `timeToStayAfterDestroyed`, `hideChildrenOnSpectacularDeath 1`
    - Damage & explosion effects: `ObjectTemplate.armor.addArmorEffect <hpThreshold> <effectTemplate> <pos> <rot>` (e.g., `e_dstate_land_mediumsmoke`, `e_vexp_*`, `e_mexp_*`, `e_sAmb_wreckfire`).
