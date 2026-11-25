#!/usr/bin/env python3
"""Entry program for The Robot Pickup Line Championship.

Writes one pickup line (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
a robot's best attempt at romance. It involves a software
update, avoided commitment, and a restart.
"""

import os

LINE = (
    "Excuse me, are you running a background process? "
    "Because you've been on my mind using 100% of my CPU "
    "since you walked in."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
