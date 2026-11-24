"""Entry for make.fun's "Monday, Reviewed in One Line" bounty.

Writes one funny one-line review of Monday to entry.txt in the output
directory (1-200 UTF-8 characters, single line). The same bytes are
written on every run.
"""

import os

# Draft: "Monday gave my weekend one star, then booked a 9 a.m. meeting
# to discuss why I was still tired."
# Revised: flip the review — I rate Monday one star, Monday retaliates
# by moving the meeting earlier and marking the weekend unresolved.
# The turn lands harder and the concrete detail (9 a.m. moved to 8)
# is the punchline itself.
LINE = (
    "I rated Monday one star; it replied by moving my 9 a.m. meeting "
    "to 8 and marking my weekend unresolved."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
