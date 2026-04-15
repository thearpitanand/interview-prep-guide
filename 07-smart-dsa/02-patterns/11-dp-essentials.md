# DP Essentials

## Recognition Signals (how to spot this in <90s)
- Problem asks for a **count**, **maximum**, **minimum**, or **boolean feasibility** over an exponential search space
- Keywords: "number of ways", "minimum cost", "maximum profit", "can you reach", "longest subsequence/substring"
- Brute-force recursion has **overlapping subproblems** — you'd compute the same subproblem multiple times
- Optimal solution can be built from **optimal solutions to smaller subproblems** (optimal substructure)
- After you identify a subproblem, you can write a recurrence like `dp[i] = f(dp[i-1], dp[i-2], ...)` before writing a single line of code

## Mental Model
Dynamic programming is **recursion with memory** — nothing more. The only thing that distinguishes a DP problem from plain recursion is that the recursion tree has repeated nodes (overlapping subproblems), so you cache results to avoid recomputation. The implementation can be top-down (memoized recursion) or bottom-up (iterative table), but the underlying recurrence is identical.

The two-step ritual that unlocks every DP problem:

1. **Define the state**: What does `dp[i]` (or `dp[i][j]`) represent in plain English? Write this as a comment before coding. If you cannot state it in one sentence, your state is wrong.
2. **Write the transition**: Given that you know all smaller states, how do you compute the current one? This is the recurrence. Base cases are the states you can answer without looking at smaller states.

Once you have those two things, the code nearly writes itself. Engineers who struggle with DP usually jump straight to the table — they skip the state definition and the recurrence, so every problem feels new. Engineers who nail DP always start with the English definition and the recurrence on paper or out loud before touching a keyboard.

## Reusable Python Template

### 1. 1D DP (linear sequence)

```python
def dp_1d(n: int) -> int:
    """
    State: dp[i] = <answer for subproblem of size i>
    Transition: dp[i] = f(dp[i-1], dp[i-2], ...)
    Base: dp[0] = ..., dp[1] = ...
    """
    if n <= 1:
        return n  # base case — adjust per problem

    dp: list[int] = [0] * (n + 1)
    dp[0] = 1  # ← define base cases explicitly
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # ← your recurrence here

    return dp[n]

# Space-optimised version when only last k states matter:
def dp_1d_optimised(n: int) -> int:
    a, b = 1, 1  # dp[0], dp[1]
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### 2. 2D Grid DP

```python
def dp_grid(grid: list[list[int]]) -> int:
    """
    State: dp[r][c] = <answer to reach/use cell (r,c)>
    Transition: dp[r][c] = f(dp[r-1][c], dp[r][c-1])
    Base: first row and first column seeded directly.
    """
    rows, cols = len(grid), len(grid[0])
    dp: list[list[int]] = [[0] * cols for _ in range(rows)]

    # Seed base cases
    dp[0][0] = grid[0][0]  # or 1 for path-counting problems
    for c in range(1, cols):
        dp[0][c] = dp[0][c - 1] + grid[0][c]  # top row
    for r in range(1, rows):
        dp[r][0] = dp[r - 1][0] + grid[r][0]  # left column

    for r in range(1, rows):
        for c in range(1, cols):
            dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])  # min-path variant

    return dp[rows - 1][cols - 1]
```

### 3. 0/1 Knapsack

```python
def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    """
    State: dp[i][w] = max value using first i items with weight budget w.
    Transition:
      - Don't take item i: dp[i][w] = dp[i-1][w]
      - Take item i (if weights[i-1] <= w): dp[i][w] = dp[i-1][w - weights[i-1]] + values[i-1]
    Take the max of both options.
    """
    n = len(weights)
    dp: list[list[int]] = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]                # skip item i
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1],  # take item i
                )

    return dp[n][capacity]

# Unbounded knapsack (item can be reused — Coin Change, Combination Sum count):
# Change dp[i-1][w - weights[i-1]] → dp[i][w - weights[i-1]]
# This allows picking the same item again in the same row.
```

### 4. String DP — 2-pointer 2D table

```python
def dp_string_2d(s: str, t: str) -> int:
    """
    Canonical for: LCS, Edit Distance, Longest Common Substring.
    State: dp[i][j] = answer for s[:i] and t[:j]
    Transition: depends on whether s[i-1] == t[j-1].
    """
    m, n = len(s), len(t)
    # (m+1) x (n+1) to accommodate empty-string base cases
    dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases: dp[i][0] = 0, dp[0][j] = 0  (empty string LCS/LCSubstr is 0)
    # For Edit Distance: dp[i][0] = i, dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1       # LCS: extend match
                # Edit Distance: dp[i][j] = dp[i-1][j-1]  (no cost)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # LCS: skip one char
                # Edit Distance: dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]
```

### 5. Longest Increasing Subsequence (LIS) — O(n²) then O(n log n)

```python
def lis(nums: list[int]) -> int:
    """
    State: dp[i] = length of LIS ending at index i.
    Transition: dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i].
    Base: dp[i] = 1 (the element itself).
    """
    n = len(nums)
    if n == 0:
        return 0
    dp: list[int] = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# O(n log n) version using patience sort (binary search on tails):
import bisect

def lis_fast(nums: list[int]) -> int:
    tails: list[int] = []   # tails[i] = smallest tail of all IS of length i+1
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)   # extend longest IS
        else:
            tails[pos] = num    # replace to keep tails as small as possible
    return len(tails)
