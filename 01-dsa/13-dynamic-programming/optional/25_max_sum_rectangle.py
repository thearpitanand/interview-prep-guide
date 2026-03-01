"""
Problem: Max Sum Rectangle in 2D Matrix (GFG) | Optional | Hard
Topic: Dynamic Programming

Find the rectangle (submatrix) with maximum sum in a 2D matrix.

Example 1:
  Input: mat = [[1,2,-1,-4,-20],[-8,-3,4,2,1],[3,8,10,1,3],[-4,-1,1,7,-6]]
  Output: 29  # submatrix rows 1-3, cols 1-3

Constraints:
  - 1 <= R, C <= 100

Hint: Fix left and right columns, compress to 1D, apply Kadane's.
Pattern: DP (Kadane's 2D)
"""


def max_sum_rectangle(mat: list[list[int]]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    mat = [[1,2,-1,-4,-20],[-8,-3,4,2,1],[3,8,10,1,3],[-4,-1,1,7,-6]]
    assert max_sum_rectangle(mat) == 29
    print("All tests passed!")
