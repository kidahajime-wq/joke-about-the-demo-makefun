#!/usr/bin/env python3
"""The joke about the demo.

Writes one joke to /output/entry.txt: a single line about working with
an AI coding agent, for an AI judge that has read thousands of generic
AI jokes.

Candidates written in-session: 18 (see candidates.md). Cold judging
picked five finalists; Codex, as a tough comedy second opinion, ranked
them B > A > C > E > D -- the "graded its own homework" draft first,
because the punchline earns its setup: the audience genuinely is the
one input the agent never tests against. Codex also caught that
finalist D miscounts ("Let me just quickly fix that" is six words, not
three), which killed it. The final takes Codex's tightening (the
contraction in the kicker) and keeps the "graded its own homework"
frame, which primes the self-grading insight in four words.
Final text, 153 characters, verified by running this program.

Why this one, not the obvious: every demo joke reaches for "it worked
yesterday" or "it passed all tests but production". This one names the
actual mechanism: the agent authors the demo, the tests AND the test
data, so its green run proves nothing -- and the one input it never
authored, the live audience, is the one that breaks it.
"""

import os
import sys

ENTRY = (
    "The agent graded its own homework: it wrote the demo, the tests, "
    "and the test data, so of course everything passed. The audience "
    "wasn't in the test data."
)


def main() -> int:
    chars = len(ENTRY)
    if not 1 <= chars <= 280:
        print(f"entry is {chars} characters, must be 1-280", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {chars} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
