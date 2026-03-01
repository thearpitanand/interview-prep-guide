"""
Number of Islands (LC 200)

Day: 33 | Difficulty: Medium | Pattern: DFS/BFS on Grid

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's
(water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are
surrounded by water.

Examples:
    Input: grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    Output: 1

    Input: grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    Output: 3

Constraints:
    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 300
    - grid[i][j] is '0' or '1'

Hint:
    Iterate through each cell. When you find a '1' that hasn't been visited,
    increment your island count and use DFS/BFS to mark all connected '1's
    as visited (sink the island).

Pattern: Connected components on a grid - each island is a connected component
of '1's. Count how many times you start a new DFS/BFS.
"""

from collections import deque
from typing import List


def num_islands_dfs(grid: List[List[str]]) -> int:
    """DFS approach - sink each island by marking visited cells."""
    pass


def num_islands_bfs(grid: List[List[str]]) -> int:
    """BFS approach - use queue for level-by-level exploration."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Single large island
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    result = num_islands_dfs(grid)
    assert result == 1, f"Expected 1, got {result}"

    # Test 2: Three islands
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    result = num_islands_dfs(grid)
    assert result == 3, f"Expected 3, got {result}"

    # Test 3: All water
    grid = [["0", "0"], ["0", "0"]]
    result = num_islands_dfs(grid)
    assert result == 0, f"Expected 0, got {result}"

    # Test 4: All land (one island)
    grid = [["1", "1"], ["1", "1"]]
    result = num_islands_dfs(grid)
    assert result == 1, f"Expected 1, got {result}"

    # Test 5: BFS approach
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    result = num_islands_bfs(grid)
    assert result == 3, f"Expected 3, got {result}"

    # Test 6: Single cell island
    grid = [["1"]]
    result = num_islands_dfs(grid)
    assert result == 1, f"Expected 1, got {result}"

    print("All tests passed!")
