
# PR:BF2 Pre-Commit Script Audit Checklist

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
