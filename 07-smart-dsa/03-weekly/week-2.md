# Week 2 — Sliding Window + Binary Search

**Pattern theme:** Variable and fixed sliding windows for subarray/substring optimization; binary search on sorted arrays and on the answer space.

**Why this matters for target companies:** Sliding window and binary search are the two patterns most likely to separate a "passed" from a "strong hire" at BrowserStack, Chargebee, Paytm, and Fi. Sliding window tests whether you can maintain invariants under a shrinking constraint — a reasoning skill that mirrors real systems thinking. Binary search on the answer (Koko Bananas, capacity problems) is a specific senior signal: interviewers at growth-stage companies use it as a filter for engineers who can abstract "find the minimum k such that f(k) is feasible" into a search problem.

---

## Day-by-Day Table

| Day | P1 | P2 | Pattern |
|---|---|---|---|
| 8 | Best Time to Buy/Sell Stock (E, 15m) 🎯 | Longest Substring Without Repeat (M, 25m) 🤝 | Window expand/shrink |
| 9 | Longest Repeating Char Replacement (M, 30m) 🎯 | Permutation in String (M, 25m) 🎯 | Fixed/variable window |
| 10 | Minimum Window Substring (H, 40m) 🎯 | Sliding Window Maximum (H→M, 30m) 🎯 | Window + deque |
| 11 | Binary Search (E, 15m) 🤝 | Search in Rotated Sorted Array (M, 25m) 🎯 | BS invariants |
| 12 | Find Minimum in Rotated Sorted Array (M, 25m) 🎯 | Time-Based KV Store (M, 30m) 🎯 | BS on index |
| 13 (Sat) | Koko Eating Bananas (M, 30m) 🎯 | Rev × 2 | BS on answer |
| 14 (Sun) | Flex + Pattern-recognition drill #1 | — | — |

---

## Day 8 — Best Time to Buy/Sell Stock, Longest Substring Without Repeat

**New pattern today?** Yes — Sliding Window. Read `../02-patterns/03-sliding-window.md` first (I do stage, 15m).

**Problem 1** 🎯 — Best Time to Buy/Sell Stock — Stub: `../03-problems/d08-p1_best_time_buy_sell.py`
Track the running minimum price as you scan left to right. Profit at each step is `price - running_min`; keep a running maximum of that profit.

**Problem 2** 🤝 — Longest Substring Without Repeating Characters — Stub: `../03-problems/d08-p2_longest_substring_no_repeat.py`
Expand the right boundary one character at a time, adding to a set. When a duplicate appears, shrink from the left until the window is valid again. The answer is the maximum window size seen.

**If 🤝 (we do) — scaffolded outline for Longest Substring Without Repeating Characters:**
1. Initialize `left = 0`, `seen = set()`, `best = 0`.
2. For each `right` in range `len(s)`: while `s[right]` is already in `seen`, remove `s[left]` from `seen` and advance `left`.
3. Add `s[right]` to `seen`. Update `best = max(best, right - left + 1)`.
4. Return `best`.

