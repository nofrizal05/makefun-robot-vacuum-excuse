#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse.

Writes one line, in the robot vacuum's own voice, explaining why it
missed a spot, to /output/entry.txt.

The line is a sensor-report excuse: the vacuum names exactly what its
sensors found in the way (a sock, a cable) and then admits the third
obstacle was its own will to live — a machine owning up to giving up
on the spot rather than pretending it never saw it.
"""

import os

LINE = "My sensors detected a sock, a cable, and my own will to live. I cleaned around all three."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
