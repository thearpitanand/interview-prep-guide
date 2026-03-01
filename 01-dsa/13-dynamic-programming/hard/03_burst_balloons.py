"""
Problem: Burst Balloons
Day: 39 | Difficulty: Hard | Topic: Interval DP
Link: https://leetcode.com/problems/burst-balloons/

Description:
    You are given n balloons, indexed from 0 to n - 1. Each balloon is
    painted with a number on it represented by an array nums. You are asked
    to burst all the balloons. If you burst the ith balloon, you will get
    nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out
    of bounds of the array, treat it as if there is a balloon with a 1
    painted on it. Return the maximum coins you can collect by bursting
    the balloons wisely.

Examples:
    Input: nums = [3, 1, 5, 8]
    Output: 167
    Explanation: nums = [3,1,5,8] -> [3,5,8] -> [3,8] -> [8] -> []
    coins = 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 15+120+24+8 = 167

    Input: nums = [1, 5]
    Output: 10

Constraints:
    - n == nums.length
    - 1 <= n <= 300
    - 0 <= nums[i] <= 100

Hint:
    Think in reverse: instead of which balloon to burst first, think which
    balloon to burst LAST in each subinterval. Add 1s at both ends.
    dp[i][j] = max coins from bursting all balloons between i and j (exclusive).
    For each k between i and j as the last balloon to burst:
    dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])
    Fill by increasing interval length.

Pattern: Interval DP. The key insight is thinking about which balloon is
    burst LAST (not first). Pad the array with 1s at both ends.
"""

from typing import List


def max_coins(nums: List[int]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"nums": [3, 1, 5, 8], "expected": 167},
        {"nums": [1, 5], "expected": 10},
        {"nums": [1], "expected": 1},
        {"nums": [5], "expected": 5},
        {"nums": [3, 1, 5], "expected": 35},
        {"nums": [1, 2, 3, 4, 5], "expected": 110},
    ]

    for i, t in enumerate(tests):
        result = max_coins(t["nums"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