**Feynman — Best Time to Buy/Sell Stock (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Feynman — Longest Substring Without Repeating Characters (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Log:** solved ___/2 • budget hit ___/2 • confidence ___/5 • next review: Day 9

---

## Day 9 — Longest Repeating Char Replacement, Permutation in String

**New pattern today?** No — continuing Sliding Window (variable and fixed windows).

**Problem 1** 🎯 — Longest Repeating Character Replacement — Stub: `../03-problems/d09-p1_longest_repeating_char_replacement.py`
The window is valid when `(window_size - max_frequency_in_window) <= k` — that's the number of characters you'd need to replace. Expand right freely; when invalid, slide left by one.

**Problem 2** 🎯 — Permutation in String — Stub: `../03-problems/d09-p2_permutation_in_string.py`
Fixed window of size `len(s1)`. Slide it over `s2` comparing frequency maps. Use a running difference counter (how many chars are "satisfied") to avoid re-comparing the full map each step.

**Feynman — Longest Repeating Char Replacement (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Feynman — Permutation in String (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Log:** solved ___/2 • budget hit ___/2 • confidence ___/5 • next review: Day 10

---

## Day 10 — Minimum Window Substring, Sliding Window Maximum

**New pattern today?** No — Sliding Window pushed to hard territory.

**Problem 1** 🎯 — Minimum Window Substring — Stub: `../03-problems/d10-p1_min_window_substring.py`
Classic expand-to-satisfy, shrink-to-minimize pattern. Track how many distinct characters from `t` are still "needed" (their count in the window hasn't reached the required count). Shrink greedily once all needs are met.

**Problem 2** 🎯 — Sliding Window Maximum — Stub: `../03-problems/d10-p2_sliding_window_maximum.py`
A monotonic deque (decreasing by value, storing indices) keeps the current maximum at the front. Pop the back when a new element is larger; pop the front when it falls out of the window.

**Feynman — Minimum Window Substring (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Feynman — Sliding Window Maximum (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Log:** solved ___/2 • budget hit ___/2 • confidence ___/5 • next review: Day 11

---

## Day 11 — Binary Search, Search in Rotated Sorted Array

**New pattern today?** Yes — Binary Search. Read `../02-patterns/04-binary-search.md` first (I do stage, 15m).

**Problem 1** 🤝 — Binary Search — Stub: `../03-problems/d11-p1_binary_search.py`
The canonical template: `lo`, `hi`, `mid`. Compare `nums[mid]` to target and halve the search space. This is the "I do" exercise — get the template into muscle memory before tackling rotated variants.

**Problem 2** 🎯 — Search in Rotated Sorted Array — Stub: `../03-problems/d11-p2_search_rotated_sorted.py`
After rotation, one half of the array is always sorted. Determine which half at each step by comparing `nums[lo]` and `nums[mid]`, then check if the target falls in the sorted half.

**If 🤝 (we do) — scaffolded outline for Binary Search:**
1. Set `lo = 0`, `hi = len(nums) - 1`.
2. While `lo <= hi`: compute `mid = (lo + hi) // 2`.
3. If `nums[mid] == target` return `mid`. If `nums[mid] < target` set `lo = mid + 1`. Else set `hi = mid - 1`.
4. Return `-1` (target not found).

**Feynman — Binary Search (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Feynman — Search in Rotated Sorted Array (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Log:** solved ___/2 • budget hit ___/2 • confidence ___/5 • next review: Day 12

---

## Day 12 — Find Minimum in Rotated Sorted Array, Time-Based KV Store

**New pattern today?** No — Binary Search on index variants.

**Problem 1** 🎯 — Find Minimum in Rotated Sorted Array — Stub: `../03-problems/d12-p1_find_min_rotated.py`
Binary search converges to the pivot. If `nums[mid] > nums[hi]`, the minimum is in the right half; otherwise it's in the left half (mid could be the answer).

**Problem 2** 🎯 — Time-Based KV Store — Stub: `../03-problems/d12-p2_time_based_kv.py`
Store `(timestamp, value)` pairs per key. On get, binary search for the largest timestamp `<= query` — a classic "rightmost valid position" binary search variant.

**Feynman — Find Minimum in Rotated Sorted Array (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Feynman — Time-Based KV Store (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Log:** solved ___/2 • budget hit ___/2 • confidence ___/5 • next review: Day 13

---

## Day 13 (Saturday) — Koko Eating Bananas + Rev × 2

**New pattern today?** No — Binary Search on the answer space (a senior signal).

**Problem 1** 🎯 — Koko Eating Bananas — Stub: `../03-problems/d13-p1_koko_bananas.py`
Reframe: "what is the minimum speed k such that she can finish in h hours?" k lies in [1, max(piles)]. Binary search on that range; the feasibility check is O(n) — total time = sum of ceil(pile/k).

**Revision (Rev × 2):** Pull the two earliest-due problems from `../04-revision/revision-schedule.md`. Re-solve from blank with timer.

**Feynman — Koko Eating Bananas (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Log:** solved ___/1 new • rev ___/2 • budget hit ___/3 • confidence ___/5 • next review: Day 14

---

## Day 14 (Sunday) — Flex + Pattern-Recognition Drill #1

Use the first half of this session (≤ 45 min) for flex: rest, catch-up, or a re-solve of any problem rated confidence < 3.

**Pattern-Recognition Drill #1:** Open `../04-revision/pattern-drills.md` and complete Drill #1 (10 problem statements, 90 seconds each — write only the pattern name + 2-sentence plan, no code). Score yourself. If hit rate < 7/10, re-read `../01-method/pattern-recognition.md` before starting Week 3.

---

> **Revision due next week:** After Day 14, check `../04-revision/revision-schedule.md` for problems due in Week 3. These land in the Day 15 warm-up and the Day 20 (Sat) revision slots.
>
> **Pattern-Recognition Drill #1 results:** score ___/10. If < 7: re-read `../01-method/pattern-recognition.md` before Day 15. If ≥ 7: proceed to Week 3 (Stack + Linked List).
