#!/usr/bin/env python3
"""Generate a _bf2 one-man co-op vehicle variant from a multi-crew vehicle."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


REMOVE_CON_PREFIXES = (
    "geometrytemplate.create",
    "collisionmanager.createtemplate",
)

PATH_REPOINT_PREFIXES = (
    "objecttemplate.geometry",
    "objecttemplate.collisionmesh",
    "objecttemplate.setcollisionmesh",
)

SOUND_FILE_PATTERN = re.compile(
    r'^(objecttemplate\.sound\.soundfilename\s+"?)([^"\s]+)("?)',
    re.IGNORECASE,
)
RUN_INCLUDE_PATTERN = re.compile(
    r"^(run\s+)([^\s]+\.inc)(.*)$",
    re.IGNORECASE,
)
CREATE_PCO_PATTERN = re.compile(
    r"^objecttemplate\.create\s+PlayerControlObject\s+(\S+)",
    re.IGNORECASE,
)
CREATE_RB_PATTERN = re.compile(
    r"^objecttemplate\.create\s+RotationalBundle\s+(\S+)",
    re.IGNORECASE,
)


def repoint_relative_path(asset_value: str, original_folder: str) -> str:
    """Repoint a local relative asset path back to ../<original_folder>/."""
    normalized_value = asset_value.replace("\\", "/")
    if "/" not in normalized_value and not normalized_value.startswith(".."):
        return f"../{original_folder}/{normalized_value}"
    return asset_value


def starts_with_any_prefix(
    lowercase_line: str,
    prefixes: tuple[str, ...],
) -> bool:
    """Return True if lowercase_line begins with any prefix in prefixes."""
    for prefix in prefixes:
        if lowercase_line.startswith(prefix):
            return True
    return False


def convert_con_for_bf2(
    con_text: str,
    original_name: str,
    bf2_name: str,
) -> tuple[str, list[str]]:
    """Transform vehicle .con into _bf2.con and collect turret names."""
    output_lines: list[str] = []
    turret_candidates: list[str] = []

    for line in con_text.splitlines():
        stripped_line = line.strip()
        lowercase_line = stripped_line.lower()

        if starts_with_any_prefix(lowercase_line, REMOVE_CON_PREFIXES):
            continue

        create_pco_match = CREATE_PCO_PATTERN.match(stripped_line)
        if create_pco_match is not None:
            pco_name = create_pco_match.group(1)
            if pco_name.lower() == original_name.lower():
                renamed_line = re.sub(
                    re.escape(pco_name),
                    bf2_name,
                    line,
                    count=1,
                )
                output_lines.append(renamed_line)
            else:
                turret_candidates.append(pco_name)
                output_lines.append(line)
            continue

        create_rb_match = CREATE_RB_PATTERN.match(stripped_line)
        if create_rb_match is not None:
            rotational_bundle_name = create_rb_match.group(1)
            lowercase_bundle = rotational_bundle_name.lower()
            if "turret" in lowercase_bundle or "gun" in lowercase_bundle:
                turret_candidates.append(rotational_bundle_name)

        if starts_with_any_prefix(lowercase_line, PATH_REPOINT_PREFIXES):
            line_parts = stripped_line.split(maxsplit=1)
            if (
                len(line_parts) == 2
                and line_parts[1].lower() == original_name.lower()
            ):
                output_lines.append(line)
                continue

        sound_match = SOUND_FILE_PATTERN.match(stripped_line)
        if sound_match is not None:
            repointed_path = repoint_relative_path(
                sound_match.group(2),
                original_name,
            )
            output_lines.append(
                f"{sound_match.group(1)}{repointed_path}"
                f"{sound_match.group(3)}"
            )
            continue

        run_match = RUN_INCLUDE_PATTERN.match(stripped_line)
        if run_match is not None:
            repointed_inc = repoint_relative_path(
                run_match.group(2),
                original_name,
            )
            output_lines.append(
                f"{run_match.group(1)}{repointed_inc}{run_match.group(3)}"
            )
            continue

        updated_line = re.sub(
            rf"(include\s+){re.escape(original_name)}\.tweak\b",
            rf"\1{bf2_name}.tweak",
            line,
            flags=re.IGNORECASE,
        )
        output_lines.append(updated_line)

    return "\n".join(output_lines) + "\n", turret_candidates


def convert_tweak_for_bf2(
    tweak_text: str,
    original_name: str,
    bf2_name: str,
    turret_candidates: list[str],
) -> str:
    """Transform vehicle .tweak into _bf2.tweak with turret merge notes."""
    output_lines: list[str] = []
    replaced_root_template = False

    root_activesafe_pattern = re.compile(
        rf"^objecttemplate\.activesafe\s+PlayerControlObject\s+"
        rf"{re.escape(original_name)}\b",
        re.IGNORECASE,
    )

    for line in tweak_text.splitlines():
        stripped_line = line.strip()

        if (
            not replaced_root_template
            and root_activesafe_pattern.match(stripped_line) is not None
        ):
            output_lines.append(
                f"ObjectTemplate.activeSafe PlayerControlObject {bf2_name}"
            )
            if turret_candidates:
                output_lines.append(
                    "rem --- TODO(_bf2): Verify merged gunner turret(s) "
                    "for single-bot control ---"
                )
                for turret_name in turret_candidates:
                    output_lines.append(
                        f"rem ObjectTemplate.addTemplate {turret_name}"
                    )
            replaced_root_template = True
            continue

        sound_match = SOUND_FILE_PATTERN.match(stripped_line)
        if sound_match is not None:
            repointed_path = repoint_relative_path(
                sound_match.group(2),
                original_name,
            )
            output_lines.append(
                f"{sound_match.group(1)}{repointed_path}"
                f"{sound_match.group(3)}"
            )
            continue

        output_lines.append(line)

    return "\n".join(output_lines) + "\n"


def detect_root_pco_name(con_text: str, fallback_name: str) -> str:
    """Find the first PlayerControlObject name in the .con file."""
    for line in con_text.splitlines():
        create_match = CREATE_PCO_PATTERN.match(line.strip())
        if create_match is not None:
            return create_match.group(1)
    return fallback_name


def parse_arguments() -> argparse.Namespace:
    """Parse CLI arguments for the co-op _bf2 vehicle converter."""
    parser = argparse.ArgumentParser(
        description=(
            "Convert a multi-crew vehicle .con/.tweak into a _bf2 "
            "one-man co-op variant."
        )
    )
    parser.add_argument(
        "con_file",
        type=Path,
        help="Input vehicle .con file.",
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
        help=(
            "Output directory (defaults to <parent>_bf2 sibling directory)."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print converted files without writing.",
    )
    return parser.parse_args()


def main() -> int:
    """Entry point for generating a _bf2 one-man co-op vehicle variant."""
    arguments = parse_arguments()

    if not arguments.con_file.is_file():
        print(f"File not found: {arguments.con_file}", file=sys.stderr)
        return 2

    con_text = arguments.con_file.read_text(
        encoding="utf-8",
        errors="replace",
    )
    original_name = detect_root_pco_name(con_text, arguments.con_file.stem)
    bf2_name = f"{original_name}_bf2"

    new_con_text, detected_turrets = convert_con_for_bf2(
        con_text=con_text,
        original_name=original_name,
        bf2_name=bf2_name,
    )

    if arguments.tweak is not None:
        tweak_path = arguments.tweak
    else:
        tweak_path = arguments.con_file.with_suffix(".tweak")

    new_tweak_text: str | None = None
    if tweak_path.is_file():
        original_tweak_text = tweak_path.read_text(
            encoding="utf-8",
            errors="replace",
        )
        new_tweak_text = convert_tweak_for_bf2(
            tweak_text=original_tweak_text,
            original_name=original_name,
            bf2_name=bf2_name,
            turret_candidates=detected_turrets,
        )

    if arguments.out_dir is not None:
        output_directory = arguments.out_dir
    else:
        parent_directory = arguments.con_file.parent
        output_directory = (
            parent_directory.parent / f"{parent_directory.name}_bf2"
        )

    output_con_path = output_directory / f"{bf2_name}.con"
    output_tweak_path = output_directory / f"{bf2_name}.tweak"

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

    if detected_turrets:
        turret_list = ", ".join(detected_turrets)
        print(
            "Turret/sub-PCO candidates detected for driver merge: "
            f"{turret_list}"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
