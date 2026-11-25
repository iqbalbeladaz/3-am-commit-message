#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun bounty entry.

Writes one commit message to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: the same bytes on every run, no input, no randomness, no
network. Standard library only.

The message: an AI agent's own status line up front — "confidence 0.97,
tests 0" — then the confession and the punchline: it tested in production
at 3 AM because staging was asleep. The humour is agent-shaped all the way
down: only a model reports a confidence score next to a zero test count,
only an agent treats "staging was asleep" as a reasonable excuse, and only
an agent files that as a fix(prod) commit at 3 AM. It reads like a real
commit message (conventional-commit scope, admission + implied revert in
the fix), lands a real punchline about the 3 AM outage instead of a wry
"oops", and avoids the stock lines — no "please work", no "oops", no
"it works on my machine".
"""

import os
from pathlib import Path

ENTRY = (
    "fix(prod): confidence 0.97, tests 0 \u2014 I tested in production at 3 AM "
    "because staging was asleep"
)

# Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
