#!/usr/bin/env python3
"""Pre-commit linter and static auditor for PR:BF2 scripts."""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
from pathlib import Path
import re
import sys


SCRIPT_EXTENSIONS = {".con", ".tweak", ".inc", ".ai"}

NETWORKED_CLASSES = {
    "playercontrolobject",
    "rotationalbundle",
    "genericfirearm",
    "spawnpoint",
    "controlpoint",
    "destroyableobject",
}

LEGACY_SAI_BROKEN_CONDITIONALS = {
    "averagestrategicstrength",
    "attackstrategicstrength",
    "defencestrategicstrength",
    "security",
}

LEGACY_SAI_ALWAYS_ZERO_CONDITIONALS = {
    "air",
    "bomber",
    "fighter",
    "naval",
    "heavynaval",
    "lcvp",
    "antiair",
    "infantry",
    "infantery",
    "antitank",
    "heavyattack",
    "carrier",
    "fastattack",
    "artillery",
}

NON_DUPLICATE_OBJECTTEMPLATE_PREFIXES = (
    "objecttemplate.create",
    "objecttemplate.activesafe",
    "objecttemplate.active ",
    "objecttemplate.addtemplate",
    "objecttemplate.createcomponent",
    "objecttemplate.mapmaterial",
    "objecttemplate.armor.addarmoreffect",
    "objecttemplate.fire.addfirerate",
    "objecttemplate.fire.addtimeevent",
    "objecttemplate.zoom.addzoomfactor",
)

BEGIN_COMPONENT_PATTERN = re.compile(
    r"^rem\s+---BeginComp:(\S+)\s*---",
    re.IGNORECASE,
)
END_COMPONENT_PATTERN = re.compile(
    r"^rem\s+---EndComp\s*---",
    re.IGNORECASE,
)
CREATE_COMPONENT_PATTERN = re.compile(
    r"^objecttemplate\.createcomponent\s+(\S+)",
    re.IGNORECASE,
)
CREATE_TEMPLATE_PATTERN = re.compile(
    r"^objecttemplate\.create\s+(\S+)\s+(\S+)",
    re.IGNORECASE,
)
ACTIVE_SAFE_PATTERN = re.compile(
    r"^objecttemplate\.activesafe\s+(\S+)\s+(\S+)",
    re.IGNORECASE,
)
ACTIVE_TEMPLATE_PATTERN = re.compile(
    r"^objecttemplate\.active\s+(\S+)",
    re.IGNORECASE,
)
ADD_TEMPLATE_PATTERN = re.compile(
    r"^objecttemplate\.addtemplate\s+(\S+)",
    re.IGNORECASE,
)
NETWORKABLE_PATTERN = re.compile(
    r"^objecttemplate\.setnetworkableinfo\s+(\S+)",
    re.IGNORECASE,
)
GUI_INDEX_PATTERN = re.compile(
    r"^objecttemplate\.(?:vehiclehud|weaponhud)\.guiindex\s+(-?\d+)",
    re.IGNORECASE,
)
HUD_SHOW_GUI_PATTERN = re.compile(
    r"^hudbuilder\.setnodelogicshowvariable\s+\S+\s+guiindex\s+(-?\d+)",
    re.IGNORECASE,
)
CRD_EXPONENTIAL_PATTERN = re.compile(
    r"CRD_EXPONENTIAL/([^/\s]+)/([^/\s]+)/([^/\s]+)",
    re.IGNORECASE,
)
ROUNDS_PER_MINUTE_PATTERN = re.compile(
    r"^objecttemplate\.fire\.roundsperminute\s+(\d+)",
    re.IGNORECASE,
)
MAGAZINE_SIZE_PATTERN = re.compile(
    r"^objecttemplate\.ammo\.magsize\s+(-?\d+)",
    re.IGNORECASE,
)
ATTENUATION_RANGE_PATTERN = re.compile(
    r"^objecttemplate\.attenuationrange[12]\s+([0-9]+(?:\.[0-9]+)?)",
    re.IGNORECASE,
)
INCLUDE_DIRECTIVE_PATTERN = re.compile(
    r"^include\s+(.+)$",
    re.IGNORECASE,
)
ASSET_PATH_PATTERN = re.compile(
    r"(?:soundfilename|weaponicon|setpicturenodetexture|"
    r"animationsystem1p|animationsystem3p|addanimation)"
    r'\s+"?([^\s"]+)"?',
    re.IGNORECASE,
)


