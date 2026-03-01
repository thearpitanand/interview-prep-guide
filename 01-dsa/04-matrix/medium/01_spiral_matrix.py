"""
Problem: Spiral Matrix
LeetCode: 54 - https://leetcode.com/problems/spiral-matrix/
Day: 15
Difficulty: Medium
Topic: Spiral Traversal

Description:
    Given an m x n matrix, return all elements of the matrix in
    spiral order.

Examples:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
    - m == matrix.length
    - n == matrix[i].length
    - 1 <= m, n <= 10
    - -100 <= matrix[i][j] <= 100

Hint:
    Use four boundaries: top, bottom, left, right. In each iteration:
    1) Go right across top row, then top++
    2) Go down along right col, then right--
    3) Go left across bottom row (if top <= bottom), then bottom--
    4) Go up along left col (if left <= right), then left++
    Stop when boundaries cross.

Pattern: Spiral Traversal
    - Maintain 4 boundaries that shrink inward
    - Process one edge per step (right, down, left, up)
    - Check boundary validity before bottom-row and left-col passes
      to avoid duplicates in non-square matrices
"""

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    pass


# ---------- Test Cases ----------
if __name__ == "__main__":
    # Test 1: 3x3 square matrix
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1, 2, 3, 6, 9, 8, 7, 4, 5
    ]

    # Test 2: 3x4 rectangular matrix
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
        1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7
    ]

    # Test 3: Single row
    assert spiral_order([[1, 2, 3, 4]]) == [1, 2, 3, 4]

    # Test 4: Single column
    assert spiral_order([[1], [2], [3]]) == [1, 2, 3]

    # Test 5: 1x1 matrix
    assert spiral_order([[7]]) == [7]

    # Test 6: 2x2 matrix
    assert spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]

    print("All test cases passed!")
