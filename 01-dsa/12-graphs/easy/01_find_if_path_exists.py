"""
Find if Path Exists in Graph (LC 1971)

Day: 33 | Difficulty: Easy | Pattern: BFS/DFS

There is a bi-directional graph with n vertices, where each vertex is labeled
from 0 to n - 1. The edges in the graph are represented as a 2D integer array
edges where each edges[i] = [ui, vi] denotes a bi-directional edge between
vertex ui and vertex vi. Determine if there is a valid path from source to
destination.

Examples:
    Input: n=3, edges=[[0,1],[1,2],[2,0]], source=0, destination=2
    Output: True
    Explanation: 0 -> 1 -> 2 or 0 -> 2

    Input: n=6, edges=[[0,1],[0,2],[3,5],[5,4],[4,3]], source=0, destination=5
    Output: False
    Explanation: No path between 0 and 5

Constraints:
    - 1 <= n <= 2 * 10^5
    - 0 <= edges.length <= 2 * 10^5
    - edges[i].length == 2
    - 0 <= ui, vi <= n - 1
    - ui != vi
    - 0 <= source, destination <= n - 1
    - No duplicate edges, no self-loops

Hint:
    Build an adjacency list, then use BFS or DFS from source.
    If you reach destination at any point, return True.

Pattern: Graph traversal - BFS/DFS on an adjacency list to check connectivity.
"""

from collections import defaultdict, deque
from typing import List


def valid_path_bfs(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """BFS approach - use queue to explore level by level."""
    pass


def valid_path_dfs(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """DFS approach - use recursion or stack to go deep first."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Path exists (triangle)
    result = valid_path_bfs(3, [[0, 1], [1, 2], [2, 0]], 0, 2)
    assert result == True, f"Expected True, got {result}"

    # Test 2: No path (disconnected graph)
    result = valid_path_bfs(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5)
    assert result == False, f"Expected False, got {result}"

    # Test 3: Source equals destination
    result = valid_path_bfs(1, [], 0, 0)
    assert result == True, f"Expected True, got {result}"

    # Test 4: DFS approach
    result = valid_path_dfs(3, [[0, 1], [1, 2], [2, 0]], 0, 2)
    assert result == True, f"Expected True, got {result}"

    # Test 5: DFS - no path
    result = valid_path_dfs(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5)
    assert result == False, f"Expected False, got {result}"

    # Test 6: Linear path
    result = valid_path_bfs(4, [[0, 1], [1, 2], [2, 3]], 0, 3)
    assert result == True, f"Expected True, got {result}"

    print("All tests passed!")
