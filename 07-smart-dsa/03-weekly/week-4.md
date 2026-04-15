# Week 4 — Trees (DFS + BFS) + BST

**Theme:** Recursive tree traversal, BFS level-order, and BST invariant exploitation.

**Why this matters for target companies:** Tree problems appear in at least one round at almost every product company — LCA, serialize/deserialize, right side view, and validate BST show up at Razorpay, Meesho, BrowserStack, Chargebee, and CRED. The DFS recursion pattern transfers directly to graphs in Week 6, so getting the return-value discipline right here pays compound dividends. Interviewers use these problems to test whether you can reason about recursive call stacks without losing track of state.

---

## Week 4 Schedule

| Day | P1 | P2 | Pattern | Marker |
|-----|----|----|---------|----- --|
| 22 | Invert Binary Tree (E, 15m) | Max Depth of Binary Tree (E, 15m) | Recursion warmup | 🤝 P1 |
| 23 | Diameter of Binary Tree (M, 25m) | Balanced Binary Tree (M, 20m) | DFS with return | 🎯 both |
| 24 | Same Tree (E, 15m) | LCA of Binary Tree (M, 30m) | DFS with state | 🎯 both |
| 25 | Binary Tree Level Order Traversal (M, 25m) | Binary Tree Right Side View (M, 25m) | BFS template | 🤝 P1 |
| 26 | Validate BST (M, 25m) | Kth Smallest in BST (M, 25m) | BST invariants | 🤝 P1 |
| 27 (Sat) | Serialize/Deserialize Binary Tree (H, 40m) | Rev × 2 | DFS + encoding | 🎯 P1 |
| 28 (Sun) | Flex + Pattern-recognition drill #2 | — | — | — |

---

## Day 22 — Invert Binary Tree + Max Depth

**New pattern today? Yes (Tree DFS) — read `02-patterns/07-trees-dfs-bfs.md` before starting.**

---

### Problem 1 🤝 — Invert Binary Tree (LC 226)

**Stub:** `07-smart-dsa/03-problems/d22-p1_invert_binary_tree.py`

**Intuition:** Recursion mirrors the tree's own structure — invert left subtree, invert right subtree, then swap the two children at the current node.

**Scaffolded outline (we do together):**
1. Base case: if `root` is `None`, return `None`.
2. Recursively call `invert_tree(root.left)` and `invert_tree(root.right)`.
3. Swap: `root.left, root.right = root.right, root.left`.
4. Return `root` — the caller needs the (now-inverted) subtree root to wire it into its own swap.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 23

---

### Problem 2 🎯 — Max Depth of Binary Tree (LC 104)

**Stub:** `07-smart-dsa/03-problems/d22-p2_max_depth_binary_tree.py`

**Intuition:** The depth of a node is 1 plus the max depth of its two children; base case is 0 for a null node — a clean one-liner in Python.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 23

---

## Day 23 — Diameter + Balanced Binary Tree

**New pattern today? No — DFS with a return value that combines subtree results.**

---

### Problem 1 🎯 — Diameter of Binary Tree (LC 543)

**Stub:** `07-smart-dsa/03-problems/d23-p1_diameter_binary_tree.py`

**Intuition:** The diameter through a node equals left-depth + right-depth; track the global maximum with a closure variable while the recursive helper returns depth, not diameter.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 24

---

### Problem 2 🎯 — Balanced Binary Tree (LC 110)

**Stub:** `07-smart-dsa/03-problems/d23-p2_balanced_binary_tree.py`

**Intuition:** Have the DFS helper return -1 to propagate "unbalanced" up the call stack; if either child returns -1 or heights differ by more than 1, propagate -1 immediately instead of recomputing heights.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 24

---

## Day 24 — Same Tree + LCA of Binary Tree

**New pattern today? No — DFS with accumulated state passed down or bubbled up.**

---

### Problem 1 🎯 — Same Tree (LC 100)

**Stub:** `07-smart-dsa/03-problems/d24-p1_same_tree.py`

**Intuition:** Two trees are the same if their roots have equal values and both subtrees are recursively the same; any structural or value mismatch short-circuits to `False`.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 25

---

### Problem 2 🎯 — LCA of Binary Tree (LC 236)

**Stub:** `07-smart-dsa/03-problems/d24-p2_lca_binary_tree.py`

**Intuition:** Post-order DFS: if a node is p or q return it; the first ancestor that gets non-null returns from both children is the LCA — the problem reduces to a boolean "found p or q in this subtree" returned upward.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 25

---

