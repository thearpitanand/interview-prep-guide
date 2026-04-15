# Binary Search

## Recognition Signals (how to spot this in <90s)
- Array is **sorted** (or implicitly sorted) and you're looking for a value, boundary, or optimal answer — the first thing to ask after reading constraints
- Problem says "find the minimum/maximum X such that condition Y holds" — that's binary search on the *answer*, not the array
- Search space is large (e.g. answer could be 1 to 10^9) but you can **evaluate a condition in O(n)** — binary search on the range
- Problem involves a rotated or partially sorted array where direct lookup is hard but halving still applies
- Linear scan would be O(n) but constraints demand O(log n), or O(n log n) is clearly the target complexity

## Mental Model

Binary search works on any **monotone predicate**: a function `f(x)` that is False for all x below some threshold and True for all x above (or vice versa). You're looking for the exact threshold. Each iteration you pick the midpoint, evaluate `f(mid)`, and discard the half that can't contain the threshold. The key insight is that you're not just searching for a value in an array — you're bisecting any monotone space, including answer spaces like "how many bananas per hour?" or "what's the minimum speed?".

The most common bug in binary search is the loop boundary and mid-calculation. Use the invariant: **the answer always lies in `[left, right]`**. At termination (`left == right`), both pointers point at the answer. Choose `mid = left + (right - left) // 2` (avoids overflow in other languages; in Python it doesn't matter but it's habit). For "find minimum satisfying condition" problems, when `f(mid)` is True, you try to do better by moving right *down* (`right = mid`); when False, you eliminate mid and move left up (`left = mid + 1`). This pattern — `right = mid` on True, `left = mid + 1` on False — is the "left-finding" template and covers ~80% of BS-on-answer problems.

## Reusable Python Template

```python
# --- Classic binary search on a sorted array ---
def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1                               # not found


# --- Binary search on answer (find minimum valid value) ---
def bs_on_answer(data: list[int], limit: int) -> int:
    def feasible(candidate: int) -> bool:
        # O(n) check: "can we achieve the goal with candidate?"
        # return True if candidate satisfies the constraint
        ...

    left = 1                                # smallest possible answer
    right = max(data)                       # or some upper bound

    while left < right:                    # note: < not <=
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid                    # mid works; try smaller
        else:
            left = mid + 1                 # mid too small; eliminate

    return left                            # left == right == answer


# --- Find first True in a boolean array [F, F, F, T, T, T] ---
def first_true(nums: list[int], condition) -> int:
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if condition(nums[mid]):
            result = mid                   # record candidate; try left half
            right = mid - 1
        else:
            left = mid + 1
    return result
```

## Common Mistakes

- **`while left <= right` vs. `while left < right`**: for classic search use `<=` (searches the full closed interval, returns -1 if not found). For BS-on-answer use `<` (terminates when `left == right`, which is the answer). Mixing these is the #1 bug.
- **`mid = (left + right) // 2` causing integer overflow**: not an issue in Python (arbitrary ints), but write `left + (right - left) // 2` anyway — it builds good cross-language habits and interviewers notice.
- **Setting `right = mid - 1` instead of `right = mid` in BS-on-answer**: when `feasible(mid)` is True, `mid` itself is a valid answer — you must keep it in the search space by doing `right = mid`, not `right = mid - 1`.
- **Forgetting to define tight bounds**: if your `left` or `right` starts outside the valid answer range, you might skip the answer or loop infinitely. For Koko-style problems: `left = 1` (minimum meaningful speed), `right = max(piles)` (eating everything in one hour per pile is always valid).
- **Writing `feasible` with the wrong direction**: make sure `feasible` returns True for values that are *at or above* the threshold you're seeking. If True/False are flipped, your pointers converge on the wrong end.

## Watch Me Solve (I do)

**Problem: Koko Eating Bananas (LC 875)**

Koko can eat `k` bananas per hour. There are `n` piles of bananas; guards return in `h` hours. Find the minimum integer `k` such that Koko can eat all bananas within `h` hours.

---

I read this and my brain flags two things: (1) I'm looking for a *minimum k*, and (2) there's a clear check — given a candidate `k`, can I compute the total hours needed in O(n)? That's the BS-on-answer pattern: search over candidate answers, evaluate feasibility in O(n), binary search over the candidates.

Why is this monotone? If Koko can finish in time at speed `k`, she can definitely finish at speed `k+1`. The predicate `can_finish(k)` is False for small `k` and True for large `k` — a clean monotone step from False to True. I want the leftmost True.

Bounds:
- `left = 1` — she must eat at least 1 banana per hour.
- `right = max(piles)` — eating the largest pile in one hour is always sufficient (she finishes in exactly `n` hours ≤ h since n ≤ h is guaranteed by the constraints). No need for `right = max(piles) * h` — that's wasteful.

Feasibility check: for each pile `p`, Koko takes `ceil(p / k)` hours = `(p + k - 1) // k` in integer arithmetic. Sum these; if ≤ h, it's feasible.

```python
import math

def min_eating_speed(piles: list[int], h: int) -> int:
    def can_finish(k: int) -> bool:
        total_hours = sum(math.ceil(p / k) for p in piles)
        return total_hours <= h

    left, right = 1, max(piles)

    while left < right:                     # terminates when left == right == answer
        mid = left + (right - left) // 2
        if can_finish(mid):
            right = mid                     # mid is valid; try to go lower
        else:
            left = mid + 1                  # mid too slow; eliminate it

    return left
```

**Complexity:** O(n log m) where m = max(piles). The binary search runs log(m) iterations (~30 for m ≤ 10^9), each with an O(n) feasibility check.

**Why `right = mid` not `right = mid - 1`?** Because `can_finish(mid)` is True — `mid` itself is a valid answer and I must not exclude it. I keep it in the search space and try to find something smaller. If I wrote `right = mid - 1`, I'd overshoot and miss the answer.

**Edge cases I'd raise:**
1. `h == len(piles)`: Koko has exactly one hour per pile. Answer is `max(piles)` — she must clear each pile in one sitting. The algorithm gives this: `right = max(piles)` and only that value is feasible when h equals n.
2. Single pile: works fine, search space is `[1, piles[0]]`.
3. `piles` has 1 element with a huge value (10^9): `right = 10^9`, loop runs ~30 iterations. No issue.

**The senior signal in this problem:** recognizing that you're not searching *in* the array — you're searching over an implicit answer space. Once you identify that, the template is identical to any other BS-on-answer problem. State this insight explicitly before coding; interviewers are listening for it.
