"""
Problem: Find Specific Pair in Matrix (GFG) | Optional | Hard
Topic: Matrix

Given an n x n sorted matrix, find max(mat[c][d] - mat[a][b]) where c > a and d > b.

Example 1:
  Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
  Output: 8  # mat[2][2] - mat[0][0] = 9-1 = 8

Constraints:
  - 1 <= n <= 100

Hint: Precompute max from bottom-right corner and iterate.
Pattern: Dynamic Programming on Matrix
"""


def specific_pair(mat: list[list[int]]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert specific_pair([[1,2,3],[4,5,6],[7,8,9]]) == 8
    assert specific_pair([[1,2],[3,4]]) == 3
    print("All tests passed!")
