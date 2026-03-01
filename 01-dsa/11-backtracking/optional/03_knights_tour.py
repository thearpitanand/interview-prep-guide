"""
Problem: Knight's Tour Problem (GFG) | Optional | Hard
Topic: Backtracking

Given an N×N chessboard, find a path for a knight that visits every square exactly once.

Example 1:
  Input: n = 5
  Output: a valid knight's tour (5x5 matrix with move numbers)

Constraints:
  - 5 <= n <= 8

Hint: Backtracking with Warnsdorff's heuristic (go to square with fewest onward moves).
Pattern: Backtracking
"""


def knights_tour(n: int) -> list[list[int]]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = knights_tour(5)
    if result:
        assert len(result) == 5
        assert all(len(row) == 5 for row in result)
        # Check all values 0 to 24 appear
        flat = [result[i][j] for i in range(5) for j in range(5)]
        assert sorted(flat) == list(range(25))
    print("All tests passed!")
