# Week 8 — Final Sprint

This is not a learning week. The pattern curriculum is complete. Week 8 has one job: simulate the real interview loop at full intensity and expose every remaining gap before it matters.

**What happens this week:**
- **2 stretch hards** (Days 50–51) — problems that appear in senior rounds at Dream11, CRED, Razorpay. Solve them to prove the DP and stack patterns are load-bearing, not just "understood."
- **3 self-mocks** (#5, #6, #7) — same protocol as before; Mock #7 is the hardest (unseen medium from sealed list, treated as a real final-round).
- **Top-30 cold-solve sprint** (Days 53, 54, 56) — 30 canonical problems from the 60-day schedule, 30 minutes each, no hints, scored by confidence. Target: ≥ 25/30 at confidence ≥ 4.
- **Targeted re-solve** (Day 57) — any problem that scored confidence < 4 in the sprint gets one more attempt.
- **Pattern Drill #4 + UMPIRE review** (Day 59).
- **Deload** (Day 60) — rest, re-read, no new problems.

If you arrive at Day 50 with confidence < 3 in any Week 7 pattern, spend 30 minutes re-reading that pattern guide before starting the day's problem.

---

## Day Table (Days 50–60)

| Day | Activity | Type |
|-----|----------|------|
| 50 (Mon) | Median of Two Sorted Arrays (H, 40m) + Rev × 2 | 1 hard + revision |
| 51 (Tue) | Longest Valid Parentheses (H, 35m) + Rev × 2 | 1 hard + revision |
| 52 (Wed) | **Mock #5** (45m) + AI review | Mock |
| 53 (Thu) | Top-30 cold-solve sprint part 1 — problems 1–10 (30m each) | Sprint |
| 54 (Sat) | Top-30 cold-solve sprint part 2 — problems 11–20 (30m each) | Sprint |
| 55 (Sun) | **Mock #6** (45m) + AI review | Mock |
| 56 (Mon) | Top-30 cold-solve sprint part 3 — problems 21–30 + gap analysis | Sprint |
| 57 (Tue) | Targeted re-solve of all confidence < 4 items from sprint | Revision |
| 58 (Wed) | **Mock #7** — hardest (45m) + AI review | Mock |
| 59 (Thu) | Final Pattern Drill #4 + UMPIRE framework review | Drill |
| 60 (Fri) | Rest / deload | Deload |

---

## Day 50 — Median of Two Sorted Arrays + Rev × 2

### 🎯 P1 — Median of Two Sorted Arrays (you do, 40m)

Hard. This is a binary search on the partition index, not a merge. If you blow 40m: stop. Re-read `02-patterns/04-binary-search.md`, think about what "correct partition" means, re-solve tomorrow.

```python
# Fill in: python 07-smart-dsa/03-problems/d50-p1_median_two_sorted_arrays.py
```

**Feynman (3 sentences after solving):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### Rev × 2

Pull the two oldest unreviewed problems from `04-revision/review-log.md`. Re-solve each from a blank file within original time budget.

| Problem | Time budget | Confidence after |
|---------|-------------|-----------------|
| ___ | ___m | ___/5 |
| ___ | ___m | ___/5 |

**Log:** solved ___/1 new · rev ___/2 · confidence ___/5 · next review: Day 51

---

## Day 51 — Longest Valid Parentheses + Rev × 2

### 🎯 P1 — Longest Valid Parentheses (you do, 35m)

Hard. Two valid approaches: stack-based (track indices) or DP (left/right pass). Know both exist — start with whichever comes to mind, then think whether the other is cleaner. If blown: stop and re-read `02-patterns/05-stack-monotonic.md`.

```python
# Fill in: python 07-smart-dsa/03-problems/d51-p1_longest_valid_parentheses.py
```

**Feynman (3 sentences after solving):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### Rev × 2

| Problem | Time budget | Confidence after |
|---------|-------------|-----------------|
| ___ | ___m | ___/5 |
| ___ | ___m | ___/5 |

**Log:** solved ___/1 new · rev ___/2 · confidence ___/5 · next review: Day 52

---

## Day 52 — Mock #5

**Pre-mock checklist:**
- [ ] Fathom recording set up and tested
- [ ] 45-min timer ready
- [ ] Sealed mock list open — pick next unseen number
- [ ] No peeking at solutions until AI review is complete

### Mock #5 log

- **Problem:** unseen #___ from sealed list
- **Fathom transcript:** _(attach path or paste)_
- **AI review scores:**
  - Problem clarification: ___/5
  - Communication: ___/5
  - Optimization thinking: ___/5
  - Edge cases: ___/5
  - Recovery: ___/5
- **Top 2 behaviors to fix before sprint:** ___

---

## Day 53 — Top-30 Cold-Solve Sprint: Part 1 (Problems 1–10)

**Rules:**
- 30 minutes per problem. Stop at 30m even if unsolved.
- No hints, no pattern labels, no notes. Pure cold solve.
- After each problem: score confidence 1–5 immediately.
- Do not review solutions until all 10 are done.

### Scoring Table — Problems 1–10

| # | Problem | Solved? | Time used | Confidence (1–5) |
|---|---------|---------|-----------|-----------------|
| 1 | Two Sum | | | |
| 2 | Longest Substring Without Repeat | | | |
| 3 | 3Sum | | | |
| 4 | Container With Most Water | | | |
| 5 | Trapping Rain Water | | | |
| 6 | Minimum Window Substring | | | |
| 7 | Search in Rotated Sorted Array | | | |
| 8 | Koko Eating Bananas | | | |
| 9 | Valid Parentheses | | | |
| 10 | Min Stack | | | |

**Part 1 summary:** solved ___/10 · avg confidence ___/5 · flag for re-solve: ___

---

## Day 54 — Top-30 Cold-Solve Sprint: Part 2 (Problems 11–20)

### Scoring Table — Problems 11–20

| # | Problem | Solved? | Time used | Confidence (1–5) |
|---|---------|---------|-----------|-----------------|
| 11 | Daily Temperatures | | | |
| 12 | Largest Rectangle in Histogram | | | |
| 13 | Reverse Linked List | | | |
| 14 | Linked List Cycle | | | |
| 15 | LRU Cache | | | |
| 16 | LCA of Binary Tree | | | |
| 17 | Binary Tree Level Order Traversal | | | |
| 18 | Validate BST | | | |
| 19 | Serialize / Deserialize Binary Tree | | | |
| 20 | Kth Largest Element in Array | | | |

**Part 2 summary:** solved ___/10 · avg confidence ___/5 · flag for re-solve: ___

---

## Day 55 — Mock #6

### Mock #6 log

- **Problem:** unseen #___ from sealed list
- **Fathom transcript:** _(attach path or paste)_
- **AI review scores:**
  - Problem clarification: ___/5
  - Communication: ___/5
  - Optimization thinking: ___/5
  - Edge cases: ___/5
  - Recovery: ___/5
- **Trend vs Mock #5:** ___

---

## Day 56 — Top-30 Cold-Solve Sprint: Part 3 (Problems 21–30) + Gap Analysis

### Scoring Table — Problems 21–30

| # | Problem | Solved? | Time used | Confidence (1–5) |
|---|---------|---------|-----------|-----------------|
| 21 | Merge K Sorted Lists | | | |
| 22 | Find Median from Data Stream | | | |
| 23 | Subsets | | | |
| 24 | Combination Sum | | | |
| 25 | Word Search | | | |
| 26 | Number of Islands | | | |
| 27 | Course Schedule | | | |
| 28 | Word Ladder | | | |
| 29 | Coin Change | | | |
| 30 | Edit Distance | | | |

**Part 3 summary:** solved ___/10 · avg confidence ___/5

### Gap Analysis (fill in after all 30 are done)

**Overall sprint result:** solved ___/30 at confidence ≥ 4

**Problems scoring confidence < 4 (queue for Day 57):**

| Problem | Confidence | Pattern | Action |
|---------|------------|---------|--------|
| | | | re-solve cold |
| | | | re-solve cold |
| | | | re-solve cold |

**Pattern-level gaps** (≥ 2 confidence < 4 in same pattern = pattern gap, not problem gap):

- ___: re-read `02-patterns/<N>-<pattern>.md` before re-solving
- ___: re-read `02-patterns/<N>-<pattern>.md` before re-solving

**Verdict:** target is ≥ 25/30 at confidence ≥ 4. If below 25, add a Day 57b (extra re-solve session) before Mock #7.

---

## Day 57 — Targeted Re-Solve

Take every problem flagged confidence < 4 from the gap analysis. Re-solve each from a blank file with original time budget. No looking at previous attempts.

| Problem | Original confidence | New confidence | Time used |
|---------|---------------------|----------------|-----------|
| | | | |
| | | | |
| | | | |

**Goal:** get every item to confidence ≥ 4 before Mock #7. If still < 4 after re-solve: note the specific step where you got stuck (invariant? transition? base case?) and add a sticky note to the pattern guide.

---

## Day 58 — Mock #7 (Hardest)

This is the final mock. Treat it as a real final-round interview. Pick the hardest unseen number from your sealed list.

**Pre-mock ritual:**
- [ ] Re-read `01-method/interview-framework.md` UMPIRE steps (10 min)
- [ ] 5-minute silence — no phone, no music
- [ ] Fathom recording started
- [ ] 45-min timer set

### Mock #7 log

- **Problem:** unseen #___ from sealed list (hardest pick)
- **Fathom transcript:** _(attach path or paste)_
- **AI review scores:**
  - Problem clarification: ___/5
  - Communication: ___/5
  - Optimization thinking: ___/5
  - Edge cases: ___/5
  - Recovery: ___/5
- **Overall mock progression (fill in all 7):**

| Mock | Day | Score /25 | Top fix |
|------|-----|-----------|---------|
| #1 | 35 | | |
| #2 | 42 | | |
| #3 | 49 | | |
| #4 | 49 | | |
| #5 | 52 | | |
| #6 | 55 | | |
| #7 | 58 | | |

---

## Day 59 — Final Pattern Drill #4 + UMPIRE Review

### Pattern Drill #4

Open `04-revision/pattern-drills.md` — Drill #4 (10 problem statements). For each: write the pattern name + 2-sentence plan in ≤ 90 seconds. No coding.

| # | Pattern identified | Plan (2 sentences) | Time used |
|---|-------------------|--------------------|-----------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |

**Score:** ___/10 correct pattern names in ≤ 90s each. Target ≥ 7/10.

If score < 7: re-read `01-method/pattern-recognition.md`. Do not advance until ≥ 7 — this drill measures the one skill that fails people most (pattern matching under pressure).

### UMPIRE Framework Review

Work through each step of the UMPIRE sequence aloud on a problem you already know well (pick any from Week 7). Time yourself — the goal is < 3 minutes from problem statement to "code approved by interviewer."

- [ ] U — Restate, ask 2 clarifying questions, confirm I/O shape
- [ ] M — Out loud: "This smells like ___ because ___"
- [ ] P — Approach in English, state time/space, get buy-in
- [ ] I — Clean code, narrating each block
- [ ] R — Dry-run given example + one edge case
- [ ] E — Final complexity + one optimization with more time

---

## Day 60 — Rest / Deload

No new problems. No re-solves. No pressure.

1. Re-read `01-method/interview-framework.md` — slowly, no notes. Just let it land.
2. Re-read `01-method/pattern-recognition.md` — same pace.
3. Optional: flip through your Feynman notes from Weeks 1–7. Notice how much you know now that you didn't on Day 1.

**You are done.** The 60-day program is complete.

---

## Post-60-Day: How to Maintain

The goal now is not to keep learning new problems — it's to keep the patterns warm so you don't regress before your actual interviews.

### Minimum Maintenance Protocol (1–2h/week)

**One day per week (pick a fixed day):**
- Pull 2–3 problems from `04-revision/review-log.md` that are due for their next spaced-repetition interval (Day N+1, N+3, N+7, or N+21 rules).
- Re-solve each from a blank file, within original time budget.
- If confidence < 3: reset interval to N+1.
- If confidence ≥ 4: mark passive (read Feynman notes only, 5 min).

**One mock per week (preferably Sunday):**
- Same self-mock protocol: unseen problem, 45 min, Fathom, AI review.
- Log in `05-mocks/mock-log.md`.
- If you have a real interview scheduled within 2 weeks: increase to 2 mocks/week.

### Before a Real Interview Loop

1 week out:
- Run the Top-30 cold-solve sprint again (condensed: 15 min each, just the ones you flagged < 4 previously).
- Re-read the pattern guide for the 2 patterns you're shakiest on.

Day before:
- One mock (unseen medium).
- Re-read `01-method/interview-framework.md`.
- Rest.

Day of:
- Light review of Feynman notes only.
- No new problems.
- Trust the 60 days.
