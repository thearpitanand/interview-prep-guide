# Deliberate Practice

The single rule that separates this program from passive LeetCode grinding:
**every problem has a time budget, and when the budget blows, you stop.**

---

## Time Budgets

| Difficulty | Budget |
|---|---|
| Easy | 15 min |
| Medium | 25–35 min (see stub for exact target) |
| Hard | 40–45 min |
| Revision re-solve | 60% of original budget |

The budget is in each problem's docstring. Set a physical timer before you type a single line.

---

## The Hard Rule

**If the timer goes off and you don't have a working solution: stop. Close the file.**

Do not peek at the solution. Do not read hints. Do not Google the approach.

Instead:
1. Re-read the relevant pattern guide in `02-patterns/` — specifically the "Watch Me Solve" section.
2. Sleep on it (or wait until the next day's session).
3. Re-open a blank file. Re-solve from scratch with the timer running again.

This is non-negotiable. A half-solved problem that you finished by reading a hint gives you zero
retrieval practice and a false confidence signal. The re-solve from scratch the next day is where
the learning happens.

---

## Why Timers, Not Just Goals

You already have goals ("finish the problem"). Goals don't constrain behavior under discomfort.

A timer does three things a goal cannot:

1. **It simulates interview pressure.** Interviews are 45 minutes. A problem you can solve in 60
   relaxed minutes is a problem you will fail in an interview. The timer calibrates you to the
   actual constraint.

2. **It forces honest accounting.** Without a timer you will tell yourself "I almost had it" or
   "I just needed five more minutes." With a timer you either beat it or you don't. The log
   entry is binary: budget hit or not.

3. **It makes the re-solve cycle the default path, not the fallback.** When you know the rule is
   "blow the budget → re-solve tomorrow," you stop mentally negotiating with yourself mid-problem.
   The rule decides for you.

---

## No Googling Mid-Problem

Once the timer starts, the only resources you may consult:
- The problem statement itself (re-read it)
- Your own previous Feynman logs in the week files

You may not:
- Open any browser tab to look up syntax, patterns, or solutions
- Read your previous solve of the same problem
- Ask anyone (human or AI) for a hint

If you forget a syntax detail (e.g., `heapq.heappush` argument order), write a placeholder
comment like `# push (val, idx) here` and continue. Fix syntax in the Review step.

---

## No Passive Solution Reading

After the hard rule fires (timer blown), you re-read the pattern guide — you do **not** look up
the specific problem's solution on LeetCode, YouTube, or any other source.

The pattern guide gives you the strategy. You must reconstruct the implementation.

This distinction matters: reading a solution for *this exact problem* trains you to recognize
that solution. Reading the pattern trains you to generate solutions for the whole family.

---

## Budget Philosophy: Effort Calibration

The budgets are not arbitrary. They're calibrated to what a 4/5 (hire) performance looks like in
a real interview loop at the target companies. A Medium solved cleanly in 25 minutes with good
narration is a strong signal. A Medium solved in 50 minutes with backtracking is a weak signal
even if the code is correct.

Track your budget hits in the week log. By Week 4 you should be hitting budget on ~70% of Mediums.
By Week 7: ~85%. If you're below those thresholds, the bottleneck is pattern recognition speed,
not problem-solving ability — drill `pattern-recognition.md`.

---

## Log Format

In the week file, each day's log line captures budget adherence:

```
**Log:** solved 2/2 • budget hit 1/2 • confidence 3/5 • next review: Day +3
```

- **solved:** how many problems you finished (not peeked on)
- **budget hit:** how many you finished within time budget
- **confidence:** 1–5 self-rating of how well you understand the solution
- **next review:** based on the spaced repetition schedule in `04-revision/revision-schedule.md`

Confidence < 3 on any problem → re-solve the next day regardless of budget.
