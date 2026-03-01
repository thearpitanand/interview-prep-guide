"""
Problem: Row with Maximum 1s (GFG) | Optional | Easy
Topic: Matrix

Given a boolean matrix where each row is sorted, find the row with maximum 1s.

Example 1:
  Input: mat = [[0,0,0,1],[0,1,1,1],[1,1,1,1],[0,0,0,0]]
  Output: 2  # row index 2 has max 1s (four 1s)

Constraints:
  - Rows are sorted (0s before 1s)

Hint: Start from top-right corner. Move left while 1, down otherwise.
Pattern: Staircase Search
"""


def row_max_ones(mat: list[list[int]]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert row_max_ones([[0,0,0,1],[0,1,1,1],[1,1,1,1],[0,0,0,0]]) == 2
    assert row_max_ones([[0,0],[0,1]]) == 1
    print("All tests passed!")
