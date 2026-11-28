#!/usr/bin/env python3
"""Trace ObjectTemplate hierarchy and include/run execution chains."""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass, field
import json
from pathlib import Path
import re
import sys


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
CREATE_COMPONENT_PATTERN = re.compile(
    r"^objecttemplate\.createcomponent\s+(\S+)",
    re.IGNORECASE,
)
INCLUDE_DIRECTIVE_PATTERN = re.compile(
    r"^include\s+([^\s]+)",
    re.IGNORECASE,
)
RUN_DIRECTIVE_PATTERN = re.compile(
    r"^run\s+([^\s]+)(?:\s+(.*))?",
    re.IGNORECASE,
)


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


def resolve_script_path(
    target_path_str: str,
    current_file: Path,
    mod_root: Path | None,
) -> Path | None:
    """Resolve an include/run path relative to current_file or mod_root."""
    relative_path = Path(target_path_str.replace("\\", "/"))
    candidate_paths = [current_file.parent / relative_path]

    if not relative_path.suffix:
        candidate_paths.append(
            current_file.parent / f"{relative_path}.txt"
        )
    if mod_root is not None:
        candidate_paths.append(mod_root / relative_path)

    for candidate_path in candidate_paths:
        if candidate_path.is_file():
            return candidate_path
    return None


def trace_script_file(
    script_path: Path,
    mod_root: Path | None,
    templates: dict[str, TemplateNode],
    execution_steps: list[ExecutionStep],
    visited_paths: set[Path],
) -> None:
    """Recursively trace a PR:BF2 script file and follow include/run."""
    resolved_path = script_path.resolve()
    if resolved_path in visited_paths:
        return
    visited_paths.add(resolved_path)

    file_lines = script_path.read_text(
        encoding="utf-8",
        errors="replace",
    ).splitlines()
    in_block_comment = False
    active_template_key: str | None = None

    for raw_line in file_lines:
        stripped_line = raw_line.strip()
        if not stripped_line:
            continue

        lowercase_line = stripped_line.lower()
        if lowercase_line == "beginrem":
            in_block_comment = True
            continue
        if lowercase_line == "endrem":
            in_block_comment = False
            continue
        if (
            in_block_comment
            or lowercase_line.startswith("rem ")
            or lowercase_line == "rem"
            or stripped_line.startswith("#")
        ):
            continue

        include_match = INCLUDE_DIRECTIVE_PATTERN.match(stripped_line)
        if include_match is not None:
            target_path_str = include_match.group(1)
            next_script = resolve_script_path(
                target_path_str=target_path_str,
                current_file=script_path,
                mod_root=mod_root,
            )
            execution_steps.append(
                ExecutionStep(
                    directive="include",
                    target=target_path_str,
                    scope="shared",
                    args=[],
                    caller=str(script_path),
                    resolved=next_script is not None,
                )
            )
            if next_script is not None:
                trace_script_file(
                    script_path=next_script,
                    mod_root=mod_root,
                    templates=templates,
                    execution_steps=execution_steps,
                    visited_paths=visited_paths,
                )
            continue

        run_match = RUN_DIRECTIVE_PATTERN.match(stripped_line)
        if run_match is not None:
            target_path_str = run_match.group(1)
            raw_arguments = run_match.group(2)
            parsed_arguments = raw_arguments.split() if raw_arguments else []
            next_script = resolve_script_path(
                target_path_str=target_path_str,
                current_file=script_path,
                mod_root=mod_root,
            )
            execution_steps.append(
                ExecutionStep(
                    directive="run",
                    target=target_path_str,
                    scope="isolated",
                    args=parsed_arguments,
                    caller=str(script_path),
                    resolved=next_script is not None,
                )
            )
            if next_script is not None:
                trace_script_file(
                    script_path=next_script,
                    mod_root=mod_root,
                    templates=templates,
                    execution_steps=execution_steps,
                    visited_paths=visited_paths,
                )
            continue

        create_match = CREATE_TEMPLATE_PATTERN.match(stripped_line)
        active_safe_match = ACTIVE_SAFE_PATTERN.match(stripped_line)
        active_match = ACTIVE_TEMPLATE_PATTERN.match(stripped_line)
        add_template_match = ADD_TEMPLATE_PATTERN.match(stripped_line)
        create_comp_match = CREATE_COMPONENT_PATTERN.match(stripped_line)

        if create_match is not None:
            template_class = create_match.group(1)
            template_name = create_match.group(2)
            active_template_key = template_name.lower()
            template_node = templates.setdefault(
                active_template_key,
                TemplateNode(
                    name=template_name,
                    template_class=template_class,
                    defined_in=str(script_path),
                ),
            )
            template_node.template_class = template_class
            if not template_node.defined_in:
                template_node.defined_in = str(script_path)
        elif active_safe_match is not None:
            template_class = active_safe_match.group(1)
            template_name = active_safe_match.group(2)
            active_template_key = template_name.lower()
            template_node = templates.setdefault(
                active_template_key,
                TemplateNode(
                    name=template_name,
                    template_class=template_class,
                    defined_in=str(script_path),
                ),
            )
            if template_node.template_class == "Unknown":
                template_node.template_class = template_class
        elif active_match is not None:
            template_name = active_match.group(1)
            active_template_key = template_name.lower()
            templates.setdefault(
                active_template_key,
                TemplateNode(
                    name=template_name,
                    defined_in=str(script_path),
                ),
            )
        elif add_template_match is not None:
            if (
                active_template_key is not None
                and active_template_key in templates
            ):
                templates[active_template_key].children.append(
                    add_template_match.group(1)
                )
        elif create_comp_match is not None:
            if (
                active_template_key is not None
                and active_template_key in templates
            ):
                templates[active_template_key].components.append(
                    create_comp_match.group(1)
                )
        elif (
            lowercase_line.startswith("objecttemplate.")
            and active_template_key is not None
            and active_template_key in templates
        ):
            templates[active_template_key].properties.append(stripped_line)


