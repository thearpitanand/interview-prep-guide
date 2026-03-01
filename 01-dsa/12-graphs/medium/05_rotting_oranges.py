"""
Rotting Oranges (LC 994)

Day: 34 | Difficulty: Medium | Pattern: Multi-source BFS

You are given an m x n grid where each cell can have one of three values:
  0 = empty cell
  1 = fresh orange
  2 = rotten orange

Every minute, any fresh orange that is 4-directionally adjacent to a rotten
orange becomes rotten. Return the minimum number of minutes that must elapse
until no cell has a fresh orange. If impossible, return -1.

Examples:
    Input: grid=[[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

    Input: grid=[[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in bottom-left corner is never reached.

    Input: grid=[[0,2]]
    Output: 0
    Explanation: No fresh oranges at minute 0.

Constraints:
    - m == grid.length
    - n == grid[i].length
    - 1 <= m, n <= 10
    - grid[i][j] is 0, 1, or 2

Hint:
    Start BFS from ALL rotten oranges simultaneously (multi-source BFS).
    Add all initial rotten oranges to the queue, then process level by level.
    Each level = 1 minute. Count fresh oranges at start; if any remain after
    BFS, return -1.

Pattern: Multi-source BFS - start from multiple sources simultaneously.
The BFS level represents time elapsed.
"""

from collections import deque
from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    """Multi-source BFS from all initially rotten oranges."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Standard case
    result = oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
    assert result == 4, f"Expected 4, got {result}"

    # Test 2: Impossible - isolated fresh orange
    result = oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
    assert result == -1, f"Expected -1, got {result}"

    # Test 3: No fresh oranges
    result = oranges_rotting([[0, 2]])
    assert result == 0, f"Expected 0, got {result}"

    # Test 4: All fresh, no rotten
    result = oranges_rotting([[1, 1], [1, 1]])
    assert result == -1, f"Expected -1, got {result}"

    # Test 5: All rotten already
    result = oranges_rotting([[2, 2], [2, 2]])
    assert result == 0, f"Expected 0, got {result}"

    # Test 6: Single rotten orange
    result = oranges_rotting([[2]])
    assert result == 0, f"Expected 0, got {result}"

    # Test 7: Empty grid (no oranges)
    result = oranges_rotting([[0]])
    assert result == 0, f"Expected 0, got {result}"

    print("All tests passed!")
