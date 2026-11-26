
# PR:BF2 Props, Command Posts, Deployables & Spawners (`objects_common_server.zip`)

- **Command Posts / ACVs** (`common/command_post/...`): `PlayerControlObject`s combining vehicle mobility (`Steeringwheel`, `Drivetrain_*`, `Engine`) with command/supply abilities (`Ability`, `StrategicObject`).
- **Deployables & Ammo Caches** (`common/deployables/...`, `common/ammocache/...`): `PlayerControlObject`s with `isDestructable 1`, `setNetworkableInfo BasicInfo`, `Armor` component, and `SupplyObject` / `Ability` radius settings.
- **Spawners & Props** (`spawners/...`, `common/command_post/props/...`): `ObjectSpawner` / `SimpleObject` / `SupplyObject` templates placed in `GamePlayObjects.con` or attached via `addTemplate`.
