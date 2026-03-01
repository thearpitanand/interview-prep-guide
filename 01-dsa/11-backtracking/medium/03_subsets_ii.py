"""
Subsets II (LC 90)

Day: 31 | Difficulty: Medium | Pattern: Backtracking + Dedup

Given an integer array nums that may contain duplicates, return all possible
subsets (the power set). The solution set must not contain duplicate subsets.
Return the solution in any order.

Examples:
    Input: nums = [1, 2, 2]
    Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

    Input: nums = [0]
    Output: [[], [0]]

    Input: nums = [4, 4, 4, 1, 4]
    Output: [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4],
             [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]

Constraints:
    - 1 <= nums.length <= 10
    - -10 <= nums[i] <= 10

Hint:
    Sort the array first so duplicates are adjacent. When iterating choices at
    the same recursion level, skip an element if it's the same as the previous
    one (i > start and nums[i] == nums[i-1]). This prevents generating duplicate
    subsets while still allowing the same value to appear multiple times in
    different positions of a subset.

Pattern: Backtracking with sort + skip duplicates at same level. The condition
`i > start` (not `i > 0`) ensures we only skip at the same recursion level.
"""

from typing import List


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    """Generate all unique subsets, handling duplicates."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Array with duplicates
    result = sorted(subsets_with_dup([1, 2, 2]))
    expected = sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 2: Single element
    result = sorted(subsets_with_dup([0]))
    expected = sorted([[], [0]])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 3: No duplicates (should behave like regular subsets)
    result = sorted(subsets_with_dup([1, 2, 3]))
    expected = sorted([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 4: All same elements
    result = sorted(subsets_with_dup([2, 2, 2]))
    expected = sorted([[], [2], [2, 2], [2, 2, 2]])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 5: Verify no duplicates in result
    result = subsets_with_dup([1, 2, 2, 3])
    tuples = [tuple(s) for s in result]
    assert len(tuples) == len(set(tuples)), "Found duplicate subsets in result"

    # Test 6: Correct count
    result = subsets_with_dup([4, 4, 4, 1, 4])
    assert len(result) == 10, f"Expected 10 subsets, got {len(result)}"

    print("All tests passed!")
