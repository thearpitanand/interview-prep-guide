# Week 6 — Graphs + DP Intro

**Days 36–42 | Mock #2 + Pattern Drill #3**

## Theme

Graphs are the pattern that separates senior from staff in many loops. This week covers DFS/BFS on grids and adjacency lists, topological sort, and Union-Find — four distinct graph techniques you can be asked about in the same interview. DP intro focuses on the simplest 1D cases to build intuition before the heavier 2D work in Week 7.

## Why It Matters

- **Graphs:** Hasura, Glean, and Appsmith use graph-shaped data models; dependency resolution and cycle detection come up in real product code. Course Schedule and Word Ladder are direct transliterations of production problems.
- **DP intro:** DP phobia is the single biggest elimination cause at senior-level loops. Climbing Stairs → House Robber → LIS is the gentlest ramp available. Mastering 1D DP this week makes Week 7 tractable.

---

## Day Table

| Day | P1 | P2 | Pattern | Markers |
|-----|----|----|---------|---------| 
| 36 (Mon) | Number of Islands (M, 25m) | Clone Graph (M, 30m) | DFS/BFS on grid/graph | 🤝 P1, 🎯 P2 |
| 37 (Tue) | Pacific Atlantic Water Flow (M, 35m) | Course Schedule (M, 30m) | Multi-source BFS / topo sort | 🎯 P1, 🎯 P2 |
| 38 (Wed) | Graph Valid Tree (M, 30m) | Number of Connected Components (M, 25m) | Union-Find | 🤝 P1, 🎯 P2 |
| 39 (Thu) | Word Ladder (H, 40m) | Rev × 1 | BFS shortest path | 🎯 P1 |
| 40 (Fri) | Climbing Stairs (E, 15m) | House Robber (M, 20m) | 1D DP intro | 🤝 P1, 🎯 P2 |
| 41 (Sat) | Longest Increasing Subsequence (M, 30m) | Rev × 2 | LIS pattern | 🎯 P1 |
| 42 (Sun) | **Mock #2** (45m) + AI review + Pattern Drill #3 | — | — | — |

---

## Day 36 — Number of Islands + Clone Graph

### New-Pattern Check
Before touching code, read `02-patterns/10-graphs-essentials.md` → "Watch Me Solve" section (~15 min). Focus on the DFS template and visited-tracking strategies (in-place mutation vs. set).

### Problem 1 — 🤝 Number of Islands
**Stub:** `03-problems/d36-p1_number_of_islands.py`
**Time target:** 25 minutes (overshooting is OK)

**Scaffolded outline:**
1. Brute force / intuition: scan the grid. When you find a `'1'`, increment count and "sink" the entire island to avoid double-counting.
2. DFS template to sink an island:
   ```
   def dfs(r, c):
       if out-of-bounds or grid[r][c] != '1':
           return
       grid[r][c] = '0'           # mark visited (in-place mutation)
       dfs(r+1, c); dfs(r-1, c)
       dfs(r, c+1); dfs(r, c-1)
   ```
3. Outer loop: for every cell, if `grid[r][c] == '1'`, call `dfs(r, c)` and increment count.
4. Time: O(m × n). Space: O(m × n) call stack worst case. State both.
5. Alternative: BFS with a deque — same complexity, different style.

**Intuition:** Each connected component of land is an island. DFS floods it to zero so you never count it twice.

