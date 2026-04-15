"""
Problem: 3Sum (LC 15) | Smart-DSA Day 5 | Medium
Pattern: Two Pointers
Time target: 30 minutes

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j != k and nums[i] + nums[j] + nums[k] == 0.
The solution set must not contain duplicate triplets.

Example 1:
  Input: nums = [-1, 0, 1, 2, -1, -4]
  Output: [[-1, -1, 2], [-1, 0, 1]]

Example 2:
  Input: nums = [0, 0, 0]
  Output: [[0, 0, 0]]

Constraints:
  - 3 <= nums.length <= 3000
  - -10^5 <= nums[i] <= 10^5

Hint (⚠ read only after time budget is blown):
  Sort the array. Fix nums[i], then use two pointers for the remaining sum
  (-nums[i]). Skip duplicate values of i, left, and right to avoid duplicate
  triplets.
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    pass


if __name__ == "__main__":
    assert sorted(three_sum([-1, 0, 1, 2, -1, -4])) == sorted([[-1, -1, 2], [-1, 0, 1]])
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([1, 2, 3]) == []
    print("All tests passed!")
