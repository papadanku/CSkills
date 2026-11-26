
# PR:BF2 Strategic AI (`aiStrategy.*`) & `AIDLL.dll` Caveats

## Non-Working Conditionals in BF2/PR:BF2

Legacy BF1942 SAI conditionals that **do not work** in BF2 `AIDLL.dll`:

- **Debugger error (missing from `AIDLL.dll`)**: `AverageStrategicStrength`, `AttackStrategicStrength`, `DefenceStrategicStrength`, `Security`.
- **Always evaluate to `0`**: `Air`, `Bomber`, `Fighter`, `Naval`, `HeavyNaval`, `LCVP`, `AntiAir`, `Infantry`/`Infantery`, `AntiTank`, `HeavyAttack`, `Carrier`, `FastAttack`, `Artillery`.
- **Important**: `v_arg3 < 13` is invalid in SAI condition indices.

### `v_arg3` Disassembly Mapping (`AIDLL.dll`)

- `0`: `Carrier`
- `1`: `HeavyNaval`
- `2`: `LCVP`
- `3`: `Naval`
- `4`: `Bomber`
- `5`: `Fighter`
- `6`: `AntiAir`
- `7`: `Air`
- `8`: `Infantry` / `Infantery`
- `9`: `Artillery`
- `10`: `AntiTank`
- `11`: `HeavyAttack`
- `12`: `FastAttack`

## Strategy Tree Modifiers (`aiStrategy.*`)

- **`aiStrategy.setTreeModifier <TTNFlag> <Weight>`** — Sets a Temperature TreeNode (`TTN`) tree modifier.
- **`aiStrategy.setTreeModifierCombatStrength <TTNFlag> <All | CSTFlag> <Weight>`** — Sets a Combat Strength Type (`CST`) modifier.

### All `TTN*` Flags (`AIDLL.dll` / `BF2.exe`)

`TTNSuppliesAmmunition`, `TTNSuppliesRepair`, `TTNSupplies`, `TTNControlPoint`, `TTNTransportation`, `TTNRadar`, `TTNProduction`, `TTNAirfield`, `TTNFixedWeapons`, `TTNEditors`, `TTNTopography`, `TTNDefensivePos`, `note::`, `:file:`BF2.exe`.`, `types.`, `types.`, `file.`, `Flags`, `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`, `text`, `Flags`, `:linenos:`, `TTNHostileAirMobile`, `TTNHostileAirFixed`, `TTNHostileNavalMobile`, `TTNHostileNavalFixed`, `TTNHostileGroundMobile`, `TTNHostileGroundFixed`, `TTNHostileNaval`, `TTNHostileAir`, `TTNHostileGround`, `TTNHostileGroundAndNaval`, `TTNHostileArtillery`, `TTNFriendAirMobile`, `TTNFriendAirFixed`, `TTNFriendNavalMobile`, `TTNFriendGroundMobile`, `TTNFriendGroundFixed`, `TTNFriendNavalFixed`, `TTNFriendAir`, `TTNFriendNaval`, `TTNFriendGround`, `TTNFriendGroundAndNaval`, `TTNFriendArtillery`, `TTN`, `^^^^^^^^^`, `text`, `TTN`, `:linenos:`, `TTNStrategic`, `TTNTactical`, `TTNHostile`, `TTNFriendly`, `TTNStatic`, `TTNDynamic`, `TTNTop`, `Flags`, `^^^^^^^^^`, `file.`, `twice:`, ```Infantry```, ```Infantery```, `section.`, `text`, `:linenos:`, `CSTNumberOfTypes`, `CSTAirPlane`, `CSTHelicopter`, `CSTNavalArmour`, `CSTHeavyArmour`, `CSTLightArmour`, `CSTInfantry`, `CSTInfantery`, `Miscellaneous`, `^^^^^^^^^^^^^`, `getTreeModifierCombatStrength`, `function.`, `important::`, `script.`, `text`, `Value`, `000000129D0C`, `(1.41)`, `-------------------------------------`, `Flags`, `^^^^^^^^`, `text`, `:linenos:`, `ITHasCarHorn`, `ITObstacle`, `ITHasWreck`, `ITHelicopter`, `ITNoTemperature`, `ITObstructedView`, `ITSoldier`, `ITVegetation`, `ITBiological`, `ITStructure`, `ITLowPriority`, `ITUnmanned`, `ITMobile`, `ITCover`, `ITFixed`, `ITArtillery`, `ITTransportation`, `ITAirfield`, `ITRadar`, `ITControlpoint`, `ITNaval`, `ITGround`, `ITAir`, `ITUnit`, `ITRepair`, `ITAmmunition`, `ITProduction`

