"""
Problem: BFS Implementation from Scratch (GFG) | Optional | Easy
Topic: Graphs

Implement Breadth-First Search traversal from a given source vertex.

Example 1:
  Input: V = 5, edges = [[0,1],[0,2],[1,3],[1,4]], src = 0
  Output: [0, 1, 2, 3, 4]

Constraints:
  - 1 <= V <= 10^5

Hint: Use a queue. Process level by level.
Pattern: BFS
"""
from collections import deque


def bfs(V: int, edges: list[list[int]], src: int) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert bfs(5, [[0,1],[0,2],[1,3],[1,4]], 0) == [0, 1, 2, 3, 4]
    assert bfs(3, [[0,1],[1,2]], 0) == [0, 1, 2]
    print("All tests passed!")
