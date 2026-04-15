# Week 5 — Heaps / Top-K + Backtracking

**Days 29–35 | Mocks start this week**

## Theme

Two new patterns this week. Heaps let you maintain ordered extremes in O(log n) — the workhorse behind Top-K, scheduling, and stream problems. Backtracking is controlled exhaustive search: define the choice space, recurse, and undo. Together they appear in a majority of senior-loop screens at product companies.

## Why It Matters

- **Heaps / Top-K:** Swiggy, Zepto, Meesho use top-K in feed ranking, search, and routing contexts. Stream median is a classic two-heap hard that recurs at CRED and Dream11.
- **Backtracking:** Subsets, permutations, and combination sum are the three archetypes. If you can identify "enumerate all valid states," you own this pattern. Appears in CRED, Razorpay, and growth-stage startups that want to see recursion comfort.

---

## Day Table

| Day | P1 | P2 | Pattern | Markers |
|-----|----|----|---------|---------| 
| 29 (Mon) | Kth Largest Element in Array (E→M, 20m) | K Closest Points to Origin (M, 25m) | Heap basics | 🤝 P1, 🎯 P2 |
| 30 (Tue) | Merge K Sorted Lists (H, 35m) | Task Scheduler (M, 30m) | Heap + greedy | 🎯 P1, 🎯 P2 |
| 31 (Wed) | Find Median from Data Stream (H, 40m) | Rev × 1 | Two heaps | 🎯 P1 |
| 32 (Thu) | Subsets (M, 25m) | Permutations (M, 25m) | Backtracking template | 🤝 P1, 🎯 P2 |
| 33 (Fri) | Combination Sum (M, 30m) | Word Search (M, 30m) | Backtracking with state | 🎯 P1, 🎯 P2 |
| 34 (Sat) | Palindrome Partitioning (M, 30m) | Rev × 2 | Backtracking + cuts | 🎯 P1 |
| 35 (Sun) | **Mock #1** (45m) + AI review | — | — | — |

---

## Day 29 — Kth Largest Element + K Closest Points

### New-Pattern Check
Before touching code, read `02-patterns/08-heap-topk.md` → "Watch Me Solve" section (~15 min). Note the push/pop invariant and when to use a min-heap vs max-heap.

### Problem 1 — 🤝 Kth Largest Element in Array
**Stub:** `03-problems/d29-p1_kth_largest.py`
**Time target:** 20 minutes (overshooting is OK — goal is correct execution)

**Scaffolded outline (fill in code, strategy is pre-written):**
1. Brute force: sort descending, return index k-1. O(n log n). State this first.
2. Heap approach: maintain a **min-heap of size k**.
   - Invariant: heap always holds the k largest elements seen so far.
   - The root (minimum of the heap) is the kth largest overall.
3. Walk the array:
   - Push each element onto the heap.
   - If heap size exceeds k, pop the smallest (heapq.heappop).
4. After the loop, the root is the answer.
5. Time: O(n log k). Space: O(k). State both before you code.

**Intuition:** You never need more than k elements. Keep evicting the smallest intruder.

