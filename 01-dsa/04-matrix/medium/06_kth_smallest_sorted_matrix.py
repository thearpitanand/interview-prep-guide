"""
Problem: Kth Smallest in Sorted Matrix (LC 378) | Day 16 | Medium
Topic: Matrix

Given an n x n matrix where each row and column is sorted in ascending order,
return the kth smallest element.

Example 1:
  Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
  Output: 13

Constraints:
  - n == matrix.length == matrix[i].length
  - 1 <= n <= 300
  - -10^9 <= matrix[i][j] <= 10^9
  - 1 <= k <= n^2

Hint: Binary search on value range, or use min-heap with n pointers.
Pattern: Binary Search on Value / Min-Heap
"""


def kth_smallest(matrix: list[list[int]], k: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert kth_smallest([[1,5,9],[10,11,13],[12,13,15]], 8) == 13
    assert kth_smallest([[1,2],[1,3]], 2) == 1
    assert kth_smallest([[-5]], 1) == -5
    print("All tests passed!")
