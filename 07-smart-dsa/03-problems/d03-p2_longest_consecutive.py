"""
Problem: Longest Consecutive Sequence (LC 128) | Smart-DSA Day 3 | Medium
Pattern: Arrays & Hashing (Hash set)
Time target: 30 minutes

Given an unsorted array of integers nums, return the length of the longest
consecutive sequence. Must run in O(n) time.

Example 1:
  Input: nums = [100, 4, 200, 1, 3, 2]
  Output: 4  (sequence: 1, 2, 3, 4)

Example 2:
  Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
  Output: 9

Constraints:
  - 0 <= nums.length <= 10^5
  - -10^9 <= nums[i] <= 10^9

Hint (⚠ read only after time budget is blown):
  Put all numbers in a set. For each number, only start counting if num-1 is
  NOT in the set (it's the start of a sequence). Then expand forward.
"""


def longest_consecutive(nums: list[int]) -> int:
    pass


if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    assert longest_consecutive([1]) == 1
    print("All tests passed!")
