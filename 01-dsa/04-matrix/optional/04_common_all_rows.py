"""
Problem: Common Elements in All Rows (GFG) | Optional | Medium
Topic: Matrix

Given an m x n matrix, find all elements common to all rows.

Example 1:
  Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
  Output: [5]

Constraints:
  - 1 <= m, n <= 100

Hint: Use hash map — count element occurrences across rows (count per row, not per cell).
Pattern: Hashing
"""


def common_all_rows(mat: list[list[int]]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert common_all_rows([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]) == [5]
    assert common_all_rows([[1,2],[2,3]]) == [2]
    print("All tests passed!")
