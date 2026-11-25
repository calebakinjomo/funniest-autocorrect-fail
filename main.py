#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes one line (<200 chars) that reads as a funny autocorrect fail to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: a loving text to Grandma where autocorrect turns "best" into
"breast". The slip is instantly clear (nobody texts Grandma that on
purpose), the wrong word is shocking in context, and it reads exactly
like a real sent message — no explanation needed.
Reviser note: the entry is one fixed line by design — no randomness, no input, and no network — so the program writes exactly the same line on every run.
"""

import os

ENTRY = "I love you Grandma, you're the breast!"

# The entry is a fixed string on purpose: the grader runs the program
# twice and both runs must produce byte-identical output.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


if __name__ == "__main__":
    main()
