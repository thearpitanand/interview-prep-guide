"""
Problem: Transpose Matrix
LeetCode: 867 - https://leetcode.com/problems/transpose-matrix/
Day: 15
Difficulty: Easy
Topic: Matrix Manipulation

Description:
    Given a 2D integer array matrix, return the transpose of matrix.
    The transpose of a matrix flips the matrix over its main diagonal,
    switching the row and column indices.

Examples:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,4,7],[2,5,8],[3,6,9]]

    Input: matrix = [[1,2,3],[4,5,6]]
    Output: [[1,4],[2,5],[3,6]]

Constraints:
    - m == matrix.length
    - n == matrix[i].length
    - 1 <= m, n <= 1000
    - 1 <= m * n <= 10^5
    - -10^9 <= matrix[i][j] <= 10^9

Hint:
    The element at position [i][j] in the original matrix goes to
    position [j][i] in the transposed matrix. The result dimensions
    are n x m (swapped from original m x n).

Pattern: Matrix Manipulation
    - Create a new matrix with swapped dimensions (cols x rows)
    - Copy element [i][j] to [j][i]
    - For square matrices you can do it in-place by swapping upper
      triangle with lower triangle
"""

from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    pass


# ---------- Test Cases ----------
if __name__ == "__main__":
    # Test 1: Square matrix
    assert transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
    ]

    # Test 2: Non-square matrix (2x3 -> 3x2)
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [
        [1, 4],
        [2, 5],
        [3, 6],
    ]

    # Test 3: Single row
    assert transpose([[1, 2, 3]]) == [[1], [2], [3]]

    # Test 4: Single column
    assert transpose([[1], [2], [3]]) == [[1, 2, 3]]

    # Test 5: 1x1 matrix
    assert transpose([[42]]) == [[42]]

    print("All test cases passed!")
