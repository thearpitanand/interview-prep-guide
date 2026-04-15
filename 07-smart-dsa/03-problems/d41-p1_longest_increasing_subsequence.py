"""
Problem: Longest Increasing Subsequence (LC 300) | Smart-DSA Day 41 | Medium
Pattern: Dynamic Programming (LIS)
Time target: 30 minutes

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

Example 1:
  Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
  Output: 4
  Explanation: [2, 3, 7, 101]

Example 2:
  Input: nums = [0, 1, 0, 3, 2, 3]
  Output: 4

Example 3:
  Input: nums = [7, 7, 7, 7, 7]
  Output: 1

Constraints:
  - 1 <= nums.length <= 2500
  - -10^4 <= nums[i] <= 10^4

Hint (⚠ read only after time budget is blown):
  O(n²) DP: dp[i] = max(dp[j] + 1 for j < i if nums[j] < nums[i]), base 1.
  Answer is max(dp). Bonus O(n log n): maintain a patience-sorting array `tails`
  and binary-search for each element's insertion point.
"""
import bisect


def length_of_lis(nums: list[int]) -> int:
    pass


if __name__ == "__main__":
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7, 7]) == 1
    assert length_of_lis([1]) == 1
    assert length_of_lis([3, 1, 2]) == 2
    print("All tests passed!")
