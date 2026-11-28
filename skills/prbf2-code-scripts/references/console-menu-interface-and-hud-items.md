# Console Menu: Interface, HUD Items, and HUD Manager

## HUD Items & Manager
### hudItems

- `hudItems.setBool <std::string bool>`
    - Returns: `void`
- `hudItems.setFloat <std::string float>`
    - Returns: `void`
- `hudItems.setstd::string <std::string std::string>`
    - Returns: `void`

### hudManager

- `hudManager.addFavouriteServer <bool>`
    - Returns: `void`
- `hudManager.addTextureAtlas <std::string>`
    - Returns: `void`
- `hudManager.enableSayAllChatBox <bool>`
    - Returns: `void`
- `hudManager.enableSaySquadChatBox <bool>`
    - Returns: `void`
- `hudManager.enableSayTeamChatBox <bool>`
    - Returns: `void`
- `hudManager.refresh`
    - Returns: `bool`
- `hudManager.setCommMousePos <int int>`
    - Returns: `bool`
- `hudManager.setCommMouseSensitivity <int>`
    - Returns: `bool`
- `hudManager.setCommPos <int int>`
    - Returns: `bool`
- `hudManager.setCommSize <int int>`
    - Returns: `bool`
- `hudManager.setDisplayControlpoints <bool>`
    - Returns: `void`
- `hudManager.setDisplayTickets <bool>`
    - Returns: `void`
- `hudManager.setDone <bool>`
    - Returns: `void`
- `hudManager.setMapStatic <bool>`
    - Returns: `void`
- `hudManager.setMaximumNrOfCPs <int>`
    - Returns: `void`
- `hudManager.setMouseTextureArtillery <std::string>`
    - Returns: `bool`
- `hudManager.setMouseTextureCancel <std::string>`
    - Returns: `bool`
- `hudManager.setMouseTextureEmpty <std::string>`
    - Returns: `bool`
- `hudManager.setMouseTextureFull <std::string>`
    - Returns: `bool`
- `hudManager.setMouseTextureSupply <std::string>`
    - Returns: `bool`
- `hudManager.setMouseTextureUAV <std::string>`
    - Returns: `bool`
- `hudManager.setPaint <bool>`
    - Returns: `void`
- `hudManager.setPointerMouseSensitivity <int>`
    - Returns: `bool`
- `hudManager.setPointerSize <int int>`
    - Returns: `bool`
- `hudManager.setSpottedAngle <float>`
    - Returns: `void`
- `hudManager.setSpottedMenuPos <int int>`
    - Returns: `bool`
- `hudManager.setSpottedMenuSize <int int>`
    - Returns: `bool`
- `hudManager.setSpottedMousePos <int int>`
    - Returns: `bool`
- `hudManager.setTargetTop <float>`
    - Returns: `void`
- `hudManager.setUpdate <bool>`
    - Returns: `void`

## Menu
## menuTeamManager

- `menuTeamManager.addKit <std::string>`
    - Returns: `void`
- `menuTeamManager.addTeam <std::string std::string>`
    - Returns: `void`
- `menuTeamManager.addWeapon <std::string int int>`
    - Returns: `void`
- `menuTeamManager.setTeamId <int>`
    - Returns: `void`

## minimap

- `minimap.setCommanderOffset <Vec2>`
    - Returns: `void`
- `minimap.setCurrOrderList <int>`
    - Returns: `void`
- `minimap.setDestinationBlend <int>`
    - Returns: `void`
- `minimap.setFilterColor <float float float>`
    - Returns: `void`
- `minimap.setFullScreenZoom <int>`
    - Returns: `void`
- `minimap.setPaintAllKits`
    - Returns: `void`
- `minimap.setPaintAllVehicles`
    - Returns: `void`
- `minimap.setPaintKit <int>`
    - Returns: `void`
- `minimap.setPaintVehicle <int>`
    - Returns: `void`
- `minimap.setSourceBlend <int>`
    - Returns: `void`
- `minimap.setZoom`
    - Returns: `void`
- `minimap.toggleShowKits`
    - Returns: `void`

## nametags

- `nametags.createBar <NametagItemIDs int int>`
    - Returns: `void`
- `nametags.createIcon <NametagItemIDs>`
    - Returns: `void`
- `nametags.deathFadeOutTime <float>`
    - Returns: `float`
- `nametags.deployableDistance <double>`
    - Returns: `double`
- `nametags.enemyDotLimit <float>`
    - Returns: `float`
- `nametags.enemyTagDelayTime <double>`
    - Returns: `double`
- `nametags.enemyTagFadeInTime <double>`
    - Returns: `double`
- `nametags.enemyTagFadeOutTime <double>`
    - Returns: `double`
- `nametags.getCullDistance <TagType>`
    - Returns: `Vec2`
- `nametags.manDownFadeOutTime <float>`
    - Returns: `float`
- `nametags.maxCallDistance <float>`
    - Returns: `float`
- `nametags.maxFriendlyDistance <float>`
    - Returns: `float`
- `nametags.setCullDistance <TagType Vec2>`
    - Returns: `void`
- `nametags.setTexture <int std::string int>`
    - Returns: `void`
- `nametags.vehicleNametagOffset <float>`
    - Returns: `float`
- `nametags.vehicleNametagOffsetFactor <float>`
    - Returns: `float`
