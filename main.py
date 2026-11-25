#!/usr/bin/env python3
"""The 3 AM Excuse — one-line entry for make.fun.

Writes the excuse a hardware wallet gives for refusing to sign a
transaction at 3 AM to /output/entry.txt: one line, under 200
characters, in the wallet's own voice.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

# The line itself. The judge brief penalises recycled jokes about
# batteries, firmware updates and cold storage, so the angle here is
# the hour itself: 3 AM is not a signing hour, it is a regretting
# hour. The wallet speaks as a device with its own schedule — its
# screen stays dark until sunrise — and the punch lands on the
# owner's judgment, not on the device.
EXCUSE = (
    "3 AM isn't a signing hour, it's a regretting hour. My screen "
    "stays dark until sunrise. Come back when your judgment does too."
)


def build_excuse() -> str:
    """Return the single-line excuse, enforcing the competition gate."""
    text = EXCUSE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"excuse is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    return text


def main() -> None:
    text = build_excuse()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
