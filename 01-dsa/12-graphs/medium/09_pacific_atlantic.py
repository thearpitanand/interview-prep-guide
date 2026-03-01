"""
Pacific Atlantic Water Flow (LC 417)

Day: 35 | Difficulty: Medium | Pattern: Multi-source DFS/BFS

There is an m x n rectangular island that borders both the Pacific and Atlantic
oceans. The Pacific Ocean touches the island's left and top edges, and the
Atlantic Ocean touches the island's right and bottom edges.

The island receives rain. Water can flow to neighboring cells (up, down, left,
right) if the neighboring cell's height is less than or equal to the current
cell's height. Water can also flow into the ocean.

Return a list of grid coordinates where water can flow to BOTH the Pacific
and Atlantic oceans.

Examples:
    Input: heights = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

    Input: heights = [[1]]
    Output: [[0,0]]

Constraints:
    - m == heights.length
    - n == heights[r].length
    - 1 <= m, n <= 200
    - 0 <= heights[r][c] <= 10^5

Hint:
    Instead of flowing water DOWN from each cell, flow water UP from the
    oceans. Run DFS/BFS from all Pacific border cells and mark reachable cells.
    Do the same from all Atlantic border cells. The answer is the intersection
    of both sets.

Pattern: Multi-source DFS/BFS in reverse - start from the ocean boundaries
and flow uphill, then find cells reachable from both oceans.
"""

from collections import deque
from typing import List


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    """Find cells where water can flow to both oceans using DFS."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Standard case
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    result = pacific_atlantic(heights)
    expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    result_set = set(map(tuple, result))
    expected_set = set(map(tuple, expected))
    assert result_set == expected_set, f"Expected {expected}, got {result}"

    # Test 2: Single cell
    result = pacific_atlantic([[1]])
    assert result == [[0, 0]], f"Expected [[0, 0]], got {result}"

    # Test 3: Single row
    result = pacific_atlantic([[1, 2, 3]])
    result_set = set(map(tuple, result))
    expected_set = {(0, 0), (0, 1), (0, 2)}
    assert result_set == expected_set, f"Expected {expected_set}, got {result_set}"

    # Test 4: All same height
    result = pacific_atlantic([[1, 1], [1, 1]])
    result_set = set(map(tuple, result))
    expected_set = {(0, 0), (0, 1), (1, 0), (1, 1)}
    assert result_set == expected_set, f"Expected {expected_set}, got {result_set}"

    print("All tests passed!")
