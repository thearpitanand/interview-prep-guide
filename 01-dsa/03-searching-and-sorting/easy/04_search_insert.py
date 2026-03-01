"""
Problem: Search Insert Position (LC 35) | Day 12 | Easy
Topic: Searching and Sorting

Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be inserted
in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
  Input: nums = [1,3,5,6], target = 5
  Output: 2

Example 2:
  Input: nums = [1,3,5,6], target = 2
  Output: 1

Example 3:
  Input: nums = [1,3,5,6], target = 7
  Output: 4

Constraints:
  - 1 <= nums.length <= 10^4
  - -10^4 <= nums[i] <= 10^4
  - nums contains distinct values sorted in ascending order
  - -10^4 <= target <= 10^4

Hint: This is equivalent to finding the leftmost index where nums[index] >= target.
      After binary search, left pointer will be at the insert position.
Pattern: Binary Search (Boundary Finding)
"""

from typing import List


def search_insert(nums: List[int], target: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4
    assert search_insert([1, 3, 5, 6], 0) == 0
    assert search_insert([1], 0) == 0
    print("All tests passed!")
