"""
Problem: Find Minimum in Rotated Sorted Array (LC 153) | Smart-DSA Day 12 | Medium
Pattern: Binary Search
Time target: 25 minutes

Suppose an array of length n sorted in ascending order is rotated between 1 and
n times. Given the rotated array nums, return the minimum element.
Must run in O(log n) time.

Example 1:
  Input: nums = [3, 4, 5, 1, 2]
  Output: 1

Example 2:
  Input: nums = [4, 5, 6, 7, 0, 1, 2]
  Output: 0

Example 3:
  Input: nums = [11, 13, 15, 17]
  Output: 11  (not rotated)

Constraints:
  - n == nums.length
  - 1 <= n <= 5000
  - -5000 <= nums[i] <= 5000
  - All values are unique.

Hint (⚠ read only after time budget is blown):
  If nums[mid] > nums[hi], the minimum is in the right half (rotate happened
  there). Otherwise it's in the left half (including mid). Converge lo and hi.
"""


def find_min(nums: list[int]) -> int:
    pass


if __name__ == "__main__":
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([11, 13, 15, 17]) == 11
    assert find_min([2, 1]) == 1
    print("All tests passed!")
