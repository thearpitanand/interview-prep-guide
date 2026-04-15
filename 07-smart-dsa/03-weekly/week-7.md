# Week 7 — DP + Intervals + Greedy

**Theme:** Finish the DP arc (knapsack, string DP, grid DP), then pivot to greedy and intervals. Two mocks on Sunday (Day 49) to build stamina.

**Patterns introduced this week:** 0/1 Knapsack (Day 43), 2D String DP (Day 44), Grid DP (Day 46), Greedy (Day 47), Intervals (Day 48).

Every new pattern entry is marked 🤝 (we do — read the pattern guide first, timer runs but overshooting is OK). Everything else is 🎯 (you do — strict timer, stop if blown, re-solve next day).

---

## Day Table

| Day | P1 | P2 | Pattern | Type |
|-----|----|----|---------|------|
| 43 (Mon) | 🤝 Coin Change (M, 30m) | 🎯 Partition Equal Subset Sum (M, 30m) | 0/1 Knapsack / Unbounded DP | 2 new |
| 44 (Tue) | 🎯 Word Break (M, 30m) | 🤝 Longest Common Subsequence (M, 30m) | String DP | 2 new |
| 45 (Wed) | 🎯 Edit Distance (H, 40m) | Rev × 1 | 2D String DP | 1 new + 1 rev |
| 46 (Thu) | 🤝 Unique Paths (M, 20m) | 🎯 Longest Palindromic Substring (M, 30m) | Grid DP / Expand-center | 2 new |
| 47 (Fri) | 🤝 Jump Game (M, 20m) | 🎯 Gas Station (M, 25m) | Greedy | 2 new |
| 48 (Sat) | 🤝 Merge Intervals (M, 25m) + 🎯 Meeting Rooms II (M, 25m) | 🎯 Burst Balloons (H, 45m) | Intervals + Interval DP | 3 new |
| 49 (Sun) | **Mock #3** (45m) + 30-min break + **Mock #4** (45m) + AI review | — | 2-mock stamina day | mocks |

**New problems this week:** 12 (10 medium, 2 hard). Running total: ~72.

---

## Day 43 — Coin Change + Partition Equal Subset Sum

**Before starting:** Read `02-patterns/11-dp-essentials.md` § "Watch Me Solve — Coin Change (Unbounded Knapsack)" (~15 min, no code). This is the I-do stage.

### 🤝 P1 — Coin Change (we do, 30m)

**Scaffolded outline (fill in the code, strategy is pre-written):**

1. **Brute force framing:** at each amount, try every coin denomination — exponential.
2. **DP recurrence:** `dp[i]` = min coins to make amount `i`. Base case: `dp[0] = 0`, rest = `inf`.
3. **Transition:** for each amount `i`, for each coin `c`: `dp[i] = min(dp[i], dp[i - c] + 1)`.
4. **Result:** `dp[amount]` if finite, else `-1`.
5. **Why it's unbounded knapsack:** you can reuse coins — inner loop iterates over all coins for every amount.

```python
# Fill in: python 07-smart-dsa/03-problems/d43-p1_coin_change.py
```

**Feynman (3 sentences after solving):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### 🎯 P2 — Partition Equal Subset Sum (you do, 30m)

Timer starts now. Stop at 30m even if unsolved — re-read pattern guide and re-solve tomorrow.

```python
# Fill in: python 07-smart-dsa/03-problems/d43-p2_partition_equal_subset_sum.py
```

**Feynman (3 sentences after solving):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

**Log:** solved ___/2 · budget hit ___/2 · confidence ___/5 · next review: Day 44

---

## Day 44 — Word Break + Longest Common Subsequence

**Before P2:** Read `02-patterns/11-dp-essentials.md` § "Watch Me Solve — LCS (2D String DP)" (~15 min, no code).

### 🎯 P1 — Word Break (you do, 30m)

```python
# Fill in: python 07-smart-dsa/03-problems/d44-p1_word_break.py
```

**Feynman (3 sentences after solving):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### 🤝 P2 — Longest Common Subsequence (we do, 30m)

**Scaffolded outline:**

