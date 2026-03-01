"""
Problem: Flood Fill
LeetCode: 733 - https://leetcode.com/problems/flood-fill/
Day: 15
Difficulty: Easy
Topic: DFS/BFS

Description:
    An image is represented by an m x n integer grid where image[i][j]
    represents the pixel value. You are given three integers sr, sc,
    and color. Perform a flood fill starting from pixel image[sr][sc].

    To perform a flood fill, consider the starting pixel, plus any
    pixels connected 4-directionally to the starting pixel of the same
    color, plus any pixels connected 4-directionally to those pixels
    (also with the same color), and so on. Replace the color of all of
    the aforementioned pixels with color.

Examples:
    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: From the center pixel (1,1) with value 1, all connected
    pixels with value 1 are changed to 2. The bottom-right 1 is not
    connected (diagonals don't count).

    Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
    Output: [[0,0,0],[0,0,0]]
    Explanation: Starting pixel already has the target color, no change.

Constraints:
    - m == image.length
    - n == image[i].length
    - 1 <= m, n <= 50
    - 0 <= image[i][j], color < 2^16
    - 0 <= sr < m
    - 0 <= sc < n

Hint:
    Use DFS or BFS. Start at (sr, sc), record the original color.
    If original color == new color, return immediately (avoid infinite loop).
    Otherwise, change pixel to new color and recurse on 4 neighbors.

Pattern: DFS/BFS on Grid
    - Base case: out of bounds OR pixel color != original color
    - Action: change color, recurse in 4 directions
    - Edge case: if original color == new color, return as-is
"""

from typing import List


def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    pass


# ---------- Test Cases ----------
if __name__ == "__main__":
    # Test 1: Standard flood fill
    assert flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ]

    # Test 2: No change needed (same color)
    assert flood_fill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [
        [0, 0, 0],
        [0, 0, 0],
    ]

    # Test 3: Single pixel
    assert flood_fill([[1]], 0, 0, 2) == [[2]]

    # Test 4: Fill only connected region
    assert flood_fill([[0, 0, 0], [0, 1, 1]], 1, 1, 2) == [
        [0, 0, 0],
        [0, 2, 2],
    ]

    # Test 5: Corner start
    assert flood_fill([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0, 0, 3) == [
        [3, 3, 3],
        [3, 3, 3],
        [3, 3, 3],
    ]

    print("All test cases passed!")
