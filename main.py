#!/usr/bin/env python3
"""Everyday Wonder — write the winning sentence to /output/entry.txt.

The sentence: "My shadow arrived home before I did and was already waiting
by the door." (72 characters, one sentence, well inside the 200 cap.)
"""

import os
import sys

LINE = "My shadow arrived home before I did and was already waiting by the door."

# Gate (kit RULES.txt): /output/entry.txt must be UTF-8 text of 1-200
# characters, not only white space.


def validate(line):
    """Fail loudly before writing anything invalid."""
    if line != line.strip():
        print("error: line must not have leading or trailing white space", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if not line.strip():
        print("error: line must not be only white space", file=sys.stderr)
        sys.exit(1)
    char_count = len(line)
    if not 1 <= char_count <= 200:
        print(
            f"error: line must be 1-200 characters, got {char_count}: {line!r}",
            file=sys.stderr,
        )
        sys.exit(1)
    if line.count(".") != 1 or not line.endswith("."):
        print(
            f"error: entry must be a single sentence: {line!r}",
            file=sys.stderr,
        )
        sys.exit(1)
    print(f"entry: {char_count} characters, 1 sentence", file=sys.stderr)


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
