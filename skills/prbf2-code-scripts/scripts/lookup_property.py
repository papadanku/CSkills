#!/usr/bin/env python3
"""Search PR:BF2 property, AI, and token catalogs under references/properties/."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
PROPS_DIR = SKILL_ROOT / "references" / "properties"

CATEGORY_GLOBS = {
    "all": "**/*.md",
    "ai": "ai/**/*.md",
    "objecttemplate": "objecttemplate/**/*.md",
    "tokens": "tokens-*.md",
}


@dataclass
class PropertyMatch:
    """Represents a matching property or token entry from references/properties/."""

    file: str
    line: int
    entry: str
    details: list[str]


def search_properties(
    query: str, category: str, limit: int
) -> list[PropertyMatch]:
    """Search markdown reference files for entries matching query."""
    pattern = CATEGORY_GLOBS[category]
    q_lower = query.lower()
    matches: list[PropertyMatch] = []

    for md_path in sorted(PROPS_DIR.glob(pattern)):
        lines = md_path.read_text(encoding="utf-8", errors="replace").splitlines()
        rel_path = str(md_path.relative_to(SKILL_ROOT))
        idx = 0
        while idx < len(lines):
            line = lines[idx]
            stripped = line.strip()
            if stripped.startswith("- `") and q_lower in stripped.lower():
                entry = stripped[2:].strip()
                details: list[str] = []
                j = idx + 1
                while j < len(lines) and (
                    lines[j].startswith("    ") or not lines[j].strip()
                ):
                    detail = lines[j].strip()
                    if detail:
                        details.append(detail)
                    j += 1
                matches.append(
                    PropertyMatch(
                        file=rel_path,
                        line=idx + 1,
                        entry=entry,
                        details=details,
                    )
                )
                if len(matches) >= limit:
                    return matches
                idx = j
                continue
            elif "`" in stripped and q_lower in stripped.lower() and not stripped.startswith("#"):
                # Catch inline token lists (e.g., tokens-objects-and-enums.md)
                matches.append(
                    PropertyMatch(
                        file=rel_path,
                        line=idx + 1,
                        entry=stripped,
                        details=[],
                    )
                )
                if len(matches) >= limit:
                    return matches
            idx += 1

    return matches


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Search PR:BF2 properties and tokens across references/properties/."
    )
    parser.add_argument("query", help="Property prefix or keyword (e.g. magSize, guiIndex, aistrategy).")
    parser.add_argument(
        "--category",
        choices=sorted(CATEGORY_GLOBS.keys()),
        default="all",
        help="Restrict search to a property category.",
    )
    parser.add_argument(
        "--limit", type=int, default=25, help="Maximum number of matches to return."
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    args = parser.parse_args()

    if not PROPS_DIR.is_dir():
        print(f"Properties directory not found: {PROPS_DIR}", file=sys.stderr)
        return 2

    results = search_properties(args.query, args.category, args.limit)

    if args.json:
        print(json.dumps([asdict(r) for r in results], indent=2))
        return 0

    if not results:
        print(f"No matches found for `{args.query}` in category `{args.category}`.")
        return 0

    for item in results:
        print(f"{item.file}:{item.line}: {item.entry}")
        for detail in item.details:
            print(f"    {detail}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
