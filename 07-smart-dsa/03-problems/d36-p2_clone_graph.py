"""
Problem: Clone Graph (LC 133) | Smart-DSA Day 36 | Medium
Pattern: Graph DFS/BFS
Time target: 30 minutes

Given a reference to a node in a connected undirected graph, return a deep
copy (clone) of the graph. Each node contains a value (int) and a list of
its neighbors.

Example 1:
  Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
  (Node 1 connects to 2,4; Node 2 connects to 1,3; etc.)
  Output: A deep copy of the same graph structure.

Example 2:
  Input: adjList = [[]]
  Output: Node with val=1, no neighbors.

Constraints:
  - The number of nodes is in the range [0, 100].
  - 1 <= Node.val <= 100
  - Node.val is unique for each node.
  - No repeated edges and no self-loops.

Hint (⚠ read only after time budget is blown):
  Use a hash map {original: clone}. DFS/BFS the graph. For each node, if not
  yet in the map, create a clone. Recursively clone each neighbor and append
  to the clone's neighbor list.
"""
from typing import Optional


class Node:
    def __init__(self, val: int = 0, neighbors: "Optional[list[Node]]" = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    pass


# Helper: build graph from adjacency list (1-indexed)
def build_graph(adj: list[list[int]]) -> Optional[Node]:
    if not adj:
        return None
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, neighbors in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0]


def graph_to_adj(node: Optional[Node]) -> list[list[int]]:
    """Convert cloned graph back to sorted adjacency list for assertion."""
    if not node:
        return []
    visited: dict[int, Node] = {}
    stack = [node]
    while stack:
        cur = stack.pop()
        if cur.val in visited:
            continue
        visited[cur.val] = cur
        for nb in cur.neighbors:
            stack.append(nb)
    result = []
    for val in sorted(visited):
        result.append(sorted(nb.val for nb in visited[val].neighbors))
    return result


if __name__ == "__main__":
    # Test 1: standard graph
    g1 = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
    cloned1 = clone_graph(g1)
    assert cloned1 is not g1
    assert graph_to_adj(cloned1) == [[2, 4], [1, 3], [2, 4], [1, 3]]

    # Test 2: single node no neighbors
    g2 = build_graph([[]])
    cloned2 = clone_graph(g2)
    assert cloned2.val == 1
    assert cloned2.neighbors == []

    # Test 3: None input
    assert clone_graph(None) is None
    print("All tests passed!")
