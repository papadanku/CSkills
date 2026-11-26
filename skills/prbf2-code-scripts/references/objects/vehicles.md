
# PR:BF2 Vehicles (`objects_vehicles_server.zip`)

- **Root Template**: `ObjectTemplate.create PlayerControlObject <vehName>` with `GeometryTemplate.create BundledMesh <vehName>`, `CollisionManager.createTemplate <vehName>`, `ObjectTemplate.hasMobilePhysics 1`, and `ObjectTemplate.setNetworkableInfo BasicInfo`.
- **Hierarchy & Sub-Templates**:
    - `RotationalBundle`: Wheels/drivetrains, steering, turrets, control surfaces (ailerons, elevators, rudders), rotors, landing gear.
    - `Bundle` / `Engine` / `Spring` / `Rotor` / `Wing`: Propulsion, suspension, and aerodynamics.
    - `EntryPoint`: Crew/passenger entry positions (`ObjectTemplate.setEntryRadius`, `setPosition`).
    - `Camera`: Pilot, driver, gunner, and commander cameras (`ObjectTemplate.worldFOV`, `insideFOV`, `CVMChase`, `CVMInside`).
    - `GenericFireArm`: Coaxial/turret/pylon weapons (`ObjectTemplate.addTemplate <weaponName>`).
- **Components**: `Armor`, `VehicleHud` (`guiIndex` linking to `hud/hudsetup/vehicles/...`), `AbilityHud`, `WarningHud`.
- **Co-Op Variants**: `_bf2` one-man variants reuse parent meshes/sounds/animations via relative paths and merge gunner turrets into the driver PCO.
