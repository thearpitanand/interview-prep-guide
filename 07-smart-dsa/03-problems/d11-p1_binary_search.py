"""
Problem: Binary Search (LC 704) | Smart-DSA Day 11 | Easy
Pattern: Binary Search
Time target: 15 minutes

Given an array of integers nums sorted in ascending order and an integer target,
return the index of target if found, or -1 if not found.
Must run in O(log n) time.

Example 1:
  Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
  Output: 4

Example 2:
  Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
  Output: -1

Constraints:
  - 1 <= nums.length <= 10^4
  - -10^4 <= nums[i], target <= 10^4
  - All values in nums are unique.
  - nums is sorted in ascending order.

Hint (⚠ read only after time budget is blown):
  Maintain lo and hi pointers. Compute mid = (lo + hi) // 2. If nums[mid] ==
  target return mid; if nums[mid] < target move lo up; else move hi down.
"""


def binary_search(nums: list[int], target: int) -> int:
    pass


if __name__ == "__main__":
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([5], 3) == -1
    print("All tests passed!")
