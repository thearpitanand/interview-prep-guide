"""
Problem: Longest Route in Matrix with Hurdles (GFG) | Optional | Hard
Topic: Backtracking

Find the longest path in a matrix from source to destination without visiting
any cell with a hurdle (0).

Example 1:
  Input: mat = [[1,1,1],[1,0,1],[1,1,1]], src = (0,0), dest = (2,2)
  Output: 8

Constraints:
  - 1 <= R, C <= 10

Hint: DFS/backtracking — try all paths, track visited, return max length.
Pattern: Backtracking / DFS
"""


def longest_route(mat: list[list[int]], src: tuple, dest: tuple) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    mat = [[1,1,1],[1,0,1],[1,1,1]]
    assert longest_route(mat, (0,0), (2,2)) == 8
    print("All tests passed!")
