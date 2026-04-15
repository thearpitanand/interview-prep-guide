# Week 1 — Arrays & Hashing + Two Pointers

**Pattern theme:** Hash maps for O(1) lookup; two pointers for in-place traversal and pair/triplet problems.

**Why this matters for target companies:** Hash map and two-pointer problems dominate the first screening round at Razorpay, Meesho, Swiggy, Postman, and CRED. Roughly 60% of phone screens open with an array problem. Solving these fluently — including explaining *why* you reach for a hash map vs a nested loop — is the single highest-ROI investment in the first week. Two Sum and 3Sum variants appear in some form at almost every product company in India's growth-stage space.

---

## Day-by-Day Table

| Day | P1 | P2 | Pattern |
|---|---|---|---|
| 1 | Two Sum (E, 15m) 🤝 | Valid Anagram (E, 15m) 🎯 | Hash map basics |
| 2 | Group Anagrams (M, 25m) 🎯 | Top K Frequent Elements (M, 25m) 🎯 | Hash + counting |
| 3 | Product of Array Except Self (M, 25m) 🎯 | Longest Consecutive Sequence (M, 30m) 🎯 | Prefix / hash set |
| 4 | Valid Palindrome (E, 15m) 🤝 | Two Sum II — Sorted (E, 15m) 🎯 | Two pointers intro |
| 5 | 3Sum (M, 30m) 🎯 | Container With Most Water (M, 25m) 🎯 | Two pointers core |
| 6 (Sat) | Trapping Rain Water (M, 35m) 🎯 | Rev × 2 | Two pointers stretch |
| 7 (Sun) | Flex / catch-up | — | — |

---

## Day 1 — Two Sum, Valid Anagram

**New pattern today?** Yes — Arrays & Hashing. Read `../02-patterns/01-arrays-hashing.md` first (I do stage, 15m).

**Problem 1** 🤝 — Two Sum — Stub: `../03-problems/d01-p1_two_sum.py`
For every element, check if its complement (target − current) already exists in the map. One pass is enough — you build and query the map simultaneously.

**Problem 2** 🎯 — Valid Anagram — Stub: `../03-problems/d01-p2_valid_anagram.py`
Count character frequencies in both strings and compare. Equal maps means equal letters — an anagram.

**If 🤝 (we do) — scaffolded outline for Two Sum:**
1. Create an empty hash map `seen = {}` mapping value → index.
2. For each index `i` and value `num` in `nums`: compute `complement = target - num`.
3. If `complement` is in `seen`, return `[seen[complement], i]`. Otherwise add `num → i` to `seen`.

