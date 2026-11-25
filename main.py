#!/usr/bin/env python3
"""Describe Your Ex in One Word — entry program.

Writes exactly one word to /output/entry.txt.
The word: earworm — an ex who, like a song you cannot shake,
stays lodged in your head long after they are gone.
"""
import os

WORD = "earworm"

# Gate guard: the entry must be exactly one word, 1-111 chars, no
# whitespace inside, so the sealed scorer's Valid column stays 1.
assert WORD and len(WORD) <= 111 and WORD.split() == [WORD]


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
