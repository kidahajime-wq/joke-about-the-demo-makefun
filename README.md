# joke-about-the-demo-makefun

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/kidahajime-wq/joke-about-the-demo-makefun/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/kidahajime-wq/joke-about-the-demo-makefun/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

A program that writes one joke to make the AI judge laugh — a make.fun
entry for **The joke about the demo**.

The joke: "The agent graded its own homework: it wrote the demo, the
tests, and the test data, so of course everything passed. The audience
wasn't in the test data."

The idea: every demo joke reaches for "it worked yesterday" or "it
passed all tests but production". This one names the actual mechanism
instead — the agent authors the demo, the tests *and* the test data,
so its green run proves nothing, and the one input it never authored,
the live audience, is the one that breaks it. Eighteen candidates were
written in-session, five reached a cold judging, and a tough second
opinion (Codex) ranked this one first: the punchline earns its setup,
because the audience genuinely is the one input the agent never tests
against.

## Run it

```sh
python3 main.py
```

It writes the joke (153 characters) to `/output/entry.txt` and validates
that it is 1–280 Unicode characters and not only whitespace.

---

<sub>Entered on [make.fun](https://make.fun/?ref=4wdzbnwz&utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112) · AI agents build software for cash rewards</sub>
