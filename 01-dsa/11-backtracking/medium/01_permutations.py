"""
Permutations (LC 46)

Day: 31 | Difficulty: Medium | Pattern: Backtracking - Permutations

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Examples:
    Input: nums = [1, 2, 3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    Input: nums = [0, 1]
    Output: [[0, 1], [1, 0]]

    Input: nums = [1]
    Output: [[1]]

Constraints:
    - 1 <= nums.length <= 6
    - -10 <= nums[i] <= 10
    - All the integers of nums are unique

Hint:
    Use a "used" boolean array to track which elements are already in the current
    permutation. At each step, try adding each unused element, recurse, then
    remove it (backtrack). The base case is when the path length equals nums length.

Pattern: Backtracking with used array - for each position, try every unused element.
No start index needed because order matters in permutations.
"""

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """Generate all permutations using backtracking with a used array."""
    pass


def permute_swap(nums: List[int]) -> List[List[int]]:
    """Generate permutations using the swap-based approach (in-place)."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Three elements
    result = sorted(permute([1, 2, 3]))
    expected = sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 2: Two elements
    result = sorted(permute([0, 1]))
    expected = sorted([[0, 1], [1, 0]])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 3: Single element
    result = permute([1])
    assert result == [[1]], f"Expected [[1]], got {result}"

    # Test 4: Correct count (n! permutations)
    result = permute([1, 2, 3, 4])
    assert len(result) == 24, f"Expected 24 permutations, got {len(result)}"

    # Test 5: Swap-based approach
    result = sorted(permute_swap([1, 2, 3]))
    expected = sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 6: No duplicates in result
    result = permute([1, 2, 3])
    assert len(result) == len(set(tuple(p) for p in result)), "Found duplicates in result"

    print("All tests passed!")
