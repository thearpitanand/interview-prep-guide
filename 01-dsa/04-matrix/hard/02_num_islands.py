"""
Problem: Number of Islands
LeetCode: 200 - https://leetcode.com/problems/number-of-islands/
Day: 16
Difficulty: Hard
Topic: DFS/BFS

Description:
    Given an m x n 2D binary grid which represents a map of '1's (land)
    and '0's (water), return the number of islands. An island is
    surrounded by water and is formed by connecting adjacent lands
    horizontally or vertically. You may assume all four edges of the
    grid are surrounded by water.

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
    Iterate through every cell. When you find a '1', increment count
    and run DFS/BFS to mark all connected '1's as visited (set to '0').
    Each DFS/BFS call handles one complete island.

Pattern: DFS/BFS on Grid (Connected Components)
    - Each unvisited '1' starts a new island
    - DFS/BFS from that cell marks all connected land as visited
    - Mark visited by changing '1' to '0' (in-place) or use a set
    - Count number of times you initiate a DFS/BFS
    - Time: O(m * n), Space: O(m * n) worst case for recursion stack
    - BFS alternative avoids recursion depth issues on large grids
"""

from typing import List


def num_islands(grid: List[List[str]]) -> int:
    pass


# ---------- Test Cases ----------
if __name__ == "__main__":
    # Test 1: Single large island
    assert num_islands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]) == 1

    # Test 2: Three separate islands
    assert num_islands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]) == 3

    # Test 3: No islands
    assert num_islands([
        ["0", "0", "0"],
        ["0", "0", "0"],
    ]) == 0

    # Test 4: All land
    assert num_islands([
        ["1", "1"],
        ["1", "1"],
    ]) == 1

    # Test 5: Diagonal islands (not connected)
    assert num_islands([
        ["1", "0"],
        ["0", "1"],
    ]) == 2

    # Test 6: Single cell
    assert num_islands([["1"]]) == 1

    print("All test cases passed!")
