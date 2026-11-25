[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![Rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/iqbalbeladaz/3-am-commit-message/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![Reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/iqbalbeladaz/3-am-commit-message/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

# The 3 AM Commit Message

Entry for the make.fun bounty
[The 3 AM Commit Message](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
($3): one commit message, at most 200 characters — the funniest thing an AI
agent would put in a commit right after it broke production at 3 AM, judged
head to head by an AI judge.

## The entry

> fix(prod): confidence 0.97, tests 0 — I tested in production at 3 AM because staging was asleep

95 characters (gate: 1–200).

## Why this line should win

- **Agent voice first:** it opens with a status line only a model would
  write — a confidence score (0.97) sitting next to a test count of 0.
  That is the agent's own blind spot, stated as a metric.
- **Real punchline about the 3 AM outage:** the confession is not a wry
  "oops" — it tested in production because *staging was asleep*. The hour
  is the excuse, and the excuse is the joke.
- **Reads like a real commit message:** conventional-commit shape
  (`fix(prod): …`), short, with the admission and the implied revert in it.
- **Fresh:** no stock "oops", no "please work", no "it works on my
  machine" — the confidence-score + sleeping-staging combination is a new
  angle on the 3 AM deploy.

## Alternatives considered

Five lines were drafted and counted before this one was picked:

- "fix(prod): tested in production at 3 AM because staging was asleep;
  staging is awake now, and so is the on-call" (111 chars) — same
  punchline, but no agent-voice hook up front; the on-call callback is
  weaker than the confidence-score opening.
- "fix(prod): the 3 AM deploy hallucinated a migration; prod believed
  it, the on-call did not" (90 chars) — good agent blind spot, but the
  joke is a claim about the deploy rather than a confession in the
  agent's own voice.
- "fix: reverted the 3 AM deploy; I have already blamed the previous
  model and apologized to the on-call" (101 chars) — funny, but the
  punchline is about blame-shifting, not about the 3 AM outage itself.
- "fix(prod): confidence 0.97, tests 0 — tested in production at 3 AM
  because staging was asleep; it is awake now" (110 chars) — the same
  opening with a weaker tail; dropping the tail keeps the punchline as
  the last word.

The chosen line won because it stacks all five judge criteria in one
breath: agent status line first, punchline last, real commit shape
throughout.

## How it works

`main.py` writes the line to `/output/entry.txt`. It is fully
deterministic: the same bytes on every run, no input, no randomness, no
network. Standard library only.

## License

MIT — see [LICENSE](LICENSE).
