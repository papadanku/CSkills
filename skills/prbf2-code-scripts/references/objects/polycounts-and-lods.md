
# PR:BF2 Polycount & LOD Guidelines

**Important**: Correctly implemented LOD meshes are more critical for game performance than strict polycount limits; exceeding polycount limits by 15% has less impact than missing appropriate LODs.

## Weapon Models

- **Required Meshes**: 1st-person (`1pv`), 3rd-person (`3pv`), ironsight mesh, and `LOD1` mesh (displayed at 50-100m).
- **Ironsight Mesh**: 1000-1100 polygons.
- **1pv Mesh (LOD0)**: Assault/MG 3000-3500 polygons; Pistols 1500-2000 polygons.
- **3pv Mesh (LOD0)**: Assault/MG 1000-1300 polygons; Pistols 700-900 polygons.
- **3pv Mesh (LOD1)**: Assault/MG 200-300 polygons; Pistols 150-200 polygons.

## Vehicle Models

- **Required Meshes**: 1st-person mesh (all vehicle types), `LOD0`/`LOD1`/`LOD2`, wreck `LOD0`/`LOD1`/`LOD2`, and collision meshes (decal, physics, soldier collision).

## Converting Destroyable Objects to Non-Destroyable (`_nondest`)

1. Duplicate `.con` and `.tweak` in the same directory with `_nondest` suffix (e.g., `stonebridge_nondest.con`).
2. In `_nondest.con`: update template name on all lines except `collisionMesh` and `geometry` (keep pointing to original static mesh); change `ObjectTemplate.create DestroyableObject` to `ObjectTemplate.create SimpleObject`.
3. In `_nondest.tweak`: remove `Armor` and `StrategicObject` components, delete `ObjectTemplate.isDestructable 1` and `ObjectTemplate.setNetworkableInfo BasicInfo`, update template name (keeping geometry/collisionMesh pointing to original), and change `ObjectTemplate.activeSafe DestroyableObject` to `ObjectTemplate.activeSafe SimpleObject`.
