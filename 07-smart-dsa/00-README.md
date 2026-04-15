# 07-Smart-DSA — 60-Day High-ROI DSA Program

A fully self-contained, 60-day DSA program for senior engineers targeting product companies and high-growth startups. ~80 problems, medium-dominant, sequenced for interview ROI, with three methodologies baked in from day one.

---

## The Learning Method: Gradual Release (I Do → We Do → You Do)

Every new pattern is introduced in three stages. This is not optional — it is the core mechanic.

| Stage                    | Where it lives                                                     | Duration                     | What happens                                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------ | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **I do** (model)         | `02-patterns/<pattern>.md` — "Watch Me Solve" section              | 15 min read, no keyboard     | The guide narrates one full worked solve in first person. You read. You do not code.                                                                                 |
| **We do** (guided)       | First problem of each new pattern — marked **🤝** in the week file | Full time budget, scaffolded | The day row includes a brute-force → invariant → shrink → result outline. You fill in the code. Timer runs, but overshooting is acceptable. Goal: correct execution. |
| **You do** (independent) | Every subsequent problem of that pattern — marked **🎯**           | Strict time budget           | Blank stub. No hints. If the timer blows, stop, re-read the pattern guide, re-solve the next day.                                                                    |

**Why:** a senior engineer with weak DSA fails in the _planning_ step, not the implementation. Gradual release targets exactly that gap.

---

## Who This Is For

Senior engineers (4–6 YOE) with moderate-to-weak DSA who have limited time (2–3h weekdays, 4–5h weekends) and need interview-focused coverage, not exhaustive breadth.

---

## How 60 Days Are Structured

### Weekly Rhythm

| Day of week | Type              | Load                      | What happens                                                                                                                                                                                    |
| ----------- | ----------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mon–Fri     | Learn             | 2 new problems, ≤ 3h      | New pattern → read "Watch Me Solve" (I do, 15m) → 🤝 guided problem (we do, 30–40m) → Feynman → 🎯 solo problem (you do, 25m) → Feynman → Log. Continuing pattern: 🎯 × 2 → Feynman each → Log. |
| Sat         | Revision + 1 new  | 1 new + 2 re-solves, ≤ 4h | Spaced-repetition queue first, then 1 stretch problem.                                                                                                                                          |
| Sun         | Flex / Mock (W5+) | Variable                  | Catch-up, rest, or self-mock (Weeks 5–8).                                                                                                                                                       |

**Throughput:** ~11 new problems/week × ~7.5 weeks = **~80 new problems**.

---

## 8-Week Curriculum

| Week | Patterns                                                   | Why for target companies                                                                          | Problems             | New |
| ---- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------- | --- |
| 1    | Arrays & Hashing, Two Pointers                             | 60% of screeners start here (Razorpay, Meesho, Swiggy, Postman, CRED)                             | E:4 M:7              | 11  |
| 2    | Sliding Window, Binary Search (on values + on answer)      | Frequent at BrowserStack, Chargebee, Paytm, Fi. BS-on-answer is a senior signal                   | E:2 M:8 H:1          | 11  |
| 3    | Stack / Monotonic Stack, Linked List                       | Monotonic stack filters mid vs senior; LL staple at Dream11, Cars24, Unacademy                    | E:2 M:8 H:1          | 11  |
| 4    | Trees (DFS + BFS), BST                                     | Universal — LCA, serialize, validate BST, right view appear at ≥1 round almost everywhere         | E:2 M:8 H:1          | 11  |
| 5    | Heaps / Top-K, Backtracking                                | Top-K for routing (Zepto, Swiggy, Meesho); backtracking for subsets/permutations (CRED, Razorpay) | E:1 M:8 H:1 + 1 mock | 10  |
| 6    | Graphs (BFS/DFS/Topo/Union-Find), DP intro                 | Graphs hit senior loops (Hasura, Glean, Appsmith). DP phobia is the #1 elimination cause          | M:9 H:1 + 1 mock     | 10  |
| 7    | DP (0/1 knapsack, LIS, grid, interval), Greedy + Intervals | Final filter at CRED, Razorpay, Dream11, MPL                                                      | M:8 H:2 + 2 mocks    | 10  |
| 8    | Mixed hards + full revision + mocks                        | Simulate real loops; Top-30 cold-solve sprint                                                     | M:3 H:3 + 3 mocks    | 6   |

**Totals:** ~80 new problems (≈11 easy, ≈59 medium, ≈10 hard) + 7 self-mocks.

---

## Full 60-Day Problem Schedule

