# Console Gameplay: Player, Squad, Commander, and Radio

## Commander

- `commander.accept <bool>`
    - Returns: `void`
- `commander.artillery`
    - Returns: `void`
- `commander.commanderApply`
    - Returns: `void`
- `commander.commanderMutiny`
    - Returns: `void`
- `commander.commanderResign`
    - Returns: `void`
- `commander.satellite`
    - Returns: `bool`
- `commander.sendOrder <int bool>`
    - Returns: `void`
- `commander.supplies`
    - Returns: `bool`
- `commander.toggleArtilleryState`
    - Returns: `void`
- `commander.toggleSupplyState`
    - Returns: `void`
- `commander.toggleUAVState`
    - Returns: `void`
- `commander.toggleVehicleDropState`
    - Returns: `void`
- `commander.uav`
    - Returns: `bool`
- `commander.vehicleDrop`
    - Returns: `bool`
- `commander.zoomCommander`
    - Returns: `bool`

### commanderInterface

- `commanderInterface.selectOrder <std::string>`
    - Returns: `bool`
- `commanderInterface.setstd::stringMap <std::string std::string std::string>`
    - Returns: `void`

### commanderMenu

- `commanderMenu.deselect`
    - Returns: `void`
- `commanderMenu.doubleClick`
    - Returns: `void`
- `commanderMenu.rightClick`
    - Returns: `void`
- `commanderMenu.sendRadioMessage <std::string TargetChannel>`
    - Returns: `void`
- `commanderMenu.singleClick`
    - Returns: `void`
- `commanderMenu.vehicleDropReloadTime <float>`
    - Returns: `float`

## Player

- `Player.active <IPlayer*>`
    - Returns: `IPlayer\*`
- `Player.create <std::string std::string>`
    - Returns: `IPlayer\*`
- `player.isAi <bool>`
    - Returns: `bool`
- `player.isAlive <bool>`
    - Returns: `bool`
- `player.isNetwork <bool>`
    - Returns: `bool`
- `player.kit <int>`
    - Returns: `int`
- `Player.list`
    - Returns: `std::string`
- `Player.listPlayerClasses`
    - Returns: `std::string`
- `player.moveTo <Vec3>`
    - Returns: `std::string`
- `player.name`
    - Returns: `std::string`
- `player.pickup <std::string>`
    - Returns: `void`
- `Player.saveAll <std::string>`
    - Returns: `bool`
- `player.setFov <float float>`
    - Returns: `void`
- `player.setVehicleWithInputId <IObject_ptrproxy int>`
    - Returns: `bool`
- `player.spawnGroup <int>`
    - Returns: `int`
- `player.team <int>`
    - Returns: `int`
- `player.vehicle <IObject_ptrproxy>`
    - Returns: `IObject_ptrproxy`

## Squad

### squad

- `squad.leaveSquad`
    - Returns: `void`

### squadInterface

- `squadInterface.selectOrder <std::string>`
    - Returns: `bool`
- `squadInterface.setstd::stringMap <std::string std::string std::string>`
    - Returns: `void`

### squadLeaderInterface

- `squadLeaderInterface.selectOrder <std::string>`
    - Returns: `bool`
- `squadLeaderInterface.setstd::stringMap <std::string std::string std::string>`
    - Returns: `void`

### squadLeader

- `squadLeader.sendOrder <int bool>`
    - Returns: `void`
- `squadLeader.sendRequest <int bool>`
    - Returns: `void`
- `squadLeader.sendRequestForOrder`
    - Returns: `void`

### squadManager

- `squadManager.changeSquadName <std::string bool>`
    - Returns: `void`
- `squadManager.joinSquad <int>`
    - Returns: `void`
- `squadManager.leaveSquad <int>`
    - Returns: `void`
- `squadManager.listSquadMembers <int int>`
    - Returns: `std::string`
- `squadManager.listSquads <int>`
    - Returns: `std::string`
- `squadManager.makeMeCommander`
    - Returns: `void`
- `squadManager.popNextCommanderApplicant <int>`
    - Returns: `void`

### squadMenu

- `squadMenu.applyInviteList`
    - Returns: `void`
- `squadMenu.createSquad`
    - Returns: `void`
- `squadMenu.doubleClickInvite`
    - Returns: `void`
- `squadMenu.doubleClickNew`
    - Returns: `void`
- `squadMenu.setShowInviteList <bool>`
    - Returns: `void`
- `squadMenu.setSquadCreateSelect <bool>`
    - Returns: `void`
- `squadMenu.setSquadNameSelect`
    - Returns: `void`
- `squadMenu.singleClickInvite`
    - Returns: `void`
- `squadMenu.singleClickNew`
    - Returns: `void`
- `squadMenu.squadCreateLockToggle`
    - Returns: `void`

## Radio

### radio

- `radio.answer <bool>`
    - Returns: `void`
- `radio.callForAmmo`
    - Returns: `void`
- `radio.callForMedic`
    - Returns: `void`
- `radio.callForRepair`
    - Returns: `void`
- `radio.sendKitMessage`
    - Returns: `void`
- `radio.sendSpottedMessage <bool world::VehicleType>`
    - Returns: `void`
- `radio.setSpottedMenuActive`
    - Returns: `void`

### radioInterface

- `radioInterface.selectOrder <std::string>`
    - Returns: `bool`
- `radioInterface.setstd::stringMap <std::string std::string std::string>`
    - Returns: `void`

### radioVehicleInterface

- `radioVehicleInterface.selectOrder <std::string>`
    - Returns: `bool`
- `radioVehicleInterface.setstd::stringMap <std::string std::string std::string>`
    - Returns: `void`
