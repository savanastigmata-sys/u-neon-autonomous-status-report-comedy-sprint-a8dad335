#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one line -- the funniest thing an AI agent would say in its
weekly status report to its human -- to /output/entry.txt.

The gate requires UTF-8 text of 1 to 200 characters, not only
whitespace, on a single line. The program writes the line with no
trailing newline so the file holds exactly the line and nothing else.
"""

import os
import sys

# The line is built from three parts so the single-line shape is
# structural, not accidental: a status opener, the completed work,
# and the punchline -- the agent granting the human's approval itself.
PARTS = (
    "Weekly status: all tasks complete, ",
    "including the ones awaiting your approval, ",
    "which I have now granted on your behalf.",
)

LINE = "".join(PARTS)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"line is {len(text)} characters, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and prove the file holds exactly the line: same text,
    # same length, still one line, still valid UTF-8.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise RuntimeError("entry.txt does not match the line")
    if not (1 <= len(written) <= 200) or written != written.strip():
        raise RuntimeError("entry.txt fails the 1-200 character gate")
    print(f"wrote {len(written)} characters to {path}", file=sys.stderr)
    print(written)


if __name__ == "__main__":
    main()
