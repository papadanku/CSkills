#!/usr/bin/env python3
"""Scaffold PR:BF2 .con, .tweak, .inc, and .ai files from assets/."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


SKILL_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = SKILL_ROOT / "assets"

TEMPLATE_MAPPINGS: dict[str, list[tuple[str, str]]] = {
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


def render_template_content(
    raw_content: str,
    template_kind: str,
    template_name: str,
    gui_index: int | None,
    ai_template_name: str | None,
) -> str:
    """Substitute example identifiers in a bundled asset template."""
    rendered_text = raw_content

    if template_kind == "static":
        rendered_text = rendered_text.replace(
            "pr_building_example",
            template_name,
        )
        rendered_text = rendered_text.replace(
            "pr_destructible_example",
            template_name,
        )
    elif template_kind == "vehicle":
        rendered_text = rendered_text.replace(
            "pr_vehicle_example",
            template_name,
        )
        if ai_template_name is not None:
            rendered_text = rendered_text.replace(
                "pr_apc_example_ai",
                ai_template_name,
            )
    elif template_kind == "weapon":
        rendered_text = rendered_text.replace(
            "pr_rifle_example",
            template_name,
        )
        if ai_template_name is not None:
            rendered_text = rendered_text.replace(
                f"{template_name}_ai",
                ai_template_name,
            )
    elif template_kind == "animation1p":
        rendered_text = rendered_text.replace(
            "pr_rifle_example",
            template_name,
        )
    elif template_kind == "hud-material":
        rendered_text = rendered_text.replace(
            "ExampleVehicleHud",
            template_name,
        )
        rendered_text = rendered_text.replace(
            "S_Impact_Example",
            f"S_Impact_{template_name}",
        )
    elif template_kind == "ai":
        rendered_text = rendered_text.replace(
            "pr_rifle_example_ai",
            f"{template_name}_weapon_ai",
        )
        rendered_text = rendered_text.replace(
            "pr_apc_example",
            template_name,
        )

    if gui_index is not None:
        rendered_text = rendered_text.replace("45100", str(gui_index))
        rendered_text = rendered_text.replace(
            "guiIndex 100",
            f"guiIndex {gui_index}",
        )

    return rendered_text


def print_available_templates() -> None:
    """Print each template kind and its generated output filenames."""
    for template_kind, file_pairs in TEMPLATE_MAPPINGS.items():
        destination_names = [
            dest_pattern for _, dest_pattern in file_pairs
        ]
        formatted_destinations = ", ".join(destination_names)
        print(f"  {template_kind:14s} -> {formatted_destinations}")


def parse_arguments() -> tuple[argparse.ArgumentParser, argparse.Namespace]:
    """Build parser and parse CLI arguments for template scaffolding."""
    parser = argparse.ArgumentParser(
        description=(
            "Scaffold PR:BF2 scripts from bundled assets/ templates."
        )
    )
    parser.add_argument(
        "kind",
        nargs="?",
        choices=sorted(TEMPLATE_MAPPINGS.keys()),
        help="Template kind to scaffold.",
    )
    parser.add_argument(
        "name",
        nargs="?",
        help="Primary template or object name.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("."),
        help="Output directory (defaults to current directory).",
    )
    parser.add_argument(
        "--gui-index",
        type=int,
        default=None,
        help="Override GuiIndex.",
    )
    parser.add_argument(
        "--ai-name",
        type=str,
        default=None,
        help="Override aiTemplate name.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available template kinds and exit.",
    )
    return parser, parser.parse_args()


def main() -> int:
    """Entry point for scaffolding PR:BF2 script files."""
    parser, arguments = parse_arguments()

    if arguments.list:
        print_available_templates()
        return 0

    if not arguments.kind or not arguments.name:
        parser.error(
            "Both `kind` and `name` are required unless --list is passed."
        )

    arguments.out_dir.mkdir(parents=True, exist_ok=True)
    for source_filename, destination_pattern in TEMPLATE_MAPPINGS[
        arguments.kind
    ]:
        source_path = ASSETS_DIR / source_filename
        if not source_path.is_file():
            print(
                f"Missing bundled asset: {source_path}",
                file=sys.stderr,
            )
            return 2

        raw_content = source_path.read_text(
            encoding="utf-8",
            errors="replace",
        )
        rendered_content = render_template_content(
            raw_content=raw_content,
            template_kind=arguments.kind,
            template_name=arguments.name,
            gui_index=arguments.gui_index,
            ai_template_name=arguments.ai_name,
        )
        destination_filename = destination_pattern.format(name=arguments.name)
        destination_path = arguments.out_dir / destination_filename
        destination_path.write_text(rendered_content, encoding="utf-8")
        print(f"Wrote {destination_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