**Feynman — Kth Largest (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### Problem 2 — 🎯 K Closest Points to Origin
**Stub:** `03-problems/d29-p2_k_closest_points.py`
**Time target:** 25 minutes, strict.

**Intuition:** Distance is Euclidean but you can compare squared distances (avoids sqrt). Max-heap of size k or sort — pick the one you can implement cleanly under timer.

**Feynman — K Closest (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

**Log:** solved ___/2 · budget hit ___/2 · confidence ___/5 · next review: Day 30

---

## Day 30 — Merge K Sorted Lists + Task Scheduler

### New-Pattern Check
Continuing heaps — no new pattern guide needed. You do.

### Problem 1 — 🎯 Merge K Sorted Lists
**Stub:** `03-problems/d30-p1_merge_k_sorted_lists.py`
**Time target:** 35 minutes, strict.

**Intuition:** A min-heap lets you always pick the globally smallest remaining node across k lists. Push (val, list_index, node) tuples. Pop, attach to result, advance that list's pointer, push next.

**Feynman — Merge K Sorted Lists (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### Problem 2 — 🎯 Task Scheduler
**Stub:** `03-problems/d30-p2_task_scheduler.py`
**Time target:** 30 minutes, strict.

**Intuition:** Always schedule the most frequent remaining task. A max-heap tracks frequencies. When no task is ready, idle. Use a cooldown queue to re-add tasks after n intervals.

**Feynman — Task Scheduler (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

**Log:** solved ___/2 · budget hit ___/2 · confidence ___/5 · next review: Day 31

---

## Day 31 — Find Median from Data Stream + Revision

### New-Pattern Check
Two-heap split is the key insight — no separate guide. Know the invariant: lower half in a max-heap, upper half in a min-heap, sizes differ by at most 1.

### Problem 1 — 🎯 Find Median from Data Stream
**Stub:** `03-problems/d31-p1_find_median_from_data_stream.py`
**Time target:** 40 minutes, strict.

**Intuition:** Split the stream at the median. Lower half → max-heap (negate values for Python). Upper half → min-heap. Balance sizes on each insert. Median is root of larger heap, or average of both roots.

**Feynman — Median from Stream (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### Revision Slot
Pull one problem due today from your `04-revision/review-log.md`. Re-solve from a blank file with timer. Log confidence score.

**Log:** solved ___/1 new · rev ___/1 · confidence ___/5 · next review: Day 32

---

## Day 32 — Subsets + Permutations

### New-Pattern Check
Before touching code, read `02-patterns/09-backtracking.md` → "Watch Me Solve" section (~15 min). Internalize the template: choose → recurse → unchoose.

### Problem 1 — 🤝 Subsets
**Stub:** `03-problems/d32-p1_subsets.py`
**Time target:** 25 minutes (overshooting is OK)

**Scaffolded outline:**
1. Brute force insight: a subset is formed by including or excluding each element. 2^n subsets total.
2. Backtracking template:
   ```
   def backtrack(start, current):
       result.append(list(current))   # every call is a valid subset
       for i in range(start, len(nums)):
           current.append(nums[i])    # choose
           backtrack(i + 1, current)  # recurse (i+1 avoids reuse)
           current.pop()              # unchoose
   ```
3. Start with `backtrack(0, [])`. No base case needed — the loop terminates naturally.
4. Time: O(n · 2^n). Space: O(n) call stack. State both.

**Intuition:** At each index you decide include-or-skip. The recursion tree has 2^n leaves.

**Feynman — Subsets (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### Problem 2 — 🎯 Permutations
**Stub:** `03-problems/d32-p2_permutations.py`
**Time target:** 25 minutes, strict.

**Intuition:** All elements are used; order matters. Use a `used` boolean array or swap-in-place. Base case: current length equals nums length.

**Feynman — Permutations (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

**Log:** solved ___/2 · budget hit ___/2 · confidence ___/5 · next review: Day 33

---

## Day 33 — Combination Sum + Word Search

### New-Pattern Check
Continuing backtracking. Key variation: elements can be reused (Combination Sum) and the search happens on a 2D grid (Word Search).

### Problem 1 — 🎯 Combination Sum
**Stub:** `03-problems/d33-p1_combination_sum.py`
**Time target:** 30 minutes, strict.

**Intuition:** Unlike Subsets, you can reuse elements — so the recursive call passes `i` not `i+1`. Prune early if remaining target drops below 0.

**Feynman — Combination Sum (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### Problem 2 — 🎯 Word Search
**Stub:** `03-problems/d33-p2_word_search.py`
**Time target:** 30 minutes, strict.

**Intuition:** DFS from every starting cell. Mark visited with a sentinel (e.g. `#`) to avoid revisiting within a path. Restore the cell on backtrack.

**Feynman — Word Search (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

**Log:** solved ___/2 · budget hit ___/2 · confidence ___/5 · next review: Day 34

---

## Day 34 (Saturday) — Palindrome Partitioning + Revision × 2

### Problem 1 — 🎯 Palindrome Partitioning
**Stub:** `03-problems/d34-p1_palindrome_partitioning.py`
**Time target:** 30 minutes, strict.

**Intuition:** Backtrack over every possible cut. At each position, try all substrings starting here. If the substring is a palindrome, add it to the path and recurse from the next position.

**Feynman — Palindrome Partitioning (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### Revision Slots × 2
Pull the two problems most overdue from `04-revision/review-log.md`. Re-solve cold, then update confidence scores.

**Log:** solved ___/1 new · rev ___/2 · confidence ___/5 · next review: Day 35

---

## Day 35 (Sunday) — Mock #1

### Mock Day

**This is your first 45-minute self-mock.** Follow the protocol in `../05-mocks/mock-protocol.md` exactly.

Steps:
1. Pick the next unseen problem from your sealed mock list in `05-mocks/mock-protocol.md`.
2. Start Fathom recording. Set a 45-minute timer.
3. Narrate EVERYTHING aloud using UMPIRE: clarify → match → plan → implement → review → evaluate.
4. Stop at 45 minutes regardless of where you are.
5. Export the Fathom transcript.
6. Open `../05-mocks/ai-reviewer-prompt.md`, paste problem + transcript into a Claude session, and get graded on the 5-axis rubric.

**Goal for Mock #1:** Run the full protocol cleanly. Expect rough edges — that is normal. The goal is to discover *which* axis is your weakest, not to score perfectly.

### Mock #1 Reflection

Complete this after receiving AI feedback:

**Scores (out of 5):**
- Problem clarification: ___
- Communication: ___
- Optimization thinking: ___
- Edge cases: ___
- Recovery: ___
- **Total: ___ / 25**

**One thing I did well:**

**Two behaviors to practice before Mock #2:**
1.
2.

**Log:** Mock #1 complete · total score ___/25 · next mock: Day 42

---
