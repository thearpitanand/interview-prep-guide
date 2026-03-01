"""
Problem: Minimum Path Sum
Day: 38 | Difficulty: Medium | Topic: Grid DP
Link: https://leetcode.com/problems/minimum-path-sum/

Description:
    Given an m x n grid filled with non-negative numbers, find a path from
    top-left to bottom-right which minimizes the sum of all numbers along
    its path. You can only move either down or right at any point in time.

Examples:
    Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
    Output: 7
    Explanation: Path 1->3->1->1->1 = 7 minimizes the sum.

    Input: grid = [[1,2,3],[4,5,6]]
    Output: 12

Constraints:
    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 200
    - 0 <= grid[i][j] <= 200

Hint:
    dp[i][j] = minimum path sum to reach cell (i, j).
    dp[0][0] = grid[0][0].
    First row: dp[0][j] = dp[0][j-1] + grid[0][j] (can only come from left).
    First col: dp[i][0] = dp[i-1][0] + grid[i][0] (can only come from above).
    Otherwise: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]).

Pattern: Grid DP. Similar to Unique Paths but with minimum sum instead of
    count. Can modify the grid in-place to use O(1) extra space.
"""

from typing import List


def min_path_sum(grid: List[List[int]]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"grid": [[1, 3, 1], [1, 5, 1], [4, 2, 1]], "expected": 7},
        {"grid": [[1, 2, 3], [4, 5, 6]], "expected": 12},
        {"grid": [[1]], "expected": 1},
        {"grid": [[1, 2], [3, 4]], "expected": 7},
        {"grid": [[0, 0, 0], [0, 0, 0]], "expected": 0},
        {"grid": [[1, 2, 3]], "expected": 6},
    ]

    for i, t in enumerate(tests):
        result = min_path_sum(t["grid"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
