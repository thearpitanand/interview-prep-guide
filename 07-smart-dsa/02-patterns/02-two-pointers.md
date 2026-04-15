# Two Pointers

## Recognition Signals (how to spot this in <90s)
- Array or string is **sorted** (or can be sorted without losing needed information) and you're searching for a pair or triplet
- Problem asks for pairs/triplets summing to a target — classic two-pointer territory after sorting
- You need to find the longest/shortest valid subsequence by expanding from both ends (palindrome check, container with water)
- Brute force is O(n^2) or O(n^3) and the problem has n ≤ 10^4 or larger — two pointers collapses it to O(n) or O(n^2)
- Problem involves "in-place" modification of an array (remove duplicates, partition) — two pointers write one and read the other

## Mental Model

Two pointers work because a sorted order gives you a monotone relationship: moving the left pointer right increases the sum; moving the right pointer left decreases it. This lets you binary-search in linear time — not by halving the search space each step, but by eliminating one possibility per step. The invariant is: at every step, the optimal answer (if it exists) lies within the window `[left, right]`. You never need to go back, so each pointer visits at most n positions: O(n) total moves.

For three-pointer problems like 3Sum, you fix one element in an outer loop and run the classic two-pointer scan on the remaining subarray. The fix-one idea appears whenever you need to reduce an (n-dimensional constraint) by one dimension. The crucial detail is **duplicate skipping**: after processing a value, advance past all identical elements before moving on, or you'll report the same triplet multiple times. This is the most common bug in interviews and it almost always trips people up mid-implementation — pre-plan it.

## Reusable Python Template

```python
def two_pointers_template(nums: list[int]) -> list[list[int]]:
    nums.sort()                          # almost always required
    result: list[list[int]] = []

    for i in range(len(nums) - 2):      # outer loop fixes the first element
        # skip duplicates for the fixed element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == target:
                result.append([nums[i], nums[left], nums[right]])
                # skip duplicates for both inner pointers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

            elif total < target:
                left += 1               # need a larger sum
            else:
                right -= 1              # need a smaller sum

    return result


# Simpler two-pointer (pair sum, no duplicates concern):
def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []
```

## Common Mistakes

- **Forgetting to sort first**: two pointers rely on monotonicity. If the array isn't sorted, the "move left to increase, move right to decrease" logic doesn't hold. Always confirm sort is legal (watch for problems that forbid sorting or need original indices).
- **Missing duplicate skipping in 3Sum**: you'll pass most test cases but fail on inputs like `[-2, 0, 0, 2, 2]`. The fix is two separate skip loops — one for the outer `i`, one each for `left` and `right` after appending a result.
- **Infinite loop when left == right boundary**: the `while left < right` guard prevents reading past each other, but inside the duplicate-skip loops you need the same guard: `while left < right and ...`.
- **Using two pointers on unsorted + needing original indices**: sorting destroys index information. If the problem requires returning original indices (like Two Sum), use a hash map instead.
- **Off-by-one in outer loop bound**: for 3Sum the outer loop runs to `len(nums) - 2` (need at least 2 elements left for the inner pointers). A loop to `len(nums)` wastes iterations and can cause index errors inside.

## Watch Me Solve (I do)

**Problem: 3Sum (LC 15)**

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j != k` and `nums[i] + nums[j] + nums[k] == 0`.

---

My first read: "all unique triplets that sum to zero." The word *unique* is the tell — there will be duplicates in the input and I need to deduplicate the output without using a set of tuples (which works but is messy). Two pointers on a sorted array handle deduplication naturally because I can skip adjacent equal values.

Brute force would be three nested loops — O(n^3). That's immediately off the table for any n > a few hundred. The classic improvement: fix one element, reduce to a two-sum on the remaining subarray. Since two-sum on a sorted array is O(n) via two pointers, total complexity is O(n^2). With sorting that's O(n^2) overall — acceptable.

Design decisions before I write a line:
1. **Sort the array.** Two pointers need monotonicity.
2. **Outer loop fixes `nums[i]`, inner two pointers span `[i+1, n-1]`.**
3. **Early termination:** if `nums[i] > 0`, the array is sorted so the remaining sum can't be zero — break.
4. **Duplicate skipping at three levels:** outer `i`, inner `left`, inner `right`.

```python
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result: list[list[int]] = []

    for i in range(len(nums) - 2):
        if nums[i] > 0:              # all remaining elements are positive — impossible
            break
        if i > 0 and nums[i] == nums[i - 1]:  # skip duplicate fixed element
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # advance past duplicates before next iteration
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

            elif total < 0:
                left += 1            # need a larger value
            else:
                right -= 1           # need a smaller value

    return result
```

**Complexity:** O(n log n) for sorting + O(n^2) for the nested scan = **O(n^2)** time. O(1) extra space (excluding output).

**Edge cases I'd call out:**
1. `nums = [0, 0, 0]` — only one triplet `[0,0,0]`. The duplicate-skip loops prevent reporting it twice.
2. All positives or all negatives — the `nums[i] > 0` early break handles the former; the two-pointer scan naturally produces nothing for the latter.
3. Fewer than 3 elements — the outer loop range collapses to empty, returns `[]` safely.

**The one thing people botch in interviews:** the duplicate-skip after appending. They forget the inner `while` guards or write only one skip instead of both. I always write all three skip blocks together immediately after the `result.append(...)` line, before I think about anything else.
