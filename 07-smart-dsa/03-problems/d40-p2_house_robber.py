"""
Problem: House Robber (LC 198) | Smart-DSA Day 40 | Medium
Pattern: 1D Dynamic Programming
Time target: 20 minutes

You are a robber planning to rob houses along a street. Each house has a
certain amount of money stashed. Adjacent houses have security systems
connected — if two adjacent houses are broken into on the same night, the
police are alerted. Given an integer array nums representing the amount of
money at each house, return the maximum amount you can rob without alerting
the police.

Example 1:
  Input: nums = [1, 2, 3, 1]
  Output: 4
  Explanation: Rob house 1 (1) then house 3 (3) = 4.

Example 2:
  Input: nums = [2, 7, 9, 3, 1]
  Output: 12
  Explanation: Rob house 1 (2), house 3 (9), house 5 (1) = 12.

Constraints:
  - 1 <= nums.length <= 100
  - 0 <= nums[i] <= 400

Hint (⚠ read only after time budget is blown):
  dp[i] = max(dp[i-1], dp[i-2] + nums[i]). Use two variables instead of a
  full array. At each house, you choose the better of: skip it (keep prev
  best) or rob it (add to best two houses ago).
"""


def rob(nums: list[int]) -> int:
    pass


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([0]) == 0
    assert rob([5]) == 5
    assert rob([2, 1]) == 2
    assert rob([1, 1, 1]) == 2
    print("All tests passed!")
