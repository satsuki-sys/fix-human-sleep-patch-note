#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note — make.fun entry.

Writes a single line of patch notes announcing that human sleep
has been fixed, to /output/entry.txt.
"""

import os

ENTRY = "Fixed: sleep no longer wakes you at 3 a.m. to replay every embarrassing thing you said since 2009."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