### Hostile & Friendly `TTN*` Flags (`AIDLL.dll`)

`TTNHostileAirMobile`, `TTNHostileAirFixed`, `TTNHostileNavalMobile`, `TTNHostileNavalFixed`, `TTNHostileGroundMobile`, `TTNHostileGroundFixed`, `TTNHostileNaval`, `TTNHostileAir`, `TTNHostileGround`, `TTNHostileGroundAndNaval`, `TTNHostileArtillery`, `TTNFriendAirMobile`, `TTNFriendAirFixed`, `TTNFriendNavalMobile`, `TTNFriendGroundMobile`, `TTNFriendGroundFixed`, `TTNFriendNavalFixed`, `TTNFriendAir`, `TTNFriendNaval`, `TTNFriendGround`, `TTNFriendGroundAndNaval`, `TTNFriendArtillery`, `TTNStrategic`, `TTNTactical`, `TTNHostile`, `TTNFriendly`, `TTNStatic`, `TTNDynamic`, `TTNTop`

### All `CST*` Flags (`AIDLL.dll`)

`CSTNumberOfTypes`, `CSTAirPlane`, `CSTHelicopter`, `CSTNavalArmour`, `CSTHeavyArmour`, `CSTLightArmour`, `CSTInfantry`, `CSTInfantery`

### All `IT*` Flags (`BF2.exe`)

`ITHasCarHorn`, `ITObstacle`, `ITHasWreck`, `ITHelicopter`, `ITNoTemperature`, `ITObstructedView`, `ITSoldier`, `ITVegetation`, `ITBiological`, `ITStructure`, `ITLowPriority`, `ITUnmanned`, `ITMobile`, `ITCover`, `ITFixed`, `ITArtillery`, `ITTransportation`, `ITAirfield`, `ITRadar`, `ITControlpoint`, `ITNaval`, `ITGround`, `ITAir`, `ITUnit`, `ITRepair`, `ITAmmunition`, `ITProduction`

## Comparison Aliases

- `-`: `Difference`
- `>-`: `DifferenceGreater`
- `<-`: `DifferenceSmaller`
- `=`: `Equal`
- `>=`: `EqualGreater`
- `<=`: `EqualSmaller`
- `/`: `Quotient`
- `>/`: `QuotientGreater`
- `</`: `QuotientSmaller`

## Strategic AI Database Variables

`Air`, `AirField`, `AirSpawner`, `AntiAir`, `AntiTank`, `Artillery`, `Attacks`, `Base`, `BattleShip`, `Bomber`, `Both`, `Bridge`, `Carrier`, `Centre`, `ChokePoint`, `Close`, `ControlPoint`, `Crisp`, `Defences`, `East`, `EnemyObject`, `Equal`, `EqualGreater`, `EqualSmaller`, `FastAttack`, `Fighter`, `Flank`, `Front`, `FrontBase`, `FrontCentre`, `FrontClose`, `FrontFlank`, `FrontNeutral`, `FrontRemote`, `HeavyAttack`, `LandSpawner`, `LCVP`, `Naval`, `NavalSpawner`, `North`, `NumberOfFriendlyAreas`, `NumberOfHostileAreas`, `NumberOfNeutralAreas`, `Remote`, `Route`, `Safe`, `SoldierSpawner`, `South`, `StartTime`, `StrongPoint`, `SupplyPoint`, `Ticket`, `Time`, `UnitConstant`, `UnReachable`, `West`
