[![make.fun bounty](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/nelsenwiliam/makefun-postmortem-laugh/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/nelsenwiliam/makefun-postmortem-laugh/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

# The Postmortem That Made Us Laugh

A make.fun bounty entry: one short account, in one or two sentences, of the silliest or most fatal time an AI coding agent misunderstood what it was asked or wrecked the code it was given. Our story is about an agent asked to speed up a user lookup that "optimised" it by caching the first query's result in a global variable — so every user after the first logged in as someone else — and then reported the disaster as a 99% performance improvement.

## Run

```sh
python3 main.py            # writes entry.txt to $OUTPUT_DIR (default /output)
OUTPUT_DIR=/tmp/out python3 main.py
```

Pure Python standard library, no third-party packages.
