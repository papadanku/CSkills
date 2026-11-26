
# PR:BF2 Syntax, Variables, Control Flow & `include` vs `run` Scoping

## Comments, Statements, and Path Separators

- **Line comment**: `rem <text>` - Single-line comment; everything after `rem` is ignored to end of line.
- **Block comment**: `beginRem` ... `endRem` - Multi-line comment; only supported when parsed/executed by the engine from files, **not** in the interactive in-game console.
- **Atlas comment**: `#` - Used in `.tac` / `.tai` atlas files.
- **Statement**: `Namespace.method arg1 "arg with spaces"`. Quote any string argument containing spaces.
- **Path / CRD separators**: `/` and `\` - `/` used in `CRD_*` and script paths; `\` often used in HUD/icon paths.

## Variables & Return Capture

- **Mutable variable**: `var v_name = value` (`v_` Hungarian-style prefix)
- **Constant**: `const c_name = value` (`c_` Hungarian-style prefix)
- **Return capture**: `-> v_result` - Captures command return value into a variable, e.g. `fileManager.fileExists movies/menu.bik -> v_tst`

## Conditionals & Loops

- **Control flow blocks**:
    - `if <expr>` / `elseIf <expr>` / `else` / `endIf`
    - `while <expr>` / `endWhile`
- **Expressions**: `<var> <op> <value>`
- **Comparison operators**: `==`, `!=`, `<`, `<=`, `>`, `>=`, `EQUAL`, `equals`, `notEquals` - Used in `if` / `while` expressions.
- **Logical operators**: `AND`, `OR`, `NOT` - Boolean combinators in expressions.
- **Editor vs Runtime Branching**: Level scripts (`init.con`, `terrain.con`) commonly use `if v_arg1 == BF2Editor` to load editable terrain/overgrowth in the editor and compiled `.raw`/collision data at runtime.

## `include` vs `run` vs `return`

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
