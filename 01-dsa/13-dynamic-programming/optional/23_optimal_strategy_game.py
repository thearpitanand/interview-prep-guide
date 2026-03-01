"""
Problem: Optimal Strategy for a Game (GFG) | Optional | Hard
Topic: Dynamic Programming

Two players pick coins from either end of a row. Both play optimally.
Find the maximum value the first player can collect.

Example 1:
  Input: coins = [5, 3, 7, 10]
  Output: 15  # First picks 10, second picks 7, first picks 5

Constraints:
  - 2 <= n <= 10^3

Hint: dp[i][j] = max value first player gets from coins[i..j]. Consider picking left or right.
Pattern: Interval DP / Game Theory
"""


def optimal_strategy(coins: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert optimal_strategy([5, 3, 7, 10]) == 15
    assert optimal_strategy([8, 15, 3, 7]) == 22
    print("All tests passed!")
