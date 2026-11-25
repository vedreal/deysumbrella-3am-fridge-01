#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun bounty entry.

Writes one line of text to /output/entry.txt: the message a smart fridge
sends its owner at 3am. The house gate requires UTF-8 text of 1 to 140
characters, not only whitespace.
"""

import os

LINE = (
    "It's 3am. That sandwich has been in my light for six minutes. "
    "Either eat it or marry it, I have things to chill."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE
    if not (1 <= len(text) <= 140):
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    # Pure ASCII keeps the byte count equal to the character count, which
    # matters for the tie-break (smaller text, fewer bytes, places first).
    try:
        encoded = text.encode("ascii")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be pure ASCII") from exc
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(encoded)
    # Read back and verify what landed on disk is exactly the validated text.
    with open(OUTPUT_PATH, "rb") as fh:
        if fh.read() != encoded:
            raise ValueError("verification failed: /output/entry.txt mismatch")


if __name__ == "__main__":
    main()
