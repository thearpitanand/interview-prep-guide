"""
Problem: Search a 2D Matrix (LC 74) | Day 13 | Medium
Topic: Searching and Sorting

You are given an m x n integer matrix with the following properties:
  - Each row is sorted in non-decreasing order.
  - The first integer of each row is greater than the last integer of the
    previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
  Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
  Output: True

Example 2:
  Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
  Output: False

Constraints:
  - m == matrix.length
  - n == matrix[i].length
  - 1 <= m, n <= 100
  - -10^4 <= matrix[i][j], target <= 10^4

Hint: Treat the 2D matrix as a flattened 1D sorted array of size m*n.
      Index i in 1D maps to matrix[i // n][i % n] in 2D.
      Then apply standard binary search.
Pattern: Binary Search (2D to 1D mapping)
"""

from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) is True
    assert search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) is False
    assert search_matrix([[1]], 1) is True
    assert search_matrix([[1]], 0) is False
    assert search_matrix([[1, 3]], 3) is True
    print("All tests passed!")
