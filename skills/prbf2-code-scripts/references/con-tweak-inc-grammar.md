
# PR:BF2 `.con`, `.tweak`, and `.inc` Grammar & Execution Model

Grounded in PR:BF2 `.con` grammar conventions, console object specifications, and live PR:BF2 game/mod archive structures (`objects_server.zip`, `objects_common_server.zip`, `objects_vehicles_server.zip`, `objects_weapons_server.zip`, `menu_server.zip`, `common_server.zip`, `server.zip`).

## 1. File Roles and Interaction

- **`.con`**
    - **Primary Role**: Definition, initialization, and execution entry point
    - **Typical Contents**: `GeometryTemplate.create` (`StaticMesh` or `BundledMesh`), `CollisionManager.createTemplate`, `NetworkableInfo.createNewInfo`, `ObjectTemplate.create`, `ObjectTemplate.saveInSeparateFile 1`, `include *.tweak`, `run *.inc`, `hudBuilder.*`, `Material.*`, `heightmap.*`
- **`.tweak`**
    - **Primary Role**: Property tuning and component configuration on an existing template
    - **Typical Contents**: `ObjectTemplate.activeSafe <Type> <Name>`, `GeometryTemplate.*` LOD/lightmap settings, `rem ---BeginComp:...---` / `ObjectTemplate.createComponent` / `rem ---EndComp---`, `ObjectTemplate.addTemplate`, `ObjectTemplate.aiTemplate`, HUD nodes (`hudBuilder.*`)
- **`.inc`**
    - **Primary Role**: Reusable script fragments included/run by `.con` or `.tweak`
    - **Typical Contents**: `animationSystem.*` / `animationManager.*` / `animationBundle.*` / `animationTrigger.*` (`animationsystem*.inc`), shared sub-template or kit/vehicle fragments

### Standard `.con` -> `.tweak` -> `.inc` Lifecycle

1. Engine loads `<object>.con` (e.g., `staticobjects/.../<name>.con`, `vehicles/.../<name>.con`, or `weapons/.../<name>.con` inside the mod's virtual archives).
2. `.con` defines geometry (`GeometryTemplate.create StaticMesh|BundledMesh <name>`), collision (`CollisionManager.createTemplate <name>`), and registers the object template (`ObjectTemplate.create <Class> <name>`).
3. `.con` sets `ObjectTemplate.saveInSeparateFile 1` and calls `include <object>.tweak`.
4. `.tweak` immediately re-selects the template with `ObjectTemplate.activeSafe <Class> <name>` so all subsequent `ObjectTemplate.*` properties apply to the intended template even if the `.tweak` is re-run standalone.
5. `.con` or `.tweak` invokes `run <fragment>.inc` (or `include ...`) for animations or reusable sub-configs.

## 2. Comments, Statements, and Types

- **Line comment**: `rem <text>` (ignored to end of line).
- **Block comment**: `beginRem` ... `endRem` (multi-line; works when parsed by the engine from files, **not** in the interactive in-game console).
- **Statement**: `Namespace.method arg1 "arg with spaces"`. Quote any string argument containing spaces.
- **Variables**:
    - Mutable: `var v_name = value`
    - Constant: `const c_name = value`
    - Return capture: `fileManager.fileExists movies/menu.bik -> v_tst`
- **Conditionals & Loops**:
    - `if <expr>` / `elseIf <expr>` / `else` / `endIf`
    - `while <expr>` / `endWhile`
    - Expressions: `<var> <op> <value>` where `<op>` is `==`, `!=`, `<`, `<=`, `>`, `>=`, `equals`, `notEquals`, combined with `AND`, `OR`, `NOT`.
    - **Editor vs Runtime Branching**: Level scripts (`init.con`, `terrain.con`) commonly use `if v_arg1 == BF2Editor` to load editable terrain/overgrowth in the editor and compiled `.raw`/collision data at runtime.

## 3. `include` vs `run` vs `return`

- **`include <path>`**
    - **Scope Behavior**: Shares caller's variable scope (`v_*`, `c_*` visible)
    - **Arguments**: None
    - **When to Use**: Loading `.tweak` files (`include <object>.tweak`) or fragments that read/set caller variables
- **`run <path> [arg1 ...]`**
    - **Scope Behavior**: Creates an **isolated** scope; caller `v_*` variables are NOT visible
    - **Arguments**: Accessible as `v_arg1`, `v_arg2`, ...
    - **When to Use**: Running parameterized `.inc` or `.con` scripts (`run Terrain.con v_arg2`, `run animationsystem1p.inc`)
- **`return`**
    - **Scope Behavior**: Exits the current script file and returns control to caller
    - **Arguments**: None
    - **When to Use**: Early exit inside `if` blocks in `run`/`include` scripts

## 4. `CRD_*` Continuous Random Distribution

Syntax: `CRD_TYPE/Number1/Number2/Symmetry`

- `CRD_NONE/N/0/0`: Always returns `N`.
- `CRD_UNIFORM/Min/Max/Sym`: Random integer in `[Min, Max]` inclusive.
- `CRD_EXPONENTIAL/Mean/0/Sym`: `-Mean * ln(random(0,1))`. **Gotcha**: `Number2` is ignored; setting `Mean = 0` (`CRD_EXPONENTIAL/0/180/1`) always returns `0`.
- `CRD_NORMAL/Mean/Variance/Sym`: Bell curve around `Mean` (~80% within `Mean +/- Variance`).
- `Symmetry` (`0` or `1`): If `1`, 50% chance to negate the resulting value.

## 5. Active Template Context & Component Blocks

- **`ObjectTemplate.create <Class> <Name>`**: Instantiates a new template and makes it active. Calling `create` on an already-existing name can cause conflicts or duplicate state.
- **`ObjectTemplate.activeSafe <Class> <Name>`**: Safely activates an existing template of `<Class>` without crashing if missing (preferred in `.tweak` files over `ObjectTemplate.active`).
- **`ObjectTemplate.active <Name>`**: Activates an existing template (less safe than `activeSafe` when type-checking matters).
- **Component Blocks**:

    ```text
    rem ---BeginComp:Armor ---
    ObjectTemplate.createComponent Armor
    ObjectTemplate.armor.maxHitPoints 1600
    ...
    rem ---EndComp ---
    ```

    Always keep `ObjectTemplate.createComponent <CompName>` inside the matching `BeginComp`/`EndComp` markers so Bf2Editor and UDL folding stay valid.
