"""
Problem: Pacific Atlantic Water Flow (LC 417) | Smart-DSA Day 37 | Medium
Pattern: Multi-source BFS / DFS on Grid
Time target: 35 minutes

There is an m x n rectangular island bordered by the Pacific Ocean on the
top and left edges, and the Atlantic Ocean on the bottom and right edges.
Given an m x n matrix heights where heights[r][c] is the height of cell
(r, c), return all cells from which water can flow to both the Pacific and
Atlantic Oceans. Water flows from higher (or equal) height to adjacent cells.

Example 1:
  Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
  Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Constraints:
  - m == heights.length, n == heights[0].length
  - 1 <= m, n <= 200
  - 0 <= heights[r][c] <= 10^5

Hint (⚠ read only after time budget is blown):
  Reverse the direction: BFS uphill from Pacific border cells, mark reachable.
  BFS uphill from Atlantic border cells, mark reachable. The answer is the
  intersection of both sets.
"""
from collections import deque


def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    pass


if __name__ == "__main__":
    result1 = pacific_atlantic(
        [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    )
    assert sorted(result1) == sorted([[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])

    result2 = pacific_atlantic([[1]])
    assert result2 == [[0, 0]]

    result3 = pacific_atlantic([[1, 1], [1, 1], [1, 1]])
    assert len(result3) == 6
    print("All tests passed!")
