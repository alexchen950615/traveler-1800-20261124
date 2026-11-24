#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 -- make.fun bounty entry.

Writes a single sentence (at most 200 characters) explaining the modern
internet to someone arriving from the year 1800, using only words and
images a person of that year could already picture.
"""

import os

ENTRY = (
    "Imagine all the world's libraries and post offices joined by a single "
    "road of lightning, so that any book or letter you ask for is in your "
    "hands before you finish speaking."
)


def main() -> None:
    # The gate allows 1 to 200 characters; one sentence only.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.count(".") == 1, "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
