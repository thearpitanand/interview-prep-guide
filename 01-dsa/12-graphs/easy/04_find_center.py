"""
Find Center of Star Graph (LC 1791)

Day: 33 | Difficulty: Easy | Pattern: Graph Property

There is an undirected star graph consisting of n nodes labeled from 1 to n.
A star graph is a graph where there is one center node and exactly n-1 edges
that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi]
indicates that there is an edge between nodes ui and vi. Return the center
of the given star graph.

Examples:
    Input: edges=[[1,2],[2,3],[4,2]]
    Output: 2
    Explanation: Node 2 is connected to every other node, so 2 is the center.

    Input: edges=[[1,2],[5,1],[1,3],[1,4]]
    Output: 1

Constraints:
    - 3 <= n <= 10^5
    - edges.length == n - 1
    - edges[i].length == 2
    - 1 <= ui, vi <= n
    - ui != vi
    - The given edges represent a valid star graph

Hint:
    The center node must appear in EVERY edge. So just check the first two
    edges -- the center is the common node between them. No need to process
    all edges!

Pattern: Graph property - the center of a star graph appears in every edge.
Just find the node common to the first two edges.
"""

from typing import List


def find_center(edges: List[List[int]]) -> int:
    """Find the center of a star graph. O(1) time."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Center is 2
    result = find_center([[1, 2], [2, 3], [4, 2]])
    assert result == 2, f"Expected 2, got {result}"

    # Test 2: Center is 1
    result = find_center([[1, 2], [5, 1], [1, 3], [1, 4]])
    assert result == 1, f"Expected 1, got {result}"

    # Test 3: Minimum star graph (3 nodes)
    result = find_center([[1, 2], [2, 3]])
    assert result == 2, f"Expected 2, got {result}"

    # Test 4: Center appears as second element in first edge
    result = find_center([[3, 1], [2, 1], [1, 4]])
    assert result == 1, f"Expected 1, got {result}"

    print("All tests passed!")
