"""
Problem: Min Edges to Reverse for Path (GFG) | Optional | Hard
Topic: Graphs

Given a directed graph, find the minimum number of edges to reverse to make
a path from source to destination.

Example 1:
  Input: V = 7, edges = [[0,1],[2,1],[2,3],[5,4],[5,6],[3,6]], src = 0, dest = 6
  Output: 2

Constraints:
  - 1 <= V <= 10^5

Hint: Create modified graph: original edge has weight 0, reversed edge has weight 1. Run 0-1 BFS.
Pattern: 0-1 BFS
"""
from collections import deque


def min_edges_reverse(V: int, edges: list[list[int]], src: int, dest: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert min_edges_reverse(7, [[0,1],[2,1],[2,3],[5,4],[5,6],[3,6]], 0, 6) == 2
    print("All tests passed!")