@dataclass
class AuditIssue:
    """Represents a single lint or audit finding."""

    severity: str
    file: str
    line: int
    code: str
    message: str


@dataclass
class ComponentBlockState:
    """Tracks an open BeginComp/EndComp folding block."""

    component_name: str
    start_line: int
    saw_create_component: bool


@dataclass
class NetworkableTrackingEntry:
    """Tracks whether a networked template has setNetworkableInfo."""

    template_class: str
    file_path: str
    line_number: int
    has_networkable_info: bool


def collect_script_files(input_paths: list[Path]) -> list[Path]:
    """Expand input files and directories into sorted script paths."""
    collected_files: list[Path] = []
    for input_path in input_paths:
        if input_path.is_file():
            collected_files.append(input_path)
        elif input_path.is_dir():
            for candidate_path in sorted(input_path.rglob("*")):
                if (
                    candidate_path.is_file()
                    and candidate_path.suffix.lower() in SCRIPT_EXTENSIONS
                ):
                    collected_files.append(candidate_path)
    return collected_files


def detect_script_extension(file_path: Path) -> str:
    """Determine the effective script extension, supporting *.con.txt."""
    extension = file_path.suffix.lower()
    if extension == ".txt" and "." in file_path.stem:
        inner_extension = file_path.stem.rsplit(".", 1)[-1].lower()
        return f".{inner_extension}"
    return extension


def is_non_duplicate_property(lowercase_line: str) -> bool:
    """Return True if the ObjectTemplate line may legitimately repeat."""
    for allowed_prefix in NON_DUPLICATE_OBJECTTEMPLATE_PREFIXES:
        if lowercase_line.startswith(allowed_prefix):
            return True
    return False


