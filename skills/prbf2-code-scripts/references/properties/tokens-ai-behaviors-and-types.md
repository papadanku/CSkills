
# PR:BF2 AI Behaviors, BAPST Wrappers & Unit/Armor Types (`.ai`)

## AI Behaviors, BAPST Plan Wrappers & Movement Properties (`Keywords2` for `.ai`)

- **Plugin & Surface Types**:

    `Physical`, `Cover`, `Mobile`, `Unit`, `Armament`, `ControlInfo`, `Ground`, `Road`, `Shallows`, `Deepwater`

- **Behavior Blocks (`BB*` / `BBP*`)**:

    `BBMoveTo`, `BBPGotoWaypoint3d`, `BBIdle`, `BBPIdle3d`, `BBFire3d`, `BBPFire3d`, `BBChange`, `BBPChange`, `BBPHeliFire3d`, `BBAvoid`, `BBPAvoidCollision3d`, `BBChangeLandingCraft`, `BBPAvoidCollision2d`, `BBPGotoWaypoint2d`, `BBPIdle2d`, `BBFireUnarmed`, `BBPFireDriveAttack`, `BBRunOverSoldier`, `BBPRunOverSoldier`, `BBBridgeRepair`, `BBPBridgeRepair`, `BBDefuseMines`, `BBPDefuseMines`, `BBFireInfantery`, `BBPFireInfantery`, `BBMoveToFixed`, `BBPChangeLandingCraft`, `BBPAvoidCollisionInfantery`, `BBPGotoWaypointInfantery`, `BBPIdleInfantery`, `BBMedicAssist`, `BBPMedicAssist`, `BBC4`, `BBPC4`, `BBRevive`, `BBPRevive`, `BBRandom`, `BBPRandom`, `BBTriggerable`, `BBPTriggerable`, `BBFireLargeBore`, `BBPFire2d`, `BBChangeTeleport`, `BBPChangeTeleport`, `BBPGotoWaypointBoat`

- **BAPST Plan Wrappers**:

    `BAPSTLookAtWrapper`, `BAPSTPlanEnd`, `BAPSTAimingWrapper`, `BAPSTMergeSoldierInputs`, `BAPSTForgetTarget`, `BAPSTRunOverObject`, `BAPSTHonkHorn`, `BAPSTOverrideSensingAgent`, `BAPSTInfoWrapper`, `BAPSTPlaceC4`, `BAPSTRevive`, `BAPSTSoldierPose`, `BAPSTPhysicsEnable`, `BAPSTParallel`, `BAPSTSerial`, `BAPSTIf`, `BAPSTWait`, `BAPSTWhile`, `BAPSTWeaponWrapper`, `BAPSTFinishedWrapper`, `BAPSTUpdateVehicle`, `BAPSTChangeWeapon`, `BAPSTICTurnLock`, `BAPSTICChangeVehicle`, `BAPSTEvaluate`, `BAPSTNotifyBot`, `BAPSTIdle`, `BAPSTSetSensingAgentFocus`, `BAPSTSendRadioMessage`, `BAPSTDebug`, `BAPSTUseFlareOnMissileLock`, `BAPSTEvaluateCondition`, `InfoWrapper`

- **Movement & Control Properties**:

    `PlaneMoveTo`, `PlaneMoveToDirection`, `PlaneMoveToObject`, `Trigger`, `TriggerContinously`, `PlaneAimAt`, `PlaneResetControls`, `Sense`, `HeliMoveTo`, `HeliMoveAwayFromObject`, `HeliAimAt`, `HeliResetControls`, `HeliMoveToDirection`, `HeliMoveToObject`, `CarResetControls`, `MoveToMedium`, `MoveToObjectMedium`, `CarMoveTo`, `CarMoveToDirection`, `CarMoveToObject`, `MouseTurretAimAt`, `MouseTurretLookAt`, `InfanteryResetControls`, `TankMoveTo`, `TankTurnTo`, `TankMoveToDirection`, `TankMoveToObject`, `TankResetControls`, `MoveToMediumSoldier`, `MoveToObjectMediumSoldier`, `InfanteryMoveTo`, `InfanteryMoveToDirection`, `InfanteryMoveToObject`, `SoldierPose`, `BoatMoveTo`, `BoatMoveToDirection`, `BoatMoveToObject`, `BoatResetControls`, `MoveToMediumBoat`, `MoveToObjectMediumBoat`

## AI Unit Types, Armor Types, Vehicles, Kits & Inputs (`Keywords4` for `.ai`)

- **`IT*` Flags**:

    `ITUnit`, `ITBiological`, `ITGround`, `ITMobile`, `ITHasWreck`, `ITStructure`, `ITSoldier`, `ITAir`, `ITCover`, `ITNaval`, `ITHasCarHorn`, `ITHelicopter`, `ITObstructedView`, `ITNoTemperature`
- **Vehicle Categories & Types (`VC*`, `VT*`, `Fixed*`)**:

    `Fixed`, `FixedTurret`, `VCAir`, `VCHelicopter`, `VCLand`, `VCSea`, `VTBomber`, `VTFighter`, `VTDiveBomber`, `VTApc`, `VTHeavyTank`, `VTAA`
- **Player Inputs (`PI*`)**:

    `PIMouseLookX`, `PIMouseLookY`, `PIAltFire`, `PIToggleCameraMode`, `PIYaw`, `PIThrottle`, `PIUse`, `PIFire`, `PIAltSprint`, `PISprint`, `PICrouch`, `PIFlareFire`, `PILie`, `PIRoll`, `PIPitch`, `PIPositionSelect1`, `PIPositionSelect2`, `PIPositionSelect3`, `PIPositionSelect4`, `PIPositionSelect5`, `PIPositionSelect6`, `PIWeaponSelect1`, `PIWeaponSelect2`, `PIWeaponSelect3`, `PIWeaponSelect4`, `PIWeaponSelect5`, `PICameraX`, `PICameraY`, `PINone`
- **Armor, Pose, Behavior States, Vehicles & Kits**:

    `Vehicle`, `Infantry`, `LightArmour`, `HeavyArmour`, `NavalArmour`, `Helicopter`, `AirPlane`, `Crouching`, `Lying`, `Standing`, `Avoid`, `MoveTo`, `Idle`, `Fire`, `Special`, `TakeCover`, `Change`, `Revive`, `c4`, `Special2`, `Special3`, `Random`, `Triggerable`, `Tank`, `Plane`, `Boat`, `SmallBoat`, `Infantery`, `Car`, `Bombcar`, `LandingCraft`, `Passenger`, `LandingCraftPassenger`, `LandingCraftFixed`, `TransportHelicopter`, `ArmedCar`, `ManDown`, `ParatrooperFixed`, `TankCommander`, `APCCommander`, `APCACommander`, `VTOLTransport`, `UnitWeights`, `Full`, `Specops`, `Sniper`, `Assault`, `Support`, `Engineer`, `Medic`, `AT`
