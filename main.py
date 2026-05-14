#!/usr/bin/env python3
"""
JSON Diff CLI - Colorized JSON diff for terminal
Compare two JSON files and see the differences highlighted.

Usage:
    python main.py file1.json file2.json
    python main.py file1.json file2.json --format unified
"""

import argparse
import json
import sys
from typing import Any


def load_json(path: str) -> Any:
    with open(path) as f:
        return json.load(f)


def diff_json(a: Any, b: Any, path: str = "") -> list[str]:
    """Recursively diff two JSON values, return list of diff lines"""
    lines = []
    prefix = f"{path}: " if path else ""

    if type(a) != type(b):
        lines.append(f"- {prefix}{json.dumps(a)}")
        lines.append(f"+ {prefix}{json.dumps(b)}")
        return lines

    if isinstance(a, dict):
        all_keys = set(list(a.keys()) + list(b.keys()))
        for key in sorted(all_keys):
            child_path = f"{path}.{key}" if path else key
            if key not in a:
                lines.append(f"+ {child_path}: {json.dumps(b[key])}")
            elif key not in b:
                lines.append(f"- {child_path}: {json.dumps(a[key])}")
            else:
                lines.extend(diff_json(a[key], b[key], child_path))
    elif isinstance(a, list):
        max_len = max(len(a), len(b))
        for i in range(max_len):
            child_path = f"{path}[{i}]"
            if i >= len(a):
                lines.append(f"+ {child_path}: {json.dumps(b[i])}")
            elif i >= len(b):
                lines.append(f"- {child_path}: {json.dumps(a[i])}")
            else:
                lines.extend(diff_json(a[i], b[i], child_path))
    else:
        if a != b:
            lines.append(f"- {prefix}{json.dumps(a)}")
            lines.append(f"+ {prefix}{json.dumps(b)}")

    return lines


def colorize(line: str) -> str:
    """Add ANSI color codes to diff lines"""
    if line.startswith("-"):
        return f"\033[91m{line}\033[0m"  # Red
    elif line.startswith("+"):
        return f"\033[92m{line}\033[0m"  # Green
    return line


def main():
    parser = argparse.ArgumentParser(description="Colorized JSON diff for terminal")
    parser.add_argument("file1", help="First JSON file")
    parser.add_argument("file2", help="Second JSON file")
    parser.add_argument("--color", action="store_true", default=True, help="Enable color output (default: on)")
    parser.add_argument("--no-color", action="store_true", help="Disable color output")
    args = parser.parse_args()

    try:
        a = load_json(args.file1)
        b = load_json(args.file2)
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}", file=sys.stderr)
        sys.exit(1)

    diff_lines = diff_json(a, b)

    if not diff_lines:
        print("No differences found.")
        return

    use_color = args.color and not args.no_color
    for line in diff_lines:
        print(colorize(line) if use_color else line)

    print(f"\n{len(diff_lines)} difference(s) found.")


if __name__ == "__main__":
    main()
