"""
Problem: Find First and Last Position of Element in Sorted Array (LC 34) | Day 13 | Medium
Topic: Searching and Sorting

Given an array of integers nums sorted in non-decreasing order, find the
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
  Input: nums = [5,7,7,8,8,10], target = 8
  Output: [3,4]

Example 2:
  Input: nums = [5,7,7,8,8,10], target = 6
  Output: [-1,-1]

Example 3:
  Input: nums = [], target = 0
  Output: [-1,-1]

Constraints:
  - 0 <= nums.length <= 10^5
  - -10^9 <= nums[i] <= 10^9
  - nums is a non-decreasing array
  - -10^9 <= target <= 10^9

Hint: Run two binary searches: one to find the leftmost occurrence (keep going
      left when arr[mid] == target), one for rightmost (keep going right).
Pattern: Binary Search (Boundary Finding)
"""

from typing import List


def search_range(nums: List[int], target: int) -> List[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert search_range([], 0) == [-1, -1]
    assert search_range([1], 1) == [0, 0]
    assert search_range([2, 2], 2) == [0, 1]
    assert search_range([1, 2, 3, 3, 3, 3, 4, 5], 3) == [2, 5]
    print("All tests passed!")
