"""
Flood Fill (LC 733)

Day: 33 | Difficulty: Easy | Pattern: BFS/DFS on Grid

An image is represented by an m x n integer grid where image[i][j] represents
the pixel value. You are given three integers sr, sc, and color. Perform a
flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill: consider the starting pixel, plus any pixels connected
4-directionally to it that have the same color, plus any pixels connected to
those, and so on. Replace the color of all these pixels with color.

Examples:
    Input: image=[[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: From center pixel (1,1), flood fill all connected 1s with 2.

    Input: image=[[0,0,0],[0,0,0]], sr=0, sc=0, color=0
    Output: [[0,0,0],[0,0,0]]
    Explanation: Starting pixel is already the target color, no change needed.

Constraints:
    - m == image.length
    - n == image[i].length
    - 1 <= m, n <= 50
    - 0 <= image[i][j], color < 2^16
    - 0 <= sr < m
    - 0 <= sc < n

Hint:
    Start from (sr, sc). Use DFS/BFS to visit all 4-directionally connected
    pixels with the same original color. Change each visited pixel to the new
    color. Handle the edge case where the original color equals the new color.

Pattern: Graph traversal on a grid - treat each cell as a node with edges to
4 adjacent cells. Flood fill is essentially finding a connected component.
"""

from collections import deque
from typing import List


def flood_fill_dfs(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    """DFS approach - recursive flood fill."""
    pass


def flood_fill_bfs(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    """BFS approach - iterative flood fill using queue."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Standard flood fill
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    result = flood_fill_dfs(image, 1, 1, 2)
    assert result == [[2, 2, 2], [2, 2, 0], [2, 0, 1]], f"Expected [[2,2,2],[2,2,0],[2,0,1]], got {result}"

    # Test 2: No change needed (same color)
    image = [[0, 0, 0], [0, 0, 0]]
    result = flood_fill_dfs(image, 0, 0, 0)
    assert result == [[0, 0, 0], [0, 0, 0]], f"Expected [[0,0,0],[0,0,0]], got {result}"

    # Test 3: Single pixel
    image = [[1]]
    result = flood_fill_dfs(image, 0, 0, 2)
    assert result == [[2]], f"Expected [[2]], got {result}"

    # Test 4: BFS approach
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    result = flood_fill_bfs(image, 1, 1, 2)
    assert result == [[2, 2, 2], [2, 2, 0], [2, 0, 1]], f"Expected [[2,2,2],[2,2,0],[2,0,1]], got {result}"

    # Test 5: Corner start
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    result = flood_fill_dfs(image, 0, 0, 3)
    assert result == [[3, 3, 3], [3, 3, 0], [3, 0, 1]], f"Expected [[3,3,3],[3,3,0],[3,0,1]], got {result}"

    print("All tests passed!")
