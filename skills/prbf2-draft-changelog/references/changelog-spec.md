
# PR:BF2 Changelog Specification

## Version Header & Stacking

- **Header format**: `PR:BF2 v<X.Y.Z.W> Changelog (<YYYY/MM/DD>)` followed by a line of hyphens (`-----------------------`).
- **Hotfix stacking**: Incremental hotfix changelogs (e.g., `v1.9.0.1`) are prepended at the top of the existing major version changelog thread, above the older `v1.9.0.0` block.

## Canonical Category Order

Include only categories that have entries, in this order:

1. `General:` (factions, core gameplay rules, nametags, teamkill/scoring, tutorials, Discord RPC)
2. `COOP:` (bot AI, navmesh/pathfinding, dynamic kits, COOP server stability)
3. `Effects:` (particles, decals, materials)
4. `Menu:` (HUD, minimap/commander icons, fonts, localization, server browser, scoreboard)
5. `Soldiers:` (player models, uniforms, facial/hand textures)
6. `Statics:` (buildings, trees, lightmaps, static object collisions)
7. `Sounds:` (weapon/vehicle audio, music themes, ambient/positional sound fixes)
8. `Vehicles:` (new vehicles, sights/reticles, handling, armor, textures, cockpit/camera fixes)
9. `Weapons:` (new weapons, animations, ballistics/deviation, sights, firing sounds)
10. `Kits:` (kit loadouts, equipment swaps, kit geometries and textures)
11. `Shaders:` (shadows, lighting, terrain blending, optics blur, shader optimization)
12. `Levels:` (map-by-map changes)

## Entry Writing Rules

- **Verb-first phrasing**: Start every entry with a past-tense action verb:
    - `Added` (new content, features, layers, assets)
    - `Updated` (modified behavior, balance, sights, sounds, or rules)
    - `Improved` (visual quality, textures, FPS, LODs, collisions)
    - `Fixed` (bugs, crashes, visual glitches, typos)
    - `Removed` (deleted assets, flags, vehicles, or deprecated mechanics)
    - `Replaced` (swapped one asset/faction/vehicle for another: `Replaced X with Y.`)
    - `Reduced` / `Increased` / `Delayed` (numeric or timing adjustments)
    - `Optimized` (performance/shader/mesh improvements)
    - `Reverted` (rolled back a prior change)
- **Quantify changes**: Include concrete numbers where known (e.g., `within a 10m distance`, `from 750 to 650`, `by 100`).
- **Consistency**: End every entry with a period.

## Levels Section Formatting

- Start with `General:` for new map additions (`Added <Map> <Size> <Modes>.`), removals, and global level updates.
- List individual maps in **alphabetical order**.
- Within each map, prefix entries by scope when applicable:
    - `General:` (applies to all layers)
    - `AAS:` / `AAS16:` / `AAS32:` / `AAS64:` / `AAS128:` (or combined `AAS32 & AAS64:`)
    - `INS:` / `INS32:` / `INS64:` / `INS128:`
    - `COOP:` / `COOP16:` / `COOP32:` / `COOP64:` / `COOP128:`
    - `SKIRMISH:` / `SKIRM128:` / `CNC64:` / `VW:` / `GUNGAME:`