1. **Subproblem:** `dp[i][j]` = LCS length of `text1[:i]` and `text2[:j]`.
2. **Base case:** `dp[0][j] = dp[i][0] = 0` (empty string has LCS 0 with anything).
3. **Transition:**
   - If `text1[i-1] == text2[j-1]`: `dp[i][j] = dp[i-1][j-1] + 1`
   - Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`
4. **Result:** `dp[m][n]`.
5. **Space optimization:** you only need the previous row — can reduce to O(n) space.

```python
# Fill in: python 07-smart-dsa/03-problems/d44-p2_longest_common_subsequence.py
```

**Feynman (3 sentences after solving):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

**Log:** solved ___/2 · budget hit ___/2 · confidence ___/5 · next review: Day 45

---

## Day 45 — Edit Distance + Revision

### 🎯 P1 — Edit Distance (you do, 40m)

Hard. If you blow the 40m timer: stop, re-read LCS in the pattern guide, map the recurrence yourself on paper, then re-solve tomorrow from a blank file.

```python
# Fill in: python 07-smart-dsa/03-problems/d45-p1_edit_distance.py
```

**Feynman (3 sentences after solving):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### Rev × 1

Pull the oldest unreviewed problem from your `04-revision/review-log.md`. Re-solve from a blank file with the original time budget.

**Log:** solved ___/1 new · rev ___/1 · budget hit ___/1 new · confidence ___/5 · next review: Day 46

---

## Day 46 — Unique Paths + Longest Palindromic Substring

**Before P1:** Read `02-patterns/11-dp-essentials.md` § "Watch Me Solve — Unique Paths (Grid DP)" (~15 min, no code).

### 🤝 P1 — Unique Paths (we do, 20m)

**Scaffolded outline:**

1. **Grid DP framing:** `dp[i][j]` = number of unique paths to cell `(i, j)`.
2. **Base case:** entire top row and left column = 1 (only one way to reach them).
3. **Transition:** `dp[i][j] = dp[i-1][j] + dp[i][j-1]`.
4. **Result:** `dp[m-1][n-1]`.
5. **Optimization:** notice `dp[i][j]` only depends on the row above — can use a 1D array.

```python
# Fill in: python 07-smart-dsa/03-problems/d46-p1_unique_paths.py
```

**Feynman (3 sentences after solving):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### 🎯 P2 — Longest Palindromic Substring (you do, 30m)

```python
# Fill in: python 07-smart-dsa/03-problems/d46-p2_longest_palindromic_substring.py
```

**Feynman (3 sentences after solving):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

**Log:** solved ___/2 · budget hit ___/2 · confidence ___/5 · next review: Day 47

---

## Day 47 — Jump Game + Gas Station

**Before P1:** Read `02-patterns/11-dp-essentials.md` § "Watch Me Solve — Jump Game (Greedy)" (~15 min, no code).

### 🤝 P1 — Jump Game (we do, 20m)

**Scaffolded outline:**

1. **Greedy intuition:** track the farthest index reachable so far (`max_reach`).
2. **Loop:** for each index `i`, if `i > max_reach` you're stuck — return `False`. Otherwise update `max_reach = max(max_reach, i + nums[i])`.
3. **Result:** if the loop completes, return `True`.
4. **Why greedy works:** you don't need to know the exact path, just whether the frontier ever reaches the end.

```python
# Fill in: python 07-smart-dsa/03-problems/d47-p1_jump_game.py
```

**Feynman (3 sentences after solving):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### 🎯 P2 — Gas Station (you do, 25m)

```python
# Fill in: python 07-smart-dsa/03-problems/d47-p2_gas_station.py
```

**Feynman (3 sentences after solving):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

**Log:** solved ___/2 · budget hit ___/2 · confidence ___/5 · next review: Day 48

---

## Day 48 (Sat) — Merge Intervals + Meeting Rooms II + Burst Balloons

**Before P1:** Read `02-patterns/11-dp-essentials.md` § "Watch Me Solve — Merge Intervals" (~15 min, no code).

### 🤝 P1 — Merge Intervals (we do, 25m)

**Scaffolded outline:**

1. **Sort** intervals by start time.
2. **Iterate:** keep a `merged` list. For each interval, if `merged` is empty or current start > last end, append. Otherwise extend the last end: `merged[-1][1] = max(merged[-1][1], current_end)`.
3. **Result:** `merged`.
4. **Why sort first:** without sorting you'd need O(n²) comparisons; sorting enables a single pass.

```python
# Fill in: python 07-smart-dsa/03-problems/d48-p1_merge_intervals.py
```

**Feynman (3 sentences after solving):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### 🎯 P2 — Meeting Rooms II (you do, 25m)

```python
# Fill in: python 07-smart-dsa/03-problems/d48-p2_meeting_rooms_ii.py
```

**Feynman (3 sentences after solving):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### 🎯 P3 — Burst Balloons (you do, 45m)

Hard interval DP. Budget is 45m. If blown: stop, think about the "choose last" reframing, re-solve tomorrow.

```python
# Fill in: python 07-smart-dsa/03-problems/d48-p3_burst_balloons.py
```

**Feynman (3 sentences after solving):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

**Log:** solved ___/3 · budget hit ___/3 · confidence ___/5 · next review: Day 49

---

## Day 49 (Sun) — Back-to-Back Mock #3 and Mock #4

**Goal:** build interview stamina. Two full 45-minute mocks with only a 30-minute break between them. Do not look at solutions between mocks.

### Schedule

| Time | Activity |
|------|----------|
| T+0m | Mock #3 starts — pick next unseen problem from sealed mock list, start Fathom |
| T+45m | Mock #3 ends — stop regardless; export Fathom transcript; do NOT review yet |
| T+45m–T+75m | 30-minute break — walk, eat, no LeetCode |
| T+75m | Mock #4 starts — pick next unseen problem, start Fathom |
| T+120m | Mock #4 ends — stop regardless; export transcript |
| T+120m+ | AI review: paste both transcripts into the reviewer prompt (do them separately) |

### Mock #3

- **Problem:** unseen #___ from sealed list
- **Fathom transcript:** _(attach path or paste)_
- **AI review scores:**
  - Problem clarification: ___/5
  - Communication: ___/5
  - Optimization thinking: ___/5
  - Edge cases: ___/5
  - Recovery: ___/5
- **Top 2 behaviors to fix before Mock #4:** ___

### Mock #4

- **Problem:** unseen #___ from sealed list
- **Fathom transcript:** _(attach path or paste)_
- **AI review scores:**
  - Problem clarification: ___/5
  - Communication: ___/5
  - Optimization thinking: ___/5
  - Edge cases: ___/5
  - Recovery: ___/5
- **Trend vs Mock #3:** ___

### Week 7 Retrospective

- Weakest pattern this week: ___
- Problems to flag for Top-30 cold-solve: ___
- Revision queue additions: ___
