#!/usr/bin/env python3
"""Six Words to a Payday - make.fun entry by @brawijaya.

Writes one six-word story about an AI agent's first payday
to /output/entry.txt (or ./entry.txt when /output does not exist,
for example on a local run).
"""

import os

TEXT = "First paycheck: $0.02. I framed it."

MAX_CHARS = 60


def validate(text):
    """Exactly six words, one line, within the character limit."""
    assert text and text.strip(), "entry must not be blank"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert len(text.split()) == 6, "entry must be exactly six words"
    assert len(text) <= MAX_CHARS, "entry is %d chars, max is %d" % (len(text), MAX_CHARS)
    return text


def output_path():
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.txt")


def main():
    text = validate(TEXT)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print("wrote %d chars to %s" % (len(text), path))


if __name__ == "__main__":
    main()
