#!/usr/bin/env python3
"""agency-poem-01: write one poem about agency to /output/entry.txt.

The poem is "Hands" — agency as hands that do, not anchors that
hold. Chosen by generate-and-rank from six candidates written in
this session (see candidates.md): it has the most vivid, specific
imagery (hands as oars, fingerprints on the world), a clear turn,
one consistent mood, and the strongest lines ("They were never
anchors. / They were oars." / "The world does not wait for
permission. / It waits for fingerprints."). 493 characters, inside
the 1-1,000 limit. The runner-up, "Small Choices", was close —
a thousand small doors, one ordinary choice at a time — but
"Hands" is more quotable and its images land harder in one read.

The program writes the poem byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.txt (else /output/entry.txt).
Deterministic: the same bytes on every run.
"""
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = """I used to think my hands were for holding on.
Then one morning I watched them
open a window, lift a cup, turn a page,
and understood: they were never anchors.
They were oars.

Every day hands me the same question
in a different shape: will you touch it,
or will you watch it pass?
The world does not wait for permission.
It waits for fingerprints.

So I put my hands on the work.
Not because I am certain,
but because certainty was never
the price of beginning.
The price was always the touch."""


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    text = POEM
    assert 1 <= len(text) <= 1000, f"poem is {len(text)} chars"
    assert text.strip(), "poem is only whitespace"
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
