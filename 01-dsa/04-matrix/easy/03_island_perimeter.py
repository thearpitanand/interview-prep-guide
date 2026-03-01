"""
Problem: Island Perimeter
LeetCode: 463 - https://leetcode.com/problems/island-perimeter/
Day: 15
Difficulty: Easy
Topic: Grid Traversal

Description:
    You are given row x col grid where grid[i][j] = 1 represents land
    and grid[i][j] = 0 represents water. Determine the perimeter of
    the island. There is exactly one island (one or more connected
    land cells). The island doesn't have "lakes" (water inside that
    isn't connected to water outside).

Examples:
    Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    Output: 16

    Input: grid = [[1]]
    Output: 4

    Input: grid = [[1,0]]
    Output: 4

Constraints:
    - row == grid.length
    - col == grid[i].length
    - 1 <= row, col <= 100
    - grid[i][j] is 0 or 1
    - There is exactly one island

Hint:
    Each land cell contributes 4 to the perimeter. For each neighbor
    that is also land, subtract 1 (shared edge). Alternatively, for
    each land cell count how many of its 4 sides face water or the
    grid boundary.

Pattern: Grid Traversal
    - For each land cell, check all 4 neighbors
    - If neighbor is water or out of bounds, that edge contributes
      to perimeter
    - No DFS needed -- simple iteration works since we just need
      the total perimeter count
"""

from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    pass


# ---------- Test Cases ----------
if __name__ == "__main__":
    # Test 1: Standard island
    assert island_perimeter([
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
    ]) == 16

    # Test 2: Single cell
    assert island_perimeter([[1]]) == 4

    # Test 3: Single cell with water neighbor
    assert island_perimeter([[1, 0]]) == 4

    # Test 4: Horizontal line
    assert island_perimeter([[1, 1, 1]]) == 8

    # Test 5: 2x2 square
    assert island_perimeter([[1, 1], [1, 1]]) == 8

    print("All test cases passed!")
