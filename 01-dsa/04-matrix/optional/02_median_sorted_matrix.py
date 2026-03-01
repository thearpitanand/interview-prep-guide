"""
Problem: Median in Row-Wise Sorted Matrix (GFG) | Optional | Medium
Topic: Matrix

Given a row-wise sorted matrix of size r*c (r, c are odd), find the median.

Example 1:
  Input: mat = [[1,3,5],[2,6,9],[3,6,9]]
  Output: 5

Constraints:
  - r, c are odd
  - 1 <= r, c <= 400

Hint: Binary search on value. For each candidate, count elements <= it using upper_bound per row.
Pattern: Binary Search on Value
"""


def matrix_median(mat: list[list[int]]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert matrix_median([[1,3,5],[2,6,9],[3,6,9]]) == 5
    assert matrix_median([[1],[2],[3]]) == 2
    print("All tests passed!")
