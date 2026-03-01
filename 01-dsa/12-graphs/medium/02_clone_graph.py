"""
Clone Graph (LC 133)

Day: 33 | Difficulty: Medium | Pattern: BFS/DFS + HashMap

Given a reference of a node in a connected undirected graph, return a deep copy
(clone) of the graph. Each node in the graph contains a value (int) and a list
of its neighbors.

Examples:
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: Node 1 connects to 2,4. Node 2 connects to 1,3. etc.
                 Return a deep copy where no node is shared with the original.

    Input: adjList = [[]]
    Output: [[]]
    Explanation: Single node with no neighbors.

    Input: adjList = []
    Output: []
    Explanation: Empty graph.

Constraints:
    - The number of nodes in the graph is in range [0, 100]
    - 1 <= Node.val <= 100
    - Node.val is unique for each node
    - No repeated edges, no self-loops
    - The graph is connected and all nodes can be visited from the given node

Hint:
    Use a dictionary to map original nodes to their clones. When traversing
    (BFS or DFS), if a neighbor hasn't been cloned yet, clone it and add the
    mapping. Then connect the cloned neighbor to the current clone.

Pattern: Graph traversal with cloning - use a hashmap to track original->clone
mapping and avoid infinite loops in cyclic graphs.
"""

from collections import deque
from typing import Optional, Dict


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph_bfs(node: Optional[Node]) -> Optional[Node]:
    """BFS approach - clone graph level by level."""
    pass


def clone_graph_dfs(node: Optional[Node]) -> Optional[Node]:
    """DFS approach - recursive cloning."""
    pass


# --- Helper Functions ---

def build_graph(adj_list):
    """Build graph from adjacency list (1-indexed)."""
    if not adj_list:
        return None
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


def graph_to_adj_list(node):
    """Convert graph to adjacency list for comparison."""
    if not node:
        return []
    visited = {}
    queue = deque([node])
    visited[node.val] = node

    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor.val not in visited:
                visited[neighbor.val] = neighbor
                queue.append(neighbor)

    result = []
    for i in range(1, len(visited) + 1):
        result.append(sorted([n.val for n in visited[i].neighbors]))
    return result


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Standard graph
    original = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
    cloned = clone_graph_bfs(original)
    assert cloned is not original, "Clone should be a different object"
    assert graph_to_adj_list(cloned) == [[2, 4], [1, 3], [2, 4], [1, 3]]

    # Test 2: Single node
    original = build_graph([[]])
    cloned = clone_graph_bfs(original)
    assert cloned is not original
    assert cloned.val == 1
    assert cloned.neighbors == []

    # Test 3: Empty graph
    cloned = clone_graph_bfs(None)
    assert cloned is None

    # Test 4: DFS approach
    original = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
    cloned = clone_graph_dfs(original)
    assert cloned is not original
    assert graph_to_adj_list(cloned) == [[2, 4], [1, 3], [2, 4], [1, 3]]

    # Test 5: Two connected nodes
    original = build_graph([[2], [1]])
    cloned = clone_graph_bfs(original)
    assert cloned.val == 1
    assert len(cloned.neighbors) == 1
    assert cloned.neighbors[0].val == 2

    print("All tests passed!")