def audit_file(
    script_path: Path,
    defined_templates: dict[str, tuple[str, str, int]],
    referenced_templates: list[tuple[str, str, int]],
    hud_gui_indices: set[int],
    template_gui_indices: list[tuple[int, str, int]],
    mod_root: Path | None,
) -> list[AuditIssue]:
    """Audit a single PR:BF2 script file for syntax and logic issues."""
    issues: list[AuditIssue] = []
    file_path_str = str(script_path)
    extension = detect_script_extension(script_path)

    try:
        file_lines = script_path.read_text(
            encoding="utf-8",
            errors="replace",
        ).splitlines()
    except OSError as os_error:
        return [
            AuditIssue(
                severity="ERROR",
                file=file_path_str,
                line=0,
                code="IO_ERROR",
                message=f"Cannot read file: {os_error}",
            )
        ]

    in_block_comment = False
    block_comment_start_line = 0
    if_line_stack: list[int] = []
    while_line_stack: list[int] = []
    component_stack: list[ComponentBlockState] = []

    saw_first_code_line = False
    active_template_name: str | None = None
    seen_properties_in_block: set[str] = set()
    networkable_blocks: dict[str, NetworkableTrackingEntry] = {}

    for line_number, raw_line in enumerate(file_lines, start=1):
        stripped_line = raw_line.strip()
        if not stripped_line:
            continue

        lowercase_line = stripped_line.lower()

        if lowercase_line == "beginrem":
            if in_block_comment:
                issues.append(
                    AuditIssue(
                        severity="WARNING",
                        file=file_path_str,
                        line=line_number,
                        code="NESTED_BEGINREM",
                        message=(
                            "Nested beginRem inside an active beginRem block."
                        ),
                    )
                )
            else:
                in_block_comment = True
                block_comment_start_line = line_number
            continue

        if lowercase_line == "endrem":
            if not in_block_comment:
                issues.append(
                    AuditIssue(
                        severity="ERROR",
                        file=file_path_str,
                        line=line_number,
                        code="UNMATCHED_ENDREM",
                        message="endRem without matching beginRem.",
                    )
                )
            else:
                in_block_comment = False
            continue

        if in_block_comment:
            continue

        begin_comp_match = BEGIN_COMPONENT_PATTERN.match(stripped_line)
        if begin_comp_match is not None:
            component_stack.append(
                ComponentBlockState(
                    component_name=begin_comp_match.group(1),
                    start_line=line_number,
                    saw_create_component=False,
                )
            )
            continue

        if END_COMPONENT_PATTERN.match(stripped_line) is not None:
            if not component_stack:
                issues.append(
                    AuditIssue(
                        severity="ERROR",
                        file=file_path_str,
                        line=line_number,
                        code="UNMATCHED_ENDCOMP",
                        message=(
                            "rem ---EndComp --- without matching BeginComp."
                        ),
                    )
                )
            else:
                closed_block = component_stack.pop()
                if not closed_block.saw_create_component:
                    issues.append(
                        AuditIssue(
                            severity="WARNING",
                            file=file_path_str,
                            line=closed_block.start_line,
                            code="EMPTY_COMP_BLOCK",
                            message=(
                                f"BeginComp:{closed_block.component_name} "
                                "has no ObjectTemplate.createComponent "
                                f"{closed_block.component_name}."
                            ),
                        )
                    )
            continue

        if (
            lowercase_line.startswith("rem ")
            or lowercase_line == "rem"
            or stripped_line.startswith("#")
        ):
            continue

        if not saw_first_code_line:
            saw_first_code_line = True
            if (
                extension == ".tweak"
                and ACTIVE_SAFE_PATTERN.match(stripped_line) is None
                and not lowercase_line.startswith("geometrytemplate.")
            ):
                issues.append(
                    AuditIssue(
                        severity="ERROR",
                        file=file_path_str,
                        line=line_number,
                        code="TWEAK_MISSING_ACTIVESAFE",
                        message=(
                            ".tweak file should begin with "
                            "ObjectTemplate.activeSafe <Class> <Name>."
                        ),
                    )
                )

        if lowercase_line.startswith("if "):
            if_line_stack.append(line_number)
        elif lowercase_line == "endif":
            if not if_line_stack:
                issues.append(
                    AuditIssue(
                        severity="ERROR",
                        file=file_path_str,
                        line=line_number,
                        code="UNMATCHED_ENDIF",
                        message="endIf without matching if.",
                    )
                )
            else:
                if_line_stack.pop()
        elif lowercase_line.startswith("while "):
            while_line_stack.append(line_number)
        elif lowercase_line == "endwhile":
            if not while_line_stack:
                issues.append(
                    AuditIssue(
                        severity="ERROR",
                        file=file_path_str,
                        line=line_number,
                        code="UNMATCHED_ENDWHILE",
                        message="endWhile without matching while.",
                    )
                )
            else:
                while_line_stack.pop()

        include_match = INCLUDE_DIRECTIVE_PATTERN.match(stripped_line)
        if include_match is not None:
            include_arguments = include_match.group(1).strip().split()
            if len(include_arguments) > 1:
                issues.append(
                    AuditIssue(
                        severity="ERROR",
                        file=file_path_str,
                        line=line_number,
                        code="INCLUDE_WITH_ARGS",
                        message=(
                            "`include` accepts no arguments; use "
                            "`run <path> [args]` to pass v_arg1..N."
                        ),
                    )
                )

        create_match = CREATE_TEMPLATE_PATTERN.match(stripped_line)
        active_safe_match = ACTIVE_SAFE_PATTERN.match(stripped_line)
        active_match = ACTIVE_TEMPLATE_PATTERN.match(stripped_line)
        add_template_match = ADD_TEMPLATE_PATTERN.match(stripped_line)

        if create_match is not None:
            template_class = create_match.group(1)
            template_name = create_match.group(2)
            active_template_name = template_name
            seen_properties_in_block.clear()
            defined_templates[template_name.lower()] = (
                template_class,
                file_path_str,
                line_number,
            )
            if template_class.lower() in NETWORKED_CLASSES:
                networkable_blocks.setdefault(
                    template_name.lower(),
                    NetworkableTrackingEntry(
                        template_class=template_class,
                        file_path=file_path_str,
                        line_number=line_number,
                        has_networkable_info=False,
                    ),
                )
        elif active_safe_match is not None:
            template_class = active_safe_match.group(1)
            template_name = active_safe_match.group(2)
            active_template_name = template_name
            seen_properties_in_block.clear()
            if template_class.lower() in NETWORKED_CLASSES:
                networkable_blocks.setdefault(
                    template_name.lower(),
                    NetworkableTrackingEntry(
                        template_class=template_class,
                        file_path=file_path_str,
                        line_number=line_number,
                        has_networkable_info=False,
                    ),
                )
        elif active_match is not None:
            active_template_name = active_match.group(1)
            seen_properties_in_block.clear()
        elif add_template_match is not None:
            referenced_templates.append(
                (add_template_match.group(1), file_path_str, line_number)
            )

        if NETWORKABLE_PATTERN.match(stripped_line) is not None:
            if active_template_name is not None:
                template_key = active_template_name.lower()
                if template_key in networkable_blocks:
                    networkable_blocks[template_key].has_networkable_info = (
                        True
                    )

        create_comp_match = CREATE_COMPONENT_PATTERN.match(stripped_line)
        if create_comp_match is not None:
            component_name = create_comp_match.group(1)
            if not component_stack:
                issues.append(
                    AuditIssue(
                        severity="WARNING",
                        file=file_path_str,
                        line=line_number,
                        code="UNWRAPPED_COMPONENT",
                        message=(
                            f"ObjectTemplate.createComponent {component_name} "
                            "is not wrapped in BeginComp/EndComp."
                        ),
                    )
                )
            else:
                current_block = component_stack[-1]
                if (
                    current_block.component_name.lower()
                    != component_name.lower()
                ):
                    issues.append(
                        AuditIssue(
                            severity="ERROR",
                            file=file_path_str,
                            line=line_number,
                            code="COMP_MISMATCH",
                            message=(
                                f"createComponent {component_name} does not "
                                f"match BeginComp:"
                                f"{current_block.component_name}"
                                f" (line {current_block.start_line})."
                            ),
                        )
                    )
                else:
                    current_block.saw_create_component = True

        if lowercase_line.startswith(
            "objecttemplate."
        ) and not is_non_duplicate_property(lowercase_line):
            property_key = lowercase_line.split()[0]
            if property_key in seen_properties_in_block:
                display_template = active_template_name or "<unknown>"
                issues.append(
                    AuditIssue(
                        severity="WARNING",
                        file=file_path_str,
                        line=line_number,
                        code="DUPLICATE_PROPERTY",
                        message=(
                            f"Duplicate property `{property_key}` in active "
                            f"block `{display_template}`."
                        ),
                    )
                )
            else:
                seen_properties_in_block.add(property_key)

        for crd_match in CRD_EXPONENTIAL_PATTERN.finditer(stripped_line):
            try:
                mean_value = float(crd_match.group(1))
            except ValueError:
                continue
            if mean_value == 0.0:
                issues.append(
                    AuditIssue(
                        severity="ERROR",
                        file=file_path_str,
                        line=line_number,
                        code="CRD_EXP_ZERO_MEAN",
                        message=(
                            f"{crd_match.group(0)} always returns 0 because "
                            "Number1 (mean) is 0 and Number2 is ignored."
                        ),
                    )
                )

        rpm_match = ROUNDS_PER_MINUTE_PATTERN.match(stripped_line)
        if rpm_match is not None:
            rounds_per_minute = int(rpm_match.group(1))
            if rounds_per_minute <= 0 or 1800 % rounds_per_minute != 0:
                issues.append(
                    AuditIssue(
                        severity="WARNING",
                        file=file_path_str,
                        line=line_number,
                        code="RPM_NOT_DIVISOR_OF_1800",
                        message=(
                            f"roundsPerMinute {rounds_per_minute} does not "
                            "divide evenly into 1800."
                        ),
                    )
                )

        mag_match = MAGAZINE_SIZE_PATTERN.match(stripped_line)
        if mag_match is not None:
            magazine_size = int(mag_match.group(1))
            if magazine_size != -1 and (
                magazine_size < 0 or magazine_size > 1023
            ):
                issues.append(
                    AuditIssue(
                        severity="ERROR",
                        file=file_path_str,
                        line=line_number,
                        code="MAGSIZE_OUT_OF_RANGE",
                        message=(
                            f"magSize {magazine_size} exceeds BF2 engine "
                            "limit (max 1023, or -1 for infinite)."
                        ),
                    )
                )

        attenuation_match = ATTENUATION_RANGE_PATTERN.match(stripped_line)
        if attenuation_match is not None:
            attenuation_value = float(attenuation_match.group(1))
            if attenuation_value > 100.0:
                issues.append(
                    AuditIssue(
                        severity="WARNING",
                        file=file_path_str,
                        line=line_number,
                        code="ATTENUATION_OVER_100",
                        message=(
                            f"attenuationRange value {attenuation_value} "
                            "exceeds 100 and may trigger engine errors."
                        ),
                    )
                )

        gui_index_match = GUI_INDEX_PATTERN.match(stripped_line)
        if gui_index_match is not None:
            template_gui_indices.append(
                (int(gui_index_match.group(1)), file_path_str, line_number)
            )

        hud_show_match = HUD_SHOW_GUI_PATTERN.match(stripped_line)
        if hud_show_match is not None:
            hud_gui_indices.add(int(hud_show_match.group(1)))

        if extension == ".ai":
            tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", stripped_line)
            for token in tokens:
                lowercase_token = token.lower()
                if lowercase_token in LEGACY_SAI_BROKEN_CONDITIONALS:
                    issues.append(
                        AuditIssue(
                            severity="ERROR",
                            file=file_path_str,
                            line=line_number,
                            code="LEGACY_SAI_BROKEN",
                            message=(
                                f"Legacy BF1942 SAI conditional `{token}` is "
                                "missing from BF2 AIDLL.dll."
                            ),
                        )
                    )
                elif (
                    lowercase_token in LEGACY_SAI_ALWAYS_ZERO_CONDITIONALS
                    and "aistrategy." in lowercase_line
                ):
                    issues.append(
                        AuditIssue(
                            severity="WARNING",
                            file=file_path_str,
                            line=line_number,
                            code="LEGACY_SAI_ZERO",
                            message=(
                                f"Legacy SAI conditional `{token}` always "
                                "evaluates to 0 in BF2 AIDLL.dll."
                            ),
                        )
                    )

            if "v_arg3" in lowercase_line and "< 13" in lowercase_line:
                issues.append(
                    AuditIssue(
                        severity="ERROR",
                        file=file_path_str,
                        line=line_number,
                        code="INVALID_V_ARG3_SAI",
                        message=(
                            "`v_arg3 < 13` is invalid in BF2 AIDLL.dll "
                            "Strategic AI conditions."
                        ),
                    )
                )

        if mod_root is not None:
            asset_match = ASSET_PATH_PATTERN.search(stripped_line)
            if asset_match is not None:
                relative_asset = asset_match.group(1).replace("\\", "/")
                if (
                    "/" in relative_asset
                    and not (mod_root / relative_asset).exists()
                ):
                    issues.append(
                        AuditIssue(
                            severity="WARNING",
                            file=file_path_str,
                            line=line_number,
                            code="MISSING_ASSET_PATH",
                            message=(
                                f"Asset `{relative_asset}` not found under "
                                f"{mod_root}."
                            ),
                        )
                    )

    if in_block_comment:
        issues.append(
            AuditIssue(
                severity="ERROR",
                file=file_path_str,
                line=block_comment_start_line,
                code="UNCLOSED_BEGINREM",
                message="beginRem block not closed with endRem.",
            )
        )

    for unclosed_if_line in if_line_stack:
        issues.append(
            AuditIssue(
                severity="ERROR",
                file=file_path_str,
                line=unclosed_if_line,
                code="UNCLOSED_IF",
                message="`if` block not closed with `endIf`.",
            )
        )

    for unclosed_while_line in while_line_stack:
        issues.append(
            AuditIssue(
                severity="ERROR",
                file=file_path_str,
                line=unclosed_while_line,
                code="UNCLOSED_WHILE",
                message="`while` block not closed with `endWhile`.",
            )
        )

    for open_block in component_stack:
        issues.append(
            AuditIssue(
                severity="ERROR",
                file=file_path_str,
                line=open_block.start_line,
                code="UNCLOSED_COMP",
                message=(
                    f"BeginComp:{open_block.component_name} not closed with "
                    "rem ---EndComp ---."
                ),
            )
        )

    if extension == ".tweak":
        for template_key, entry in networkable_blocks.items():
            if not entry.has_networkable_info:
                issues.append(
                    AuditIssue(
                        severity="WARNING",
                        file=entry.file_path,
                        line=entry.line_number,
                        code="MISSING_NETWORKABLE",
                        message=(
                            f"Networked class `{entry.template_class}` "
                            f"(`{template_key}`) has no `setNetworkableInfo` "
                            "in this .tweak."
                        ),
                    )
                )

    return issues