**Feynman — Number of Islands (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### Problem 2 — 🎯 Clone Graph
**Stub:** `03-problems/d36-p2_clone_graph.py`
**Time target:** 30 minutes, strict.

**Intuition:** BFS or DFS traversal. Use a hash map `{original_node: cloned_node}` to avoid re-cloning. When you visit a neighbor, check the map first — if it exists, reuse; otherwise create and recurse.

**Feynman — Clone Graph (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

**Log:** solved ___/2 · budget hit ___/2 · confidence ___/5 · next review: Day 37

---

## Day 37 — Pacific Atlantic + Course Schedule

### New-Pattern Check
Two new graph techniques on one day. Pacific Atlantic needs multi-source BFS (start from the ocean edges, work inward). Course Schedule needs cycle detection via topological sort (Kahn's algorithm or DFS with color states).

### Problem 1 — 🎯 Pacific Atlantic Water Flow
**Stub:** `03-problems/d37-p1_pacific_atlantic.py`
**Time target:** 35 minutes, strict.

**Intuition:** Instead of simulating water flow downhill (expensive), reverse the direction: BFS uphill from the Pacific border, mark reachable cells. Do the same for Atlantic. Cells in both sets are the answer.

**Feynman — Pacific Atlantic (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### Problem 2 — 🎯 Course Schedule
**Stub:** `03-problems/d37-p2_course_schedule.py`
**Time target:** 30 minutes, strict.

**Intuition:** Build a directed graph of prerequisites. A valid schedule exists iff the graph has no cycle. Use Kahn's algorithm (track in-degrees, process nodes with in-degree 0) or DFS with three states: unvisited / visiting / visited.

**Feynman — Course Schedule (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

**Log:** solved ___/2 · budget hit ___/2 · confidence ___/5 · next review: Day 38

---

## Day 38 — Graph Valid Tree + Number of Connected Components

### New-Pattern Check
Before touching code, read the Union-Find section in `02-patterns/10-graphs-essentials.md`. Union-Find offers near-O(1) amortized merge/find — different from DFS and worth having as a separate tool.

### Problem 1 — 🤝 Graph Valid Tree
**Stub:** `03-problems/d38-p1_graph_valid_tree.py`
**Time target:** 30 minutes (overshooting is OK)

**Scaffolded outline:**
1. A valid tree has two properties: (a) exactly n-1 edges, and (b) all nodes are connected (no cycles).
2. Union-Find setup:
   ```
   parent = list(range(n))
   rank   = [0] * n

   def find(x):
       if parent[x] != x:
           parent[x] = find(parent[x])   # path compression
       return parent[x]

   def union(x, y):
       px, py = find(x), find(y)
       if px == py:
           return False   # cycle detected
       if rank[px] < rank[py]:
           px, py = py, px
       parent[py] = px
       if rank[px] == rank[py]:
           rank[px] += 1
       return True
   ```
3. Process each edge: if `union(u, v)` returns False, a cycle exists → return False.
4. After all edges, check that you processed exactly n-1 edges (ensures connectivity).
5. Time: O(n · α(n)) ≈ O(n). Space: O(n).

**Intuition:** Union-Find detects whether adding an edge connects two separate components or creates a cycle. A tree is the structure where every edge does the former.

**Feynman — Graph Valid Tree (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### Problem 2 — 🎯 Number of Connected Components
**Stub:** `03-problems/d38-p2_number_connected_components.py`
**Time target:** 25 minutes, strict.

**Intuition:** Same Union-Find skeleton. Start with n components. Each successful `union` reduces the count by 1.

**Feynman — Connected Components (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

**Log:** solved ___/2 · budget hit ___/2 · confidence ___/5 · next review: Day 39

---

## Day 39 — Word Ladder + Revision

### New-Pattern Check
BFS for shortest path on an implicit graph. The graph is never given — you construct edges on the fly by trying all one-character mutations.

### Problem 1 — 🎯 Word Ladder
**Stub:** `03-problems/d39-p1_word_ladder.py`
**Time target:** 40 minutes, strict.

**Intuition:** Each word is a node. Two words are connected if they differ by exactly one character. BFS from `beginWord` to `endWord` gives the shortest transformation sequence. Pre-process `wordList` into a set for O(1) lookup. Remove words from the set as you visit them to avoid cycles.

**Feynman — Word Ladder (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### Revision Slot
Pull one problem due today from `04-revision/review-log.md`. Re-solve from a blank file with timer.

**Log:** solved ___/1 new · rev ___/1 · confidence ___/5 · next review: Day 40

---

## Day 40 — Climbing Stairs + House Robber

### New-Pattern Check
Before touching code, read `02-patterns/11-dp-essentials.md` → "Watch Me Solve" section (~15 min). Focus on how to identify the subproblem, define `dp[i]`, and find the recurrence.

### Problem 1 — 🤝 Climbing Stairs
**Stub:** `03-problems/d40-p1_climbing_stairs.py`
**Time target:** 15 minutes (overshooting is OK)

**Scaffolded outline:**
1. Observation: to reach step n, you came from step n-1 (one step) or step n-2 (two steps).
2. Recurrence: `dp[i] = dp[i-1] + dp[i-2]`.
3. Base cases: `dp[1] = 1`, `dp[2] = 2`.
4. Space optimization: you only need the last two values — use two variables.
5. Time: O(n). Space: O(1). State both.

**Intuition:** This is Fibonacci in disguise. The number of ways to reach step i equals the sum of ways to reach the two preceding steps.

**Feynman — Climbing Stairs (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### Problem 2 — 🎯 House Robber
**Stub:** `03-problems/d40-p2_house_robber.py`
**Time target:** 20 minutes, strict.

**Intuition:** At each house, choose: rob it (add its value + best up to two houses ago) or skip (carry forward best from last house). Recurrence: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`.

**Feynman — House Robber (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

**Log:** solved ___/2 · budget hit ___/2 · confidence ___/5 · next review: Day 41

---

## Day 41 (Saturday) — Longest Increasing Subsequence + Revision × 2

### Problem 1 — 🎯 Longest Increasing Subsequence
**Stub:** `03-problems/d41-p1_longest_increasing_subsequence.py`
**Time target:** 30 minutes, strict.

**Intuition:** O(n²) DP: `dp[i]` = length of LIS ending at index i. For each j < i where `nums[j] < nums[i]`, `dp[i] = max(dp[i], dp[j] + 1)`. Answer is max of dp array. Bonus: O(n log n) with patience sorting + binary search.

**Feynman — LIS (3 sentences):**
- Pattern: ...
- Key invariant: ...
- Where I'd trip on a variation: ...

### Revision Slots × 2
Pull the two problems most overdue from `04-revision/review-log.md`. Re-solve cold, update confidence scores.

**Log:** solved ___/1 new · rev ___/2 · confidence ___/5 · next review: Day 42

---

## Day 42 (Sunday) — Mock #2 + Pattern Drill #3

### Mock Day

**45-minute self-mock.** Follow `../05-mocks/mock-protocol.md` exactly.

Steps:
1. Pick the next unseen problem from your sealed mock list.
2. Start Fathom recording. Set a 45-minute timer.
3. Narrate aloud using UMPIRE throughout.
4. Stop at 45 minutes.
5. Export transcript → paste into `../05-mocks/ai-reviewer-prompt.md` → get graded.

**Goal for Mock #2:** Improve on the two weakest axes from Mock #1. Compare scores explicitly.

### Mock #2 Reflection

**Scores (out of 5):**
- Problem clarification: ___
- Communication: ___
- Optimization thinking: ___
- Edge cases: ___
- Recovery: ___
- **Total: ___ / 25**

**Delta from Mock #1 (+ is improvement):** ___

**One thing that improved:**

**One axis still needing work before Mock #3:**

### Pattern Drill #3

After the mock and AI review, run Pattern Drill #3 from `04-revision/pattern-drills.md`.

- Read each problem statement (no code, no solutions).
- For each: write the pattern name + 2-sentence plan in ≤ 90 seconds.
- Score: ___ / 10
- If score < 7 → re-read `02-patterns/10-graphs-essentials.md` and `02-patterns/11-dp-essentials.md` before advancing to Week 7.

**Log:** Mock #2 score ___/25 · Drill #3 score ___/10 · ready for Week 7: yes / no

---