Legend: **E** Easy · **M** Medium · **H** Hard · time in minutes · 🤝 guided (we do) · 🎯 solo (you do) · Rev = spaced-repetition re-solve, not new.

### Week 1 — Arrays & Hashing + Two Pointers

| Day     | P1                                      | P2                                      | Pattern              |
| ------- | --------------------------------------- | --------------------------------------- | -------------------- |
| 1       | 🤝 Two Sum (E, 15)                      | 🎯 Valid Anagram (E, 15)                | Hash map basics      |
| 2       | 🎯 Group Anagrams (M, 25)               | 🎯 Top K Frequent Elements (M, 25)      | Hash + counting      |
| 3       | 🎯 Product of Array Except Self (M, 25) | 🎯 Longest Consecutive Sequence (M, 30) | Prefix / hash set    |
| 4       | 🤝 Valid Palindrome (E, 15)             | 🎯 Two Sum II — Sorted (E, 15)          | Two pointers intro   |
| 5       | 🎯 3Sum (M, 30)                         | 🎯 Container With Most Water (M, 25)    | Two pointers core    |
| 6 (Sat) | 🎯 Trapping Rain Water (M, 35)          | Rev × 2                                 | Two pointers stretch |
| 7 (Sun) | Flex / catch-up                         | —                                       | —                    |

### Week 2 — Sliding Window + Binary Search

| Day      | P1                                              | P2                                          | Pattern               |
| -------- | ----------------------------------------------- | ------------------------------------------- | --------------------- |
| 8        | 🎯 Best Time to Buy/Sell Stock (E, 15)          | 🤝 Longest Substring Without Repeat (M, 25) | Window expand/shrink  |
| 9        | 🎯 Longest Repeating Char Replacement (M, 30)   | 🎯 Permutation in String (M, 25)            | Fixed/variable window |
| 10       | 🎯 Minimum Window Substring (H, 40)             | 🎯 Sliding Window Maximum (H→M, 30)         | Window + deque        |
| 11       | 🤝 Binary Search (E, 15)                        | 🎯 Search in Rotated Sorted Array (M, 25)   | BS invariants         |
| 12       | 🎯 Find Minimum in Rotated Sorted Array (M, 25) | 🎯 Time-Based KV Store (M, 30)              | BS on index           |
| 13 (Sat) | 🎯 Koko Eating Bananas (M, 30)                  | Rev × 2                                     | BS on answer          |
| 14 (Sun) | Flex + Pattern-recognition drill #1             | —                                           | —                     |

### Week 3 — Stack / Monotonic Stack + Linked List

| Day      | P1                                        | P2                                | Pattern               |
| -------- | ----------------------------------------- | --------------------------------- | --------------------- |
| 15       | 🤝 Valid Parentheses (E, 15)              | 🎯 Min Stack (M, 20)              | Stack basics          |
| 16       | 🎯 Evaluate RPN (M, 25)                   | 🤝 Daily Temperatures (M, 25)     | Monotonic stack intro |
| 17       | 🎯 Largest Rectangle in Histogram (H, 40) | 🎯 Car Fleet (M, 25)              | Monotonic stack hard  |
| 18       | 🤝 Reverse Linked List (E, 15)            | 🎯 Merge Two Sorted Lists (E, 15) | LL pointer basics     |
| 19       | 🎯 Linked List Cycle (E→M, 20)            | 🎯 Reorder List (M, 30)           | Fast/slow pointers    |
| 20 (Sat) | 🎯 LRU Cache (M, 35)                      | Rev × 2                           | Hash + doubly LL      |
| 21 (Sun) | Flex                                      | —                                 | —                     |

### Week 4 — Trees (DFS + BFS) + BST

| Day      | P1                                           | P2                                     | Pattern          |
| -------- | -------------------------------------------- | -------------------------------------- | ---------------- |
| 22       | 🤝 Invert Binary Tree (E, 15)                | 🎯 Max Depth of Binary Tree (E, 15)    | Recursion warmup |
| 23       | 🎯 Diameter of Binary Tree (M, 25)           | 🎯 Balanced Binary Tree (M, 20)        | DFS with return  |
| 24       | 🎯 Same Tree (E, 15)                         | 🎯 LCA of Binary Tree (M, 30)          | DFS with state   |
| 25       | 🤝 Binary Tree Level Order Traversal (M, 25) | 🎯 Binary Tree Right Side View (M, 25) | BFS template     |
| 26       | 🤝 Validate BST (M, 25)                      | 🎯 Kth Smallest in BST (M, 25)         | BST invariants   |
| 27 (Sat) | 🎯 Serialize/Deserialize Binary Tree (H, 40) | Rev × 2                                | DFS + encoding   |
| 28 (Sun) | Flex + Pattern-recognition drill #2          | —                                      | —                |

