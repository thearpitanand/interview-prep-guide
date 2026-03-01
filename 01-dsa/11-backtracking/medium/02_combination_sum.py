"""
Combination Sum (LC 39)

Day: 31 | Difficulty: Medium | Pattern: Backtracking - Combinations

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers
sum to target. The same number may be chosen from candidates an unlimited
number of times. Two combinations are unique if the frequency of at least one
of the chosen numbers is different.

Examples:
    Input: candidates = [2, 3, 6, 7], target = 7
    Output: [[2, 2, 3], [7]]
    Explanation: 2 + 2 + 3 = 7, 7 = 7

    Input: candidates = [2, 3, 5], target = 8
    Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    Input: candidates = [2], target = 1
    Output: []

Constraints:
    - 1 <= candidates.length <= 30
    - 2 <= candidates[i] <= 40
    - All elements of candidates are distinct
    - 1 <= target <= 40

Hint:
    Sort candidates first for efficient pruning. Use a start index to avoid
    duplicate combinations (e.g., [2,3] and [3,2]). Since elements can be
    reused, recurse with the same index i (not i+1). Break early when the
    current candidate exceeds the remaining target.

Pattern: Backtracking with start index + reuse. Key difference from regular
combinations: recurse with i (same element reusable) instead of i+1.
"""

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """Find all combinations that sum to target (elements reusable)."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Multiple solutions
    result = [sorted(c) for c in combination_sum([2, 3, 6, 7], 7)]
    result.sort()
    expected = [[2, 2, 3], [7]]
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 2: Three solutions
    result = [sorted(c) for c in combination_sum([2, 3, 5], 8)]
    result.sort()
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 3: No solution
    result = combination_sum([2], 1)
    assert result == [], f"Expected [], got {result}"

    # Test 4: Single candidate equals target
    result = combination_sum([3], 9)
    assert result == [[3, 3, 3]], f"Expected [[3, 3, 3]], got {result}"

    # Test 5: Larger example
    result = [sorted(c) for c in combination_sum([2, 3, 5], 5)]
    result.sort()
    expected = [[2, 3], [5]]
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 6: Target is one candidate
    result = combination_sum([1, 2], 2)
    result = [sorted(c) for c in result]
    result.sort()
    expected = [[1, 1], [2]]
    assert result == expected, f"Expected {expected}, got {result}"

    print("All tests passed!")
