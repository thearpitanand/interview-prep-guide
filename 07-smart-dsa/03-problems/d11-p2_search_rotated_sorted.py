"""
Problem: Search in Rotated Sorted Array (LC 33) | Smart-DSA Day 11 | Medium
Pattern: Binary Search
Time target: 25 minutes

An integer array nums sorted in ascending order is rotated at an unknown pivot.
Given the rotated array and an integer target, return its index or -1 if absent.
Must run in O(log n) time.

Example 1:
  Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
  Output: 4

Example 2:
  Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
  Output: -1

Example 3:
  Input: nums = [1], target = 0
  Output: -1

Constraints:
  - 1 <= nums.length <= 5000
  - -10^4 <= nums[i], target <= 10^4
  - All values are unique.

Hint (⚠ read only after time budget is blown):
  At each mid, determine which half is sorted (compare nums[lo] <= nums[mid]).
  Check if target falls within the sorted half; if yes, search there, else
  search the other half.
"""


def search_rotated(nums: list[int], target: int) -> int:
    pass


if __name__ == "__main__":
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search_rotated([1], 0) == -1
    assert search_rotated([3, 1], 1) == 1
    print("All tests passed!")