**Feynman — Two Sum (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Feynman — Valid Anagram (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Log:** solved ___/2 • budget hit ___/2 • confidence ___/5 • next review: Day 2

---

## Day 2 — Group Anagrams, Top K Frequent Elements

**New pattern today?** No — continuing Arrays & Hashing.

**Problem 1** 🎯 — Group Anagrams — Stub: `../03-problems/d02-p1_group_anagrams.py`
Sort each word to get a canonical key; all anagrams share the same key. Group words under that key in a defaultdict.

**Problem 2** 🎯 — Top K Frequent Elements — Stub: `../03-problems/d02-p2_top_k_frequent.py`
Count frequencies with a hash map, then pick the top k using a min-heap of size k or a bucket-sort indexed by frequency.

**Feynman — Group Anagrams (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Feynman — Top K Frequent Elements (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Log:** solved ___/2 • budget hit ___/2 • confidence ___/5 • next review: Day 3

---

## Day 3 — Product of Array Except Self, Longest Consecutive Sequence

**New pattern today?** No — continuing Arrays & Hashing (prefix products + hash set).

**Problem 1** 🎯 — Product of Array Except Self — Stub: `../03-problems/d03-p1_product_except_self.py`
Build prefix products left-to-right, then multiply in suffix products right-to-left. No division needed; each position's answer is its prefix × suffix.

**Problem 2** 🎯 — Longest Consecutive Sequence — Stub: `../03-problems/d03-p2_longest_consecutive.py`
Put all numbers in a set. Start counting a sequence only when `num - 1` is absent — this ensures each sequence is processed once, giving O(n) total.

**Feynman — Product of Array Except Self (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Feynman — Longest Consecutive Sequence (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Log:** solved ___/2 • budget hit ___/2 • confidence ___/5 • next review: Day 4

---

## Day 4 — Valid Palindrome, Two Sum II

**New pattern today?** Yes — Two Pointers. Read `../02-patterns/02-two-pointers.md` first (I do stage, 15m).

**Problem 1** 🤝 — Valid Palindrome — Stub: `../03-problems/d04-p1_valid_palindrome.py`
Two pointers from both ends. Skip non-alphanumeric characters on each side, then compare lowercased characters. Any mismatch → not a palindrome.

**Problem 2** 🎯 — Two Sum II — Sorted — Stub: `../03-problems/d04-p2_two_sum_sorted.py`
The sorted order lets you move pointers directionally: sum too small → advance left; sum too large → retreat right. No hash map needed.

**If 🤝 (we do) — scaffolded outline for Valid Palindrome:**
1. Set `left = 0`, `right = len(s) - 1`.
2. While `left < right`: skip `s[left]` if not alphanumeric (advance left); skip `s[right]` if not alphanumeric (retreat right).
3. Compare `s[left].lower()` and `s[right].lower()`. If they differ, return `False`. Otherwise advance both pointers.
4. If the loop completes without a mismatch, return `True`.

**Feynman — Valid Palindrome (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Feynman — Two Sum II — Sorted (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Log:** solved ___/2 • budget hit ___/2 • confidence ___/5 • next review: Day 5

---

## Day 5 — 3Sum, Container With Most Water

**New pattern today?** No — continuing Two Pointers.

**Problem 1** 🎯 — 3Sum — Stub: `../03-problems/d05-p1_three_sum.py`
Sort first. Fix one element `nums[i]`, then run two-pointer search for the complement pair. Skip duplicates at both the outer and inner levels to avoid repeated triplets.

**Problem 2** 🎯 — Container With Most Water — Stub: `../03-problems/d05-p2_container_with_most_water.py`
Start with the widest container. Always move the pointer with the shorter bar inward — the width decreases, so only a taller bar can possibly increase area.

**Feynman — 3Sum (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Feynman — Container With Most Water (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Log:** solved ___/2 • budget hit ___/2 • confidence ___/5 • next review: Day 6

---

## Day 6 (Saturday) — Trapping Rain Water + Rev × 2

**New pattern today?** No — Two Pointers stretch problem.

**Problem 1** 🎯 — Trapping Rain Water — Stub: `../03-problems/d06-p1_trapping_rain_water.py`
Two pointers meet in the middle. The water level at each position is bounded by the shorter of the two running maxima. Process whichever side has the smaller max — you know exactly how much water that bar holds.

**Revision (Rev × 2):** Pull the two problems with the earliest due date from `../04-revision/revision-schedule.md`. Re-solve from blank with timer; no peeking at your solution.

**Feynman — Trapping Rain Water (fill after solving):**
- Pattern:
- Key invariant:
- Where I'd trip:

**Log:** solved ___/1 new • rev ___/2 • budget hit ___/3 • confidence ___/5 • next review: Day 7

---

## Day 7 (Sunday) — Flex / Catch-up

Use this day to:
- Re-solve any problem where confidence < 3 from the week.
- Re-read `../02-patterns/01-arrays-hashing.md` or `../02-patterns/02-two-pointers.md` if any Feynman note says "Where I'd trip."
- Or rest completely — the next six days will be demanding.

---

> **Revision due next week:** After Day 7, check `../04-revision/revision-schedule.md` for problems due in Week 2 (Day N+1 and Day N+3 slots from this week). Pull them into Day 8's warm-up before starting new problems.
