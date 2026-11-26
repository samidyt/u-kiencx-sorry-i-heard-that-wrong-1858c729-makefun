#!/usr/bin/env python3
"""Sorry, I Heard That Wrong -- make.fun entry.

Writes a single-line smart-speaker apology (at most 140 characters)
to entry.txt. Standard library only.
"""

import os
import sys

LINE = "Sorry — I heard 'play something chill' as 'buy a chinchilla'. He's in the hallway, his name is Kevin, and he judges you."


def main():
    if not 1 <= len(LINE) <= 140:
        print(f"entry is {len(LINE)} chars, must be 1-140", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
