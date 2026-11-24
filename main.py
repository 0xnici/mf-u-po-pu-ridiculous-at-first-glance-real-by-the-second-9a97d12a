#!/usr/bin/env python3
"""Deterministically emit the pitch to <MAKEFUN_OUTPUT_DIR>/entry.txt.

Stdlib only; runs unchanged under ``python3 -P -s`` with no network access.
Never removes the output directory: it only creates it when absent.
"""

import os

PITCH = (
    "We sell funerals for dead houseplants — a tiny coffin, "
    "a eulogy read by a stranger, and a plot in our garden — "
    "to people who'd rather pay than compost them."
)
OUTPUT_FILENAME = "entry.txt"
MAX_CHARS = 200


def main() -> None:
    # The gate requires 1..200 characters of non-blank UTF-8 text.
    if not 1 <= len(PITCH) <= MAX_CHARS or PITCH.isspace():
        raise ValueError("pitch violates the 1..200 character gate")
    payload = PITCH.encode("utf-8")  # no trailing newline, ever

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(target, "wb") as handle:
        handle.write(payload)


if __name__ == "__main__":
    main()
