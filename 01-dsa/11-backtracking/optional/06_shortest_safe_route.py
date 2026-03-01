"""
Problem: Shortest Safe Route with Landmines (GFG) | Optional | Hard
Topic: Backtracking

Given a matrix with landmines (0) and safe cells (1), find the shortest safe
route from any cell in the first column to any cell in the last column.
Adjacent cells to landmines are also unsafe.

Example 1:
  Input: mat = [[1,1,1,1,1],[1,0,1,0,1],[1,1,1,1,1]]
  Output: shortest path length

Constraints:
  - 1 <= R, C <= 12

Hint: Mark cells adjacent to mines as unsafe. BFS from all first-column safe cells.
Pattern: BFS / Backtracking
"""


def shortest_safe_route(mat: list[list[int]]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    mat = [[1,1,1,1,1],[1,0,1,0,1],[1,1,1,1,1]]
    result = shortest_safe_route(mat)
    assert result >= 0  # -1 if no path
    print("All tests passed!")
