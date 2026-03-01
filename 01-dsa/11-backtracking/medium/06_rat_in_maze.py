"""
Problem: Rat in a Maze (GFG) | Day 31 | Medium
Topic: Backtracking

Given an N x N maze where 1 = open, 0 = blocked. A rat starts at (0,0) and
must reach (N-1, N-1). Find all possible paths. Moves: D(down), L(left),
R(right), U(up).

Example 1:
  Input: maze = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
  Output: ["DDRDRR", "DRDDRR"]

Constraints:
  - 2 <= N <= 5
  - maze[0][0] = maze[N-1][N-1] = 1

Hint: Backtrack in all 4 directions (sorted: D, L, R, U for lexicographic order).
Pattern: Backtracking
"""


def rat_in_maze(maze: list[list[int]]) -> list[str]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    maze = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
    result = rat_in_maze(maze)
    assert "DDRDRR" in result
    assert "DRDDRR" in result
    assert rat_in_maze([[1,0],[0,1]]) == []
    print("All tests passed!")
