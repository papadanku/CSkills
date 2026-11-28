
# PR:BF2 `CRD_*` Distributions, Active Template Context & Component Blocks

## `CRD_*` Continuous Random Distribution

Syntax: `CRD_TYPE/Number1/Number2/Symmetry` (4-part Continuous Random Distribution)

- **`CRD_NONE/N/0/0`**: Always returns `N`.
- **`CRD_UNIFORM/Min/Max/Sym`**: Random integer in `[Min, Max]` inclusive.
- **`CRD_EXPONENTIAL/Mean/0/Sym`**: `-Mean * ln(random(0,1))`. **Gotcha**: `Number2` is ignored; setting `Mean = 0` (`CRD_EXPONENTIAL/0/180/1`) always returns `0`.
- **`CRD_NORMAL/Mean/Variance/Sym`**: Bell curve around `Mean` (~80% within `Mean +/- Variance`).
- **`Symmetry` (`0` or `1`)**: If `1`, 50% chance to negate the resulting value.

## Active Template Context (`create` / `activeSafe` / `active`)

- **`ObjectTemplate.create <Class> <Name>`**: Instantiates a new template and makes it active. Calling `create` on an already-existing name can cause conflicts or duplicate state.
- **`ObjectTemplate.activeSafe <Class> <Name>`**: Safely activates an existing template of `<Class>` without crashing if missing (preferred in `.tweak` files over `ObjectTemplate.active`).
- **`ObjectTemplate.active <Name>`**: Activates an existing template (less safe than `activeSafe` when type-checking matters).

## Component Blocks

```text
rem ---BeginComp:Armor ---
ObjectTemplate.createComponent Armor
ObjectTemplate.armor.maxHitPoints 1600
...
rem ---EndComp ---
```

Always keep `ObjectTemplate.createComponent <CompName>` inside the matching `BeginComp`/`EndComp` markers so Bf2Editor and UDL folding stay valid.
