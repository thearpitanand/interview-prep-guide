"""
Problem: Coin Change
Day: 37 | Difficulty: Medium | Topic: Unbounded Knapsack / DP
Link: https://leetcode.com/problems/coin-change/

Description:
    You are given an integer array coins representing coins of different
    denominations and an integer amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount.
    If that amount cannot be made up by any combination of the coins, return -1.
    You may assume you have an infinite number of each kind of coin.

Examples:
    Input: coins = [1, 5, 11], amount = 15
    Output: 3
    Explanation: 5 + 5 + 5 = 15 (3 coins). Note: greedy (11+1+1+1+1) = 5 coins.

    Input: coins = [2], amount = 3
    Output: -1

    Input: coins = [1], amount = 0
    Output: 0

Constraints:
    - 1 <= coins.length <= 12
    - 1 <= coins[i] <= 2^31 - 1
    - 0 <= amount <= 10^4

Hint:
    dp[a] = minimum number of coins to make amount a.
    dp[0] = 0. For each amount a from 1 to target, try all coins:
    dp[a] = min(dp[a], dp[a - coin] + 1) for each coin <= a.
    Initialize dp with infinity.

Pattern: Unbounded knapsack variant. Each coin can be used unlimited times,
    so iterate coins in the outer loop and amounts forward in the inner loop.
    Or iterate amounts in the outer loop and try all coins.
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"coins": [1, 5, 11], "amount": 15, "expected": 3},
        {"coins": [2], "amount": 3, "expected": -1},
        {"coins": [1], "amount": 0, "expected": 0},
        {"coins": [1, 2, 5], "amount": 11, "expected": 3},
        {"coins": [1], "amount": 1, "expected": 1},
        {"coins": [2, 5, 10, 1], "amount": 27, "expected": 4},
    ]

    for i, t in enumerate(tests):
        result = coin_change(t["coins"], t["amount"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
