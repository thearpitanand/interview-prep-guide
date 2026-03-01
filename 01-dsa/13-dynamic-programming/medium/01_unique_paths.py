"""
Problem: Unique Paths
Day: 37 | Difficulty: Medium | Topic: Grid DP
Link: https://leetcode.com/problems/unique-paths/

Description:
    A robot is located at the top-left corner of an m x n grid. The robot
    can only move either down or right at any point in time. The robot is
    trying to reach the bottom-right corner of the grid.
    How many possible unique paths are there?

Examples:
    Input: m = 3, n = 7
    Output: 28

    Input: m = 3, n = 2
    Output: 3
    Explanation: From top-left to bottom-right, there are 3 paths:
    Right->Down->Down, Down->Down->Right, Down->Right->Down

Constraints:
    - 1 <= m, n <= 100

Hint:
    dp[i][j] = number of ways to reach cell (i, j). You can only come from
    above (i-1, j) or from the left (i, j-1). So dp[i][j] = dp[i-1][j] +
    dp[i][j-1]. First row and first column are all 1s (only one way to
    reach them).

Pattern: Grid DP. Fill the grid row by row, left to right. Can optimize
    to O(n) space using a single row array.
"""


def unique_paths(m: int, n: int) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"m": 3, "n": 7, "expected": 28},
        {"m": 3, "n": 2, "expected": 3},
        {"m": 1, "n": 1, "expected": 1},
        {"m": 1, "n": 5, "expected": 1},
        {"m": 5, "n": 1, "expected": 1},
        {"m": 3, "n": 3, "expected": 6},
        {"m": 7, "n": 3, "expected": 28},
    ]

    for i, t in enumerate(tests):
        result = unique_paths(t["m"], t["n"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
