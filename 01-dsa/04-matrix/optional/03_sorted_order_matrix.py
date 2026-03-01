"""
Problem: Print Elements in Sorted Order (GFG) | Optional | Medium
Topic: Matrix

Given an n x n matrix where each row and column is sorted, print all elements in sorted order.

Example 1:
  Input: mat = [[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
  Output: [10,15,20,25,27,29,30,32,33,35,37,39,40,45,48,50]

Constraints:
  - 1 <= n <= 100

Hint: Use min-heap with (value, row, col), extract min and push next from same row.
Pattern: Min-Heap / K-Way Merge
"""


def sorted_matrix(mat: list[list[int]]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert sorted_matrix([[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]) == [10,15,20,25,27,29,30,32,33,35,37,39,40,45,48,50]
    print("All tests passed!")
