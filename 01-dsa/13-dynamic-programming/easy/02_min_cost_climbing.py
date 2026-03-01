"""
Problem: Min Cost Climbing Stairs
Day: 36 | Difficulty: Easy | Topic: 1D DP
Link: https://leetcode.com/problems/min-cost-climbing-stairs/

Description:
    You are given an integer array cost where cost[i] is the cost of the ith
    step on a staircase. Once you pay the cost, you can either climb one or
    two steps. You can start from step 0 or step 1.
    Return the minimum cost to reach the top of the floor (past the last step).

Examples:
    Input: cost = [10, 15, 20]
    Output: 15
    Explanation: Start at step 1 (cost 15), climb 2 steps to the top.

    Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    Output: 6
    Explanation: Pay costs at steps 0, 2, 3, 4, 6, 7 = 1+1+1+1+1+1 = 6.

Constraints:
    - 2 <= cost.length <= 1000
    - 0 <= cost[i] <= 999

Hint:
    dp[i] = minimum cost to reach step i. At each step, you came from either
    step i-1 or step i-2, so dp[i] = cost[i] + min(dp[i-1], dp[i-2]).
    The answer is min(dp[n-1], dp[n-2]) since you can reach the top from
    either of the last two steps.

Pattern: 1D DP where dp[i] depends on dp[i-1] and dp[i-2]. Can optimize
    to O(1) space with two variables.
"""

from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"cost": [10, 15, 20], "expected": 15},
        {"cost": [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], "expected": 6},
        {"cost": [0, 0], "expected": 0},
        {"cost": [1, 2], "expected": 1},
        {"cost": [10, 15], "expected": 10},
        {"cost": [0, 1, 2, 3], "expected": 2},
    ]

    for i, t in enumerate(tests):
        result = min_cost_climbing_stairs(t["cost"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
