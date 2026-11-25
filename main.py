#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun bounty entry.

Writes exactly one commit message (<= 200 characters) to entry.txt
in the output directory.
"""

import os

COMMIT_MESSAGE = (
    'fix: revert the 3 AM deploy \u2014 "one-line change" took down prod; '
    "tested in prod because staging was asleep"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)

    message = COMMIT_MESSAGE.strip()
    assert len(message) <= 200, f"commit message too long: {len(message)} chars"

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(message + "\n")


if __name__ == "__main__":
    main()
