# Pattern Recognition

Goal: read a problem statement and name the pattern in under 90 seconds.
This is a separate skill from solving. Train it separately.

---

## The 90-Second Routine

When you open an unseen problem:

1. Read the full problem statement once. (30 sec)
2. Note: input type, output type, constraint magnitude (n ≤ 10^5? 10^18?), and any
   ordering guarantee (sorted? DAG? distinct values?).
3. Scan the cheat table below. Match 2+ signals. Name the pattern out loud.
4. If two patterns match, pick the one that fits the output shape — a single value vs.
   a subarray vs. all combinations points to different families.

If you can't name a pattern in 90 sec, that's a signal to re-read the relevant pattern
guide before attempting the problem. Do not code with no pattern hypothesis.

---

## Recognition Signals Cheat Table

| Pattern | Signals (2–3 per row) |
|---|---|
| **Two Pointers** | Sorted array or string; find pair/triplet summing to target; detect cycle (fast/slow on LL); partition in-place |
| **Sliding Window** | Contiguous subarray/substring; "longest/shortest ... satisfying condition"; shrinkable window; frequency count inside window |
| **Binary Search** | Sorted input or answer lives in a monotone range; "minimum X such that condition holds"; O(log n) required; rotated sorted array |
| **Stack** | Matching/nesting (parens, brackets); "next greater/smaller element"; evaluate expression; monotonic order maintenance |
| **DFS** | Tree/graph traversal; path existence; all paths enumeration; connected components; recursive decomposition with backtracking |
| **BFS** | Shortest path in unweighted graph/grid; level-order traversal; "minimum steps/moves"; multi-source spreading |
| **Heap / Top-K** | "K largest/smallest/frequent"; merge K sorted structures; running median; greedy scheduling by priority |
| **Backtracking** | All combinations/permutations/subsets; constraint satisfaction; "generate all valid ..."; state is reversible |
| **Graph (Topo/Union-Find)** | Dependency ordering (courses, tasks); cycle detection in directed graph; dynamic connectivity; "number of groups/components" |
| **DP** | Optimal substructure + overlapping subproblems; "max/min/count ways"; decision at each step; substring/subsequence; grid paths |

---

## Disambiguation Rules

These pairs are commonly confused:

| If you're torn between... | Tiebreaker |
|---|---|
| Sliding Window vs. Two Pointers | Window = contiguous range with expand/shrink. Two Pointers = two independent indices converging or one fast/one slow. |
| DFS vs. Backtracking | If you need *all* solutions and undo state after recursion → Backtracking. If you need one path or a property of all nodes → DFS. |
| BFS vs. Dijkstra | Unweighted shortest path → BFS. Weighted → Dijkstra (heap-based BFS). |
| Greedy vs. DP | Greedy: local optimal choice is globally optimal (provable by exchange argument). DP: local choices interact — you need to track state across decisions. |
| Binary Search vs. Sliding Window | BS operates on a sorted axis; SW operates on a contiguous range. If the answer is a value (not an index), lean BS-on-answer. |

---

## Constraint Magnitude as a Signal

| n range | Likely acceptable complexity | Pattern family |
|---|---|---|
| n ≤ 20 | O(2^n) or O(n!) | Backtracking / bitmask DP |
| n ≤ 10^3 | O(n^2) | Nested loops, 2D DP |
| n ≤ 10^5 | O(n log n) | Sort + scan, heap, BS, sliding window |
| n ≤ 10^6 | O(n) | Hash map, two pointers, linear DP |
| n ≤ 10^18 | O(log n) | Binary search on answer, math |

When the constraint is tight, the complexity requirement often *selects* the pattern for you.

---

## Pattern-Recognition Drills

Four blind quizzes: end of Weeks 2, 4, 6, 8 (Days 14, 28, 42, 59).

### Drill Format

- 10 problem statements, no code, no hints.
- For each: write pattern name + 2-sentence plan. Time limit: 90 seconds per problem.
- Grade yourself: 1 point per correct pattern name. No partial credit.
- Pass threshold: 7/10. Below 7 → re-read this file before advancing to the next week.

### Drill Instructions

1. Use the 10 problem statements listed in `04-revision/pattern-drills.md` for each drill.
2. Set a 90-second timer per problem. When the timer fires, move on regardless.
3. Do not look up solutions between problems. Grade the whole set at the end.
4. Log your score in the week file: `Pattern drill #N: X/10`.
5. For each miss, write one sentence explaining what signal you missed.

### What to Do With Misses

A miss means one of three things:
- You haven't seen the pattern enough times → re-read the pattern guide.
- You saw the signal but mapped it to the wrong pattern → study the disambiguation rules above.
- You ran out of time → pattern recognition is slow; drill more cold reads.

Track miss patterns across all four drills. If the same pattern appears in your miss column
twice, that's your personal weak spot — re-solve two more problems from that family before
the next mock.

---

## Building the Habit Outside of Drills

During regular practice (Weeks 1–4), before you start each 🎯 solo problem:
spend 60 seconds writing the pattern name and one-line plan *before* you look at the starter code.
Then compare your prediction to the tagged pattern in the problem stub. If they don't match,
note why — you'll build a personal miss log faster than the quarterly drills alone.
