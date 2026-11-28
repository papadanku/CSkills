# Assets: Polycounts, LOD Guidelines, and Destroyables

## Polycounts and LOD Guidelines

This document outlines polycount and Level of Detail (LOD) guidelines based on established standards for Battlefield 2 modding.

Adherence to polycount guidelines is important, but correctly implemented LOD meshes are more critical for game performance. Exceeding polycount limits by 15% has less impact on performance than missing appropriate LODs.

### Weapon Models

#### Requirements

Beyond the first-person view (1pv) model, the following meshes are required:

- Third-person view (3pv) mesh.
- Ironsight mesh.
- LOD1 mesh (displayed at 50-100 meters).

#### Polycount Guidelines

- **Ironsight Mesh**: 1000-1100 polygons.
- **1pv Mesh (LOD0)**:
    - Assault/MG: 3000-3500 polygons.
    - Pistols: 1500-2000 polygons.
- **3pv Mesh (LOD0)**:
    - Assault/MG: 1000-1300 polygons.
    - Pistols: 700-900 polygons.
- **3pv Mesh (LOD1)**:
    - Assault/MG: 200-300 polygons.
    - Pistols: 150-200 polygons.

### Vehicle Models

#### Requirements

Vehicle models require a comprehensive set of meshes to ensure performance and collision accuracy:

- 1st-person mesh (for all vehicle types).
- LOD meshes (LOD0, LOD1, LOD2).
- Wreck meshes (LOD0, LOD1, LOD2).
- Collision meshes (decal, physics, and soldier collision).

## Convert Destroyable Object to Non-Destroyable

To convert a destroyable object to a non-destroyable object, follow these steps to create a modified version of the object's configuration files.

1. **Duplicate Files**: Create a copy of the original `.con` and `.tweak` files in the same directory. Append a `_nondest` suffix to the names of the new files (e.g., `stonebridge_nondest.con` and `stonebridge_nondest.tweak`).
2. **Configure the .con file**: Open the new `_nondest.con` file.

    Modify the object template name in each line, except for the lines specifying the collision mesh and geometry, which must continue to reference the original destroyable static mesh.

    Change `ObjectTemplate.create DestroyableObject` to `ObjectTemplate.create SimpleObject`.

3. **Configure the .tweak file**: Open the new `_nondest.tweak` file.

    - Remove all components and settings related to the destruction of the object (e.g., the `Armor` and `StrategicObject` components).
    - Delete the lines `ObjectTemplate.isDestructable 1` and `ObjectTemplate.setNetworkableInfo BasicInfo`.
    - Update the template name to reference the non-destroyable object, while ensuring the geometry and collision mesh lines continue to reference the original destroyable static object.
    - Change `ObjectTemplate.activeSafe DestroyableObject` to `ObjectTemplate.activeSafe SimpleObject`.

4. **Finalize**: Save all changes and close the files.
