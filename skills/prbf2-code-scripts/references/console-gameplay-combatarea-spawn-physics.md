# Console Gameplay: Combat Area, Ingame, Spawn Manager, and Physics

## Combat Area

- `combatArea.active <std::string>`
    - Returns: `void`
- `combatArea.addAreaPoint <Vec2>`
    - Returns: `void`
- `combatArea.create <std::string>`
    - Returns: `void`
- `combatArea.deleteActiveCombatArea`
    - Returns: `void`
- `combatArea.getActiveCombatAreaName`
    - Returns: `std::string`
- `combatArea.inverted <bool>`
    - Returns: `bool`
- `combatArea.layer <int>`
    - Returns: `int`
- `combatAreaManager.addVehicleDamage <world::VehicleCategory float>`
    - Returns: `void`
- `combatAreaManager.addVehicleTimer <world::VehicleCategory float>`
    - Returns: `void`
- `combatAreaManager.damage <float>`
    - Returns: `float`
- `combatAreaManager.timeAllowedOutside <float>`
    - Returns: `float`
- `combatAreaManager.use <bool>`
    - Returns: `void`
- `combatArea.max <Vec2>`
    - Returns: `Vec2`
- `combatArea.min <Vec2>`
    - Returns: `Vec2`
- `combatArea.team <int>`
    - Returns: `int`
- `combatArea.usedByPathFinding <bool>`
    - Returns: `bool`
- `combatArea.vehicles <int>`
    - Returns: `int`

    Controls what kind of vehicle is effected by the combat zone. This can be used for crating an extra large, separate combat zone around the base combat zone only for jets, to give them a much larger area to fly in and when you hop into a jet, you can still see the base combat zone, but the area between the base and the jet combat zone will be 1/2 transparent. When hand coding this, the values are:

    - VehicleType 0: `Land`
    - VehicleType 1: `Sea`
    - VehicleType 2: `Planes`
    - VehicleType 3: `Choppers`
    - VehicleType 4: `All`
    - VehicleType 5: `Planes & Choppers`

## Ingame

### ingameHelp

- `ingameHelp.showIngameHelp <std::string float>`
    - Returns: `void`

### InputDevices

- `InputDevices.setAxisScale <InputDeviceFlags InputDeviceAxes float>`
    - Returns: `bool`
- `InputDevices.setInvertAxis <InputDeviceFlags InputDeviceAxes bool>`
    - Returns: `bool`

### itemSelection

- `itemSelection.setReverseItems <bool>`
    - Returns: `void`

### levelsList

- `levelsList.setVoteMapShow <int>`
    - Returns: `void`
- `levelsList.singleClick <int>`
    - Returns: `void`

## Spawn Manager

- `spawnManager.commitSuicide`
    - Returns: `void`
- `spawnManager.listSpawnGroups`
    - Returns: `void`
- `spawnManager.selectNextUnlock <int>`
    - Returns: `void`
- `spawnManager.setPlayerKit <int>`
    - Returns: `void`
- `spawnManager.setPlayerTeam <int>`
    - Returns: `void`
- `spawnManager.toggleMembers <bool>`
    - Returns: `void`

## Physics

- `physics.airDensityZeroAtHeight <float>`
    - Returns: `float`
- `physics.gravity <float>`
    - Returns: `float`
- `physics.listProperties`
    - Returns: `std::string`
- `physics.wind <Vec3>`
    - Returns: `Vec3`
