#!/usr/bin/env python3
"""Parse PR:BF2 Debugger logs and map errors to CTD root-cause hints."""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
from pathlib import Path
import re
import sys


TEXCOORD_NOISE_PATTERN = re.compile(
    r"tex(?:ture)?\s*coord|uv\s+out\s+of\s+range",
    re.IGNORECASE,
)
SEVERITY_PATTERN = re.compile(
    r"\b(Assert|Error|Fatal|Warning)\b",
    re.IGNORECASE,
)

DIAGNOSTIC_HINT_RULES: list[tuple[re.Pattern[str], str]] = [
    (
        re.compile(r"collision|col\d|collisionmesh", re.IGNORECASE),
        "Check CollisionManager.createTemplate, "
        "ObjectTemplate.collisionMesh/setCollisionMesh, and col0-col3 "
        "assignments.",
    ),
    (
        re.compile(
            r"template.*not found|unknown template|addtemplate",
            re.IGNORECASE,
        ),
        "Verify load order and ObjectTemplate.create / "
        "ObjectTemplate.activeSafe <Class> <Name> context.",
    ),
    (
        re.compile(r"networkable|ghost", re.IGNORECASE),
        "Ensure ObjectTemplate.setNetworkableInfo (e.g. BasicInfo) is set "
        "on networked parts.",
    ),
    (
        re.compile(
            r"aidll|strategic|aitemplate|weapontemplate",
            re.IGNORECASE,
        ),
        "Check ObjectTemplate.aiTemplate links and remove broken legacy "
        "BF1942 SAI conditionals.",
    ),
    (
        re.compile(r"lightmap|material", re.IGNORECASE),
        "Verify GeometryTemplate.doNotGenerateLightmaps and mapMaterial "
        "indices against materialmanagerdefine.con.",
    ),
    (
        re.compile(r"hud|guiindex|atlas", re.IGNORECASE),
        "Check VehicleHud/WeaponHud.guiIndex against "
        "hudBuilder.setNodeLogicShowVariable and atlaslist.con.",
    ),
    (
        re.compile(r"not found|cannot open|failed to load", re.IGNORECASE),
        "Verify relative mesh, sound (.ssc/.ogg), animation (.ske/.baf), "
        "or _bf2 ../<orig>/ paths.",
    ),
]

ACTIONABLE_SEVERITIES = {"ERROR", "ASSERT", "FATAL"}


@dataclass
class LogFinding:
    """Represents a parsed Error, Assert, Fatal, or Warning log entry."""

    file: str
    line: int
    severity: str
    text: str
    hint: str | None = None


def infer_diagnostic_hint(log_text: str) -> str | None:
    """Return a troubleshooting hint if the log line matches a known rule."""
    for pattern, hint_message in DIAGNOSTIC_HINT_RULES:
        if pattern.search(log_text) is not None:
            return hint_message
    return None


def collect_log_files(target_path: Path) -> list[Path]:
    """Collect log files from a file path or mods/pr/logs directory."""
    if target_path.is_file():
        return [target_path]

    collected_logs: list[Path] = []
    if target_path.is_dir():
        for candidate_path in sorted(target_path.rglob("*")):
            if (
                candidate_path.is_file()
                and candidate_path.suffix.lower() in {".log", ".txt"}
            ):
                collected_logs.append(candidate_path)
    return collected_logs


def parse_log_file(
    log_path: Path,
    include_texcoord_warnings: bool,
) -> list[LogFinding]:
    """Extract Error, Assert, Fatal, and Warning lines from a log file."""
    findings: list[LogFinding] = []
    file_lines = log_path.read_text(
        encoding="utf-8",
        errors="replace",
    ).splitlines()

    for line_number, raw_line in enumerate(file_lines, start=1):
        stripped_line = raw_line.strip()
        if not stripped_line:
            continue

        if (
            not include_texcoord_warnings
            and TEXCOORD_NOISE_PATTERN.search(stripped_line) is not None
        ):
            continue

        severity_match = SEVERITY_PATTERN.search(stripped_line)
        if severity_match is not None:
            severity_label = severity_match.group(1).upper()
            hint_message: str | None = None
            if severity_label in ACTIONABLE_SEVERITIES:
                hint_message = infer_diagnostic_hint(stripped_line)

            findings.append(
                LogFinding(
                    file=str(log_path),
                    line=line_number,
                    severity=severity_label,
                    text=stripped_line,
                    hint=hint_message,
                )
            )

    return findings


def parse_arguments() -> argparse.Namespace:
    """Parse CLI arguments for the PR:BF2 log parser."""
    parser = argparse.ArgumentParser(
        description=(
            "Parse PR:BF2 Debugger logs and surface early Error/Assert "
            "root causes."
        )
    )
    parser.add_argument(
        "log_path",
        type=Path,
        help="Log file or mods/pr/logs directory.",
    )
    parser.add_argument(
        "--include-texcoord",
        action="store_true",
        help="Include benign texture-coordinate warnings.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON output.",
    )
    return parser.parse_args()


def main() -> int:
    """Entry point for parsing PR:BF2 Debugger logs."""
    arguments = parse_arguments()
    log_files = collect_log_files(arguments.log_path)
    if not log_files:
        print(
            f"No log files found at: {arguments.log_path}",
            file=sys.stderr,
        )
        return 2

    all_findings: list[LogFinding] = []
    for log_file in log_files:
        file_findings = parse_log_file(
            log_path=log_file,
            include_texcoord_warnings=arguments.include_texcoord,
        )
        all_findings.extend(file_findings)

    if arguments.json:
        serialized_findings = [asdict(finding) for finding in all_findings]
        print(json.dumps(serialized_findings, indent=2))
        return 0

    if not all_findings:
        print(
            "No Error/Assert/Warning lines found across "
            f"{len(log_files)} log file(s)."
        )
        return 0

    for finding in all_findings:
        print(
            f"[{finding.severity}] {finding.file}:{finding.line}: "
            f"{finding.text}"
        )
        if finding.hint is not None:
            print(f"    Hint: {finding.hint}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
