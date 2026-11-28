
# PR:BF2 Co-Op Navmesh & One-Man `_bf2` Vehicles

## Navmesh & Map `AI/AI.ai`

Three navmesh types in `AIPathFinding/`: `Infantry`, `Vehicle`, `AerialHeightMap`.

In `AI/AI.ai`:

```text
ai.init 2
aiPathfinding.setActiveMap Vehicle
aiPathfinding.map.maxSlope 35
aiPathfinding.map.addVehicleForClusterCost Tank
aiPathfinding.map.addVehicleForClusterCost ArmedCar
aiPathfinding.setActiveMap Infantry
aiPathfinding.map.maxSlope 45
aiPathfinding.map.addVehicleForClusterCost Infantery
```

## One-Man Co-Op Vehicles (`_bf2` suffix)

PR multi-crew vehicles cannot be operated by a single bot. Standard PR co-op pattern:

1. Duplicate vehicle folder with `_bf2` suffix (e.g., `mec_aav_gopher_bf2`), rename `.con`/`.tweak`.
2. Delete `animations/`, `meshes/`, `sounds/`, `textures/`, and `.inc` files in the `_bf2` copy.
3. In `_bf2.con`: remove `GeometryTemplate.*` and `CollisionManager.*`; point `ObjectTemplate.geometry`, `collisionMesh`, `setCollisionMesh`, sound filenames, and `run ../<orig>/animationSystem.inc` back to the original vehicle.
4. In `_bf2.tweak`: combine gunner turret into the main driver PCO (`ObjectTemplate.addTemplate <orig>_Turret`) and adjust `setPosition` if needed.