```

## Common Mistakes
- **Defining `dp[i]` vaguely**: "dp[i] is something about index i" is not a definition. It must be a precise English sentence. Wrong state → wrong recurrence → wrong answer every time.
- **Off-by-one in table size**: for string/sequence problems, `dp` needs length `n+1` so `dp[0]` represents the empty prefix. Forgetting the `+1` causes index errors or silent wrong answers.
- **Forgetting the base cases**: iterating from index 1 without seeding `dp[0]` (and `dp[1]` for Fibonacci-style) means you build on uninitialized zeros. Write base cases first, then the loop.
- **Using mutable default in memoization**: `@functools.lru_cache` on a function that takes a list crashes because lists are unhashable. Convert list args to tuples, or use a `dict` memo manually.
- **Returning `dp[n-1]` instead of `dp[n]`**: in 0-indexed tables seeded for n+1 slots (string DP), the answer is `dp[m][n]`, not `dp[m-1][n-1]`. Confirm table dimensions match your state definition before returning.

## Watch Me Solve (I do)

---

### Example 1: Climbing Stairs (LC 70)

You are climbing a staircase. It takes `n` steps to reach the top. Each time you can climb 1 or 2 steps. How many distinct ways can you climb to the top?

`n = 4` → 5 (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)

---

This is a counting problem over a finite state space. The hint is that at each step you have a binary choice, but doing a full enumeration is exponential. I ask myself: "does the answer for step `i` depend on answers for smaller steps?" Yes — to reach step `i`, I either came from step `i-1` (took a 1-step) or step `i-2` (took a 2-step). The number of ways to reach `i` is the sum of ways to reach those two predecessors. That is the Fibonacci recurrence in disguise.

**State definition**: `dp[i]` = number of distinct ways to reach step `i`.

**Transition**: `dp[i] = dp[i-1] + dp[i-2]`

**Base cases**: `dp[1] = 1` (one way: take step 1). `dp[2] = 2` (1+1 or 2).

```python
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    dp: list[int] = [0] * (n + 1)
    dp[1] = 1   # one way to reach step 1
    dp[2] = 2   # two ways to reach step 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]   # came from i-1 or i-2

    return dp[n]
```

Dry-run for n=4: `dp = [0, 1, 2, 3, 5]`. Return `dp[4] = 5`. Correct.

Because we only look back 2 steps, I can replace the array with two variables and save O(n) space:

```python
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2          # dp[1], dp[2]
    for _ in range(3, n + 1):
        a, b = b, a + b  # slide window forward
    return b
```

Time: O(n). Space: O(1).

---

### Example 2: Coin Change (LC 322) — Unbounded Knapsack Variant

You are given an integer array `coins` and an integer `amount`. Return the **fewest** number of coins needed to make up `amount`, or -1 if it is impossible.

`coins = [1, 5, 11]`, `amount = 15` → 3 (5+5+5, not 11+1+1+1+1 = 5)

---

This is a minimization problem: "fewest coins" screams DP. Brute force would try every combination — exponential. The overlapping subproblem insight: to solve `amount = 15`, I need the optimal solution for `15 - coin` for every coin. Those sub-amounts get recomputed many times in recursion.

This is **unbounded knapsack**: each coin can be reused any number of times.

**State definition**: `dp[a]` = minimum number of coins needed to make amount `a`.

**Transition**: for each coin `c`, `dp[a] = min(dp[a], dp[a - c] + 1)` when `a >= c`.

**Base cases**: `dp[0] = 0` (zero coins to make amount 0). All other `dp[a]` initialized to `float('inf')` (impossible until proven otherwise).

**Why `float('inf')` and not 0?** We are minimizing — initializing to 0 would make every answer look like 0 coins. We need a sentinel that loses to any real answer in `min()`.

```python
def coin_change(coins: list[int], amount: int) -> int:
    # dp[a] = min coins to make amount a
    dp: list[float] = [float("inf")] * (amount + 1)
    dp[0] = 0   # base case: 0 coins to make 0

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)
                # "use this coin once, add it to the optimal solution for a-coin"

    return int(dp[amount]) if dp[amount] != float("inf") else -1
```

Dry-run for `coins=[1,5,11]`, `amount=15`:
- `dp[0] = 0`
- `dp[1] = dp[0]+1 = 1` (coin 1)
- `dp[5] = dp[4]+1 = 5` (coin 1s) but then coin 5: `dp[0]+1 = 1` → `dp[5] = 1`
- `dp[10] = dp[5]+1 = 2` (two 5s)
- `dp[11] = dp[10]+1 = 3` or `dp[0]+1 = 1` → `dp[11] = 1`
- `dp[15] = dp[14]+1` ... or `dp[10]+1 = 3` (5+5+5) → `dp[15] = 3`

Return 3. Correct.

**Contrast with 0/1 Knapsack**: in 0/1 knapsack you iterate items in the outer loop and weights in the inner loop, and you use `dp[i-1]` to prevent reuse. Here we have no "items" axis — just amounts — and we allow reuse by looking at `dp[a - coin]` within the same sweep.

Time: O(amount × len(coins)). Space: O(amount).

---

**Summary: How to Attack Any DP Problem**

| Step | What to do |
|------|-----------|
| 1. State | Write `dp[i] = ...` in plain English before touching code |
| 2. Transition | "Given dp[i-1], dp[i-2], ..., how do I get dp[i]?" |
| 3. Base cases | Smallest inputs you can answer directly without looking further |
| 4. Direction | Bottom-up: fill smallest → largest. Top-down: recurse large → small + memo |
| 5. Return | Check: is the answer `dp[n]`, `max(dp)`, `dp[m][n]`? Match to your state definition |
| 6. Optimize | Can you replace the full table with a rolling window of last k rows/values? |

The patterns above cover ~90% of interview DP. When you see a new DP problem, first classify it: 1D sequence, 2D grid, knapsack, string, or LIS. Then pull the matching template and adapt the state definition and transition.
