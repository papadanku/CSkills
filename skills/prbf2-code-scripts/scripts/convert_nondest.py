#!/usr/bin/env python3
"""Convert a destroyable PR:BF2 object into a _nondest SimpleObject variant."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


CREATE_DESTROYABLE_PATTERN = re.compile(
    r"^(objecttemplate\.create\s+)DestroyableObject(\s+)(\S+)",
    re.IGNORECASE,
)
ACTIVESAFE_DESTROYABLE_PATTERN = re.compile(
    r"^(objecttemplate\.activesafe\s+)DestroyableObject(\s+)(\S+)",
    re.IGNORECASE,
)
CREATE_ANY_TEMPLATE_PATTERN = re.compile(
    r"^(objecttemplate\.create\s+\S+\s+)(\S+)",
    re.IGNORECASE,
)
ACTIVESAFE_ANY_TEMPLATE_PATTERN = re.compile(
    r"^(objecttemplate\.activesafe\s+\S+\s+)(\S+)",
    re.IGNORECASE,
)
BEGIN_COMPONENT_PATTERN = re.compile(
    r"^rem\s+---BeginComp:(\S+)\s*---",
    re.IGNORECASE,
)
END_COMPONENT_PATTERN = re.compile(
    r"^rem\s+---EndComp\s*---",
    re.IGNORECASE,
)
PRIMARY_CREATE_PATTERN = re.compile(
    r"^\s*objecttemplate\.create\s+\S+\s+(\S+)",
    re.IGNORECASE,
)

STRIP_TWEAK_PREFIXES = (
    "objecttemplate.isdestructable",
    "objecttemplate.setnetworkableinfo",
)

KEEP_ORIGINAL_NAME_PREFIXES = (
    "geometrytemplate.create",
    "collisionmanager.createtemplate",
    "objecttemplate.geometry",
    "objecttemplate.collisionmesh",
    "objecttemplate.setcollisionmesh",
)

REMOVED_DESTRUCTION_COMPONENTS = {"armor", "strategicobject"}


def starts_with_any_prefix(
    lowercase_line: str,
    prefixes: tuple[str, ...],
) -> bool:
    """Return True if lowercase_line begins with any prefix in prefixes."""
    for prefix in prefixes:
        if lowercase_line.startswith(prefix):
            return True
    return False


def convert_con_text(
    con_text: str,
    original_name: str,
    new_name: str,
) -> str:
    """Transform a .con file into a _nondest SimpleObject variant."""
    output_lines: list[str] = []

    for line in con_text.splitlines():
        stripped_line = line.strip()
        lowercase_line = stripped_line.lower()

        if starts_with_any_prefix(lowercase_line, KEEP_ORIGINAL_NAME_PREFIXES):
            output_lines.append(line)
            continue

        create_destroyable_match = CREATE_DESTROYABLE_PATTERN.match(
            stripped_line
        )
        if create_destroyable_match is not None:
            prefix = create_destroyable_match.group(1)
            whitespace = create_destroyable_match.group(2)
            output_lines.append(f"{prefix}SimpleObject{whitespace}{new_name}")
            continue

        create_any_match = CREATE_ANY_TEMPLATE_PATTERN.match(stripped_line)
        if create_any_match is not None:
            output_lines.append(f"{create_any_match.group(1)}{new_name}")
            continue

        updated_line = re.sub(
            rf"(include\s+){re.escape(original_name)}\.tweak\b",
            rf"\1{new_name}.tweak",
            line,
            flags=re.IGNORECASE,
        )
        output_lines.append(updated_line)

    return "\n".join(output_lines) + "\n"


def convert_tweak_text(tweak_text: str, new_name: str) -> str:
    """Transform a .tweak file by stripping destruction components."""
    output_lines: list[str] = []
    skip_component_block = False

    for line in tweak_text.splitlines():
        stripped_line = line.strip()
        lowercase_line = stripped_line.lower()

        begin_comp_match = BEGIN_COMPONENT_PATTERN.match(stripped_line)
        if begin_comp_match is not None:
            component_name = begin_comp_match.group(1).lower()
            if component_name in REMOVED_DESTRUCTION_COMPONENTS:
                skip_component_block = True
                continue

        if skip_component_block:
            if END_COMPONENT_PATTERN.match(stripped_line) is not None:
                skip_component_block = False
            continue

        if starts_with_any_prefix(lowercase_line, STRIP_TWEAK_PREFIXES):
            continue

        if starts_with_any_prefix(lowercase_line, KEEP_ORIGINAL_NAME_PREFIXES):
            output_lines.append(line)
            continue

        activesafe_destroyable_match = ACTIVESAFE_DESTROYABLE_PATTERN.match(
            stripped_line
        )
        if activesafe_destroyable_match is not None:
            prefix = activesafe_destroyable_match.group(1)
            whitespace = activesafe_destroyable_match.group(2)
            output_lines.append(f"{prefix}SimpleObject{whitespace}{new_name}")
            continue

        activesafe_any_match = ACTIVESAFE_ANY_TEMPLATE_PATTERN.match(
            stripped_line
        )
        if activesafe_any_match is not None:
            output_lines.append(f"{activesafe_any_match.group(1)}{new_name}")
            continue

        output_lines.append(line)

    return "\n".join(output_lines) + "\n"


def detect_template_name(con_text: str, fallback_name: str) -> str:
    """Extract the primary ObjectTemplate name from .con text."""
    for line in con_text.splitlines():
        create_match = PRIMARY_CREATE_PATTERN.match(line)
        if create_match is not None:
            return create_match.group(1)
    return fallback_name


def parse_arguments() -> argparse.Namespace:
    """Parse CLI arguments for the _nondest converter."""
    parser = argparse.ArgumentParser(
        description=(
            "Convert destroyable .con/.tweak scripts into _nondest "
            "SimpleObject variants."
        )
    )
    parser.add_argument(
        "con_file",
        type=Path,
        help="Input .con file.",
    )
    parser.add_argument(
        "--tweak",
        type=Path,
        default=None,
        help=(
            "Optional .tweak file (defaults to sibling <stem>.tweak "
            "if present)."
        ),
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Output directory (defaults to input .con directory).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print converted output without writing files.",
    )
    return parser.parse_args()


def main() -> int:
    """Entry point for converting destroyable objects to _nondest."""
    arguments = parse_arguments()

    if not arguments.con_file.is_file():
        print(f"File not found: {arguments.con_file}", file=sys.stderr)
        return 2

    con_text = arguments.con_file.read_text(
        encoding="utf-8",
        errors="replace",
    )
    original_name = detect_template_name(con_text, arguments.con_file.stem)
    new_name = f"{original_name}_nondest"

    if arguments.tweak is not None:
        tweak_path = arguments.tweak
    else:
        tweak_path = arguments.con_file.with_suffix(".tweak")

    new_con_text = convert_con_text(
        con_text=con_text,
        original_name=original_name,
        new_name=new_name,
    )

    new_tweak_text: str | None = None
    if tweak_path.is_file():
        original_tweak_text = tweak_path.read_text(
            encoding="utf-8",
            errors="replace",
        )
        new_tweak_text = convert_tweak_text(original_tweak_text, new_name)

    if arguments.out_dir is not None:
        output_directory = arguments.out_dir
    else:
        output_directory = arguments.con_file.parent

    output_con_path = output_directory / f"{new_name}.con"
    output_tweak_path = output_directory / f"{new_name}.tweak"

    if arguments.dry_run:
        print(f"=== {output_con_path} ===\n{new_con_text}")
        if new_tweak_text is not None:
            print(f"=== {output_tweak_path} ===\n{new_tweak_text}")
        return 0

    output_directory.mkdir(parents=True, exist_ok=True)
    output_con_path.write_text(new_con_text, encoding="utf-8")
    print(f"Wrote {output_con_path}")

    if new_tweak_text is not None:
        output_tweak_path.write_text(new_tweak_text, encoding="utf-8")
        print(f"Wrote {output_tweak_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
