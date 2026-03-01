"""
Problem: Search in Rotated Sorted Array (LC 33) | Day 13 | Medium
Topic: Searching and Sorting

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown
pivot index k. For example, [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2].

Given the rotated array nums and an integer target, return the index of target
if it is in nums, or -1 if it is not.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
  Input: nums = [4,5,6,7,0,1,2], target = 0
  Output: 4

Example 2:
  Input: nums = [4,5,6,7,0,1,2], target = 3
  Output: -1

Constraints:
  - 1 <= nums.length <= 5000
  - -10^4 <= nums[i] <= 10^4
  - All values of nums are unique
  - nums is an ascending array that is possibly rotated

Hint: In binary search, at least one half (left or right of mid) is always sorted.
      Determine which half is sorted, then check if target falls in that range.
Pattern: Modified Binary Search
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([1], 1) == 0
    assert search([3, 1], 1) == 1
    assert search([5, 1, 3], 3) == 2
    print("All tests passed!")
