#!/usr/bin/env python3
"""Generate a _bf2 one-man co-op vehicle variant (.con/.tweak) from a multi-crew vehicle."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REMOVE_CON_PREFIXES = (
    "geometrytemplate.create",
    "collisionmanager.createtemplate",
)
PATH_REPOINT_PREFIXES = (
    "objecttemplate.geometry",
    "objecttemplate.collisionmesh",
    "objecttemplate.setcollisionmesh",
)
SOUND_FILE_RE = re.compile(
    r'^(objecttemplate\.sound\.soundfilename\s+"?)([^"\s]+)("?)', re.IGNORECASE
)
RUN_INC_RE = re.compile(r"^(run\s+)([^\s]+\.inc)(.*)$", re.IGNORECASE)
CREATE_PCO_RE = re.compile(
    r"^objecttemplate\.create\s+PlayerControlObject\s+(\S+)", re.IGNORECASE
)
CREATE_RB_RE = re.compile(
    r"^objecttemplate\.create\s+RotationalBundle\s+(\S+)", re.IGNORECASE
)


def repoint_relative(value: str, orig_folder: str) -> str:
    """Repoint a local relative asset path back to ../<orig_folder>/."""
    norm = value.replace("\\", "/")
    if "/" not in norm and not norm.startswith(".."):
        return f"../{orig_folder}/{norm}"
    return value


def convert_con_for_bf2(con_text: str, orig_name: str, bf2_name: str) -> tuple[str, list[str]]:
    """Transform vehicle .con into _bf2.con and collect turret/sub-PCO names."""
    out_lines: list[str] = []
    turret_candidates: list[str] = []

    for line in con_text.splitlines():
        stripped = line.strip()
        lower = stripped.lower()

        if any(lower.startswith(p) for p in REMOVE_CON_PREFIXES):
            continue

        if m := CREATE_PCO_RE.match(stripped):
            pco = m.group(1)
            if pco.lower() == orig_name.lower():
                out_lines.append(
                    re.sub(
                        re.escape(pco),
                        bf2_name,
                        line,
                        count=1,
                    )
                )
            else:
                turret_candidates.append(pco)
                out_lines.append(line)
            continue

        if m := CREATE_RB_RE.match(stripped):
            rb = m.group(1)
            if "turret" in rb.lower() or "gun" in rb.lower():
                turret_candidates.append(rb)

        if any(lower.startswith(p) for p in PATH_REPOINT_PREFIXES):
            parts = stripped.split(maxsplit=1)
            if len(parts) == 2 and parts[1].lower() == orig_name.lower():
                out_lines.append(line)
                continue

        if m := SOUND_FILE_RE.match(stripped):
            new_path = repoint_relative(m.group(2), orig_name)
            out_lines.append(f"{m.group(1)}{new_path}{m.group(3)}")
            continue

        if m := RUN_INC_RE.match(stripped):
            new_inc = repoint_relative(m.group(2), orig_name)
            out_lines.append(f"{m.group(1)}{new_inc}{m.group(3)}")
            continue

        updated = re.sub(
            rf"(include\s+){re.escape(orig_name)}\.tweak\b",
            rf"\1{bf2_name}.tweak",
            line,
            flags=re.IGNORECASE,
        )
        out_lines.append(updated)

    return "\n".join(out_lines) + "\n", turret_candidates


def convert_tweak_for_bf2(
    tweak_text: str, orig_name: str, bf2_name: str, turret_candidates: list[str]
) -> str:
    """Transform vehicle .tweak into _bf2.tweak with guidance for merging gunner turrets."""
    out_lines: list[str] = []
    replaced_root = False

    for line in tweak_text.splitlines():
        stripped = line.strip()
        if not replaced_root and re.match(
            rf"^objecttemplate\.activesafe\s+PlayerControlObject\s+{re.escape(orig_name)}\b",
            stripped,
            re.IGNORECASE,
        ):
            out_lines.append(f"ObjectTemplate.activeSafe PlayerControlObject {bf2_name}")
            if turret_candidates:
                out_lines.append(
                    "rem --- TODO(_bf2): Verify merged gunner turret(s) for single-bot control ---"
                )
                for turret in turret_candidates:
                    out_lines.append(f"rem ObjectTemplate.addTemplate {turret}")
            replaced_root = True
            continue

        if m := SOUND_FILE_RE.match(stripped):
            new_path = repoint_relative(m.group(2), orig_name)
            out_lines.append(f"{m.group(1)}{new_path}{m.group(3)}")
            continue

        out_lines.append(line)

    return "\n".join(out_lines) + "\n"


def detect_root_pco(con_text: str, fallback: str) -> str:
    """Find the first PlayerControlObject name in the .con file."""
    for line in con_text.splitlines():
        if m := CREATE_PCO_RE.match(line.strip()):
            return m.group(1)
    return fallback


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert a multi-crew vehicle .con/.tweak into a _bf2 one-man co-op variant."
    )
    parser.add_argument("con_file", type=Path, help="Input vehicle .con file.")
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
        help="Output directory (defaults to <parent>_bf2 sibling directory).",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Print converted files without writing."
    )
    args = parser.parse_args()

    if not args.con_file.is_file():
        print(f"File not found: {args.con_file}", file=sys.stderr)
        return 2

    con_text = args.con_file.read_text(encoding="utf-8", errors="replace")
    orig_name = detect_root_pco(con_text, args.con_file.stem)
    bf2_name = f"{orig_name}_bf2"

    new_con_text, turrets = convert_con_for_bf2(con_text, orig_name, bf2_name)

    tweak_path = args.tweak or args.con_file.with_suffix(".tweak")
    new_tweak_text = (
        convert_tweak_for_bf2(
            tweak_path.read_text(encoding="utf-8", errors="replace"),
            orig_name,
            bf2_name,
            turrets,
        )
        if tweak_path.is_file()
        else None
    )

    out_dir = args.out_dir or (args.con_file.parent.parent / f"{args.con_file.parent.name}_bf2")
    out_con = out_dir / f"{bf2_name}.con"
    out_tweak = out_dir / f"{bf2_name}.tweak"

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

    if turrets:
        print(f"Turret/sub-PCO candidates detected for driver merge: {', '.join(turrets)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