## Day 25 — Level Order Traversal + Right Side View

**New pattern today? Yes (Tree BFS) — re-read the BFS section of `02-patterns/07-trees-dfs-bfs.md` before starting.**

---

### Problem 1 🤝 — Binary Tree Level Order Traversal (LC 102)

**Stub:** `07-smart-dsa/03-problems/d25-p1_level_order_traversal.py`

**Intuition:** A queue processes nodes level by level; snapshot `len(queue)` at the start of each level to know how many nodes belong to that level before children are enqueued.

**Scaffolded outline (we do together):**
1. If root is `None` return `[]`. Initialize `queue = deque([root])` and `result = []`.
2. While the queue is non-empty: record `level_size = len(queue)` and `level = []`.
3. Loop `level_size` times: pop left from the queue, append its value to `level`, enqueue its left and right children if they exist.
4. Append `level` to `result`. After the outer while loop, return `result`.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 26

---

### Problem 2 🎯 — Binary Tree Right Side View (LC 199)

**Stub:** `07-smart-dsa/03-problems/d25-p2_right_side_view.py`

**Intuition:** Level order traversal with BFS; for each level keep only the last node's value — the rightmost visible node from that depth.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 26

---

## Day 26 — Validate BST + Kth Smallest in BST

**New pattern today? Yes (BST invariants) — read the BST section of `02-patterns/07-trees-dfs-bfs.md` before starting.**

---

### Problem 1 🤝 — Validate BST (LC 98)

**Stub:** `07-smart-dsa/03-problems/d26-p1_validate_bst.py`

**Intuition:** Pass valid bounds `(low, high)` down the recursion — every node must lie strictly inside the bounds inherited from its ancestors, not just be greater/less than its direct parent.

**Scaffolded outline (we do together):**
1. Define `validate(node, low, high)` where initially `low = -inf` and `high = +inf`.
2. Base case: if `node` is `None`, return `True`.
3. If `node.val <= low` or `node.val >= high`, return `False` (BST requires strict inequality).
4. Recurse: `validate(node.left, low, node.val)` AND `validate(node.right, node.val, high)`.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 27

---

### Problem 2 🎯 — Kth Smallest in BST (LC 230)

**Stub:** `07-smart-dsa/03-problems/d26-p2_kth_smallest_bst.py`

**Intuition:** In-order traversal of a BST visits nodes in ascending order; the kth node visited is the kth smallest — no sorting needed.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 27

---

## Day 27 (Sat) — Serialize/Deserialize Binary Tree + Revision × 2

**New pattern today? No — DFS with pre-order encoding.**

---

### Problem 1 🎯 — Serialize/Deserialize Binary Tree (LC 297)

**Stub:** `07-smart-dsa/03-problems/d27-p1_serialize_deserialize_binary_tree.py`

**Intuition:** Pre-order DFS produces a sequence that encodes structure unambiguously when null nodes are included as sentinels; deserialize by consuming values from the sequence in the same pre-order.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 28

---

### Revision × 2

Pull the two problems due per your revision schedule (check `04-revision/review-log.md`). Re-solve from a blank file with the timer running.

---

## Day 28 (Sun) — Flex + Pattern-Recognition Drill #2

Open `04-revision/pattern-drills.md` and run **Drill #2** (10 problems, ≤ 90 seconds each — pattern name + 2-sentence plan, no coding). Target score: ≥ 7/10. If you score < 7, re-read `02-patterns/05-stack-monotonic.md`, `02-patterns/06-linked-list.md`, and `02-patterns/07-trees-dfs-bfs.md` before starting Week 5.

Also: run one **dry-run self-mock** today (45 min, Fathom on) to verify the recording + AI-reviewer-prompt chain produces useful output before Mock #1 fires on Day 35.

---

## Week 4 Revision Reminder

By the end of this week, the following problems should be in your spaced-repetition queue. Verify they appear in `04-revision/review-log.md`:

- Day 22: Invert Binary Tree, Max Depth of Binary Tree
- Day 23: Diameter of Binary Tree, Balanced Binary Tree
- Day 24: Same Tree, LCA of Binary Tree
- Day 25: Level Order Traversal, Right Side View
- Day 26: Validate BST, Kth Smallest in BST
- Day 27: Serialize/Deserialize Binary Tree

Confidence < 3 on any re-solve → reset interval to Day+1 and re-solve from scratch tomorrow.

→ **Next up:** Week 5 — Heaps / Top-K + Backtracking. Pattern drill #3 fires at the end of Week 6.
