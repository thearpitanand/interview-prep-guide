"""
Problem: Binary Search (LC 704) | Day 12 | Easy
Topic: Searching and Sorting

Given a sorted array of integers nums and a target value, return the index
of target if found, otherwise return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
  Input: nums = [-1,0,3,5,9,12], target = 9
  Output: 4

Example 2:
  Input: nums = [-1,0,3,5,9,12], target = 2
  Output: -1

Constraints:
  - 1 <= nums.length <= 10^4
  - -10^4 < nums[i], target < 10^4
  - All integers in nums are unique
  - nums is sorted in ascending order

Hint: Use two pointers (left, right) and check the middle element each iteration.
Pattern: Standard Binary Search
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([5], 5) == 0
    assert search([2, 5], 5) == 1
    assert search([1], -1) == -1
    print("All tests passed!")
