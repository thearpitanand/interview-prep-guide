"""
Critical Connections in a Network (LC 1192)

Day: 35 | Difficulty: Hard | Pattern: Tarjan's Bridge Finding Algorithm

There are n servers numbered from 0 to n - 1 connected by undirected
server-to-server connections forming a network. A critical connection is a
connection that, if removed, will make some servers unable to reach some other
servers. Find all critical connections.

A critical connection is also known as a "bridge" in graph theory.

Examples:
    Input: n=4, connections=[[0,1],[1,2],[2,0],[1,3]]
    Output: [[1,3]]
    Explanation: Removing [1,3] disconnects node 3 from the rest.
                 Removing any other edge still keeps the graph connected.

    Input: n=2, connections=[[0,1]]
    Output: [[0,1]]
    Explanation: The only edge is a bridge.

Constraints:
    - 2 <= n <= 10^5
    - n - 1 <= connections.length <= 10^5
    - 0 <= ai, bi <= n - 1
    - ai != bi
    - No repeated connections

Hint:
    Use Tarjan's algorithm. Maintain discovery time (disc) and lowest
    reachable time (low) for each node. An edge (u, v) is a bridge if
    low[v] > disc[u] -- meaning v cannot reach any ancestor of u through
    a back edge, so removing (u, v) disconnects v's subtree.

Pattern: Tarjan's Bridge Finding - DFS-based algorithm that tracks discovery
times and lowest reachable ancestors to identify bridges (critical edges).
"""

from collections import defaultdict
from typing import List


def critical_connections(n: int, connections: List[List[int]]) -> List[List[int]]:
    """Find all bridges using Tarjan's algorithm."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: One bridge
    result = critical_connections(4, [[0, 1], [1, 2], [2, 0], [1, 3]])
    result_set = set(tuple(sorted(e)) for e in result)
    assert result_set == {(1, 3)}, f"Expected {{(1, 3)}}, got {result_set}"

    # Test 2: Single edge is a bridge
    result = critical_connections(2, [[0, 1]])
    result_set = set(tuple(sorted(e)) for e in result)
    assert result_set == {(0, 1)}, f"Expected {{(0, 1)}}, got {result_set}"

    # Test 3: No bridges (complete cycle)
    result = critical_connections(3, [[0, 1], [1, 2], [2, 0]])
    assert result == [], f"Expected [], got {result}"

    # Test 4: Multiple bridges
    result = critical_connections(6, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]])
    result_set = set(tuple(sorted(e)) for e in result)
    assert result_set == {(1, 3)}, f"Expected {{(1, 3)}}, got {result_set}"

    # Test 5: Linear graph (all edges are bridges)
    result = critical_connections(4, [[0, 1], [1, 2], [2, 3]])
    result_set = set(tuple(sorted(e)) for e in result)
    expected = {(0, 1), (1, 2), (2, 3)}
    assert result_set == expected, f"Expected {expected}, got {result_set}"

    print("All tests passed!")
