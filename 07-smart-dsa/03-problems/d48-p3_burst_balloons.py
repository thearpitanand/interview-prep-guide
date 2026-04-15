"""
Problem: Burst Balloons (LC 312) | Smart-DSA Day 48 | Hard
Pattern: Dynamic Programming — Interval DP
Time target: 45 minutes

You are given n balloons indexed 0 to n-1. Each balloon is painted with a
number on it. You are asked to burst all the balloons. If you burst balloon i
you will get nums[i-1] * nums[i] * nums[i+1] coins. If i-1 or i+1 is out of
bounds, treat it as a balloon with value 1.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:
  Input: nums = [3, 1, 5, 8]
  Output: 167
  Explanation: [3,1,5,8] → burst 1: 3*1*5=15 → [3,5,8] →
               burst 5: 3*5*8=120 → [3,8] → burst 3: 1*3*8=24 →
               burst 8: 1*8*1=8. Total = 15+120+24+8 = 167.

Example 2:
  Input: nums = [1, 5]
  Output: 10

Constraints:
  - n == nums.length
  - 1 <= n <= 300
  - 0 <= nums[i] <= 100

Hint (⚠ read only after time budget is blown):
  Key reframe: instead of "which balloon to burst first", think "which
  balloon to burst LAST in interval (l, r)". Pad nums with 1s on both ends.
  dp[l][r] = max coins from bursting all balloons strictly between l and r.
  For each candidate k as the LAST balloon burst in (l, r):
  dp[l][r] = max(dp[l][k] + nums[l]*nums[k]*nums[r] + dp[k][r]).
"""


def max_coins(nums: list[int]) -> int:
    pass


if __name__ == "__main__":
    assert max_coins([3, 1, 5, 8]) == 167
    assert max_coins([1, 5]) == 10
    assert max_coins([1]) == 1
    assert max_coins([0]) == 0
    assert max_coins([7, 9, 8, 0, 7, 1, 3, 5, 5, 2, 3]) == 1654
    print("All tests passed!")
