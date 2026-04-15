# Revision Schedule — Spaced Repetition Rules

Every problem you solve enters a spaced-repetition queue. The queue is tracked in `review-log.md`. This file explains the rules; `review-log.md` is the table you maintain.

---

## The Interval Table

| When first solved | Review 1 | Review 2 | Review 3 | Review 4 |
|-------------------|----------|----------|----------|----------|
| Day N | Day N+1 | Day N+3 | Day N+7 | Day N+21 |

Example: solve Two Sum on Day 1 → review due Day 2, Day 4, Day 8, Day 22.

After Review 4 the problem graduates. It still appears in the Top-30 cold-solve sprint, but it leaves the active queue.

---

## Confidence Scale

After every review, score yourself honestly. This is the only input the system needs from you.

| Score | Meaning |
|-------|---------|
| 1 | Blank — could not start |
| 2 | Major gaps — knew the pattern but got stuck on implementation |
| 3 | Partial — solved with hints or significant false starts |
| 4 | Good — solved cleanly within time, minor hesitations acceptable |
| 5 | Fluent — solved comfortably under time, could explain to a junior engineer |

---

## Rules

### When confidence < 3 on any review

Reset the interval. The next due date becomes today + 1, not today + next-step.

Update the `Next Due` column in `review-log.md` to tomorrow's day number and mark confidence in the log. The problem re-enters the queue as if it was just solved for the first time.

This is not punishment — it means the problem was not actually learned yet, and the interval was wrong.

### When confidence ≥ 4

Passive review only. Do not re-solve.

1. Read your Feynman note for the problem in the relevant week file (takes ~2 minutes).
2. On paper (not keyboard), sketch the solution template: variable names, loop structure, return shape. Do not write actual code — just the skeleton. Takes ~3 minutes.
3. Mark the log with the new confidence and advance to the next interval.

Total time: ~5 minutes per problem.

### When confidence is 3 (exactly)

Re-solve from a blank file with the timer running. This is the default re-solve path.

Steps:

1. Open a new scratch file (do not open the original stub).
2. Set the timer to the target time cold (from `top-30-list.md` if the problem is in the Top 30, or the original budget otherwise).
3. Solve without looking at notes.
4. After time expires or you finish: compare to your original stub. Note any differences in your Feynman log.
5. Score and advance the interval.

---

## Saturday "Rev × 2" Slots

Every Saturday in the 60-day schedule includes a "Rev × 2" slot. This means: pull the two problems most overdue from `review-log.md` and work through them before starting the new stretch problem.

How to pull the queue:

1. Open `review-log.md`.
2. Filter rows where `Next Due (day)` ≤ today's day number.
3. Sort by `Next Due (day)` ascending — the most overdue problems come first.
4. Take the top 2.

If fewer than 2 problems are due, take what is due and use the remaining time for the new problem. Do not manufacture extra reviews.

If more than 2 are due (can happen after a missed day), take the top 2 for this slot and catch up the rest on Sunday flex day.

Apply the confidence rules above to each:

- Confidence ≥ 4 → 5-minute passive review.
- Confidence 3 → re-solve from blank with timer.
- Confidence < 3 → re-solve from blank with timer, then reset interval.

---

## How the Review Log Feeds Into Daily "Revision Due Today"

Each week file (`../03-weekly/week-N.md`) has a "Revision Due Today" section at the top of each day row. Here is how to fill it:

At the start of each day:

1. Open `review-log.md`.
2. Find all rows where `Next Due (day)` equals today's day number.
3. List those problem names in the "Revision Due Today" field of the day row.
4. If none are due, write "none".

On learn days (Mon–Fri), revision due items are handled before the new problems. Budget 5–10 minutes per passive review, 20–30 minutes per re-solve. If the revision queue is heavy (3+ re-solves due), move one new problem to the next day rather than skipping revision — spaced repetition only works if the intervals hold.

After completing each review, update `review-log.md` immediately: new confidence, new `Last Review (day)`, new `Next Due (day)`. Do not batch-update at the end of the week — stale entries cause the queue to drift.

---

## Handling Missed Days

If you miss a day entirely, do not backdate entries. The next time you open `review-log.md`, items that were due on the missed day will show up as overdue. Treat them as due immediately — same rules apply. The intervals do not collapse; just work through the overdue stack in priority order (most overdue first).

Missing 1–2 days in a week is recoverable. Missing more than 3 consecutive days means the queue will be larger than a Saturday slot can absorb; use Sunday flex day to clear the backlog before Week N+1 begins.
