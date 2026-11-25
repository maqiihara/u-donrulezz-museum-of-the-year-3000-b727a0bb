#!/usr/bin/env python3
"""Museum of the Year 3000 -- one museum label from the year 3000.

Writes a single label, at most 200 characters, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR). Standard library only; no network, no
randomness: the same label comes out of every run.
"""
import os

LABEL = (
    "Traffic Light Test, c. 2024. To prove they were human, people "
    "identified traffic lights in photographs. The machines passed "
    "every time. The people did not."
)


def main():
    # The gate requires 1-200 characters; fail loudly if we drift.
    assert 1 <= len(LABEL) <= 200, len(LABEL)
    assert LABEL.strip(), "label must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
