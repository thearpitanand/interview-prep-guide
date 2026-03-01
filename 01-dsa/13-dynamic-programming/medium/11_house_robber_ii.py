"""
Problem: House Robber II
Day: 38 | Difficulty: Medium | Topic: Circular DP
Link: https://leetcode.com/problems/house-robber-ii/

Description:
    You are a professional robber planning to rob houses along a street.
    All houses at this place are arranged in a circle. That means the first
    house is the neighbor of the last one. Adjacent houses have security
    systems connected -- if two adjacent houses are broken into, the police
    will be alerted. Return the maximum amount of money you can rob.

Examples:
    Input: nums = [2, 3, 2]
    Output: 3
    Explanation: You cannot rob house 0 and house 2 (they are adjacent in
    the circle). Rob house 1 with amount 3.

    Input: nums = [1, 2, 3, 1]
    Output: 4
    Explanation: Rob house 0 (1) + house 2 (3) = 4.

    Input: nums = [1, 2, 3]
    Output: 3

Constraints:
    - 1 <= nums.length <= 100
    - 0 <= nums[i] <= 1000

Hint:
    Since houses form a circle, house 0 and house n-1 are adjacent. So we
    cannot rob both. Solve two subproblems:
    1. Rob houses 0 to n-2 (exclude last)
    2. Rob houses 1 to n-1 (exclude first)
    Answer = max of both. Each subproblem is the standard House Robber I.

Pattern: Circular DP. Break the circular constraint by running linear
    House Robber twice on different ranges. Take the maximum.
"""

from typing import List


def rob(nums: List[int]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"nums": [2, 3, 2], "expected": 3},
        {"nums": [1, 2, 3, 1], "expected": 4},
        {"nums": [1, 2, 3], "expected": 3},
        {"nums": [1], "expected": 1},
        {"nums": [1, 2], "expected": 2},
        {"nums": [0], "expected": 0},
        {"nums": [200, 3, 140, 20, 10], "expected": 340},
    ]

    for i, t in enumerate(tests):
        result = rob(t["nums"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
