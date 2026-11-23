"""One Letter for Your Day.

Writes exactly one letter, A-Z and nothing else, to /output/entry.txt.

The letter is H, for "haywire": the day went haywire. Every plan, gadget
and good intention misfired at once, in that funny, specific way a day
goes sideways and you can only laugh at it. H is the sharp initial for
it, not the obvious happy or horrible.
"""

import os

LETTER = "H"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if LETTER not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        raise ValueError("LETTER must be a single uppercase letter A-Z")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Self-check: the gate wants exactly one UTF-8 letter, nothing else.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        if f.read() != LETTER:
            raise ValueError("entry.txt is not exactly the chosen letter")


if __name__ == "__main__":
    main()
