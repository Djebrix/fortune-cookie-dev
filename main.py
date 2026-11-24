"""Fortune-cookie wisdom for a software developer.

One original line, written to entry.txt.
"""

import os

TEXT = "The code you delete today is the only feature that can never break in production."


def main():
    line = TEXT.strip()
    assert 1 <= len(line) <= 120, "line must be 1-120 characters"
    assert line, "line must not be blank"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