def run_cross_file_checks(
    defined_templates: dict[str, tuple[str, str, int]],
    referenced_templates: list[tuple[str, str, int]],
    hud_gui_indices: set[int],
    template_gui_indices: list[tuple[int, str, int]],
) -> list[AuditIssue]:
    """Verify addTemplate targets and GuiIndex links across multiple files."""
    cross_file_issues: list[AuditIssue] = []

    for referenced_name, file_path, line_number in referenced_templates:
        if referenced_name.lower() not in defined_templates:
            cross_file_issues.append(
                AuditIssue(
                    severity="WARNING",
                    file=file_path,
                    line=line_number,
                    code="UNRESOLVED_ADDTEMPLATE",
                    message=(
                        f"addTemplate target `{referenced_name}` was not "
                        "created in scanned files."
                    ),
                )
            )

    if hud_gui_indices:
        for gui_index, file_path, line_number in template_gui_indices:
            if gui_index not in hud_gui_indices:
                cross_file_issues.append(
                    AuditIssue(
                        severity="WARNING",
                        file=file_path,
                        line=line_number,
                        code="UNMATCHED_GUIINDEX",
                        message=(
                            f"GuiIndex {gui_index} has no matching "
                            "hudBuilder.setNodeLogicShowVariable in scanned "
                            "HUD files."
                        ),
                    )
                )

    return cross_file_issues


