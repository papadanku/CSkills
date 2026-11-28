
# PR:BF2 Weapon & Unit AI (`Weapons.ai` & `Objects.ai`)

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

- **`weaponTemplate.setStrength <CST> <float>`**: Strength against `Infantry` (also `Infantery` in legacy files), `LightArmour`, `HeavyArmour`, `NavalArmour`, `Helicopter`, `AirPlane`.
- **`weaponTemplate.indirect <0|1>`**: Set `1` for mortars/artillery/indirect fire.
- **`weaponTemplate.isAntiAirWeapon <0|1>`**: Marks weapon for anti-air targeting.
- **`weaponTemplate.weaponActivate <PI*>`**: Input that activates/selects the weapon (`PINone`, `PIFire`, `PIAltFire`).
- **`weaponTemplate.weaponFire <PI*>`**: Input that fires the weapon.

## 2. Vehicle & Unit AI (`Objects.ai`)

Defines how bots perceive, drive, aim, and evaluate a vehicle or soldier (`aiTemplate.*` + `aiTemplatePlugIn.*`):

- `aiTemplate.create <Name>` / `aiTemplate.active <Name>`
- **`aiTemplate.addType <IT*>`**: e.g., `ITUnit`, `ITGround`, `ITMobile`, `ITAir`, `ITHelicopter`, `ITNaval`, `ITHasWreck`, `ITStructure`, `ITSoldier`, `ITCover`, `ITHasCarHorn`, `ITObstructedView`, `ITNoTemperature`
- `aiTemplate.degeneration <float>`, `aiTemplate.allowedTimeDiff <float>`, `aiTemplate.basicTemp <float>`, `aiTemplate.commonKnowledge <0|1>`
- `aiTemplate.addPlugIn <PlugInName>`
- **`aiTemplatePlugIn.create <Type> <PlugInName>`**: Types include `Unit`, `Physical`, `ControlInfo`, `Armament`, `Mobile`, `Cover`.
- `aiTemplatePlugIn.vehicleNumber <int>`, `setBattleStrength <CST> <float>`, `setStrategicStrength <CST> <float>`, `setStrType <VT*>`, `setPathfindingMap <Infantry|Vehicle|Air>`, `maxSpeed`, `driveThrottleControl`, `driveTurnControl`, `aimVerticalControl`, `aimHorizontalControl`.
