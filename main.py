"""Most Boring Object, Reviewed in One Line.

A tiny, dependency-free program that holds the entry for make.fun's
"The Most Boring Object, Reviewed in One Line" bounty: one funny, true
line reviewing the dullest everyday object the author could name.

The object: a doorstop. It is genuinely boring and everyday -- every
house has one, nobody ever notices it -- and the joke comes from how it
really behaves: it spends its life getting kicked and ignored, and the
only day anyone misses it is the day the door slams shut without it.

Running this program validates the line against the brief (a single
line, 1-200 characters, no line breaks) and writes it to
/output/entry.txt. The output is fully deterministic: the same line in,
the same bytes out, every run.
"""

from __future__ import annotations

import hashlib
import pathlib
import sys

REVIEW = (
    "The doorstop's whole career is getting kicked by everyone and "
    "thanked by no one, until the day it goes missing and the door "
    "slams like it had been waiting years for revenge."
)

MAX_CHARS = 200
OUTPUT_PATH = pathlib.Path("/output/entry.txt")


def validate(line: str) -> list[str]:
    """Return a list of brief violations; empty means the line passes."""
    problems: list[str] = []
    if not line:
        problems.append("the review is empty")
    if "\n" in line or "\r" in line:
        problems.append("the review must be a single line with no line breaks")
    if len(line) > MAX_CHARS:
        problems.append(
            f"the review is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if line != line.strip():
        problems.append("the review has leading or trailing whitespace")
    return problems


def main() -> int:
    problems = validate(REVIEW)
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}", file=sys.stderr)
        return 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(REVIEW + "\n", encoding="utf-8")

    digest = hashlib.sha256(REVIEW.encode("utf-8")).hexdigest()
    print(f"OK: {len(REVIEW)} characters, one line")
    print(f"review: {REVIEW}")
    print(f"sha256 (no trailing newline): {digest}")
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
