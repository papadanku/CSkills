#!/usr/bin/env python3
"""Trace ObjectTemplate hierarchy, components, and include/run execution chains."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

CREATE_RE = re.compile(r"^objecttemplate\.create\s+(\S+)\s+(\S+)", re.IGNORECASE)
ACTIVE_SAFE_RE = re.compile(r"^objecttemplate\.activesafe\s+(\S+)\s+(\S+)", re.IGNORECASE)
ACTIVE_RE = re.compile(r"^objecttemplate\.active\s+(\S+)", re.IGNORECASE)
ADD_TEMPLATE_RE = re.compile(r"^objecttemplate\.addtemplate\s+(\S+)", re.IGNORECASE)
CREATE_COMP_RE = re.compile(r"^objecttemplate\.createcomponent\s+(\S+)", re.IGNORECASE)
INCLUDE_RE = re.compile(r"^include\s+([^\s]+)", re.IGNORECASE)
RUN_RE = re.compile(r"^run\s+([^\s]+)(?:\s+(.*))?", re.IGNORECASE)


@dataclass
class TemplateNode:
    """Represents a traced ObjectTemplate and its properties/children."""

    name: str
    template_class: str = "Unknown"
    defined_in: str = ""
    children: list[str] = field(default_factory=list)
    components: list[str] = field(default_factory=list)
    properties: list[str] = field(default_factory=list)


@dataclass
class ExecutionStep:
    """Represents an include or run directive encountered during tracing."""

    directive: str
    target: str
    scope: str
    args: list[str]
    caller: str
    resolved: bool


def resolve_script(target: str, current_file: Path, mod_root: Path | None) -> Path | None:
    """Resolve an include/run path relative to current file or mod root."""
    rel = Path(target.replace("\\", "/"))
    candidates = [current_file.parent / rel]
    if not rel.suffix:
        candidates.append(current_file.parent / f"{rel}.txt")
    if mod_root is not None:
        candidates.append(mod_root / rel)
    for cand in candidates:
        if cand.is_file():
            return cand
    return None


def trace_file(
    path: Path,
    mod_root: Path | None,
    templates: dict[str, TemplateNode],
    steps: list[ExecutionStep],
    visited: set[Path],
) -> None:
    """Recursively trace a PR:BF2 script file."""
    resolved_path = path.resolve()
    if resolved_path in visited:
        return
    visited.add(resolved_path)

    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    in_block_rem = False
    active_key: str | None = None

    for raw_line in lines:
        stripped = raw_line.strip()
        if not stripped:
            continue
        lower = stripped.lower()

        if lower == "beginrem":
            in_block_rem = True
            continue
        if lower == "endrem":
            in_block_rem = False
            continue
        if in_block_rem or lower.startswith("rem ") or lower == "rem" or stripped.startswith("#"):
            continue

        if m := INCLUDE_RE.match(stripped):
            target = m.group(1)
            next_file = resolve_script(target, path, mod_root)
            steps.append(
                ExecutionStep("include", target, "shared", [], str(path), next_file is not None)
            )
            if next_file is not None:
                trace_file(next_file, mod_root, templates, steps, visited)
            continue

        if m := RUN_RE.match(stripped):
            target = m.group(1)
            raw_args = m.group(2).split() if m.group(2) else []
            next_file = resolve_script(target, path, mod_root)
            steps.append(
                ExecutionStep("run", target, "isolated", raw_args, str(path), next_file is not None)
            )
            if next_file is not None:
                trace_file(next_file, mod_root, templates, steps, visited)
            continue

        if m := CREATE_RE.match(stripped):
            cls, name = m.group(1), m.group(2)
            active_key = name.lower()
            node = templates.setdefault(
                active_key, TemplateNode(name=name, template_class=cls, defined_in=str(path))
            )
            node.template_class = cls
            if not node.defined_in:
                node.defined_in = str(path)
        elif m := ACTIVE_SAFE_RE.match(stripped):
            cls, name = m.group(1), m.group(2)
            active_key = name.lower()
            node = templates.setdefault(
                active_key, TemplateNode(name=name, template_class=cls, defined_in=str(path))
            )
            if node.template_class == "Unknown":
                node.template_class = cls
        elif m := ACTIVE_RE.match(stripped):
            name = m.group(1)
            active_key = name.lower()
            templates.setdefault(active_key, TemplateNode(name=name, defined_in=str(path)))
        elif m := ADD_TEMPLATE_RE.match(stripped):
            if active_key and active_key in templates:
                templates[active_key].children.append(m.group(1))
        elif m := CREATE_COMP_RE.match(stripped):
            if active_key and active_key in templates:
                templates[active_key].components.append(m.group(1))
        elif lower.startswith("objecttemplate.") and active_key and active_key in templates:
            templates[active_key].properties.append(stripped)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Trace ObjectTemplate hierarchy and include/run chains in PR:BF2 scripts."
    )
    parser.add_argument("entry_file", type=Path, help="Entry .con or .tweak file.")
    parser.add_argument(
        "--mod-root",
        type=Path,
        default=None,
        help="Optional extracted mod root for resolving include/run paths.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    args = parser.parse_args()

    if not args.entry_file.is_file():
        print(f"File not found: {args.entry_file}", file=sys.stderr)
        return 2

    templates: dict[str, TemplateNode] = {}
    steps: list[ExecutionStep] = []
    trace_file(args.entry_file, args.mod_root, templates, steps, set())

    if args.json:
        payload = {
            "entry": str(args.entry_file),
            "execution_chain": [asdict(s) for s in steps],
            "templates": {k: asdict(v) for k, v in templates.items()},
        }
        print(json.dumps(payload, indent=2))
        return 0

    print(f"Entry: {args.entry_file}")
    if steps:
        print("\nExecution Chain:")
        for step in steps:
            status = "resolved" if step.resolved else "unresolved"
            arg_str = f" args={step.args}" if step.args else ""
            print(
                f"  - {step.directive} {step.target} [{step.scope} scope, {status}]{arg_str}"
            )

    print("\nTemplates:")
    for node in templates.values():
        print(f"  - {node.name} ({node.template_class}) [{node.defined_in}]")
        if node.components:
            print(f"      components: {', '.join(node.components)}")
        if node.children:
            print(f"      children:   {', '.join(node.children)}")
        print(f"      properties: {len(node.properties)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
