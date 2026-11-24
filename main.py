#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) to out/entry.txt:
an explanation of the modern internet built only from things a
person from 1800 already knows -- a road, a letter, a library.
No word coined after the traveler's time.
"""

import os

ENTRY = (
    "It is a road of thin copper wire joining every town on earth, "
    "so a letter you write can reach any house in the world in the "
    "time of one blink, and every book ever printed waits upon a "
    "shelf for you."
)


# Words coined after 1800 that must never appear in the entry.
BANNED_AFTER_1800 = {
    "internet", "computer", "website", "email", "phone", "telephone",
    "telegraph", "screen", "digital", "online", "software", "data",
    "electric", "electricity", "wireless", "signal", "network",
}


def validate_entry(text: str) -> None:
    """Enforce the sealed gate: 1-200 chars, one sentence, no post-1800 words."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    words = {w.strip(".,;:!?").lower() for w in text.split()}
    bad = words & BANNED_AFTER_1800
    if bad:
        raise ValueError(f"entry uses words coined after 1800: {sorted(bad)}")


def main() -> None:
    validate_entry(ENTRY)
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"chars: {len(ENTRY)}")


if __name__ == "__main__":
    main()
