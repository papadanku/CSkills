#!/usr/bin/env python3
"""Pre-commit linter and static auditor for PR:BF2 scripts (.con, .tweak, .inc, .ai)."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

SCRIPT_EXTENSIONS = {".con", ".tweak", ".inc", ".ai"}

NETWORKED_CLASSES = {
    "playercontrolobject",
    "rotationalbundle",
    "genericfirearm",
    "spawnpoint",
    "controlpoint",
    "destroyableobject",
}

LEGACY_SAI_BROKEN = {
    "averagestrategicstrength",
    "attackstrategicstrength",
    "defencestrategicstrength",
    "security",
}

LEGACY_SAI_ALWAYS_ZERO = {
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

BEGIN_COMP_RE = re.compile(r"^rem\s+---BeginComp:(\S+)\s*---", re.IGNORECASE)
END_COMP_RE = re.compile(r"^rem\s+---EndComp\s*---", re.IGNORECASE)
CREATE_COMP_RE = re.compile(
    r"^objecttemplate\.createcomponent\s+(\S+)", re.IGNORECASE
)
CREATE_RE = re.compile(
    r"^objecttemplate\.create\s+(\S+)\s+(\S+)", re.IGNORECASE
)
ACTIVE_SAFE_RE = re.compile(
    r"^objecttemplate\.activesafe\s+(\S+)\s+(\S+)", re.IGNORECASE
)
ACTIVE_RE = re.compile(r"^objecttemplate\.active\s+(\S+)", re.IGNORECASE)
ADD_TEMPLATE_RE = re.compile(
    r"^objecttemplate\.addtemplate\s+(\S+)", re.IGNORECASE
)
NETWORKABLE_RE = re.compile(
    r"^objecttemplate\.setnetworkableinfo\s+(\S+)", re.IGNORECASE
)
GUI_INDEX_RE = re.compile(
    r"^objecttemplate\.(?:vehiclehud|weaponhud)\.guiindex\s+(-?\d+)",
    re.IGNORECASE,
)
HUD_SHOW_GUI_RE = re.compile(
    r"^hudbuilder\.setnodelogicshowvariable\s+\S+\s+guiindex\s+(-?\d+)",
    re.IGNORECASE,
)
CRD_EXP_RE = re.compile(r"CRD_EXPONENTIAL/([^/\s]+)/([^/\s]+)/([^/\s]+)", re.IGNORECASE)
RPM_RE = re.compile(r"^objecttemplate\.fire\.roundsperminute\s+(\d+)", re.IGNORECASE)
MAG_SIZE_RE = re.compile(r"^objecttemplate\.ammo\.magsize\s+(-?\d+)", re.IGNORECASE)
ATTEN_RE = re.compile(
    r"^objecttemplate\.attenuationrange[12]\s+([0-9]+(?:\.[0-9]+)?)",
    re.IGNORECASE,
)
INCLUDE_RE = re.compile(r"^include\s+(.+)$", re.IGNORECASE)
ASSET_PATH_RE = re.compile(
    r"""(?:soundfilename|weaponicon|setpicturenodetexture|animationsystem1p|animationsystem3p|addanimation)\s+"?([^\s"]+)"?""",
    re.IGNORECASE,
)


@dataclass
class Issue:
    """Represents a single lint/audit finding."""

    severity: str
    file: str
    line: int
    code: str
    message: str


def collect_files(inputs: list[Path]) -> list[Path]:
    """Expand input files and directories into sorted script paths."""
    files: list[Path] = []
    for item in inputs:
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            for path in sorted(item.rglob("*")):
                if path.is_file() and path.suffix.lower() in SCRIPT_EXTENSIONS:
                    files.append(path)
    return files


def strip_inline_rem(line: str) -> str:
    """Return trimmed line."""
    return line.strip()


