"""
Problem: Number of Islands (LC 200) | Smart-DSA Day 36 | Medium
Pattern: Graph DFS/BFS on Grid
Time target: 25 minutes

Given an m x n 2D binary grid where '1' represents land and '0' represents
water, return the number of islands. An island is surrounded by water and
formed by connecting adjacent lands horizontally or vertically.

Example 1:
  Input: grid = [["1","1","1","1","0"],
                 ["1","1","0","1","0"],
                 ["1","1","0","0","0"],
                 ["0","0","0","0","0"]]
  Output: 1

Example 2:
  Input: grid = [["1","1","0","0","0"],
                 ["1","1","0","0","0"],
                 ["0","0","1","0","0"],
                 ["0","0","0","1","1"]]
  Output: 3

Constraints:
  - m == grid.length, n == grid[i].length
  - 1 <= m, n <= 300
  - grid[i][j] is '0' or '1'.

Hint (⚠ read only after time budget is blown):
  DFS from every unvisited '1'. Sink the island by setting visited cells to
  '0'. Increment the island count each time you start a new DFS.
"""


def num_islands(grid: list[list[str]]) -> int:
    pass


if __name__ == "__main__":
    grid1 = [["1","1","1","1","0"],
             ["1","1","0","1","0"],
             ["1","1","0","0","0"],
             ["0","0","0","0","0"]]
    assert num_islands(grid1) == 1

    grid2 = [["1","1","0","0","0"],
             ["1","1","0","0","0"],
             ["0","0","1","0","0"],
             ["0","0","0","1","1"]]
    assert num_islands(grid2) == 3

    grid3 = [["1"]]
    assert num_islands(grid3) == 1

    grid4 = [["0"]]
    assert num_islands(grid4) == 0
    print("All tests passed!")
