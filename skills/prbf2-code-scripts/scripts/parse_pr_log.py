#!/usr/bin/env python3
"""Parse PR:BF2 Debugger logs (mods/pr/logs/) and map errors to CTD root-cause hints."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

TEXCOORD_NOISE_RE = re.compile(r"tex(?:ture)?\s*coord|uv\s+out\s+of\s+range", re.IGNORECASE)
SEVERITY_RE = re.compile(r"\b(Assert|Error|Fatal|Warning)\b", re.IGNORECASE)

DIAGNOSTIC_HINTS: list[tuple[re.Pattern[str], str]] = [
    (
        re.compile(r"collision|col\d|collisionmesh", re.IGNORECASE),
        "Check CollisionManager.createTemplate, ObjectTemplate.collisionMesh/setCollisionMesh, and col0-col3 assignments.",
    ),
    (
        re.compile(r"template.*not found|unknown template|addtemplate", re.IGNORECASE),
        "Verify load order and ObjectTemplate.create / ObjectTemplate.activeSafe <Class> <Name> context.",
    ),
    (
        re.compile(r"networkable|ghost", re.IGNORECASE),
        "Ensure ObjectTemplate.setNetworkableInfo (e.g. BasicInfo) is set on networked parts.",
    ),
    (
        re.compile(r"aidll|strategic|aitemplate|weapontemplate", re.IGNORECASE),
        "Check ObjectTemplate.aiTemplate links and remove broken legacy BF1942 SAI conditionals.",
    ),
    (
        re.compile(r"lightmap|material", re.IGNORECASE),
        "Verify GeometryTemplate.doNotGenerateLightmaps and mapMaterial indices against materialmanagerdefine.con.",
    ),
    (
        re.compile(r"hud|guiindex|atlas", re.IGNORECASE),
        "Check VehicleHud/WeaponHud.guiIndex against hudBuilder.setNodeLogicShowVariable and atlaslist.con.",
    ),
    (
        re.compile(r"not found|cannot open|failed to load", re.IGNORECASE),
        "Verify relative mesh, sound (.ssc/.ogg), animation (.ske/.baf), or _bf2 ../<orig>/ paths.",
    ),
]


@dataclass
class LogFinding:
    """Represents a parsed Error, Assert, or Warning entry from a PR log."""

    file: str
    line: int
    severity: str
    text: str
    hint: str | None = None


def infer_hint(text: str) -> str | None:
    """Return a troubleshooting hint if the log line matches a known pattern."""
    for pattern, hint in DIAGNOSTIC_HINTS:
        if pattern.search(text):
            return hint
    return None


def collect_logs(target: Path) -> list[Path]:
    """Collect log files from a file path or mods/pr/logs directory."""
    if target.is_file():
        return [target]
    if target.is_dir():
        return sorted(
            p
            for p in target.rglob("*")
            if p.is_file() and p.suffix.lower() in {".log", ".txt"}
        )
    return []


def parse_log_file(path: Path, include_texcoord: bool) -> list[LogFinding]:
    """Extract Error, Assert, and Warning lines from a single log file."""
    findings: list[LogFinding] = []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    for lineno, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped:
            continue
        if not include_texcoord and TEXCOORD_NOISE_RE.search(stripped):
            continue
        if m := SEVERITY_RE.search(stripped):
            sev = m.group(1).upper()
            findings.append(
                LogFinding(
                    file=str(path),
                    line=lineno,
                    severity=sev,
                    text=stripped,
                    hint=infer_hint(stripped) if sev in {"ERROR", "ASSERT", "FATAL"} else None,
                )
            )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Parse PR:BF2 Debugger logs and surface early Error/Assert root causes."
    )
    parser.add_argument("log_path", type=Path, help="Log file or mods/pr/logs directory.")
    parser.add_argument(
        "--include-texcoord",
        action="store_true",
        help="Include benign texture-coordinate warnings.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    args = parser.parse_args()

    logs = collect_logs(args.log_path)
    if not logs:
        print(f"No log files found at: {args.log_path}", file=sys.stderr)
        return 2

    all_findings: list[LogFinding] = []
    for log in logs:
        all_findings.extend(parse_log_file(log, args.include_texcoord))

    if args.json:
        print(json.dumps([asdict(f) for f in all_findings], indent=2))
        return 0

    if not all_findings:
        print(f"No Error/Assert/Warning lines found across {len(logs)} log file(s).")
        return 0

    for item in all_findings:
        print(f"[{item.severity}] {item.file}:{item.line}: {item.text}")
        if item.hint:
            print(f"    Hint: {item.hint}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
