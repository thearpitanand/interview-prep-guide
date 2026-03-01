"""
Problem: Minimum Steps by Knight (GFG) | Optional | Medium
Topic: Graphs

Given an N×N chessboard, find minimum steps for a knight to reach from
source to target position.

Example 1:
  Input: n = 6, src = (4,5), target = (1,1)
  Output: 3

Constraints:
  - 1 <= N <= 1000

Hint: BFS from source. Knight has 8 possible moves.
Pattern: BFS
"""
from collections import deque


def min_steps_knight(n: int, src: tuple[int, int], target: tuple[int, int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert min_steps_knight(6, (4, 5), (1, 1)) == 3
    assert min_steps_knight(8, (0, 0), (0, 0)) == 0
    print("All tests passed!")
