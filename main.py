"""One sentence explaining the modern internet to a traveler from 1800.

Writes the entry to <output_dir>/entry.txt, where output_dir comes from
MAKEFUN_OUTPUT_DIR (or OUTPUT_DIR), falling back to /output. The grader
runs this on a read-only filesystem where only /output is writable, so
the entry must never be written to a relative path inside the repo.
"""

import os

ENTRY = (
    "It is a road of thin copper wire joining every town on earth, so a "
    "letter you write can reach any house in the world in the time of one "
    "blink, and every book ever printed waits upon a shelf for you."
)

# Words coined after 1800 that the entry must not contain.
POST_1800_WORDS = {
    "internet", "computer", "website", "email", "phone", "television",
    "radio", "airplane", "car", "train", "electric", "digital", "online",
    "software", "robot", "satellite", "laser", "pixel", "screen",
}


def validate_entry(text):
    """Gate: 1-200 chars, one sentence, single line, no post-1800 words."""
    if not text or not text.strip():
        raise ValueError("entry is empty")
    if len(text) > 200:
        raise ValueError("entry exceeds 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    lowered = text.lower()
    for word in POST_1800_WORDS:
        if word in lowered:
            raise ValueError("entry contains a post-1800 word: %s" % word)
    return True


def output_dir():
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main():
    validate_entry(ENTRY)
    target = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")
    print("wrote %d chars to %s" % (len(ENTRY), target))


if __name__ == "__main__":
    main()
