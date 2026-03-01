"""
Problem: Search in Row-Col Sorted Matrix (LC 240) | Day 16 | Medium
Topic: Matrix

Write an efficient algorithm that searches for a value in an m x n integer
matrix. Each row is sorted left to right. Each column is sorted top to bottom.

Example 1:
  Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
  Output: True

Constraints:
  - m == matrix.length, n == matrix[i].length
  - 1 <= m, n <= 300
  - -10^9 <= matrix[i][j] <= 10^9

Hint: Start from top-right corner. If target < current, move left; if target > current, move down.
Pattern: Staircase Search
"""


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    assert search_matrix(mat, 5) == True
    assert search_matrix(mat, 20) == False
    assert search_matrix([[1]], 1) == True
    print("All tests passed!")
