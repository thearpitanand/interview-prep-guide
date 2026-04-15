"""
Problem: Two Sum (LC 1) | Smart-DSA Day 1 | Easy
Pattern: Arrays & Hashing
Time target: 15 minutes

Given an array of integers nums and an integer target, return the indices of
the two numbers that add up to target. Exactly one solution exists.
You may not use the same element twice. Return indices in any order.

Example 1:
  Input: nums = [2, 7, 11, 15], target = 9
  Output: [0, 1]

Example 2:
  Input: nums = [3, 2, 4], target = 6
  Output: [1, 2]

Constraints:
  - 2 <= nums.length <= 10^4
  - -10^9 <= nums[i] <= 10^9
  - Exactly one valid answer exists.

Hint (⚠ read only after time budget is blown):
  Store each number's index in a hash map. For each element, check if
  (target - element) is already in the map.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    pass


if __name__ == "__main__":
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]
    assert sorted(two_sum([3, 3], 6)) == [0, 1]
    print("All tests passed!")
