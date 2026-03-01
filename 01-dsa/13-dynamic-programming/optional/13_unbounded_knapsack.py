"""
Problem: Unbounded Knapsack (GFG) | Optional | Medium
Topic: Dynamic Programming

Given weights and values of items (unlimited supply of each), maximize value
for a given capacity.

Example 1:
  Input: values = [1, 30], weights = [1, 50], W = 100
  Output: 100  # take 100 items of weight 1

Constraints:
  - 1 <= N <= 1000
  - 1 <= W <= 1000

Hint: dp[w] = max value for capacity w. dp[w] = max(dp[w], val[i]+dp[w-wt[i]]).
Pattern: 1D DP
"""


def unbounded_knapsack(values: list[int], weights: list[int], W: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert unbounded_knapsack([1, 30], [1, 50], 100) == 100
    assert unbounded_knapsack([10, 40, 50, 70], [1, 3, 4, 5], 8) == 110
    print("All tests passed!")
