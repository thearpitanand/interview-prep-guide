"""
Problem: Rod Cutting Problem (GFG) | Day 37 | Medium
Topic: Dynamic Programming

Given a rod of length N and prices for each piece length, determine the
maximum revenue obtainable by cutting the rod and selling pieces.

Example 1:
  Input: prices = [1, 5, 8, 9, 10, 17, 17, 20], n = 8
  Output: 22  # cut into pieces of length 2 and 6 → 5+17=22

Constraints:
  - 1 <= N <= 1000

Hint: dp[i] = max revenue for rod of length i. dp[i] = max(prices[j] + dp[i-j-1]) for all j < i.
Pattern: Unbounded Knapsack variant
"""


def rod_cutting(prices: list[int], n: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert rod_cutting([1, 5, 8, 9, 10, 17, 17, 20], 8) == 22
    assert rod_cutting([3, 5, 8, 9, 10, 17, 17, 20], 8) == 24
    assert rod_cutting([1], 1) == 1
    print("All tests passed!")
