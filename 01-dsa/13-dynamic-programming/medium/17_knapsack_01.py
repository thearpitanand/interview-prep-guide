"""
Problem: 0/1 Knapsack (GFG) | Day 37 | Medium
Topic: Dynamic Programming

Given weights and values of N items, put them in a knapsack of capacity W.
Each item can be included at most once. Maximize total value.

Example 1:
  Input: values = [60, 100, 120], weights = [10, 20, 30], W = 50
  Output: 220  # items with weight 20 and 30

Constraints:
  - 1 <= N <= 1000
  - 1 <= W <= 1000

Hint: dp[i][w] = max value using first i items with capacity w. dp[i][w] = max(dp[i-1][w], val[i]+dp[i-1][w-wt[i]]).
Pattern: 2D DP / Space-Optimized 1D DP
"""


def knapsack_01(values: list[int], weights: list[int], W: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert knapsack_01([60, 100, 120], [10, 20, 30], 50) == 220
    assert knapsack_01([10, 20, 30], [1, 1, 1], 2) == 50
    assert knapsack_01([1, 2, 3], [4, 5, 1], 4) == 3
    print("All tests passed!")
