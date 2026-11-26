
# PR:BF2 `.ai` & Co-Op Scripting Reference

Reference for `.ai` templates, Strategic AI (`AIDLL.dll`) caveats, and PR:BF2 Co-Op patterns.

## 1. Weapon AI (`Weapons.ai` / `*_weapons.ai`)

Links a `GenericFireArm` (via `ObjectTemplate.aiTemplate <aiName>` in `.tweak`) to bot targeting and fire logic:

```text
rem *** coaxial Machine Gun ***
weaponTemplate.create Coaxial_mg_ai
weaponTemplate.indirect 0
weaponTemplate.minRange 0.0
weaponTemplate.maxRange 60.0
weaponTemplate.weaponActivate PINone
weaponTemplate.setStrength Infantry     100.0
weaponTemplate.setStrength LightArmour  0.0
weaponTemplate.setStrength HeavyArmour  0.0
weaponTemplate.setStrength NavalArmour  0.0
weaponTemplate.setStrength Helicopter   0.0
weaponTemplate.setStrength AirPlane     0.0
weaponTemplate.allowedDeviation 1.0
weaponTemplate.setSoundSphereRadius   200.0
weaponTemplate.setFiresThroughTransparent 1
```

Key properties:

- `weaponTemplate.setStrength <CST> <float>`: Strength against `Infantry` (also `Infantery` in legacy files), `LightArmour`, `HeavyArmour`, `NavalArmour`, `Helicopter`, `AirPlane`.
- `weaponTemplate.indirect <0|1>`: Set `1` for mortars/artillery/indirect fire.
- `weaponTemplate.isAntiAirWeapon <0|1>`: Marks weapon for anti-air targeting.
- `weaponTemplate.weaponActivate <PI*>`: Input that activates/selects the weapon (`PINone`, `PIFire`, `PIAltFire`).
- `weaponTemplate.weaponFire <PI*>`: Input that fires the weapon.

## 2. Vehicle & Unit AI (`Objects.ai`)

Defines how bots perceive, drive, aim, and evaluate a vehicle or soldier (`aiTemplate.*` + `aiTemplatePlugIn.*`):

- `aiTemplate.create <Name>` / `aiTemplate.active <Name>`
- `aiTemplate.addType <IT*>` (e.g., `ITUnit`, `ITGround`, `ITMobile`, `ITAir`, `ITHelicopter`, `ITNaval`, `ITHasWreck`, `ITStructure`, `ITSoldier`, `ITCover`, `ITHasCarHorn`, `ITObstructedView`, `ITNoTemperature`)
- `aiTemplate.degeneration <float>`, `aiTemplate.allowedTimeDiff <float>`, `aiTemplate.basicTemp <float>`, `aiTemplate.commonKnowledge <0|1>`
- `aiTemplate.addPlugIn <PlugInName>`
- `aiTemplatePlugIn.create <Type> <PlugInName>`: Types include `Unit`, `Physical`, `ControlInfo`, `Armament`, `Mobile`, `Cover`.
- `aiTemplatePlugIn.vehicleNumber <int>`, `setBattleStrength <CST> <float>`, `setStrategicStrength <CST> <float>`, `setStrType <VT*>`, `setPathfindingMap <Infantry|Vehicle|Air>`, `maxSpeed`, `driveThrottleControl`, `driveTurnControl`, `aimVerticalControl`, `aimHorizontalControl`.

## 3. Strategic AI & `AIDLL.dll` Caveats

### Non-Working Conditionals in BF2/PR:BF2

Legacy BF1942 SAI conditionals that **do not work** in BF2 `AIDLL.dll`:

- **Debugger error (missing from `AIDLL.dll`)**: `AverageStrategicStrength`, `AttackStrategicStrength`, `DefenceStrategicStrength`, `Security`.
- **Always evaluate to `0`**: `Air`, `Bomber`, `Fighter`, `Naval`, `HeavyNaval`, `LCVP`, `AntiAir`, `Infantry`/`Infantery`, `AntiTank`, `HeavyAttack`, `Carrier`, `FastAttack`, `Artillery`.
- **Important**: `v_arg3 < 13` is invalid in SAI condition indices (`0..12` map to `Carrier`..`FastAttack`).

### Strategy Tree Modifiers (`aiStrategy.*`)

- `aiStrategy.setTreeModifier <TTNFlag> <Weight>`
- `aiStrategy.setTreeModifierCombatStrength <TTNFlag> <All | CSTFlag> <Weight>`
- Valid `TTN*` flags include `TTNSuppliesAmmunition`, `TTNSuppliesRepair`, `TTNControlPoint`, `TTNTransportation`, `TTNRadar`, `TTNAirfield`, `TTNFixedWeapons`, `TTNHostileAirMobile`, `TTNHostileGroundMobile`, `TTNFriendGround`, `TTNStrategic`, `TTNTactical`, etc.

## 4. PR:BF2 Co-Op Patterns

### Navmesh & Map `AI/AI.ai`

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

### One-Man Co-Op Vehicles (`_bf2` suffix)

PR multi-crew vehicles cannot be operated by a single bot. Standard PR co-op pattern:

1. Duplicate vehicle folder with `_bf2` suffix (e.g., `mec_aav_gopher_bf2`), rename `.con`/`.tweak`.
2. Delete `animations/`, `meshes/`, `sounds/`, `textures/`, and `.inc` files in the `_bf2` copy.
3. In `_bf2.con`: remove `GeometryTemplate.*` and `CollisionManager.*`; point `ObjectTemplate.geometry`, `collisionMesh`, `setCollisionMesh`, sound filenames, and `run ../<orig>/animationSystem.inc` back to the original vehicle.
4. In `_bf2.tweak`: combine gunner turret into the main driver PCO (`ObjectTemplate.addTemplate <orig>_Turret`) and adjust `setPosition` if needed.
