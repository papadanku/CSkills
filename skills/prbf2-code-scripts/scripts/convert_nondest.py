#!/usr/bin/env python3
"""Convert a destroyable PR:BF2 object (.con/.tweak) into a non-destroyable (_nondest) variant."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CREATE_DEST_RE = re.compile(
    r"^(objecttemplate\.create\s+)DestroyableObject(\s+)(\S+)", re.IGNORECASE
)
ACTIVESAFE_DEST_RE = re.compile(
    r"^(objecttemplate\.activesafe\s+)DestroyableObject(\s+)(\S+)", re.IGNORECASE
)
CREATE_ANY_RE = re.compile(
    r"^(objecttemplate\.create\s+\S+\s+)(\S+)", re.IGNORECASE
)
ACTIVESAFE_ANY_RE = re.compile(
    r"^(objecttemplate\.activesafe\s+\S+\s+)(\S+)", re.IGNORECASE
)
BEGIN_COMP_RE = re.compile(r"^rem\s+---BeginComp:(\S+)\s*---", re.IGNORECASE)
END_COMP_RE = re.compile(r"^rem\s+---EndComp\s*---", re.IGNORECASE)

STRIP_PREFIXES = (
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


def convert_con_text(text: str, orig_name: str, new_name: str) -> str:
    """Transform a .con file for _nondest."""
    out_lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        lower = stripped.lower()

        if any(lower.startswith(p) for p in KEEP_ORIGINAL_NAME_PREFIXES):
            out_lines.append(line)
            continue

        if m := CREATE_DEST_RE.match(stripped):
            out_lines.append(f"{m.group(1)}SimpleObject{m.group(2)}{new_name}")
            continue

        if m := CREATE_ANY_RE.match(stripped):
            out_lines.append(f"{m.group(1)}{new_name}")
            continue

        updated = re.sub(
            rf"(include\s+){re.escape(orig_name)}\.tweak\b",
            rf"\1{new_name}.tweak",
            line,
            flags=re.IGNORECASE,
        )
        out_lines.append(updated)

    return "\n".join(out_lines) + "\n"


def convert_tweak_text(text: str, new_name: str) -> str:
    """Transform a .tweak file for _nondest by stripping Armor/StrategicObject and destructible flags."""
    out_lines: list[str] = []
    skip_comp = False

    for line in text.splitlines():
        stripped = line.strip()
        lower = stripped.lower()

        if m := BEGIN_COMP_RE.match(stripped):
            comp = m.group(1).lower()
            if comp in {"armor", "strategicobject"}:
                skip_comp = True
                continue

        if skip_comp:
            if END_COMP_RE.match(stripped):
                skip_comp = False
            continue

        if any(lower.startswith(p) for p in STRIP_PREFIXES):
            continue

        if any(lower.startswith(p) for p in KEEP_ORIGINAL_NAME_PREFIXES):
            out_lines.append(line)
            continue

        if m := ACTIVESAFE_DEST_RE.match(stripped):
            out_lines.append(f"{m.group(1)}SimpleObject{m.group(2)}{new_name}")
            continue

        if m := ACTIVESAFE_ANY_RE.match(stripped):
            out_lines.append(f"{m.group(1)}{new_name}")
            continue

        out_lines.append(line)

    return "\n".join(out_lines) + "\n"


def detect_template_name(con_text: str, fallback: str) -> str:
    """Extract primary ObjectTemplate name from .con text."""
    for line in con_text.splitlines():
        if m := re.match(r"^\s*objecttemplate\.create\s+\S+\s+(\S+)", line, re.IGNORECASE):
            return m.group(1)
    return fallback


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert destroyable .con/.tweak scripts into _nondest SimpleObject variants."
    )
    parser.add_argument("con_file", type=Path, help="Input .con file.")
    parser.add_argument(
        "--tweak",
        type=Path,
        default=None,
        help="Optional .tweak file (defaults to sibling <stem>.tweak if present).",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Output directory (defaults to input .con directory).",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Print converted output without writing files."
    )
    args = parser.parse_args()

    if not args.con_file.is_file():
        print(f"File not found: {args.con_file}", file=sys.stderr)
        return 2

    con_text = args.con_file.read_text(encoding="utf-8", errors="replace")
    orig_name = detect_template_name(con_text, args.con_file.stem)
    new_name = f"{orig_name}_nondest"

    tweak_path = args.tweak or args.con_file.with_suffix(".tweak")
    has_tweak = tweak_path.is_file()

    new_con_text = convert_con_text(con_text, orig_name, new_name)
    new_tweak_text = (
        convert_tweak_text(
            tweak_path.read_text(encoding="utf-8", errors="replace"), new_name
        )
        if has_tweak
        else None
    )

    out_dir = args.out_dir or args.con_file.parent
    out_con = out_dir / f"{new_name}.con"
    out_tweak = out_dir / f"{new_name}.tweak"

    if args.dry_run:
        print(f"=== {out_con} ===\n{new_con_text}")
        if new_tweak_text is not None:
            print(f"=== {out_tweak} ===\n{new_tweak_text}")
        return 0

    out_dir.mkdir(parents=True, exist_ok=True)
    out_con.write_text(new_con_text, encoding="utf-8")
    print(f"Wrote {out_con}")

    if new_tweak_text is not None:
        out_tweak.write_text(new_tweak_text, encoding="utf-8")
        print(f"Wrote {out_tweak}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
