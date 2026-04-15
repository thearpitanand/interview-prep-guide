# Backtracking

## Recognition Signals (how to spot this in <90s)
- Problem asks for **all** combinations, subsets, permutations, or arrangements — not just a count or optimum
- The phrase "generate all", "find all possible", "list every" appears in the problem
- Solution space is tree-shaped: at each step you make a choice, explore, then undo it
- Constraints are small (n ≤ 20 is the giveaway — exponential blowup is acceptable)
- Problem involves placing items with constraints and backtracking when a placement becomes invalid (e.g., N-Queens, Sudoku)

## Mental Model
Backtracking is a depth-first search through a **decision tree**. At each node you pick a choice, recurse into the subtree it creates, then **undo** the choice before trying the next option. The undo step (backtrack) is what distinguishes this from plain recursion. Think of it as exploring every branch of a tree with a piece of tape: you walk down, mark what you did, reach a leaf or dead end, peel the tape off, and try the sibling branch.

The key insight is that every backtracking solution has the same skeleton: a `result` list you add to at leaf nodes, a `current` state you build up, a loop over choices at each level, and a symmetric add/remove around the recursive call. Once you internalize the skeleton, you are not memorizing N different algorithms — you are writing the same 10-line frame with different "when to add to result" and "what counts as a valid choice" conditions.

## Reusable Python Template

```python
def backtrack_template(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []

    def backtrack(start: int, current: list[int]) -> None:
        # --- Base case / result collection ---
        # For subsets: always append (every prefix is valid)
        # For permutations: append when len(current) == len(nums)
        # For combination sum: append when remaining == 0
        result.append(current[:])  # snapshot, not reference

        for i in range(start, len(nums)):
            # --- Pruning (skip invalid choices early) ---
            # e.g., if nums[i] > remaining: break  (when sorted)

            current.append(nums[i])           # choose
            backtrack(i + 1, current)         # explore  ← i+1 means no reuse
            # backtrack(i, current)            # ← i means allow reuse (Combination Sum)
            current.pop()                     # un-choose

    backtrack(0, [])
    return result
```

## Common Mistakes
- **Appending the reference instead of a copy**: `result.append(current)` captures the live list; always use `result.append(current[:])` or `list(current)`.
- **Off-by-one in the `start` index**: passing `i` vs `i+1` controls whether an element can be reused. Subsets/combinations need `i+1`; Combination Sum with repetition needs `i`.
- **Forgetting the `pop()`**: the backtrack step is the most commonly dropped line. If your output has incorrect extra elements, check that every `append` has a matching `pop`.
- **No pruning on sorted input**: for problems like Combination Sum or Subsets II, sorting first lets you `break` early when `nums[i] > remaining`, which turns TLE into AC.
- **Duplicate results when input has duplicates**: after sorting, add `if i > start and nums[i] == nums[i-1]: continue` inside the loop to skip duplicate branches.

## Watch Me Solve (I do)

**Problem: Subsets (LC 78)**
Given an integer array `nums` of unique elements, return all possible subsets (the power set).
`nums = [1, 2, 3]` → `[[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]`

---

I read this and immediately see "all possible subsets" — that's the clearest backtracking signal there is. The solution space is a binary decision tree: for each element, I either include it or skip it. I'll use the template where I collect the current path at every node, not just at leaves.

I also note `nums` has unique elements and the output can be in any order. No deduplication needed. Good — simpler.

Here's my plan before writing a single line:
1. `result` starts empty.
2. `current` is the running subset I'm building.
3. I loop from `start` to end; for each index I add `nums[i]`, recurse with `i+1`, then pop.
4. At the top of each call I snapshot `current` into `result` — that captures all prefix subsets including the empty one.

```python
def subsets(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []

    def backtrack(start: int, current: list[int]) -> None:
        result.append(current[:])   # every call is a valid subset

        for i in range(start, len(nums)):
            current.append(nums[i])     # choose nums[i]
            backtrack(i + 1, current)   # recurse: only elements after i
            current.pop()               # un-choose: restore state

    backtrack(0, [])
    return result
```

Dry-run on `[1, 2, 3]`:
- `backtrack(0, [])` → append `[]`
  - pick 1 → `backtrack(1, [1])` → append `[1]`
    - pick 2 → `backtrack(2, [1,2])` → append `[1,2]`
      - pick 3 → `backtrack(3, [1,2,3])` → append `[1,2,3]`, loop exhausted, return
      - pop 3
    - pop 2
    - pick 3 → `backtrack(3, [1,3])` → append `[1,3]`, return
    - pop 3
  - pop 1
  - pick 2 → ... and so on

Time: O(n · 2ⁿ) — 2ⁿ subsets, each costs O(n) to copy. Space: same.

---

**Sketch: how the same template adapts**

**Permutations (LC 46):** Instead of a `start` index, I track a `used` boolean array. The loop goes from 0 to n every time; I skip `used[i]`. I collect at the leaf (`len(current) == n`), not at every node.

```python
def backtrack(current: list[int]) -> None:
    if len(current) == len(nums):
        result.append(current[:])
        return
    for i in range(len(nums)):
        if used[i]: continue
        used[i] = True
        current.append(nums[i])
        backtrack(current)
        current.pop()
        used[i] = False
```

**Combination Sum (LC 39):** Candidates can be reused, so I pass `i` (not `i+1`) on the recursive call. I collect when `remaining == 0`, and prune when `remaining < 0`. Sorting first lets me `break` instead of `continue` once the candidate exceeds remaining.

```python
def backtrack(start: int, current: list[int], remaining: int) -> None:
    if remaining == 0:
        result.append(current[:])
        return
    for i in range(start, len(candidates)):
        if candidates[i] > remaining:
            break   # sorted — no point continuing
        current.append(candidates[i])
        backtrack(i, current, remaining - candidates[i])  # i, not i+1
        current.pop()
```

The frame is identical in all three cases. The only differences are: where you collect, what the loop looks like, and how you manage state.
