"""
Problem: Set Matrix Zeroes
LeetCode: 73 - https://leetcode.com/problems/set-matrix-zeroes/
Day: 16
Difficulty: Medium
Topic: In-place Modification

Description:
    Given an m x n integer matrix, if an element is 0, set its entire
    row and column to 0's. You must do it in place.

Examples:
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    - m == matrix.length
    - n == matrix[0].length
    - 1 <= m, n <= 200
    - -2^31 <= matrix[i][j] <= 2^31 - 1

    Follow up:
    - O(mn) space is straightforward (store copy)
    - O(m + n) space uses sets for zero rows/cols
    - O(1) space uses first row/col as markers

Hint:
    O(1) space approach:
    1) Use first row and first col as markers
    2) Use a separate boolean for whether first row has zero
    3) Use a separate boolean for whether first col has zero
    4) Scan rest of matrix: if matrix[i][j]==0, set matrix[i][0]=0
       and matrix[0][j]=0
    5) Second pass: use markers to zero out cells
    6) Finally handle first row and first col

Pattern: In-place Modification
    - Don't zero out immediately (you'll lose information)
    - Mark first, then apply in a second pass
    - Use the matrix itself as storage for the markers
"""

from typing import List


def set_zeroes(matrix: List[List[int]]) -> None:
    """Modify matrix in-place. Do not return anything."""
    pass


# ---------- Test Cases ----------
if __name__ == "__main__":
    # Test 1: Center zero
    m1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(m1)
    assert m1 == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    # Test 2: Corner zeroes
    m2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeroes(m2)
    assert m2 == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    # Test 3: No zeroes
    m3 = [[1, 2], [3, 4]]
    set_zeroes(m3)
    assert m3 == [[1, 2], [3, 4]]

    # Test 4: All zeroes
    m4 = [[0, 0], [0, 0]]
    set_zeroes(m4)
    assert m4 == [[0, 0], [0, 0]]

    # Test 5: Single element zero
    m5 = [[0]]
    set_zeroes(m5)
    assert m5 == [[0]]

    # Test 6: Single element non-zero
    m6 = [[5]]
    set_zeroes(m6)
    assert m6 == [[5]]

    print("All test cases passed!")
