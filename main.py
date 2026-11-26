#!/usr/bin/env python3
"""Sorry, I Heard That Wrong -- make.fun entry.

Writes a single-line smart-speaker apology (at most 140 characters)
to entry.txt. Standard library only.
"""

import os
import sys

MAX_CHARS = 140

LINE = "Sorry — I heard 'play something chill' as 'buy a chinchilla'. He's in the hallway, his name is Kevin, and he judges you."


def validate(line):
    """Mirror the sealed gate: 1-140 chars, not only whitespace, one line."""
    if not 1 <= len(line) <= MAX_CHARS:
        return f"entry is {len(line)} chars, must be 1-{MAX_CHARS}"
    if not line.strip():
        return "entry is only whitespace"
    if "\n" in line or "\r" in line:
        return "entry must be a single line"
    return None


def main():
    problem = validate(LINE)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
