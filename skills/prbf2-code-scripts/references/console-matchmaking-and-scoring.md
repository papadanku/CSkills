# Console Matchmaking: Local, Maplist, Profile, and Scoring

## Local

### localPlayer

- `localPlayer.commanderSelectDelay <float>`
    - Returns: `float`
- `localPlayer.firstCommanderSelectDelay <float>`
    - Returns: `float`

### localProfile

- `localProfile.addDemoBookmark <std::string std::string std::string>`
    - Returns: `void`

    Adds a bookmark to a battlerecorder demo

- `localProfile.save`
    - Returns: `bool`
- `localProfile.setEmail <std::string>`
    - Returns: `std::string`

    Sets or shows the email adress of the current profile

- `localProfile.setGamespyNick <std::string>`
    - Returns: `std::string`

    Sets or shows the gamespy login name of the current profile

- `localProfile.setName <std::string>`
    - Returns: `std::string`

    Sets or shows the name for the current profile

- `localProfile.setNick <std::string>`
    - Returns: `std::string`

    Sets or shows the nickname for the current profile

- `localProfile.setNumTimesLoggedIn <int>`
    - Returns: `int`
- `localProfile.setPassword <std::string>`
    - Returns: `std::string`

    Sets or shows the password for the current profile

- `localProfile.setTotalPlayedTime <float>`
    - Returns: `void`

## Maplist

- `maplist.append <std::string std::string int>`
    - Returns: `bool`
- `maplist.clear`
    - Returns: `bool`
- `maplist.configFile <std::string>`
    - Returns: `std::string`
- `maplist.currentMap`
    - Returns: `int`
- `maplist.insert <int std::string std::string>`
    - Returns: `bool`
- `maplist.list`
    - Returns: `std::string`
- `maplist.load`
    - Returns: `bool`
- `maplist.mapCount`
    - Returns: `int`
- `maplist.remove <int>`
    - Returns: `int`
- `maplist.save`
    - Returns: `bool`

## Profile

- `profile.activateCharacterProfile <std::string>`
    - Returns: `bool`
- `profile.activatePlayerProfile <std::string>`
    - Returns: `bool`
- `profile.activeCharacterProfile <std::string>`
    - Returns: `std::string`
- `profile.activeMod <std::string>`
    - Returns: `std::string`
- `profile.activePlayerProfile <std::string>`
    - Returns: `std::string`
- `profile.addCharacterProfile <std::string>`
    - Returns: `bool`
- `profile.addModSetting <std::string>`
    - Returns: `bool`
- `profile.applySettings`
    - Returns: `void`
- `profile.createPlayerProfile <std::string>`
    - Returns: `bool`
- `profile.defaultKit <int>`
    - Returns: `int`
- `profile.getIndexForKit <std::string int>`
    - Returns: `void`
- `profile.playerName <std::string>`
    - Returns: `std::string`
- `profile.rank <int>`
    - Returns: `int`
- `profile.setIndexForKit <std::string int int>`
    - Returns: `void`
- `profile.tagIcon <std::string>`
    - Returns: `std::string`
- `profile.tagText <std::string>`
    - Returns: `std::string`
- `profile.visualUnlockLevel <int>`
    - Returns: `int`

## Scoring

### reservedSlots

- `reservedSlots.addNick <std::string>`
    - Returns: `void`
- `reservedSlots.clear`
    - Returns: `void`
- `reservedSlots.configFile <std::string>`
    - Returns: `std::string`
- `reservedSlots.list`
    - Returns: `std::string`
- `reservedSlots.load`
    - Returns: `bool`
- `reservedSlots.removeNick <std::string>`
    - Returns: `void`
- `reservedSlots.save`
    - Returns: `bool`

### scoreboard

- `scoreboard.setToggleShow <int>`
    - Returns: `void`
- `scoreboard.singleClick <int>`
    - Returns: `void`

### scoreManager

- `scoreManager.ammo <int>`
    - Returns: `int`
- `scoreManager.ammoScoreLimit <float>`
    - Returns: `float`
- `scoreManager.assistKill <int>`
    - Returns: `int`
- `scoreManager.controlPointCapture <int>`
    - Returns: `int`
- `scoreManager.death <int>`
    - Returns: `int`
- `scoreManager.driverPassenger <int>`
    - Returns: `int`
- `scoreManager.flagCapture <int>`
    - Returns: `int`
- `scoreManager.flagReturn <int>`
    - Returns: `int`
- `scoreManager.heal <int>`
    - Returns: `int`
- `scoreManager.healScoreLimit <float>`
    - Returns: `float`
- `scoreManager.inDirectKill <int>`
    - Returns: `int`
- `scoreManager.kill <int>`
    - Returns: `int`
- `scoreManager.objective <int>`
    - Returns: `int`
- `scoreManager.repair <int>`
    - Returns: `int`
- `scoreManager.repairScoreLimit <float>`
    - Returns: `float`
- `scoreManager.soldierRevive <int>`
    - Returns: `int`
- `scoreManager.teamDamage <int>`
    - Returns: `int`
- `scoreManager.teamDamageLimit <float>`
    - Returns: `float`
- `scoreManager.teamVehicleDamage <int>`
    - Returns: `int`
- `scoreManager.teamVehicleDamageLimit <float>`
    - Returns: `float`
- `scoreManager.TK <int>`
    - Returns: `int`
- `scoreManager.vehicleRevive <int>`
    - Returns: `int`
