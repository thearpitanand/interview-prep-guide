"""
Count of Smaller Numbers After Self (LC 315)

Day: 27 | Difficulty: Hard | Pattern: BST / Binary Indexed Tree (BIT)

Given an integer array nums, return an integer array counts where counts[i]
is the number of smaller elements to the right of nums[i].

Examples:
    Input: nums = [5,2,6,1]
    Output: [2,1,1,0]
    Explanation:
        For 5: elements to right that are smaller = [2,1] -> count = 2
        For 2: elements to right that are smaller = [1]   -> count = 1
        For 6: elements to right that are smaller = [1]   -> count = 1
        For 1: no elements to right                       -> count = 0

    Input: nums = [-1]
    Output: [0]

    Input: nums = [-1,-1]
    Output: [0,0]

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4

Hint:
    Multiple approaches exist:
    1. BST approach: Insert elements from right to left. For each insertion,
       count how many existing nodes are smaller.
    2. Merge sort approach: During merge sort, count inversions.
    3. BIT/Fenwick tree: Coordinate compress values, use BIT to count.

    The BST approach is most intuitive but can be O(n^2) worst case.
    Merge sort gives guaranteed O(n log n).

Pattern: Process from right to left. Use an augmented BST (tracking left
subtree size) or merge sort with inversion counting.
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_smaller(nums: List[int]) -> List[int]:
    """Return array where each element is count of smaller numbers to its right."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Standard case
    result = count_smaller([5, 2, 6, 1])
    assert result == [2, 1, 1, 0], f"Expected [2,1,1,0], got {result}"

    # Test 2: Single element
    result = count_smaller([-1])
    assert result == [0], f"Expected [0], got {result}"

    # Test 3: Equal elements
    result = count_smaller([-1, -1])
    assert result == [0, 0], f"Expected [0,0], got {result}"

    # Test 4: Already sorted (ascending)
    result = count_smaller([1, 2, 3, 4])
    assert result == [0, 0, 0, 0], f"Expected [0,0,0,0], got {result}"

    # Test 5: Reverse sorted (descending)
    result = count_smaller([4, 3, 2, 1])
    assert result == [3, 2, 1, 0], f"Expected [3,2,1,0], got {result}"

    # Test 6: Mixed with duplicates
    result = count_smaller([2, 0, 1])
    assert result == [2, 0, 0], f"Expected [2,0,0], got {result}"

    # Test 7: Larger example
    result = count_smaller([26, 78, 27, 100, 33, 67, 90, 23, 66, 5, 38, 7, 35, 23, 52, 22, 83, 51, 98, 69, 81, 32, 21, 28, 13, 1, 39, 56, 20, 51])
    assert len(result) == 30, f"Expected 30 elements, got {len(result)}"

    print("All tests passed!")
