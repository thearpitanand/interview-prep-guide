"""
Problem: House Robber
Day: 36 | Difficulty: Easy | Topic: 1D DP
Link: https://leetcode.com/problems/house-robber/

Description:
    You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed. Adjacent houses have
    security systems connected -- if two adjacent houses are broken into on
    the same night, the police will be alerted.
    Return the maximum amount of money you can rob without alerting the police.

Examples:
    Input: nums = [1, 2, 3, 1]
    Output: 4
    Explanation: Rob house 0 (1) + house 2 (3) = 4.

    Input: nums = [2, 7, 9, 3, 1]
    Output: 12
    Explanation: Rob house 0 (2) + house 2 (9) + house 4 (1) = 12.

Constraints:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 400

Hint:
    At each house i, you have two choices: rob it (get nums[i] + dp[i-2])
    or skip it (get dp[i-1]). So dp[i] = max(dp[i-1], dp[i-2] + nums[i]).

Pattern: 1D DP with include/exclude decision. Fibonacci-style since dp[i]
    only depends on dp[i-1] and dp[i-2]. Can optimize to O(1) space.
"""

from typing import List


def rob(nums: List[int]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"nums": [1, 2, 3, 1], "expected": 4},
        {"nums": [2, 7, 9, 3, 1], "expected": 12},
        {"nums": [0], "expected": 0},
        {"nums": [5], "expected": 5},
        {"nums": [1, 2], "expected": 2},
        {"nums": [2, 1, 1, 2], "expected": 4},
        {"nums": [1, 3, 1, 3, 100], "expected": 103},
    ]

    for i, t in enumerate(tests):
        result = rob(t["nums"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
