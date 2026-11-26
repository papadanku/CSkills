
# PR:BF2 Virtual Archive Layout

In PR:BF2, modding scripts live inside virtual game/mod archives (`objects_server.zip`, `objects_common_server.zip`, `objects_vehicles_server.zip`, `objects_weapons_server.zip`, `menu_server.zip`, `common_server.zip`, and map-level `server.zip` under `mods/pr/...`). These are **game/mod archive paths**, not files bundled in this skill.

## Archive-to-Domain Mapping

- **`objects_server.zip`**: Static buildings, props, and destructibles (`staticobjects/...`).
- **`objects_vehicles_server.zip`**: Vehicles (`PlayerControlObject`, `BundledMesh`, `_bf2` co-op variants).
- **`objects_weapons_server.zip`**: Handheld weapons (`GenericFireArm`, `BundledMesh`, `animationsystem*.inc`).
- **`objects_common_server.zip`**: Command posts / ACVs (`common/command_post/...`), deployables & ammo caches (`common/deployables/...`, `common/ammocache/...`), spawners & props (`spawners/...`, `common/command_post/props/...`), soldiers & ragdolls, and kits & spawnkits (`*_init.tweak`, `*_sp_init.tweak`, `*_ziptie_init.tweak`).
- **`menu_server.zip`**: HUD scripts (`hud/hudsetup/...`), Flash menus (`External/flashmenu/...`), and texture atlases (`atlas/...`).
- **`common_server.zip`**: Materials (`material/materialmanagerdefine.con`, `materialmanagersettings.con`, `impactsounds.con`).
- **`server.zip`** (map-level): Map and terrain scripts (`init.con`, `heightdata.con`, `terrain.con`, `water.con`, `overgrowth/overgrowth.con`, `overgrowthcollision.con`, `ambientobjects.con`, `GamePlayObjects.con`, `AI/AI.ai`).
