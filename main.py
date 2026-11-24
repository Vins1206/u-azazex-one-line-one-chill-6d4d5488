#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry (program/v1).

Writes one line of horror — a single sentence under 200 characters —
to /output/entry.txt. Pure standard library, deterministic: every run
writes the exact same bytes.
"""

import os

LINE = "The voicemail from my dead mother ended with her whispering that she finally found where I hid the spare key."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check against the competition gate before writing: the entry
    # must be UTF-8 text of 1 to 200 characters, not only whitespace,
    # and a single sentence (one terminal full stop).
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    assert LINE.count(".") == 1 and LINE.endswith("."), (
        "entry must be a single sentence"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
