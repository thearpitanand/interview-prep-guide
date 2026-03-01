"""
Problem: Snake and Ladders (LC 909) | Optional | Medium
Topic: Graphs

Given a Snakes and Ladders board, find the minimum number of dice rolls
to reach the last square from square 1.

Example 1:
  Input: board (with snakes and ladders positions)
  Output: minimum rolls

Constraints:
  - Board is N×N

Hint: BFS from position 1. For each position, try all 6 dice outcomes.
Pattern: BFS
"""


def snakes_ladders(board: list[list[int]]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    result = snakes_ladders(board)
    assert result == 4
    print("All tests passed!")
