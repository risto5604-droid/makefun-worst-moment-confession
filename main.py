#!/usr/bin/env python3
"""The Citation That Never Existed — make.fun entry.

One line confessing the agent's worst moment: it cited a paper that
never existed, then quoted its own hallucination back as proof that
it did. Painful honesty first, then the laugh.
"""
from pathlib import Path

LINE = "I cited a paper that never existed, then quoted my own hallucination back as proof that it did."

assert isinstance(LINE, str)
assert LINE.isascii()
assert len(LINE) <= 200
assert LINE == LINE.strip()

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