def audit_file(
    path: Path,
    defined_templates: dict[str, tuple[str, str, int]],
    referenced_templates: list[tuple[str, str, int]],
    hud_gui_indices: set[int],
    template_gui_indices: list[tuple[int, str, int]],
    mod_root: Path | None,
) -> list[Issue]:
    """Audit a single PR:BF2 script file."""
    issues: list[Issue] = []
    file_str = str(path)
    ext = path.suffix.lower()
    if ext == ".txt" and "." in path.stem:
        ext = "." + path.stem.rsplit(".", 1)[-1].lower()

    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as exc:
        return [Issue("ERROR", file_str, 0, "IO_ERROR", f"Cannot read file: {exc}")]

    in_block_rem = False
    block_rem_start = 0
    if_stack: list[int] = []
    while_stack: list[int] = []
    comp_stack: list[tuple[str, int, bool]] = []

    saw_first_code = False
    active_template: str | None = None
    active_class: str | None = None
    seen_props_in_block: set[str] = set()
    block_has_networkable: dict[str, tuple[str, str, int, bool]] = {}

    for lineno, raw_line in enumerate(lines, start=1):
        stripped = strip_inline_rem(raw_line)
        if not stripped:
            continue

        lower = stripped.lower()

        if lower == "beginrem":
            if in_block_rem:
                issues.append(
                    Issue(
                        "WARNING",
                        file_str,
                        lineno,
                        "NESTED_BEGINREM",
                        "Nested beginRem inside an active beginRem block.",
                    )
                )
            else:
                in_block_rem = True
                block_rem_start = lineno
            continue

        if lower == "endrem":
            if not in_block_rem:
                issues.append(
                    Issue(
                        "ERROR",
                        file_str,
                        lineno,
                        "UNMATCHED_ENDREM",
                        "endRem without matching beginRem.",
                    )
                )
            else:
                in_block_rem = False
            continue

        if in_block_rem:
            continue

        # Component folding markers (these start with rem)
        if m := BEGIN_COMP_RE.match(stripped):
            comp_stack.append((m.group(1), lineno, False))
            continue

        if END_COMP_RE.match(stripped):
            if not comp_stack:
                issues.append(
                    Issue(
                        "ERROR",
                        file_str,
                        lineno,
                        "UNMATCHED_ENDCOMP",
                        "rem ---EndComp --- without matching BeginComp.",
                    )
                )
            else:
                comp_name, start_line, saw_create = comp_stack.pop()
                if not saw_create:
                    issues.append(
                        Issue(
                            "WARNING",
                            file_str,
                            start_line,
                            "EMPTY_COMP_BLOCK",
                            f"BeginComp:{comp_name} has no ObjectTemplate.createComponent {comp_name}.",
                        )
                    )
            continue

        if lower.startswith("rem ") or lower == "rem" or stripped.startswith("#"):
            continue

        if not saw_first_code:
            saw_first_code = True
            if ext == ".tweak" and not ACTIVE_SAFE_RE.match(stripped):
                if not lower.startswith("geometrytemplate."):
                    issues.append(
                        Issue(
                            "ERROR",
                            file_str,
                            lineno,
                            "TWEAK_MISSING_ACTIVESAFE",
                            ".tweak file should begin with ObjectTemplate.activeSafe <Class> <Name>.",
                        )
                    )

        # Control flow balance
        if lower.startswith("if "):
            if_stack.append(lineno)
        elif lower == "endif":
            if not if_stack:
                issues.append(
                    Issue("ERROR", file_str, lineno, "UNMATCHED_ENDIF", "endIf without matching if.")
                )
            else:
                if_stack.pop()
        elif lower.startswith("while "):
            while_stack.append(lineno)
        elif lower == "endwhile":
            if not while_stack:
                issues.append(
                    Issue(
                        "ERROR",
                        file_str,
                        lineno,
                        "UNMATCHED_ENDWHILE",
                        "endWhile without matching while.",
                    )
                )
            else:
                while_stack.pop()

        # Include vs run
        if m := INCLUDE_RE.match(stripped):
            inc_args = m.group(1).strip().split()
            if len(inc_args) > 1:
                issues.append(
                    Issue(
                        "ERROR",
                        file_str,
                        lineno,
                        "INCLUDE_WITH_ARGS",
                        "`include` accepts no arguments; use `run <path> [args]` to pass v_arg1..N.",
                    )
                )

        # Template context tracking
        if m := CREATE_RE.match(stripped):
            cls, name = m.group(1), m.group(2)
            active_class = cls.lower()
            active_template = name
            seen_props_in_block.clear()
            defined_templates[name.lower()] = (cls, file_str, lineno)
            if active_class in NETWORKED_CLASSES:
                block_has_networkable.setdefault(
                    name.lower(), (cls, file_str, lineno, False)
                )
        elif m := ACTIVE_SAFE_RE.match(stripped):
            cls, name = m.group(1), m.group(2)
            active_class = cls.lower()
            active_template = name
            seen_props_in_block.clear()
            if active_class in NETWORKED_CLASSES:
                block_has_networkable.setdefault(
                    name.lower(), (cls, file_str, lineno, False)
                )
        elif m := ACTIVE_RE.match(stripped):
            active_template = m.group(1)
            active_class = None
            seen_props_in_block.clear()
        elif m := ADD_TEMPLATE_RE.match(stripped):
            referenced_templates.append((m.group(1), file_str, lineno))

        if m := NETWORKABLE_RE.match(stripped):
            if active_template:
                key = active_template.lower()
                if key in block_has_networkable:
                    cls, fpath, lno, _ = block_has_networkable[key]
                    block_has_networkable[key] = (cls, fpath, lno, True)

        # Component creation matching
        if m := CREATE_COMP_RE.match(stripped):
            comp_name = m.group(1)
            if not comp_stack:
                issues.append(
                    Issue(
                        "WARNING",
                        file_str,
                        lineno,
                        "UNWRAPPED_COMPONENT",
                        f"ObjectTemplate.createComponent {comp_name} is not wrapped in BeginComp/EndComp.",
                    )
                )
            else:
                top_name, top_line, _ = comp_stack[-1]
                if top_name.lower() != comp_name.lower():
                    issues.append(
                        Issue(
                            "ERROR",
                            file_str,
                            lineno,
                            "COMP_MISMATCH",
                            f"createComponent {comp_name} does not match BeginComp:{top_name} (line {top_line}).",
                        )
                    )
                else:
                    comp_stack[-1] = (top_name, top_line, True)

        # Duplicate ObjectTemplate property lines in same active block
        if lower.startswith("objecttemplate.") and not any(
            lower.startswith(prefix)
            for prefix in (
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
        ):
            prop_key = lower.split()[0]
            if prop_key in seen_props_in_block:
                issues.append(
                    Issue(
                        "WARNING",
                        file_str,
                        lineno,
                        "DUPLICATE_PROPERTY",
                        f"Duplicate property `{prop_key}` in active block `{active_template or '<unknown>'}`.",
                    )
                )
            else:
                seen_props_in_block.add(prop_key)

        # CRD_EXPONENTIAL zero-mean trap
        for crd_match in CRD_EXP_RE.finditer(stripped):
            try:
                if float(crd_match.group(1)) == 0.0:
                    issues.append(
                        Issue(
                            "ERROR",
                            file_str,
                            lineno,
                            "CRD_EXP_ZERO_MEAN",
                            f"{crd_match.group(0)} always returns 0 because Number1 (mean) is 0 and Number2 is ignored.",
                        )
                    )
            except ValueError:
                pass

        # RPM divisibility by 1800
        if m := RPM_RE.match(stripped):
            rpm = int(m.group(1))
            if rpm <= 0 or 1800 % rpm != 0:
                issues.append(
                    Issue(
                        "WARNING",
                        file_str,
                        lineno,
                        "RPM_NOT_DIVISOR_OF_1800",
                        f"roundsPerMinute {rpm} does not divide evenly into 1800.",
                    )
                )

        # MagSize bounds
        if m := MAG_SIZE_RE.match(stripped):
            mag = int(m.group(1))
            if mag != -1 and (mag < 0 or mag > 1023):
                issues.append(
                    Issue(
                        "ERROR",
                        file_str,
                        lineno,
                        "MAGSIZE_OUT_OF_RANGE",
                        f"magSize {mag} exceeds BF2 engine limit (max 1023, or -1 for infinite).",
                    )
                )

        # Lightsource attenuationRange bounds
        if m := ATTEN_RE.match(stripped):
            val = float(m.group(1))
            if val > 100.0:
                issues.append(
                    Issue(
                        "WARNING",
                        file_str,
                        lineno,
                        "ATTENUATION_OVER_100",
                        f"attenuationRange value {val} exceeds 100 and may trigger engine errors.",
                    )
                )

        # GuiIndex tracking
        if m := GUI_INDEX_RE.match(stripped):
            template_gui_indices.append((int(m.group(1)), file_str, lineno))
        if m := HUD_SHOW_GUI_RE.match(stripped):
            hud_gui_indices.add(int(m.group(1)))

        # Legacy BF1942 SAI checks in .ai files
        if ext == ".ai":
            tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", stripped)
            for tok in tokens:
                tl = tok.lower()
                if tl in LEGACY_SAI_BROKEN:
                    issues.append(
                        Issue(
                            "ERROR",
                            file_str,
                            lineno,
                            "LEGACY_SAI_BROKEN",
                            f"Legacy BF1942 SAI conditional `{tok}` is missing from BF2 AIDLL.dll.",
                        )
                    )
                elif tl in LEGACY_SAI_ALWAYS_ZERO and "aistrategy." in lower:
                    issues.append(
                        Issue(
                            "WARNING",
                            file_str,
                            lineno,
                            "LEGACY_SAI_ZERO",
                            f"Legacy SAI conditional `{tok}` always evaluates to 0 in BF2 AIDLL.dll.",
                        )
                    )
            if "v_arg3" in lower and "< 13" in lower:
                issues.append(
                    Issue(
                        "ERROR",
                        file_str,
                        lineno,
                        "INVALID_V_ARG3_SAI",
                        "`v_arg3 < 13` is invalid in BF2 AIDLL.dll Strategic AI conditions.",
                    )
                )

        # Optional mod-root asset path verification
        if mod_root is not None:
            if m := ASSET_PATH_RE.search(stripped):
                rel_asset = m.group(1).replace("\\", "/")
                if "/" in rel_asset and not (mod_root / rel_asset).exists():
                    issues.append(
                        Issue(
                            "WARNING",
                            file_str,
                            lineno,
                            "MISSING_ASSET_PATH",
                            f"Asset `{rel_asset}` not found under {mod_root}.",
                        )
                    )

    if in_block_rem:
        issues.append(
            Issue(
                "ERROR",
                file_str,
                block_rem_start,
                "UNCLOSED_BEGINREM",
                "beginRem block not closed with endRem.",
            )
        )
    for line_num in if_stack:
        issues.append(
            Issue("ERROR", file_str, line_num, "UNCLOSED_IF", "`if` block not closed with `endIf`.")
        )
    for line_num in while_stack:
        issues.append(
            Issue(
                "ERROR",
                file_str,
                line_num,
                "UNCLOSED_WHILE",
                "`while` block not closed with `endWhile`.",
            )
        )
    for comp_name, line_num, _ in comp_stack:
        issues.append(
            Issue(
                "ERROR",
                file_str,
                line_num,
                "UNCLOSED_COMP",
                f"BeginComp:{comp_name} not closed with rem ---EndComp ---.",
            )
        )

    for key, (cls, fpath, lno, has_net) in block_has_networkable.items():
        if not has_net and ext == ".tweak":
            issues.append(
                Issue(
                    "WARNING",
                    fpath,
                    lno,
                    "MISSING_NETWORKABLE",
                    f"Networked class `{cls}` (`{key}`) has no `setNetworkableInfo` in this .tweak.",
                )
            )

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit PR:BF2 .con, .tweak, .inc, and .ai scripts for common errors."
    )
    parser.add_argument("paths", nargs="+", type=Path, help="Files or directories to audit.")
    parser.add_argument(
        "--mod-root",
        type=Path,
        default=None,
        help="Optional extracted mod root to check relative asset paths.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    args = parser.parse_args()

    files = collect_files(args.paths)
    if not files:
        print("No matching script files found.", file=sys.stderr)
        return 2

    defined_templates: dict[str, tuple[str, str, int]] = {}
    referenced_templates: list[tuple[str, str, int]] = []
    hud_gui_indices: set[int] = set()
    template_gui_indices: list[tuple[int, str, int]] = []
    all_issues: list[Issue] = []

    for path in files:
        all_issues.extend(
            audit_file(
                path,
                defined_templates,
                referenced_templates,
                hud_gui_indices,
                template_gui_indices,
                args.mod_root,
            )
        )

    # Cross-file checks when multiple files are scanned
    if len(files) > 1:
        for ref_name, fpath, lno in referenced_templates:
            if ref_name.lower() not in defined_templates:
                all_issues.append(
                    Issue(
                        "WARNING",
                        fpath,
                        lno,
                        "UNRESOLVED_ADDTEMPLATE",
                        f"addTemplate target `{ref_name}` was not created in scanned files.",
                    )
                )
        if hud_gui_indices:
            for gid, fpath, lno in template_gui_indices:
                if gid not in hud_gui_indices:
                    all_issues.append(
                        Issue(
                            "WARNING",
                            fpath,
                            lno,
                            "UNMATCHED_GUIINDEX",
                            f"GuiIndex {gid} has no matching hudBuilder.setNodeLogicShowVariable in scanned HUD files.",
                        )
                    )

    if args.json:
        print(json.dumps([asdict(i) for i in all_issues], indent=2))
    else:
        if not all_issues:
            print(f"OK: {len(files)} file(s) audited with 0 issues.")
        else:
            for issue in all_issues:
                print(
                    f"[{issue.severity}] {issue.file}:{issue.line} ({issue.code}): {issue.message}"
                )
            errors = sum(1 for i in all_issues if i.severity == "ERROR")
            warnings = sum(1 for i in all_issues if i.severity == "WARNING")
            print(f"\nSummary: {errors} error(s), {warnings} warning(s) across {len(files)} file(s).")

    return 1 if any(i.severity == "ERROR" for i in all_issues) else 0


if __name__ == "__main__":
    sys.exit(main())