### Week 5 — Heaps / Top-K + Backtracking (mocks START)

| Day      | P1                                        | P2                                    | Pattern                 |
| -------- | ----------------------------------------- | ------------------------------------- | ----------------------- |
| 29       | 🤝 Kth Largest Element in Array (E→M, 20) | 🎯 K Closest Points to Origin (M, 25) | Heap basics             |
| 30       | 🎯 Merge K Sorted Lists (H, 35)           | 🎯 Task Scheduler (M, 30)             | Heap + greedy           |
| 31       | 🎯 Find Median from Data Stream (H, 40)   | Rev × 1                               | Two heaps               |
| 32       | 🤝 Subsets (M, 25)                        | 🎯 Permutations (M, 25)               | Backtracking template   |
| 33       | 🎯 Combination Sum (M, 30)                | 🎯 Word Search (M, 30)                | Backtracking with state |
| 34 (Sat) | 🎯 Palindrome Partitioning (M, 30)        | Rev × 2                               | Backtracking + cuts     |
| 35 (Sun) | **Mock #1** (45m) + AI review             | —                                     | —                       |

### Week 6 — Graphs + DP Intro

| Day      | P1                                               | P2                                        | Pattern                 |
| -------- | ------------------------------------------------ | ----------------------------------------- | ----------------------- |
| 36       | 🤝 Number of Islands (M, 25)                     | 🎯 Clone Graph (M, 30)                    | DFS/BFS on grid/graph   |
| 37       | 🎯 Pacific Atlantic Water Flow (M, 35)           | 🎯 Course Schedule (M, 30)                | Multi-source BFS / topo |
| 38       | 🤝 Graph Valid Tree (M, 30)                      | 🎯 Number of Connected Components (M, 25) | Union-Find              |
| 39       | 🎯 Word Ladder (H, 40)                           | Rev × 1                                   | BFS shortest path       |
| 40       | 🤝 Climbing Stairs (E, 15)                       | 🎯 House Robber (M, 20)                   | 1D DP intro             |
| 41 (Sat) | 🎯 Longest Increasing Subsequence (M, 30)        | Rev × 2                                   | LIS pattern             |
| 42 (Sun) | **Mock #2** (45m) + AI review + Pattern drill #3 | —                                         | —                       |

### Week 7 — DP + Intervals + Greedy

| Day      | P1                                                       | P2                                       | Pattern                 |
| -------- | -------------------------------------------------------- | ---------------------------------------- | ----------------------- |
| 43       | 🤝 Coin Change (M, 30)                                   | 🎯 Partition Equal Subset Sum (M, 30)    | 1D / 0-1 knapsack       |
| 44       | 🎯 Word Break (M, 30)                                    | 🤝 Longest Common Subsequence (M, 30)    | String DP               |
| 45       | 🎯 Edit Distance (H, 40)                                 | Rev × 1                                  | 2D string DP            |
| 46       | 🤝 Unique Paths (M, 20)                                  | 🎯 Longest Palindromic Substring (M, 30) | Grid DP / expand center |
| 47       | 🤝 Jump Game (M, 20)                                     | 🎯 Gas Station (M, 25)                   | Greedy                  |
| 48 (Sat) | 🤝 Merge Intervals (M, 25) + 🎯 Meeting Rooms II (M, 25) | 🎯 Burst Balloons (H, 45)                | Intervals + interval DP |
| 49 (Sun) | **Mocks #3 and #4** + AI review                          | —                                        | —                       |

### Week 8 — Final Sprint

| Day      | Activity                                                                                          |
| -------- | ------------------------------------------------------------------------------------------------- |
| 50       | Mixed hard: Median of Two Sorted Arrays (H, 40) + Rev × 2                                         |
| 51       | Mixed hard: Longest Valid Parentheses (H, 35) + Rev × 2                                           |
| 52       | **Mock #5** + AI review                                                                           |
| 53       | Top-30 cold-solve sprint part 1 (10 problems, 30m each)                                           |
| 54 (Sat) | Top-30 cold-solve sprint part 2 (10 problems)                                                     |
| 55 (Sun) | **Mock #6** + AI review                                                                           |
| 56       | Top-30 cold-solve sprint part 3 (10 problems) + gap analysis                                      |
| 57       | Targeted re-solve of anything that scored confidence < 4                                          |
| 58       | **Mock #7** (hardest — unseen medium from sealed list) + AI review                                |
| 59       | Final pattern-recognition drill #4 + interview framework run-through                              |
| 60       | Rest / deload. Re-read `01-method/interview-framework.md` and `01-method/pattern-recognition.md`. |

