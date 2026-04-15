# Trees: DFS & BFS

## Recognition Signals (how to spot this in <90s)

### DFS Signals
- Problem asks about **paths**, **depth**, **height**, or **diameter**
- You need to aggregate information **bottom-up** (each subtree reports a value to its parent)
- "Validate", "check if two trees are equal", "find LCA"
- A recursive structure is natural — the answer for a node depends on the answers for its children

### BFS Signals
- "Level order", "level by level", "right side view", "zigzag traversal"
- **Shortest path** in a tree or graph (BFS finds the shortest path by definition)
- You need to process nodes **in the order they appear by depth**, not by subtree
- "Minimum depth" — you want to stop at the first leaf, not after visiting everything

## Mental Model

DFS on a tree is the natural extension of recursion. At each node, you trust that the recursive calls on the left and right subtrees will return the correct answer for those subtrees — your only job is to combine those answers with the current node's value. This "trust the recursive contract" mindset unlocks every DFS problem. Before writing code, decide: what should the function return? Common choices are a boolean, an integer (depth/count), a pair (is_valid, height), or a node (for LCA problems). The return type IS the design.

BFS is queue-based. You start with the root, process it, then enqueue its children. The queue guarantees level-order processing: you fully exhaust level k before touching level k+1. The key technique is the "level snapshot" — at the start of each level, record `level_size = len(queue)`, then process exactly that many nodes before moving on. This lets you track which level you are on without extra bookkeeping. Every BFS tree problem uses this snapshot idiom.

## Reusable Python Template

```python
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


# --- Recursive DFS (post-order: children before parent) ---
def dfs_postorder(node: Optional[TreeNode]) -> int:
    if node is None:
        return 0  # base case — define what "nothing" returns for your problem

    left_result = dfs_postorder(node.left)    # trust the left subtree
    right_result = dfs_postorder(node.right)  # trust the right subtree

    # combine: this is where your logic lives
    return 1 + max(left_result, right_result)  # example: max depth


# --- Iterative DFS (pre-order using explicit stack) ---
def dfs_iterative(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    result: list[int] = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)          # process current node
        if node.right:
            stack.append(node.right)     # push right first → left processed first
        if node.left:
            stack.append(node.left)
    return result


# --- BFS (level order with level snapshot) ---
def bfs_level_order(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []
    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)          # snapshot: how many nodes at this level
        level: list[int] = []

        for _ in range(level_size):      # process exactly this level's nodes
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

## Common Mistakes

- **Forgetting the None base case in DFS**: Every recursive DFS must handle `if node is None: return <base_value>`. Forgetting this causes an AttributeError on leaf children.
- **Wrong base value for the None case**: Returning `0` for max depth is right, but for min depth you'd want to return infinity so it doesn't contaminate the minimum. Think carefully about what "nothing" should contribute.
- **BFS without the level snapshot**: Doing `while queue: node = queue.popleft()` processes all nodes but loses level information. Always capture `level_size = len(queue)` before the inner loop.
- **Using a list as a BFS queue**: `list.pop(0)` is O(n). Use `collections.deque` and `popleft()` — O(1).
- **Confusing pre/in/post order**: Pre-order (root first) is natural for printing/serializing. Post-order (children first) is natural for computing heights/diameters. In-order (left, root, right) produces sorted output for BSTs. Know which one your problem needs before writing the traversal.

## Watch Me Solve (I do)

**Problem: Binary Tree Level Order Traversal (LC 102)**

Given the root of a binary tree, return the node values level by level (left to right), as a list of lists.

---

"Level by level" is the loudest BFS signal possible. I immediately reach for a queue.

My plan: start with just the root in the queue. Each iteration of the outer loop processes one full level. I take a snapshot of the queue size at the start of each level — that tells me how many nodes belong to the current level. I dequeue exactly that many, collect their values, and enqueue their children. After processing all those nodes, I have one complete level. Repeat until the queue is empty.

Let me trace through this tree:
```
        3
       / \
      9  20
        /  \
       15   7
```

- Queue starts: `[3]`
- Level 1: `level_size = 1`. Dequeue 3, collect `[3]`. Enqueue 9, 20. Queue: `[9, 20]`. Append `[3]`.
- Level 2: `level_size = 2`. Dequeue 9, collect `[9]`, no children. Dequeue 20, collect `[9, 20]`, enqueue 15, 7. Queue: `[15, 7]`. Append `[9, 20]`.
- Level 3: `level_size = 2`. Dequeue 15, collect `[15]`, no children. Dequeue 7, collect `[15, 7]`, no children. Queue: `[]`. Append `[15, 7]`.
- Queue is empty. Done.

Result: `[[3], [9, 20], [15, 7]]` ✓

```python
from collections import deque

def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []

    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)   # how many nodes are on this level RIGHT NOW
        level: list[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)   # children join the NEXT level
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

**Complexity:** O(n) time — every node enqueued and dequeued once. O(n) space — the queue holds at most one full level, which in a complete binary tree is n/2 nodes.

**Variants this template handles with tiny changes:**
- Right side view → after each level loop, take `level[-1]` instead of all values.
- Zigzag traversal → flip a boolean after each level; if True, reverse the level list before appending.
- Minimum depth → return a depth counter the moment you dequeue a node with no children.

---

**Short DFS example: Maximum Depth of Binary Tree (LC 104)**

I want the maximum depth — the longest path from root to any leaf. The recursive structure is perfect: the max depth of a tree is 1 (for the current node) plus the max depth of its deeper subtree.

```python
def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0                    # empty tree has depth 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)   # current node adds 1
```

For the tree above: `max_depth(3)` → `1 + max(max_depth(9), max_depth(20))` → `1 + max(1, 2)` → `3`. ✓

The key DFS habit: define the return value first ("the function returns the height of the subtree rooted at this node"), then write the base case, then combine. Never start with the combination before knowing what the subproblems return.
