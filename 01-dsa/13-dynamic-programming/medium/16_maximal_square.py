"""
Problem: Maximal Square
Day: 39 | Difficulty: Medium | Topic: 2D DP
Link: https://leetcode.com/problems/maximal-square/

Description:
    Given an m x n binary matrix filled with 0's and 1's, find the largest
    square containing only 1's and return its area.

Examples:
    Input: matrix = [["1","0","1","0","0"],
                     ["1","0","1","1","1"],
                     ["1","1","1","1","1"],
                     ["1","0","0","1","0"]]
    Output: 4
    Explanation: The largest square of 1's has side length 2, area = 4.

    Input: matrix = [["0","1"],["1","0"]]
    Output: 1

    Input: matrix = [["0"]]
    Output: 0

Constraints:
    - m == matrix.length
    - n == matrix[i].length
    - 1 <= m, n <= 300
    - matrix[i][j] is '0' or '1'

Hint:
    dp[i][j] = side length of the largest square whose bottom-right corner
    is at (i, j). If matrix[i][j] == '1':
    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    The answer is max(dp[i][j])^2.
    Intuition: a square of side k at (i,j) requires squares of side k-1
    at (i-1,j), (i,j-1), and (i-1,j-1).

Pattern: 2D DP. Each cell depends on its top, left, and top-left neighbors.
    Can optimize to O(n) space using a single row + one variable for the
    diagonal element.
"""

from typing import List


def maximal_square(matrix: List[List[str]]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {
            "matrix": [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
            "expected": 4,
        },
        {"matrix": [["0", "1"], ["1", "0"]], "expected": 1},
        {"matrix": [["0"]], "expected": 0},
        {"matrix": [["1"]], "expected": 1},
        {
            "matrix": [
                ["1", "1", "1"],
                ["1", "1", "1"],
                ["1", "1", "1"],
            ],
            "expected": 9,
        },
        {"matrix": [["0", "0"], ["0", "0"]], "expected": 0},
    ]

    for i, t in enumerate(tests):
        result = maximal_square(t["matrix"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