def parse_arguments() -> argparse.Namespace:
    """Parse CLI arguments for the PR:BF2 script auditor."""
    parser = argparse.ArgumentParser(
        description=(
            "Audit PR:BF2 .con, .tweak, .inc, and .ai scripts for "
            "common errors."
        )
    )
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="Files or directories to audit.",
    )
    parser.add_argument(
        "--mod-root",
        type=Path,
        default=None,
        help="Optional extracted mod root to check relative asset paths.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON output.",
    )
    return parser.parse_args()


def main() -> int:
    """Entry point for the PR:BF2 script auditor."""
    arguments = parse_arguments()
    script_files = collect_script_files(arguments.paths)
    if not script_files:
        print("No matching script files found.", file=sys.stderr)
        return 2

    defined_templates: dict[str, tuple[str, str, int]] = {}
    referenced_templates: list[tuple[str, str, int]] = []
    hud_gui_indices: set[int] = set()
    template_gui_indices: list[tuple[int, str, int]] = []
    all_issues: list[AuditIssue] = []

    for script_file in script_files:
        file_issues = audit_file(
            script_path=script_file,
            defined_templates=defined_templates,
            referenced_templates=referenced_templates,
            hud_gui_indices=hud_gui_indices,
            template_gui_indices=template_gui_indices,
            mod_root=arguments.mod_root,
        )
        all_issues.extend(file_issues)

    if len(script_files) > 1:
        cross_file_issues = run_cross_file_checks(
            defined_templates=defined_templates,
            referenced_templates=referenced_templates,
            hud_gui_indices=hud_gui_indices,
            template_gui_indices=template_gui_indices,
        )
        all_issues.extend(cross_file_issues)

    if arguments.json:
        serialized_issues = [asdict(issue) for issue in all_issues]
        print(json.dumps(serialized_issues, indent=2))
    else:
        if not all_issues:
            print(f"OK: {len(script_files)} file(s) audited with 0 issues.")
        else:
            for issue in all_issues:
                print(
                    f"[{issue.severity}] {issue.file}:{issue.line} "
                    f"({issue.code}): {issue.message}"
                )

            error_count = 0
            warning_count = 0
            for issue in all_issues:
                if issue.severity == "ERROR":
                    error_count += 1
                elif issue.severity == "WARNING":
                    warning_count += 1

            print(
                f"\nSummary: {error_count} error(s), "
                f"{warning_count} warning(s) across "
                f"{len(script_files)} file(s)."
            )

    for issue in all_issues:
        if issue.severity == "ERROR":
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