def parse_arguments() -> argparse.Namespace:
    """Parse CLI arguments for the PR:BF2 template tracer."""
    parser = argparse.ArgumentParser(
        description=(
            "Trace ObjectTemplate hierarchy and include/run chains in "
            "PR:BF2 scripts."
        )
    )
    parser.add_argument(
        "entry_file",
        type=Path,
        help="Entry .con or .tweak file.",
    )
    parser.add_argument(
        "--mod-root",
        type=Path,
        default=None,
        help=(
            "Optional extracted mod root for resolving include/run paths."
        ),
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON output.",
    )
    return parser.parse_args()


def main() -> int:
    """Entry point for tracing ObjectTemplate hierarchies."""
    arguments = parse_arguments()

    if not arguments.entry_file.is_file():
        print(
            f"File not found: {arguments.entry_file}",
            file=sys.stderr,
        )
        return 2

    templates: dict[str, TemplateNode] = {}
    execution_steps: list[ExecutionStep] = []
    trace_script_file(
        script_path=arguments.entry_file,
        mod_root=arguments.mod_root,
        templates=templates,
        execution_steps=execution_steps,
        visited_paths=set(),
    )

    if arguments.json:
        serialized_templates = {
            template_key: asdict(template_node)
            for template_key, template_node in templates.items()
        }
        serialized_steps = [asdict(step) for step in execution_steps]
        payload = {
            "entry": str(arguments.entry_file),
            "execution_chain": serialized_steps,
            "templates": serialized_templates,
        }
        print(json.dumps(payload, indent=2))
        return 0

    print(f"Entry: {arguments.entry_file}")
    if execution_steps:
        print("\nExecution Chain:")
        for step in execution_steps:
            status_label = "resolved" if step.resolved else "unresolved"
            arg_suffix = f" args={step.args}" if step.args else ""
            print(
                f"  - {step.directive} {step.target} "
                f"[{step.scope} scope, {status_label}]{arg_suffix}"
            )

    print("\nTemplates:")
    for template_node in templates.values():
        print(
            f"  - {template_node.name} ({template_node.template_class}) "
            f"[{template_node.defined_in}]"
        )
        if template_node.components:
            component_list = ", ".join(template_node.components)
            print(f"      components: {component_list}")
        if template_node.children:
            children_list = ", ".join(template_node.children)
            print(f"      children:   {children_list}")
        print(f"      properties: {len(template_node.properties)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
