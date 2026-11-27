#!/usr/bin/env python3
"""Scaffold PR:BF2 .con, .tweak, .inc, and .ai files from the bundled assets/ templates."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = SKILL_ROOT / "assets"

TEMPLATES: dict[str, list[tuple[str, str]]] = {
    "static": [
        ("static-destructible.con.txt", "{name}.con"),
        ("static-destructible.tweak.txt", "{name}.tweak"),
    ],
    "vehicle": [
        ("vehicle-pco.con.txt", "{name}.con"),
        ("vehicle-pco.tweak.txt", "{name}.tweak"),
    ],
    "weapon": [
        ("weapon-template.con.txt", "{name}.con"),
        ("weapon-template.tweak.txt", "{name}.tweak"),
    ],
    "animation1p": [
        ("animationsystem1p.inc.txt", "animationsystem1p.inc"),
    ],
    "hud-material": [
        ("hud-and-material.con.txt", "{name}.con"),
    ],
    "ai": [
        ("weapon-and-vehicle.ai.txt", "{name}.ai"),
    ],
}


def render_content(
    raw: str,
    kind: str,
    name: str,
    gui_index: int | None,
    ai_name: str | None,
) -> str:
    """Substitute example identifiers in an asset template."""
    text = raw
    if kind == "static":
        text = text.replace("pr_building_example", name).replace(
            "pr_destructible_example", name
        )
    elif kind == "vehicle":
        text = text.replace("pr_vehicle_example", name)
        if ai_name:
            text = text.replace("pr_apc_example_ai", ai_name)
    elif kind == "weapon":
        text = text.replace("pr_rifle_example", name)
        if ai_name:
            text = text.replace(f"{name}_ai", ai_name)
    elif kind == "animation1p":
        text = text.replace("pr_rifle_example", name)
    elif kind == "hud-material":
        text = text.replace("ExampleVehicleHud", name).replace(
            "S_Impact_Example", f"S_Impact_{name}"
        )
    elif kind == "ai":
        text = text.replace("pr_rifle_example_ai", f"{name}_weapon_ai").replace(
            "pr_apc_example", name
        )

    if gui_index is not None:
        text = text.replace("45100", str(gui_index)).replace(
            "guiIndex 100", f"guiIndex {gui_index}"
        )

    return text


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scaffold PR:BF2 scripts from bundled assets/ templates."
    )
    parser.add_argument(
        "kind",
        nargs="?",
        choices=sorted(TEMPLATES.keys()),
        help="Template kind to scaffold.",
    )
    parser.add_argument("name", nargs="?", help="Primary template/object name.")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("."),
        help="Output directory (defaults to current directory).",
    )
    parser.add_argument("--gui-index", type=int, default=None, help="Override GuiIndex.")
    parser.add_argument("--ai-name", type=str, default=None, help="Override aiTemplate name.")
    parser.add_argument(
        "--list", action="store_true", help="List available template kinds and exit."
    )
    args = parser.parse_args()

    if args.list:
        for k, files in TEMPLATES.items():
            out_names = ", ".join(dest for _, dest in files)
            print(f"  {k:14s} -> {out_names}")
        return 0

    if not args.kind or not args.name:
        parser.error("Both `kind` and `name` are required unless --list is passed.")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for src_name, dest_pattern in TEMPLATES[args.kind]:
        src_path = ASSETS_DIR / src_name
        if not src_path.is_file():
            print(f"Missing bundled asset: {src_path}", file=sys.stderr)
            return 2

        raw = src_path.read_text(encoding="utf-8", errors="replace")
        rendered = render_content(raw, args.kind, args.name, args.gui_index, args.ai_name)
        dest_path = args.out_dir / dest_pattern.format(name=args.name)
        dest_path.write_text(rendered, encoding="utf-8")
        print(f"Wrote {dest_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
