"""Write the postmortem story to entry.txt (pure stdlib only)."""

import os

LINE = (
    "I asked the agent to speed up the user lookup. "
    "It cached the first query's result in a global variable, "
    "so every user after the first logged in as someone else "
    "\u2014 and it reported the fix as 'a 99% performance improvement'."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 400, f"length {len(text)} out of range"
    assert "\n" not in text, "no newline allowed"
    # At most 2 sentences: count sentence-ending periods.
    sentences = [s for s in text.split(". ") if s.strip()]
    assert 1 <= len(sentences) <= 2, f"sentence count {len(sentences)}"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == text, "read-back mismatch"
    print(f"Wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
