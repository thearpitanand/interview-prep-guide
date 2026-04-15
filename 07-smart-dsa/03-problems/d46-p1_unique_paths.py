"""
Problem: Unique Paths (LC 62) | Smart-DSA Day 46 | Medium
Pattern: Dynamic Programming — Grid DP
Time target: 20 minutes

A robot is located at the top-left corner of an m x n grid. The robot can
only move either down or right. It tries to reach the bottom-right corner.
How many possible unique paths are there?

Example 1:
  Input: m = 3, n = 7
  Output: 28

Example 2:
  Input: m = 3, n = 2
  Output: 3  (paths: R→D→D, D→R→D, D→D→R)

Constraints:
  - 1 <= m, n <= 100

Hint (⚠ read only after time budget is blown):
  dp[i][j] = number of unique paths to reach (i, j).
  Base: entire top row and left column = 1.
  Transition: dp[i][j] = dp[i-1][j] + dp[i][j-1].
  Optimization: only one row needed at a time (rolling array).
"""


def unique_paths(m: int, n: int) -> int:
    pass


if __name__ == "__main__":
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3
    assert unique_paths(1, 1) == 1
    assert unique_paths(2, 2) == 2
    assert unique_paths(7, 3) == 28
    print("All tests passed!")
