#!/usr/bin/env python3
"""Search PR:BF2 property, AI, console, and token reference catalogs."""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
from pathlib import Path
import sys


SKILL_ROOT = Path(__file__).resolve().parent.parent
REFERENCES_DIR = SKILL_ROOT / "references"
GUIDES_PROPERTIES_DIR = SKILL_ROOT / "guides" / "properties"

CATEGORY_TARGETS: dict[str, list[tuple[Path, str]]] = {
    "all": [
        (REFERENCES_DIR, "*.md"),
        (GUIDES_PROPERTIES_DIR, "*.md"),
    ],
    "ai": [
        (REFERENCES_DIR, "ai-*.md"),
    ],
    "objecttemplate": [
        (REFERENCES_DIR, "console-objecttemplate-*.md"),
    ],
    "console": [
        (REFERENCES_DIR, "console-*.md"),
    ],
    "vars": [
        (REFERENCES_DIR, "console-vars-*.md"),
    ],
    "tokens": [
        (GUIDES_PROPERTIES_DIR, "tokens-*.md"),
    ],
}


@dataclass
class PropertyMatch:
    """Represents a matching property or token entry from references."""

    file: str
    line: int
    entry: str
    details: list[str]


def collect_target_markdown_files(category: str) -> list[Path]:
    """Return sorted, deduplicated markdown files for the chosen category."""
    seen_paths: set[Path] = set()
    markdown_files: list[Path] = []

    for base_directory, glob_pattern in CATEGORY_TARGETS[category]:
        if not base_directory.is_dir():
            continue
        for candidate_path in sorted(base_directory.glob(glob_pattern)):
            if candidate_path.is_file() and candidate_path not in seen_paths:
                seen_paths.add(candidate_path)
                markdown_files.append(candidate_path)

    return markdown_files


def search_properties(
    query: str,
    category: str,
    result_limit: int,
) -> list[PropertyMatch]:
    """Search markdown reference files for entries matching query."""
    normalized_query = query.lower()
    matches: list[PropertyMatch] = []
    markdown_files = collect_target_markdown_files(category)

    for markdown_path in markdown_files:
        file_lines = markdown_path.read_text(
            encoding="utf-8",
            errors="replace",
        ).splitlines()
        relative_path = str(markdown_path.relative_to(SKILL_ROOT))
        line_index = 0

        while line_index < len(file_lines):
            current_line = file_lines[line_index]
            stripped_line = current_line.strip()

            if (
                stripped_line.startswith("- `")
                and normalized_query in stripped_line.lower()
            ):
                entry_text = stripped_line[2:].strip()
                detail_lines: list[str] = []
                detail_index = line_index + 1

                while detail_index < len(file_lines):
                    next_line = file_lines[detail_index]
                    if next_line.startswith("    ") or not next_line.strip():
                        stripped_detail = next_line.strip()
                        if stripped_detail:
                            detail_lines.append(stripped_detail)
                        detail_index += 1
                    else:
                        break

                matches.append(
                    PropertyMatch(
                        file=relative_path,
                        line=line_index + 1,
                        entry=entry_text,
                        details=detail_lines,
                    )
                )
                if len(matches) >= result_limit:
                    return matches
                line_index = detail_index
                continue

            if (
                "`" in stripped_line
                and normalized_query in stripped_line.lower()
                and not stripped_line.startswith("#")
            ):
                matches.append(
                    PropertyMatch(
                        file=relative_path,
                        line=line_index + 1,
                        entry=stripped_line,
                        details=[],
                    )
                )
                if len(matches) >= result_limit:
                    return matches

            line_index += 1

    return matches


def parse_arguments() -> argparse.Namespace:
    """Parse CLI arguments for the PR:BF2 property lookup tool."""
    parser = argparse.ArgumentParser(
        description=(
            "Search PR:BF2 properties, console commands, and tokens across "
            "references/ and guides/properties/."
        )
    )
    parser.add_argument(
        "query",
        help=(
            "Property prefix or keyword (e.g. magSize, guiIndex, "
            "aistrategy)."
        ),
    )
    parser.add_argument(
        "--category",
        choices=sorted(CATEGORY_TARGETS.keys()),
        default="all",
        help="Restrict search to a property category.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=25,
        help="Maximum number of matches to return.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON output.",
    )
    return parser.parse_args()


def main() -> int:
    """Entry point for searching PR:BF2 reference documentation."""
    arguments = parse_arguments()

    if not REFERENCES_DIR.is_dir():
        print(
            f"References directory not found: {REFERENCES_DIR}",
            file=sys.stderr,
        )
        return 2

    search_results = search_properties(
        query=arguments.query,
        category=arguments.category,
        result_limit=arguments.limit,
    )

    if arguments.json:
        serialized_results = [asdict(match) for match in search_results]
        print(json.dumps(serialized_results, indent=2))
        return 0

    if not search_results:
        print(
            f"No matches found for `{arguments.query}` in category "
            f"`{arguments.category}`."
        )
        return 0

    for match in search_results:
        print(f"{match.file}:{match.line}: {match.entry}")
        for detail_line in match.details:
            print(f"    {detail_line}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
