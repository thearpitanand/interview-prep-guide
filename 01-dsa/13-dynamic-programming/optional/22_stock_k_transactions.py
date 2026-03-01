"""
Problem: Buy/Sell Stock At Most K Times (LC 188) | Optional | Hard
Topic: Dynamic Programming

Given stock prices and K, find max profit with at most K transactions.

Example 1:
  Input: prices = [3,2,6,5,0,3], k = 2
  Output: 7  # buy@2 sell@6, buy@0 sell@3

Constraints:
  - 0 <= k <= 100
  - 0 <= prices.length <= 1000

Hint: dp[t][i] = max profit using at most t transactions up to day i. Optimize with running max.
Pattern: DP
"""


def max_profit_k(prices: list[int], k: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_profit_k([3, 2, 6, 5, 0, 3], 2) == 7
    assert max_profit_k([2, 4, 1], 2) == 2
    assert max_profit_k([3, 2, 6, 5, 0, 3], 1) == 4
    print("All tests passed!")
