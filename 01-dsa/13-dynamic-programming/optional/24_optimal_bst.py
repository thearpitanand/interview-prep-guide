"""
Problem: Optimal Binary Search Tree (GFG) | Optional | Hard
Topic: Dynamic Programming

Given keys with search frequencies, construct a BST that minimizes total
search cost.

Example 1:
  Input: keys = [10, 12, 20], freq = [34, 8, 50]
  Output: 142

Constraints:
  - 1 <= n <= 100

Hint: dp[i][j] = min cost BST for keys[i..j]. Try each key as root, cost = sum(freq) + dp[i][r-1] + dp[r+1][j].
Pattern: Interval DP
"""


def optimal_bst(keys: list[int], freq: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert optimal_bst([10, 12, 20], [34, 8, 50]) == 142
    assert optimal_bst([10, 12], [34, 50]) == 118
    print("All tests passed!")
