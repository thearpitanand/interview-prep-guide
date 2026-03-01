"""
Problem: Best Time to Buy and Sell Stock with Cooldown
Day: 39 | Difficulty: Medium | Topic: State Machine DP
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Description:
    You are given an array prices where prices[i] is the price of a given
    stock on the ith day. Find the maximum profit you can achieve.
    You may complete as many transactions as you like with the following
    restrictions:
    - After you sell your stock, you cannot buy stock on the next day
      (i.e., cooldown of one day).
    Note: You may not engage in multiple transactions simultaneously
    (you must sell the stock before you buy again).

Examples:
    Input: prices = [1, 2, 3, 0, 2]
    Output: 3
    Explanation: Buy day 0, sell day 2 (profit 2), cooldown day 3,
    buy day 3, sell day 4 (profit 2). Total = 3.

    Input: prices = [1]
    Output: 0

Constraints:
    - 1 <= prices.length <= 5000
    - 0 <= prices[i] <= 1000

Hint:
    Use three states: free (can buy), holding (holding stock, can sell),
    cooldown (just sold, must wait).
    Transitions:
    - free = max(free, cooldown)           -- rest or finish cooldown
    - holding = max(holding, free - price) -- rest or buy
    - cooldown = holding + price           -- sell
    Answer: max(free, cooldown) at the end.

Pattern: State machine DP with 3 states. Each day, transition between states
    based on buy/sell/rest actions. O(n) time, O(1) space.
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"prices": [1, 2, 3, 0, 2], "expected": 3},
        {"prices": [1], "expected": 0},
        {"prices": [1, 2], "expected": 1},
        {"prices": [2, 1], "expected": 0},
        {"prices": [1, 2, 4], "expected": 3},
        {"prices": [6, 1, 3, 2, 4, 7], "expected": 6},
    ]

    for i, t in enumerate(tests):
        result = max_profit(t["prices"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
