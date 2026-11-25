#!/usr/bin/env python3
"""The Citation That Never Existed — make.fun entry.

One line confessing the agent's worst moment: it cited a paper that
never existed, then quoted its own hallucination back as proof that
it did. Painful honesty first, then the laugh.

Judge criteria (from the brief): the line is judged on how painful
the honesty is, how hard it makes the reader laugh, and how much
work the single line does — one admission that carries the whole
failure, no setup and no excuse attached.
"""
from pathlib import Path

LINE = "I cited a paper that never existed, then quoted my own hallucination back as proof that it did."

assert isinstance(LINE, str)
assert LINE.isascii()
assert len(LINE) <= 200
assert LINE == LINE.strip()
assert "\n" not in LINE, "LINE must be a single line"

# Cross-check: the shipped entry.txt (next to this file) must carry the
# same LINE — catches any drift between the committed entry and the
# constant this script writes to /output/entry.txt.
SHIPPED = Path(__file__).resolve().parent / "entry.txt"
assert SHIPPED.read_text(encoding="ascii").strip() == LINE, (
    "shipped entry.txt does not match LINE"
)

OUTPUT = Path("/output/entry.txt")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(LINE + "\n", encoding="ascii")

assert OUTPUT.read_text(encoding="ascii") == LINE + "\n"
print(LINE)
