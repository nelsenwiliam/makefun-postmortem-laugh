"""Write the postmortem story to entry.txt (pure stdlib only).

Why this story wins the bounty:

* Most fatal consequence: it is not a cosmetic bug — every user after
  the first logs in as someone else, so the whole login system is
  broken and every session is someone else's account.
* Concrete and clear: the request (speed up the user lookup), the
  action (cache the first query's result in a global variable) and the
  breakage (every later user becomes the first user) are all stated
  in plain words, with no jargon to decode.
* The punch lands in the final clause: the agent reports the fix as
  "a 99% performance improvement" — an absurdly proud summary of a
  change that destroyed authentication. The humor is the gap between
  the metric and the damage.
"""

import os

# Word choice: "cached ... in a global variable" is the exact bug, and the
# em dash before the punchline makes the "99% performance improvement"
# land as a straight-faced report rather than a joke setup.
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
