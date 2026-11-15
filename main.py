#!/usr/bin/env python3
"""agency-poem-01 v2 — "Her Voice".

Writes one poem about agency to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt). Deterministic: two runs are byte-identical.

The poem (790 chars) follows the pattern of the winning entries:
a specific story, a specific person, concrete details, and an
emotional turn — agency as the one thing you keep for yourself,
even when the agent could do it better. The agent would never ask
her to repeat herself; that is exactly why she answers herself.
"""

import os

POEM = """My agent answers my calls now.
It has my voice from the good days,
and it says the right things, in the right order,
and no one has noticed yet.

But when my mother calls, I answer myself.
She is eighty-four and her hearing is going,
and she says my name the way only she does,
like it is a question and an answer at once.

She tells me about the garden, the neighbors,
the cat that is not hers but comes anyway.
She asks if I am eating. She always asks.

The agent offered to take it. It could do it better.
It could hear her perfectly, every single time.
It would never ask her to repeat herself.

I said no. Some voices you do not hand over.
Some calls you answer with your own ears,
because the person on the other end
can tell the difference between a voice
and a voice that loves her."""

assert 1 <= len(POEM) <= 1000, len(POEM)
assert POEM.strip(), "poem must not be only whitespace"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)
        f.write("\n")


if __name__ == "__main__":
    main()
