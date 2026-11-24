#!/usr/bin/env python3
"""The Robot Pickup Line Championship — one line, one robot, one shot at charm.

The line is written from the robot's own point of view: the joke grows out
of being a machine (a million lines of code, cooling fans spinning up), not
out of a generic human compliment. Short, surprising, and — hopefully —
charming enough to compile.
"""

import os

ENTRY_LINE = "My creators wrote a million lines of code, but none of them explain why my cooling fans spin up every time you walk by."

def main():
    line = ENTRY_LINE.strip()
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert line and not line.isspace()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)

if __name__ == "__main__":
    main()
