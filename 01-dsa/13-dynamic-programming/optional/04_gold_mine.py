"""
Problem: Gold Mine Problem (GFG) | Optional | Easy
Topic: Dynamic Programming

Given an m×n grid with gold in each cell, start from any cell in first column
and move right, right-up, or right-down. Maximize gold collected.

Example 1:
  Input: grid = [[1,3,3],[2,1,4],[0,6,4]]
  Output: 12  # path: 2→1→4 or 2→6→4

Constraints:
  - 1 <= m, n <= 50

Hint: DP right-to-left: dp[i][j] = grid[i][j] + max(dp[i-1][j+1], dp[i][j+1], dp[i+1][j+1]).
Pattern: DP on Grid
"""


def gold_mine(grid: list[list[int]]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert gold_mine([[1,3,3],[2,1,4],[0,6,4]]) == 12
    assert gold_mine([[1,3,1,5],[2,2,4,1],[5,0,2,3],[0,6,1,2]]) == 16
    print("All tests passed!")
