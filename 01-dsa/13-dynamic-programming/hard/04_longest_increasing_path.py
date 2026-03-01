"""
Problem: Longest Increasing Path in a Matrix
Day: 39 | Difficulty: Hard | Topic: DFS + Memoization
Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Description:
    Given an m x n integers matrix, return the length of the longest
    increasing path in the matrix. From each cell, you can either move
    in four directions: left, right, up, or down. You may not move
    diagonally or move outside the boundary.

Examples:
    Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
    Output: 4
    Explanation: The longest increasing path is [1, 2, 6, 9].

    Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
    Output: 4
    Explanation: The longest increasing path is [3, 4, 5, 6].

    Input: matrix = [[1]]
    Output: 1

Constraints:
    - m == matrix.length
    - n == matrix[i].length
    - 1 <= m, n <= 200
    - 0 <= matrix[i][j] <= 2^31 - 1

Hint:
    Use DFS with memoization. For each cell, try all 4 directions. Only
    move to a neighbor if it has a strictly larger value. Cache the result
    for each cell. memo[i][j] = length of longest increasing path starting
    from (i, j). No need for a visited set because we only move to strictly
    larger values (no cycles possible).

Pattern: DFS + Memoization (top-down DP on a DAG). The strictly increasing
    constraint ensures no cycles, so this is a DAG longest path problem.
"""

from typing import List


def longest_increasing_path(matrix: List[List[int]]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"matrix": [[9, 9, 4], [6, 6, 8], [2, 1, 1]], "expected": 4},
        {"matrix": [[3, 4, 5], [3, 2, 6], [2, 2, 1]], "expected": 4},
        {"matrix": [[1]], "expected": 1},
        {"matrix": [[1, 2]], "expected": 2},
        {"matrix": [[1, 2, 3], [6, 5, 4], [7, 8, 9]], "expected": 9},
        {"matrix": [[7, 8, 9], [9, 7, 6], [7, 2, 3]], "expected": 6},
    ]

    for i, t in enumerate(tests):
        result = longest_increasing_path(t["matrix"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
