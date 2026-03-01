"""
Problem: Target Sum
Day: 38 | Difficulty: Medium | Topic: 0/1 Knapsack Variant
Link: https://leetcode.com/problems/target-sum/

Description:
    You are given an integer array nums and an integer target. You want to
    build an expression out of nums by adding one of the symbols '+' or '-'
    before each integer in nums and then concatenate all the integers.
    Return the number of different expressions that evaluate to target.

Examples:
    Input: nums = [1, 1, 1, 1, 1], target = 3
    Output: 5
    Explanation: Five ways: -1+1+1+1+1, +1-1+1+1+1, +1+1-1+1+1,
    +1+1+1-1+1, +1+1+1+1-1

    Input: nums = [1], target = 1
    Output: 1

Constraints:
    - 1 <= nums.length <= 20
    - 0 <= nums[i] <= 1000
    - 0 <= sum(nums) <= 1000
    - -1000 <= target <= 1000

Hint:
    Let P = sum of positive subset, N = sum of negative subset.
    P - N = target and P + N = total_sum.
    So P = (target + total_sum) / 2. If this is not an integer, answer is 0.
    Reduce to: "count subsets with sum = P" -- a 0/1 knapsack counting problem.
    dp[s] = number of subsets that sum to s.

Pattern: Transform into subset sum counting problem using the math trick
    above. Then solve with 0/1 knapsack counting DP.
"""

from typing import List


def find_target_sum_ways(nums: List[int], target: int) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"nums": [1, 1, 1, 1, 1], "target": 3, "expected": 5},
        {"nums": [1], "target": 1, "expected": 1},
        {"nums": [1, 0], "target": 1, "expected": 2},
        {"nums": [0, 0, 0, 0, 0], "target": 0, "expected": 32},
        {"nums": [1, 2, 1], "target": 0, "expected": 2},
        {"nums": [100], "target": -200, "expected": 0},
    ]

    for i, t in enumerate(tests):
        result = find_target_sum_ways(t["nums"], t["target"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
