"""
Is Graph Bipartite? (LC 785)

Day: 35 | Difficulty: Medium | Pattern: BFS/DFS Coloring

There is an undirected graph with n nodes where each node is labeled between
0 and n - 1. You are given a 2D array graph where graph[u] is an array of
nodes that node u is adjacent to.

A graph is bipartite if the nodes can be partitioned into two independent sets
A and B such that every edge connects a node in A to a node in B.

Return true if and only if it is bipartite.

Examples:
    Input: graph=[[1,2,3],[0,2],[0,1,3],[0,2]]
    Output: False
    Explanation: No way to partition nodes into two sets where every edge
                 crosses between sets.

    Input: graph=[[1,3],[0,2],[1,3],[0,2]]
    Output: True
    Explanation: Set A = {0, 2}, Set B = {1, 3}. All edges cross sets.

Constraints:
    - graph.length == n
    - 1 <= n <= 100
    - 0 <= graph[u].length < n
    - 0 <= graph[u][i] <= n - 1
    - graph[u] does not contain u (no self-loops)
    - All values in graph[u] are unique
    - If graph[u] contains v, then graph[v] contains u

Hint:
    Try to 2-color the graph using BFS/DFS. Start with any uncolored node,
    color it with color 0. Color all its neighbors with color 1, their
    neighbors with color 0, etc. If you ever need to color a node that's
    already colored with the wrong color, it's not bipartite.

Pattern: Graph 2-coloring using BFS/DFS - assign alternating colors and check
for conflicts. Must handle disconnected components.
"""

from collections import deque
from typing import List


def is_bipartite_bfs(graph: List[List[int]]) -> bool:
    """BFS 2-coloring approach."""
    pass


def is_bipartite_dfs(graph: List[List[int]]) -> bool:
    """DFS 2-coloring approach."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Not bipartite (odd cycle)
    result = is_bipartite_bfs([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
    assert result == False, f"Expected False, got {result}"

    # Test 2: Bipartite (even cycle)
    result = is_bipartite_bfs([[1, 3], [0, 2], [1, 3], [0, 2]])
    assert result == True, f"Expected True, got {result}"

    # Test 3: Single node (trivially bipartite)
    result = is_bipartite_bfs([[]])
    assert result == True, f"Expected True, got {result}"

    # Test 4: Two connected nodes (bipartite)
    result = is_bipartite_bfs([[1], [0]])
    assert result == True, f"Expected True, got {result}"

    # Test 5: DFS approach - not bipartite
    result = is_bipartite_dfs([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
    assert result == False, f"Expected False, got {result}"

    # Test 6: DFS approach - bipartite
    result = is_bipartite_dfs([[1, 3], [0, 2], [1, 3], [0, 2]])
    assert result == True, f"Expected True, got {result}"

    # Test 7: Disconnected bipartite graph
    result = is_bipartite_bfs([[1], [0], [3], [2]])
    assert result == True, f"Expected True, got {result}"

    print("All tests passed!")