---

## How to Use This Pillar

1. **Start with Day 0.** Read `00-day-0-onboarding.md` before anything else. It takes ~90 minutes and sets up your tools, sealed mock list, and calendar.
2. **Follow the week files.** Open `03-weekly/week-N.md` at the start of each week. Each day has a row in a table; Feynman note slots sit below each row.
3. **Before a 🤝 problem:** read the "Watch Me Solve" section in the relevant `02-patterns/` file (15 min, no keyboard). Then open the stub.
4. **Run problem stubs directly:**
   ```bash
   python 07-smart-dsa/03-problems/d01-p1_two_sum.py
   ```
   A passing file prints `All tests passed!`. Zero external dependencies.
5. **After every solve:** write your 3-sentence Feynman explanation in the week file. If you can't explain it plainly, you don't own it yet.
6. **Timer blows?** Stop immediately. Re-read the pattern guide. Re-solve from a blank file the next day.
7. **Saturday:** pull the spaced-repetition queue from `04-revision/review-log.md` before touching any new problems.
8. **Mocks (Weeks 5–8):** follow `05-mocks/mock-protocol.md` exactly. Export the Fathom transcript and run it through `05-mocks/ai-reviewer-prompt.md`.

---

## File Map

```
07-smart-dsa/
├── 00-README.md                    ← you are here
├── 00-day-0-onboarding.md          ← start here before Day 1
├── 01-method/
│   ├── feynman-protocol.md         ← 3-sentence out-loud explanation after every solve
│   ├── deliberate-practice.md      ← strict timers, re-solve rules
│   ├── pattern-recognition.md      ← map a problem → pattern in < 90s
│   └── interview-framework.md      ← UMPIRE sequence for unseen problems
├── 02-patterns/                    ← 11 pattern guides (I do stage lives here)
│   ├── 01-arrays-hashing.md
│   ├── 02-two-pointers.md
│   ├── 03-sliding-window.md
│   ├── 04-binary-search.md
│   ├── 05-stack-monotonic.md
│   ├── 06-linked-list.md
│   ├── 07-trees-dfs-bfs.md
│   ├── 08-heap-topk.md
│   ├── 09-backtracking.md
│   ├── 10-graphs-essentials.md
│   └── 11-dp-essentials.md
├── 03-weekly/                      ← 8 week files with day tables + Feynman slots
│   ├── week-1.md … week-8.md
├── 03-problems/                    ← ~80 problem stubs, prefixed by day
│   ├── d01-p1_two_sum.py
│   ├── d01-p2_valid_anagram.py
│   └── … d60-p1_*.py
├── 04-revision/
│   ├── top-30-list.md              ← 30 canonical problems for Week 8 sprint
│   ├── revision-schedule.md        ← 1d / 3d / 7d / 21d spaced repetition rules
│   ├── review-log.md               ← tracking template (keep open in second tab)
│   └── pattern-drills.md           ← 4 blind pattern-recognition quizzes
└── 05-mocks/
    ├── mock-protocol.md            ← 45m solo mock + Fathom recording steps
    ├── rubric.md                   ← 5-axis scoring rubric
    ├── ai-reviewer-prompt.md       ← copy-paste into a chat session post-mock
    └── mock-log.md                 ← per-mock score tracking
```

---

## Revision System at a Glance

| First solved | Review 1 | Review 2 | Review 3 | Review 4 |
| ------------ | -------- | -------- | -------- | -------- |
| Day N        | Day N+1  | Day N+3  | Day N+7  | Day N+21 |

- Confidence ≥ 4: passive review — read Feynman notes, rebuild template on paper, 5 min.
- Confidence < 4: re-solve from blank file with timer.
- Any confidence < 3 on a review: reset interval to Day+1.

---

## Mock Schedule

| Mock   | Day | Notes                                                         |
| ------ | --- | ------------------------------------------------------------- |
| #1     | 35  | First mock — goal is to run the full protocol, not score well |
| #2     | 42  | Pattern drill same day                                        |
| #3, #4 | 49  | Back-to-back to build stamina                                 |
| #5     | 52  | Pre-sprint check                                              |
| #6     | 55  | Mid-sprint                                                    |
| #7     | 58  | Hardest — unseen medium from sealed list                      |
