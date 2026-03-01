"""
Problem: Rotate Image
LeetCode: 48 - https://leetcode.com/problems/rotate-image/
Day: 15
Difficulty: Medium
Topic: In-place Rotation

Description:
    You are given an n x n 2D matrix representing an image. Rotate the
    image by 90 degrees clockwise. You have to rotate the image in-place,
    which means you have to modify the input 2D matrix directly. DO NOT
    allocate another 2D matrix and do the rotation.

Examples:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
    - n == matrix.length == matrix[i].length
    - 1 <= n <= 20
    - -1000 <= matrix[i][j] <= 1000

Hint:
    Two-step approach:
    1) Transpose the matrix: swap matrix[i][j] with matrix[j][i]
       (only for i < j to avoid double-swapping)
    2) Reverse each row

    Alternative: rotate in layers, moving 4 elements at a time.

Pattern: In-place Modification
    - Transpose: for i in range(n), for j in range(i+1, n), swap
    - Reverse rows: for each row, reverse it
    - This transforms (i,j) -> (j, n-1-i) which is 90 degree clockwise
    - For counter-clockwise: reverse each row first, then transpose
"""

from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """Rotate the matrix in-place. Do not return anything."""
    pass


# ---------- Test Cases ----------
if __name__ == "__main__":
    # Test 1: 3x3 matrix
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(m1)
    assert m1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # Test 2: 4x4 matrix
    m2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(m2)
    assert m2 == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    # Test 3: 1x1 matrix
    m3 = [[1]]
    rotate(m3)
    assert m3 == [[1]]

    # Test 4: 2x2 matrix
    m4 = [[1, 2], [3, 4]]
    rotate(m4)
    assert m4 == [[3, 1], [4, 2]]

    print("All test cases passed!")
