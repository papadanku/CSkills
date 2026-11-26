
# PR:BF2 `.con`, `.tweak`, and `.inc` File Roles & Lifecycle

Grounded in PR:BF2 `.con` grammar conventions, object properties, and live PR:BF2 game/mod archive structures (`objects_server.zip`, `objects_common_server.zip`, `objects_vehicles_server.zip`, `objects_weapons_server.zip`, `menu_server.zip`, `common_server.zip`, `server.zip`).

## File Roles

- **`.con`**
    - **Primary Role**: Definition, initialization, and execution entry point
    - **Typical Contents**: `GeometryTemplate.create` (`StaticMesh` or `BundledMesh`), `CollisionManager.createTemplate`, `NetworkableInfo.createNewInfo`, `ObjectTemplate.create`, `ObjectTemplate.saveInSeparateFile 1`, `include *.tweak`, `run *.inc`, `hudBuilder.*`, `Material.*`, `heightmap.*`
- **`.tweak`**
    - **Primary Role**: Property tuning and component configuration on an existing template
    - **Typical Contents**: `ObjectTemplate.activeSafe <Type> <Name>`, `GeometryTemplate.*` LOD/lightmap settings, `rem ---BeginComp:...---` / `ObjectTemplate.createComponent` / `rem ---EndComp---`, `ObjectTemplate.addTemplate`, `ObjectTemplate.aiTemplate`, HUD nodes (`hudBuilder.*`)
- **`.inc`**
    - **Primary Role**: Reusable script fragments included/run by `.con` or `.tweak`
    - **Typical Contents**: `animationSystem.*` / `animationManager.*` / `animationBundle.*` / `animationTrigger.*` (`animationsystem*.inc`), shared sub-template or kit/vehicle fragments

## Standard `.con` -> `.tweak` -> `.inc` Lifecycle

1. Engine loads `<object>.con` (e.g., `staticobjects/.../<name>.con`, `vehicles/.../<name>.con`, or `weapons/.../<name>.con` inside the mod's virtual archives).
2. `.con` defines geometry (`GeometryTemplate.create StaticMesh|BundledMesh <name>`), collision (`CollisionManager.createTemplate <name>`), and registers the object template (`ObjectTemplate.create <Class> <name>`).
3. `.con` sets `ObjectTemplate.saveInSeparateFile 1` and calls `include <object>.tweak`.
4. `.tweak` immediately re-selects the template with `ObjectTemplate.activeSafe <Class> <name>` so all subsequent `ObjectTemplate.*` properties apply to the intended template even if the `.tweak` is re-run standalone.
5. `.con` or `.tweak` invokes `run <fragment>.inc` (or `include ...`) for animations or reusable sub-configs.
