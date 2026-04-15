# Feynman Protocol

After every solve — guided or solo — say three sentences out loud before logging and moving on.
No writing, no typing, no skipping. Out loud. Thirty seconds minimum.

---

## Why It Works

Retrieval is stronger than re-reading. Forcing yourself to narrate reveals the exact moment your
explanation breaks down — that gap is what will bite you six weeks later in an interview.
Writing a solution does not expose the gap. Speaking it to an imaginary colleague does.

The three-sentence structure targets the three failure modes interviewers actually test:

1. Can you name the pattern and justify why you reached for it?
2. Can you state the invariant that makes the solution correct?
3. Can you generalize — or do you only know *this* problem?

---

## The Template

Say these three sentences, in order, every time:

> **Sentence 1 — Pattern:**
> "This is a [pattern name] problem because [one concrete signal from the problem statement]."

> **Sentence 2 — Invariant:**
> "The key invariant is [what stays true throughout the algorithm / why the loop terminates correctly]."

> **Sentence 3 — Variation:**
> "I'd trip on a variation where [one twist that would break your current solution or require a different pattern]."

Fill in the brackets. Do not say "um." Do not read from your code.

---

## Worked Example — 3Sum

After solving 3Sum (sort + fix i + two-pointer inner loop):

> **Sentence 1:** "This is a Two Pointers problem because we need triplets summing to zero — sorting first
> lets us move a left/right pointer deterministically based on whether the current sum is too small or too large."

> **Sentence 2:** "The invariant is that after fixing `nums[i]`, the two-pointer scan will find every valid
> pair exactly once because duplicates are skipped at both the outer and inner level."

> **Sentence 3:** "I'd trip on a variation where the target isn't zero — I'd forget to adjust the
> duplicate-skipping logic — or where we need *four-sum*, where the outer loop becomes two nested loops
> and the index bounds shift."

Total: ~25 seconds spoken. That's the whole protocol.

---

## Logging

After speaking, write the three sentences into the Feynman slot in the week file:

```
**Feynman — 3Sum (3 sentences):**
- Pattern: Two Pointers — sorting enables deterministic pointer movement toward target sum.
- Invariant: fix i, then l/r scan finds every valid pair once; duplicates skipped at both levels.
- Variation: 4Sum nesting, or non-zero target where skip logic shifts.
```

Keep it to one line per sentence. The purpose is a retrieval cue, not a full explanation.

---

## Failure Mode

**Just writing what the solution does is not Feynman.**

"I use a hash map to store complements and check if the current number exists in the map" —
this describes mechanics, not pattern, invariant, or variation. You could write that sentence
without understanding anything.

The test: after speaking your three sentences, could a sharp junior engineer implement the
solution from scratch without seeing your code? If yes, you've done Feynman. If no, you've
described your code.

---

## Edge Cases for the Protocol Itself

- **You can't produce Sentence 2 (invariant)?** You don't understand *why* your solution is correct. Do not log it as solved. Re-read the pattern guide's worked example, then re-explain.
- **You can't produce Sentence 3 (variation)?** Fine for Day 1 of a pattern. By Day 3 of the same pattern you should be generating variations automatically.
- **Time-boxed days:** if you're short on time, the three sentences replace the log entry — do not skip them to save time. They take 30 seconds.
