
# PR:BF2 UDL Commands, Variables, and Tokens Reference

Catalog of BF2/PR:BF2 UDL keywords, console command namespaces, template components, object enums, AI directives, and Atlas tokens.

## 1. Syntax & Flow Control Tokens (`.con`, `.tweak`, `.inc`, `.ai`)

- **Line Comment**: `rem` - Single-line comment; everything after `rem` is ignored.
- **Block Comment**: `beginRem` ... `endRem` - Multi-line comment; only supported when executed by engine (not interactive console).
- **Atlas Comment**: `#` - Used in `.tac` / `.tai` atlas files.
- **Variable Prefixes**: `var v_name`, `const c_name` - Mutable (`v_`) and immutable (`c_`) Hungarian-style prefixes.
- **Return Capture**: `-> v_result` - Captures command return value into a variable.
- **Conditionals / Loops**: `if`, `elseIf`, `else`, `endIf`, `while`, `endWhile` - Standard control flow blocks.
- **Comparison Operators**: `==`, `!=`, `<`, `<=`, `>`, `>=`, `EQUAL`, `equals`, `notEquals` - Used in `if` / `while` expressions.
- **Logical Operators**: `AND`, `OR`, `NOT` - Boolean combinators in expressions.
- **Path / CRD Separators**: `/`, `\` - `/` used in `CRD_*` and script paths; `\` often used in HUD/icon paths.
- **Distribution Prefix**: `CRD_NONE`, `CRD_UNIFORM`, `CRD_EXPONENTIAL`, `CRD_NORMAL` - 4-part Continuous Random Distribution: `CRD_TYPE/num1/num2/symmetry`.
- **Execution Flow**: `include`, `run`, `return` - `include` shares caller scope; `run` isolates scope and passes `v_arg1..N`.

## 2. Command Namespaces (`.con`, `.tweak`, `.inc`)

All 139 namespace prefixes from `Battlefield 2 (Dark).xml`, cross-referenced with documented command counts in `RealityDocs`.

- **`rhooks.`** (0 documented): *(engine/internal command namespace)*
- **`admin.`** (0 documented): *(engine/internal command namespace)*
- **`ai.`** (77 documented): `ai.createheightmap `, `ai.readheightmapfromfile `, `ai.init `
- **`aiPathfinding.`** (36 documented): `aipathfinding.createmap `, `aipathfinding.activemap `, `aipathfinding.tracemap `
- **`aiSettings.`** (60 documented): `aisettings.setmaxnbots `, `aisettings.setmaxnautocontrollers `, `aisettings.maxbotsincludehumans `
- **`aiStrategy.`** (43 documented): `aistrategy.createstrategy `, `aistrategy.setactivestrategy `, `aistrategy.getactivestrategyname `
- **`aiStrategicArea.`** (63 documented): `aistrategicarea.create `, `aistrategicarea.setflankposition `, `aistrategicarea.createfromcontrolpoint `
- **`AIStrategicArea.`** (63 documented): `aistrategicarea.create `, `aistrategicarea.setflankposition `, `aistrategicarea.createfromcontrolpoint `
- **`aiTemplate.`** (10 documented): `aitemplate.create `, `aitemplate.active `, `aitemplate.types `
- **`aiTemplatePlugIn.`** (65 documented): `aitemplateplugin.create `, `aitemplateplugin.active `, `aitemplateplugin.vehiclenumber `
- **`animationBundle.`** (21 documented): `animationBundle.abruptPlayback <bool>`, `animationBundle.addAnimation <std::string>`, `animationBundle.addEvent <std::string>`
- **`animationManager.`** (7 documented): `animationManager.fadeInTime <float>`, `animationManager.ignoreMotherOrientation <int>`, `animationManager.length <float>`
- **`animationSystem.`** (32 documented): `animationSystem.activestd::string `, `animationSystem.activeAnimation <std::string>`, `animationSystem.activeBundle <std::string>`
- **`animationTrigger.`** (13 documented): `animationTrigger.addBundle <std::string>`, `animationTrigger.addChild <std::string>`, `animationTrigger.clearValueHolder `
- **`animationValueHolder.`** (7 documented): `animationValueHolder.getFilename `, `animationValueHolder.max <float>`, `animationValueHolder.min <float>`
- **`AudioSettings.`** (15 documented): `audioSettings.alwaysAllowSystemOpenAL <bool>`, `audioSettings.effectsVolume <float>`, `audioSettings.enableEAX <bool>`
- **`bf2Engine.`** (1 documented): `bf2Engine.playMovie <std::string int>`
- **`BitStream.`** (0 documented): *(engine/internal command namespace)*
- **`buffermanager.`** (0 documented): *(engine/internal command namespace)*
- **`chat.`** (2 documented): `chat.sayAll <std::string>`, `chat.sayTeam <std::string>`
- **`CollisionCheck.`** (1 documented): `CollisionCheck.checkStaticCollisionMeshes <int>`
- **`collisionLog.`** (0 documented): *(engine/internal command namespace)*
- **`CollisionManager.`** (23 documented): `collisionManager.buildDebugCollisionMeshes `, `collisionManager.create <std::string>`, `collisionManager.createTemplate <std::string>`
- **`CombatArea.`** (12 documented): `combatArea.active <std::string>`, `combatArea.addAreaPoint <Vec2>`, `combatArea.create <std::string>`
- **`CombatAreaManager.`** (5 documented): `combatAreaManager.addVehicleDamage <world::VehicleCategory float>`, `combatAreaManager.addVehicleTimer <world::VehicleCategory float>`, `combatAreaManager.damage <float>`
- **`commander.`** (15 documented): `commander.accept <bool>`, `commander.artillery `, `commander.commanderApply `
- **`commanderInterface.`** (2 documented): `commanderInterface.selectOrder <std::string>`, `commanderInterface.setstd::stringMap <std::string std::string std::string>`
- **`commanderMenu.`** (6 documented): `commanderMenu.deselect `, `commanderMenu.doubleClick `, `commanderMenu.rightClick `
- **`config.`** (0 documented): *(engine/internal command namespace)*
- **`console.`** (24 documented): `Console.allowMultipleFileLoad <bool>`, `Console.bindKeyToConsoleScript <int std::string>`, `Console.echo <bool>`
- **`ControlMap.`** (21 documented): `controlMap.addAxisToAxisMapping <int InputDeviceFlags InputDeviceAxes>`, `controlMap.addAxisToTriggerMapping <int int InputDeviceFlags>`, `controlMap.addButtonAndKeyToAxisMapping <int InputDeviceFlags InputDeviceButtons>`
- **`debug.`** (0 documented): *(engine/internal command namespace)*
- **`debugCounterManager.`** (0 documented): *(engine/internal command namespace)*
- **`decalManager.`** (8 documented): `decalManager.decalGeomClipAngle <float>`, `decalManager.decalNormalOffset <float>`, `decalManager.drawStats <bool>`
- **`demo.`** (7 documented): `demo.recordDemo <std::string>`, `demo.restartDemo `, `demo.shutdownDemo `
- **`Editor.`** (46 documented): `Editor.createNewLayer <std::string>`, `Editor.deleteAllLayers `, `Editor.deleteAllObjects `
- **`envmapManager.`** (4 documented): `envmapManager.generateEnvMaps `, `envmapManager.loadEMIFile <std::string>`, `envmapManager.perPixelEnvironmentMappingEnabled <bool>`
- **`fileChangeManager.`** (0 documented): *(engine/internal command namespace)*
- **`fileManager.`** (6 documented): `fileManager.addPath <std::string>`, `fileManager.copyFile <std::string std::string>`, `fileManager.deleteFile <std::string>`
- **`game.`** (8 documented): `game.allowToggleFullscreen <bool>`, `game.lockFps <int>`, `game.radioMessage <TargetChannel std::string>`
- **`gameLogic.`** (62 documented): `gameLogic.AddInvalidDropVehicleObject <std::string bool>`, `gameLogic.becomeSquadLeader <bool>`, `gameLogic.createObject <std::string>`
- **`GameLogic.`** (62 documented): `gameLogic.AddInvalidDropVehicleObject <std::string bool>`, `gameLogic.becomeSquadLeader <bool>`, `gameLogic.createObject <std::string>`
- **`gameServerSettings.`** (50 documented): `gameServerSettings.setAdminScript <std::string>`, `gameServerSettings.setAllowNATNegotation <bool>`, `gameServerSettings.setAutoBalanceTeam <bool>`
- **`GeneralSettings.`** (30 documented): `generalSettings.addFavouriteServer <std::string int std::string>`, `generalSettings.addServerHistory <std::string int std::string>`, `generalSettings.setAllowPunkBuster <bool>`
- **`GeometryTemplate.`** (43 documented): `geometryTemplate.active <IGeometryTemplate*>`, `geometryTemplate.color <Vec3>`, `geometryTemplate.compressVertexData <bool>`
- **`GlobalSettings.`** (2 documented): `globalSettings.setDefaultUser <std::string>`, `globalSettings.setNamePrefix <std::string>`
- **`heightmap.`** (7 documented): `heightmap.loadHeightData <std::string>`, `heightmap.loadMaterialData <std::string>`, `heightmap.setBitResolution <int>`
- **`heightmapcluster.`** (10 documented): `heightmapcluster.addHeightmap <std::string int int>`, `heightmapcluster.compileWaterMeshesIntoHeightmap `, `heightmapcluster.create <std::string>`
- **`hemiMapManager.`** (3 documented): `hemiMapManager.hemiLerpBias <float>`, `hemiMapManager.makeHemiMap <unsigned long std::string Vec3>`, `hemiMapManager.setBaseHemiMap <std::string Vec3 float>`
- **`hudBuilder.`** (118 documented): `hudBuilder.addNodeAlphaShowEffect `, `hudBuilder.addNodeBlendEffect <int int>`, `hudBuilder.addNodeMoveShowEffect <float int>`
- **`hudItems.`** (3 documented): `hudItems.setBool <std::string bool>`, `hudItems.setFloat <std::string float>`, `hudItems.setstd::string <std::string std::string>`
- **`hudManager.`** (30 documented): `hudManager.addFavouriteServer <bool>`, `hudManager.addTextureAtlas <std::string>`, `hudManager.enableSayAllChatBox <bool>`
- **`ingameHelp.`** (1 documented): `ingameHelp.showIngameHelp <std::string float>`
- **`InputDevices.`** (2 documented): `InputDevices.setAxisScale <InputDeviceFlags InputDeviceAxes float>`, `InputDevices.setInvertAxis <InputDeviceFlags InputDeviceAxes bool>`
- **`itemSelection.`** (1 documented): `itemSelection.setReverseItems <bool>`
- **`LevelSettings.`** (0 documented): *(engine/internal command namespace)*
- **`levelsList.`** (2 documented): `levelsList.setVoteMapShow <int>`, `levelsList.singleClick <int>`
- **`lightManager.`** (43 documented): `lightManager.ambientColor <Vec3>`, `lightManager.defaultEffectLightAffectionFactor <float>`, `lightManager.dynamicPointColor <Vec3>`
- **`Lightmanager.`** (43 documented): `lightManager.ambientColor <Vec3>`, `lightManager.defaultEffectLightAffectionFactor <float>`, `lightManager.dynamicPointColor <Vec3>`
- **`lightmapGeneration.`** (0 documented): *(engine/internal command namespace)*
- **`LightmapSettings.`** (0 documented): *(engine/internal command namespace)*
- **`LightSettings.`** (0 documented): *(engine/internal command namespace)*
- **`localplayer.`** (2 documented): `localPlayer.commanderSelectDelay <float>`, `localPlayer.firstCommanderSelectDelay <float>`
- **`localProfile.`** (9 documented): `localProfile.addDemoBookmark <std::string std::string std::string>`, `localProfile.save `, `localProfile.setEmail <std::string>`
- **`mapList.`** (10 documented): `maplist.append <std::string std::string int>`, `maplist.clear `, `maplist.configFile <std::string>`
- **`MapList.`** (10 documented): `maplist.append <std::string std::string int>`, `maplist.clear `, `maplist.configFile <std::string>`
- **`Material.`** (16 documented): `material.active <unsigned int>`, `material.damageLoss <float>`, `material.elasticity <float>`
- **`materialManager.`** (7 documented): `materialManager.attMaterial <unsigned int>`, `materialManager.createCell <unsigned int unsigned int>`, `materialManager.damageMod <float>`
- **`memory.`** (0 documented): *(engine/internal command namespace)*
- **`minimap.`** (12 documented): `minimap.setCommanderOffset <Vec2>`, `minimap.setCurrOrderList <int>`, `minimap.setDestinationBlend <int>`
- **`nametags.`** (16 documented): `nametags.createBar <NametagItemIDs int int>`, `nametags.createIcon <NametagItemIDs>`, `nametags.deathFadeOutTime <float>`
- **`network.`** (1 documented): `network.globalPredictionMode <PredictionMode>`
- **`networkableInfo.`** (6 documented): `networkableInfo.createNewInfo <std::string>`, `networkableInfo.deleteInfo <std::string>`, `networkableInfo.setBasePriority <float>`
- **`Object.`** (68 documented): `object.absolutePosition <Vec3>`, `object.absolutePositionSecondary <Vec3>`, `object.absoluteTransformation <Mat4>`
- **`object.`** (68 documented): `object.absolutePosition <Vec3>`, `object.absolutePositionSecondary <Vec3>`, `object.absoluteTransformation <Mat4>`
- **`objectDrawer.`** (6 documented): `objectDrawer.collectPlanesDistance <float>`, `objectDrawer.drawDebugPlanes <bool>`, `objectDrawer.faceForwardThreshold <float>`
- **`objectManager.`** (1 documented): `objectManager.drawStats <int>`
- **`ObjectSpawnerDef.`** (0 documented): *(engine/internal command namespace)*
- **`objectTemplate.`** (1241 documented): `objectTemplate.3dMapIcon <int>`, `objectTemplate.ability.hasAmmoAbility <bool>`, `objectTemplate.ability.hasHealingAbility <bool>`
- **`ObjectTemplate.`** (1241 documented): `objectTemplate.3dMapIcon <int>`, `objectTemplate.ability.hasAmmoAbility <bool>`, `objectTemplate.ability.hasHealingAbility <bool>`
- **`Overgrowth.`** (26 documented): `overgrowth.addMaterial <std::string uint>`, `overgrowth.addType <std::string>`, `overgrowth.closeDistFade <float>`
- **`OvergrowthType.`** (7 documented): `overgrowthType.density <float>`, `overgrowthType.geometry <std::string>`, `overgrowthType.minRadiusToOthers <float>`
- **`Particles.`** (2 documented): `Particles.enableOldParticles <bool>`, `Particles.enableParticles <bool>`
- **`particleSystemManager.`** (11 documented): `particleSystemManager.affectedByWind <bool>`, `particleSystemManager.drawBoundingBoxEnable <bool>`, `particleSystemManager.drawStats <bool>`
- **`physics.`** (4 documented): `physics.airDensityZeroAtHeight <float>`, `physics.gravity <float>`, `physics.listProperties `
- **`player.`** (17 documented): `Player.active <IPlayer*>`, `Player.create <std::string std::string>`, `player.isAi <bool>`
- **`portal.`** (2 documented): `portal.debugLevel <int>`, `portal.showStats <bool>`
- **`profile.`** (17 documented): `profile.activateCharacterProfile <std::string>`, `profile.activatePlayerProfile <std::string>`, `profile.activeCharacterProfile <std::string>`
- **`profiler.`** (0 documented): *(engine/internal command namespace)*
- **`pythonHost.`** (2 documented): `pythonHost.reinitialize `, `pythonHost.sendCommand <std::string std::string std::string>`
- **`radio.`** (7 documented): `radio.answer <bool>`, `radio.callForAmmo `, `radio.callForMedic `
- **`radioInterface.`** (2 documented): `radioInterface.selectOrder <std::string>`, `radioInterface.setstd::stringMap <std::string std::string std::string>`
- **`radioVehicleInterface.`** (2 documented): `radioVehicleInterface.selectOrder <std::string>`, `radioVehicleInterface.setstd::stringMap <std::string std::string std::string>`
- **`ragDoll.`** (20 documented): `ragDoll.active <bool>`, `ragDoll.addAngularConstraint <int int int>`, `ragDoll.addBone <int int>`
- **`rainManager.`** (0 documented): *(engine/internal command namespace)*
- **`raStats.`** (0 documented): *(engine/internal command namespace)*
- **`Renderer.`** (109 documented): `renderer.allowA2M <bool>`, `renderer.allowOnDemandPostProcessing <bool>`, `renderer.ambientIlluminationRange <Vec4>`
- **`renderer.`** (109 documented): `renderer.allowA2M <bool>`, `renderer.allowOnDemandPostProcessing <bool>`, `renderer.ambientIlluminationRange <Vec4>`
- **`reservedSlots.`** (7 documented): `reservedSlots.addNick <std::string>`, `reservedSlots.clear `, `reservedSlots.configFile <std::string>`
- **`resourceManager.`** (0 documented): *(engine/internal command namespace)*
- **`RoadTemplate.`** (0 documented): *(engine/internal command namespace)*
- **`RoadTemplateTexture.`** (0 documented): *(engine/internal command namespace)*
- **`scoreboard.`** (2 documented): `scoreboard.setToggleShow <int>`, `scoreboard.singleClick <int>`
- **`scoreManager.`** (22 documented): `scoreManager.ammo <int>`, `scoreManager.ammoScoreLimit <float>`, `scoreManager.assistKill <int>`
- **`SettingsManager.`** (10 documented): `SettingsManager.boolGet <std::string>`, `SettingsManager.boolSet <std::string bool>`, `SettingsManager.floatGet <std::string>`
- **`shadermanager.`** (11 documented): `shadermanager.byPassDiceStates <bool>`, `shadermanager.compileDebugTerrain <bool>`, `shadermanager.compilePartialPrecisionTypes <bool>`
- **`shadowManager.`** (41 documented): `shadowManager.allowAlphaShadows <bool>`, `shadowManager.alphaShadowThreshold <float>`, `shadowManager.dropShadowClipHeightOffset <float>`
- **`skinnedMeshRenderer.`** (1 documented): `skinnedMeshRenderer.shaderQuality <ShaderQuality>`
- **`skyDome.`** (21 documented): `skyDome.cloudLerpFactors <Vec2>`, `skyDome.cloudTemplate <std::string>`, `skyDome.cloudTexture <std::string>`
- **`Skydome.`** (21 documented): `skyDome.cloudLerpFactors <Vec2>`, `skyDome.cloudTemplate <std::string>`, `skyDome.cloudTexture <std::string>`
- **`Sound.`** (26 documented): `sound.addMenuSound <std::string std::string float>`, `sound.addSound <std::string>`, `sound.addTrigger <std::string>`
- **`sound.`** (26 documented): `sound.addMenuSound <std::string std::string float>`, `sound.addSound <std::string>`, `sound.addTrigger <std::string>`
- **`spawnManager.`** (6 documented): `spawnManager.commitSuicide `, `spawnManager.listSpawnGroups `, `spawnManager.selectNextUnlock <int>`
- **`squad.`** (1 documented): `squad.leaveSquad `
- **`squadInterface.`** (2 documented): `squadInterface.selectOrder <std::string>`, `squadInterface.setstd::stringMap <std::string std::string std::string>`
- **`squadLeader.`** (3 documented): `squadLeader.sendOrder <int bool>`, `squadLeader.sendRequest <int bool>`, `squadLeader.sendRequestForOrder `
- **`squadLeaderInterface.`** (2 documented): `squadLeaderInterface.selectOrder <std::string>`, `squadLeaderInterface.setstd::stringMap <std::string std::string std::string>`
- **`squadManager.`** (7 documented): `squadManager.changeSquadName <std::string bool>`, `squadManager.joinSquad <int>`, `squadManager.leaveSquad <int>`
- **`squadMenu.`** (10 documented): `squadMenu.applyInviteList `, `squadMenu.createSquad `, `squadMenu.doubleClickInvite `
- **`staticMeshRenderer.`** (12 documented): `staticMeshRenderer.allowAnisoFiltering <bool>`, `staticMeshRenderer.convertLightmapName <std::string>`, `staticMeshRenderer.enableLightIndexes <bool>`
- **`sv.`** (72 documented): `sv.adminScript <std::string>`, `sv.allowExternalViews <bool>`, `sv.allowFreeCam <bool>`
- **`swiffHost.`** (10 documented): `swiffHost.addAward <int int int>`, `swiffHost.addCredit <std::string int>`, `swiffHost.addGameMode <std::string std::string>`
- **`terrain.`** (23 documented): `terrain.ambientColor <Vec3>`, `terrain.create <std::string>`, `terrain.forceRenderStyle <int>`
- **`terrainCuller.`** (12 documented): `terrainCuller.baseCellSize <int>`, `terrainCuller.checkInside <bool>`, `terrainCuller.cullerType <int>`
- **`texturemanager.`** (1 documented): `texturemanager.customTextureSuffix <std::string>`
- **`triggerManager.`** (0 documented): *(engine/internal command namespace)*
- **`Undergrowth.`** (10 documented): `undergrowth.dynamicShadowsEnable <bool>`, `undergrowth.enabled <bool>`, `undergrowth.load <std::string>`
- **`undergrowthEditable.`** (0 documented): *(engine/internal command namespace)*
- **`UndergrowthEditable.`** (0 documented): *(engine/internal command namespace)*
- **`undergrowthEditableMaterial.`** (0 documented): *(engine/internal command namespace)*
- **`undergrowthEditableType.`** (0 documented): *(engine/internal command namespace)*
- **`Vars.`** (1 documented): `Vars.set <std::string std::string>`
- **`vars.`** (1 documented): `Vars.set <std::string std::string>`
- **`VideoSettings.`** (12 documented): `videoSettings.setAntialiasing <std::string>`, `videoSettings.setDynamicLightingQuality <int>`, `videoSettings.setDynamicShadowsQuality <int>`
- **`voip.`** (0 documented): *(engine/internal command namespace)*
- **`weatherManager.`** (20 documented): `weatherManager.doubleStrikeMaxDelay <float>`, `weatherManager.doubleStrikeMinDelay <float>`, `weatherManager.doubleStrikeProbability <float>`
- **`windManager.`** (2 documented): `windManager.globalWindDirection <Vec3>`, `windManager.globalWindSpeed <float>`

## 3. Template Components (`rem ---BeginComp:<Name>---` / `ObjectTemplate.createComponent`)

All 44 component blocks recognized by the BF2/PR UDL and `ObjectTemplate.createComponent`:

`Armor`, `StrategicObject`, `Ik`, `Ability`, `WeaponHud`, `VehicleHud`, `SingleFireComp`, `DefaultAmmoComp`, `WeaponBasedRecoilComp`, `SimpleDeviationComp`, `DefaultSoundComp`, `DefaultAnimationComp`, `DefaultZoomComp`, `MultiFireArmTargetComp`, `MultiFireComp`, `ToggleCameraComp`, `LPTargetComp`, `DefaultFollowComp`, `PostProcess`, `TargetDeviationComp`, `SimpleTargetComp`, `DefaultCollisionComp`, `DefaultDetonationComp`, `DefaultProjSoundComp`, `FixedTargetComp`, `PreDestinedFollowComp`, `DefaultPenetrateComp`, `SeekClosestTargetComp`, `Radio`, `WindAffector`, `AbilityHud`, `HelpHud`, `WarningHud`, `DefaultRicochetComp`, `StickyCollisionComp`, `ReplenishDetonationComp`, `SoldierDeviationComp`, `SoldierBasedRecoilComp`, `ThrownFireComp`, `ThrownAnimationComp`, `ExplosivesFireComp`, `ReplenishingAmmoComp`, `ResurrectCollisionComp`, `SpawnObjectFireComp`

## 4. Object Types, Enums, Inputs, and `IT*` Flags (`.con`, `.tweak`, `.inc`)

All 188 keywords from `Keywords4` for `.con`, `.tweak`, and `.inc`:

`SimpleObject`, `Bundle`, `LightSource`, `PlayerControlObject`, `SupplyObject`, `AnimatedBundle`, `EntryPoint`, `RotationalBundle`, `Spawnpoint`, `GenericFireArm`, `DestroyableObject`, `Camera`, `ObjectSpawner`, `EffectBundle`, `OverheadCamera`, `SpriteParticleSystem`, `Emitter`, `MeshParticleSystem`, `NonScreenAlignedParticleSystem`, `ForceObject`, `TrailSystem`, `Decal`, `Particle`, `ParticleSystemEmitter`, `AirDraftEffectBundle`, `GroundEffectBundle`, `WheelEffectBundle`, `Kit`, `Soldier`, `Ladder`, `Sound`, `DynamicBundle`, `GenericProjectile`, `RopeLink`, `HookLink`, `Zipline`, `DestroyableWindowsBundle`, `Engine`, `Rotor`, `Spring`, `Parachute`, `Wing`, `UAVVehicle`, `PlayercontrolObject`, `AntennaObject`, `SpawnPoint`, `GenericFirearm`, `RemoteControlledObject`, `DropVehicle`, `TurnableRemoteControlledObject`, `TargetObject`, `AirPlayerInputControlMap`, `Armament`, `BottomLeftAnimate`, `BottomLeftStatic`, `BottomRightAnimate`, `BottomRightStatic`, `BundledMesh`, `ControlInfo`, `ControlPoint`, `DefaultZoomCompSound`, `defaultGameControlMap`, `defaultPlayerInputControlMap`, `EnvMap`, `ForwardTrigger`, `Global`, `GrapplingHookRope`, `GrapplingHookRopeContainer`, `HandFireArmsInfo`, `HelicopterPlayerInputControlMap`, `Heightmap`, `HeighmapCluster`, `IdleTrigger`, `InfantryPlayerInputControlMap`, `LadderContainer`, `LandPlayerInputControlMap`, `MessageTrigger`, `Mobile`, `MovementTrigger`, `Physical`, `PoseTrigger`, `RandomTrigger`, `SeaPlayerInputControlMap`, `StaticMesh`, `SwitchMessageTrigger`, `Terrain`, `TerrainEditable`, `TopLayer`, `Trigger`, `Triggerable`, `TriggerableTarget`, `TurnTrigger`, `Unit`, `ZiplineContainer`, `ZiplineRope`, `GuiIndex`, `LandingGear`, `DebugSphereMesh`, `Mesh`, `SpringInfo`, `BasicInfo`, `KitInfo`, `BasicInfoNoPm`, `Assault`, `AT`, `Engineer`, `Sniper`, `Medic`, `Support`, `Specops`, `vehicle`, `Additive`, `Low`, `Medium`, `High`, `Standard`, `Front`, `Back`, `RotationalPoint`, `Point`, `MTYVehicle`, `RadialDir`, `TSHeatSeeking`, `TSTVGuided`, `TSWireGuided`, `TSParabellic`, `ControlPointInfo`, `TTHeat`, `TTUnique`, `TTLaser`, `TTNone`, `LightArmour`, `HeavyArmour`, `Fixed`, `FixedTurret`, `VCAir`, `VCHelicopter`, `VCLand`, `VCSea`, `VTBomber`, `VTFighter`, `VTDiveBomber`, `VTApc`, `VTHeavyTank`, `VTAA`, `PIMouseLookX`, `PIMouseLookY`, `PIAltFire`, `PIToggleCameraMode`, `PIYaw`, `PIThrottle`, `PIUse`, `PIFire`, `PIAltSprint`, `PISprint`, `PICrouch`, `PIFlareFire`, `PILie`, `PIRoll`, `PIPitch`, `PIPositionSelect1`, `PIPositionSelect2`, `PIPositionSelect3`, `PIPositionSelect4`, `PIPositionSelect5`, `PIPositionSelect6`, `PIWeaponSelect1`, `PIWeaponSelect2`, `PIWeaponSelect3`, `PIWeaponSelect4`, `PIWeaponSelect5`, `PICameraX`, `PICameraY`, `PINone`, `ITUnit`, `ITBiological`, `ITGround`, `ITMobile`, `ITHasWreck`, `ITStructure`, `ITSoldier`, `ITAir`, `ITCover`, `ITNaval`, `ITHasCarHorn`, `ITHelicopter`, `ITObstructedView`, `ITNoTemperature`

## 5. AI Namespaces, Behaviors, BAPST Wrappers, and Types (`.ai`)

### AI Command Namespaces (`Keywords1` for `.ai`)

- `rhooks.` (0 documented): *(see AI Scripting Reference)*
- `ai.` (77 documented): `ai.createheightmap`, `ai.readheightmapfromfile`, `ai.init`, `ai.reset`
- `aiComm.` (0 documented): *(see AI Scripting Reference)*
- `aiDebug.` (8 documented): `aidebug.textgamma`, `aidebug.draw`, `aidebug.toolpathfinding`, `aidebug.pathfindingdebugtoolvehicle`
- `aiPathfinding.` (36 documented): `aipathfinding.createmap`, `aipathfinding.activemap`, `aipathfinding.tracemap`, `aipathfinding.getmaplist`
- `aiSettings.` (60 documented): `aisettings.setmaxnbots`, `aisettings.setmaxnautocontrollers`, `aisettings.maxbotsincludehumans`, `aisettings.setignorecommanderdistance`
- `aiStrategicArea.` (63 documented): `aistrategicarea.create`, `aistrategicarea.setflankposition`, `aistrategicarea.createfromcontrolpoint`, `aistrategicarea.removeactive`
- `aiStrategy.` (43 documented): `aistrategy.createstrategy`, `aistrategy.setactivestrategy`, `aistrategy.getactivestrategyname`, `aistrategy.aggression`
- `aiTemplate.` (10 documented): `aitemplate.create`, `aitemplate.active`, `aitemplate.types`, `aitemplate.degeneration`
- `aiTemplatePlugIn.` (65 documented): `aitemplateplugin.create`, `aitemplateplugin.active`, `aitemplateplugin.vehiclenumber`, `aitemplateplugin.setpathfindingmap`
- `kitTemplate.` (0 documented): *(see AI Scripting Reference)*
- `weaponTemplate.` (27 documented): `weapontemplate.create`, `weapontemplate.active`, `weapontemplate.deviation`, `weapontemplate.deviationcorrectiontime`

### AI Behaviors, BAPST Plan Wrappers & Movement Commands (`Keywords2` for `.ai`)

`Physical`, `Cover`, `Mobile`, `Unit`, `Armament`, `ControlInfo`, `Ground`, `Road`, `Shallows`, `Deepwater`, `BBMoveTo`, `BBPGotoWaypoint3d`, `BBIdle`, `BBPIdle3d`, `BBFire3d`, `BBPFire3d`, `BBChange`, `BBPChange`, `BBPHeliFire3d`, `BBAvoid`, `BBPAvoidCollision3d`, `BBChangeLandingCraft`, `BBPAvoidCollision2d`, `BBPGotoWaypoint2d`, `BBPIdle2d`, `BBFireUnarmed`, `BBPFireDriveAttack`, `BBRunOverSoldier`, `BBPRunOverSoldier`, `BBBridgeRepair`, `BBPBridgeRepair`, `BBDefuseMines`, `BBPDefuseMines`, `BBFireInfantery`, `BBPFireInfantery`, `BBMoveToFixed`, `BBPChangeLandingCraft`, `BBPAvoidCollisionInfantery`, `BBPGotoWaypointInfantery`, `BBPIdleInfantery`, `BBMedicAssist`, `BBPMedicAssist`, `BBC4`, `BBPC4`, `BBRevive`, `BBPRevive`, `BBRandom`, `BBPRandom`, `BBTriggerable`, `BBPTriggerable`, `BBFireLargeBore`, `BBPFire2d`, `BBChangeTeleport`, `BBPChangeTeleport`, `BBPGotoWaypointBoat`, `BAPSTLookAtWrapper`, `BAPSTPlanEnd`, `BAPSTAimingWrapper`, `BAPSTMergeSoldierInputs`, `BAPSTForgetTarget`, `BAPSTRunOverObject`, `BAPSTHonkHorn`, `BAPSTOverrideSensingAgent`, `BAPSTInfoWrapper`, `BAPSTPlaceC4`, `BAPSTRevive`, `BAPSTSoldierPose`, `BAPSTPhysicsEnable`, `BAPSTParallel`, `BAPSTSerial`, `BAPSTIf`, `BAPSTWait`, `BAPSTWhile`, `BAPSTWeaponWrapper`, `BAPSTFinishedWrapper`, `BAPSTUpdateVehicle`, `BAPSTChangeWeapon`, `BAPSTICTurnLock`, `BAPSTICChangeVehicle`, `BAPSTEvaluate`, `BAPSTNotifyBot`, `BAPSTIdle`, `BAPSTSetSensingAgentFocus`, `BAPSTSendRadioMessage`, `BAPSTDebug`, `BAPSTUseFlareOnMissileLock`, `BAPSTEvaluateCondition`, `InfoWrapper`, `PlaneMoveTo`, `PlaneMoveToDirection`, `PlaneMoveToObject`, `Trigger`, `TriggerContinously`, `PlaneAimAt`, `PlaneResetControls`, `Sense`, `HeliMoveTo`, `HeliMoveAwayFromObject`, `HeliAimAt`, `HeliResetControls`, `HeliMoveToDirection`, `HeliMoveToObject`, `CarResetControls`, `MoveToMedium`, `MoveToObjectMedium`, `CarMoveTo`, `CarMoveToDirection`, `CarMoveToObject`, `MouseTurretAimAt`, `MouseTurretLookAt`, `InfanteryResetControls`, `TankMoveTo`, `TankTurnTo`, `TankMoveToDirection`, `TankMoveToObject`, `TankResetControls`, `MoveToMediumSoldier`, `MoveToObjectMediumSoldier`, `InfanteryMoveTo`, `InfanteryMoveToDirection`, `InfanteryMoveToObject`, `SoldierPose`, `BoatMoveTo`, `BoatMoveToDirection`, `BoatMoveToObject`, `BoatResetControls`, `MoveToMediumBoat`, `MoveToObjectMediumBoat`

### AI Unit Types, Armor Types, Vehicles, Kits & Inputs (`Keywords4` for `.ai`)

`ITUnit`, `ITBiological`, `ITGround`, `Fixed`, `FixedTurret`, `VCAir`, `VCHelicopter`, `VCLand`, `VCSea`, `VTBomber`, `VTFighter`, `VTDiveBomber`, `VTApc`, `VTHeavyTank`, `VTAA`, `PIMouseLookX`, `PIMouseLookY`, `PIAltFire`, `PIToggleCameraMode`, `PIYaw`, `PIThrottle`, `PIUse`, `PIFire`, `PIAltSprint`, `PISprint`, `PICrouch`, `PIFlareFire`, `PILie`, `PIRoll`, `PIPitch`, `PIPositionSelect1`, `PIPositionSelect2`, `PIPositionSelect3`, `PIPositionSelect4`, `PIPositionSelect5`, `PIPositionSelect6`, `PIWeaponSelect1`, `PIWeaponSelect2`, `PIWeaponSelect3`, `PIWeaponSelect4`, `PIWeaponSelect5`, `PICameraX`, `PICameraY`, `PINone`, `ITUnit`, `ITBiological`, `ITGround`, `ITMobile`, `ITHasWreck`, `ITStructure`, `ITSoldier`, `ITAir`, `ITCover`, `ITNaval`, `ITHasCarHorn`, `ITHelicopter`, `ITObstructedView`, `ITNoTemperature`, `Vehicle`, `Infantry`, `LightArmour`, `HeavyArmour`, `NavalArmour`, `Helicopter`, `AirPlane`, `Crouching`, `Lying`, `Standing`, `Avoid`, `MoveTo`, `Idle`, `Fire`, `Special`, `TakeCover`, `Change`, `Revive`, `c4`, `Special2`, `Special3`, `Random`, `Triggerable`, `Tank`, `Plane`, `Boat`, `SmallBoat`, `Infantery`, `Fixed`, `Car`, `Bombcar`, `LandingCraft`, `Passenger`, `LandingCraftPassenger`, `LandingCraftFixed`, `Helicopter`, `TransportHelicopter`, `ArmedCar`, `ManDown`, `ParatrooperFixed`, `FixedTurret`, `TankCommander`, `APCCommander`, `APCACommander`, `VTOLTransport`, `UnitWeights`, `Full`, `Specops`, `Sniper`, `Assault`, `Support`, `Engineer`, `Medic`, `AT`

## 6. Atlas Tokens (`.tac`, `.tai`)

- **Keywords1**: `group`
- **Keywords2**: `border`, `width`, `height`, `format`, `miplevels`
