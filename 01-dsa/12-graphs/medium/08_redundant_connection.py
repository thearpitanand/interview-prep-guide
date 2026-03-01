"""
Redundant Connection (LC 684)

Day: 35 | Difficulty: Medium | Pattern: Union-Find

In this problem, a tree is an undirected graph that is connected and has no
cycles. You are given a graph that started as a tree with n nodes (1 to n),
with one additional edge added. The added edge connects two vertices that are
already connected, creating a cycle.

Return the edge that can be removed so that the resulting graph is a tree. If
there are multiple answers, return the edge that occurs last in the input.

Examples:
    Input: edges=[[1,2],[1,3],[2,3]]
    Output: [2,3]
    Explanation: Removing [2,3] gives a tree: 1-2, 1-3.

    Input: edges=[[1,2],[2,3],[3,4],[1,4],[1,5]]
    Output: [1,4]
    Explanation: Removing [1,4] breaks the cycle 1-2-3-4-1.

Constraints:
    - n == edges.length
    - 3 <= n <= 1000
    - edges[i].length == 2
    - 1 <= ai < bi <= edges.length
    - ai != bi
    - No repeated edges
    - The given graph is connected

Hint:
    Process edges one by one using Union-Find. For each edge, check if the
    two nodes are already connected (same root). If yes, this edge creates
    a cycle -- it's the redundant edge. The last such edge in the input is
    the answer.

Pattern: Union-Find cycle detection - the first edge that connects two
already-connected nodes is the redundant connection.
"""

from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True


def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    """Find the redundant edge using Union-Find."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Triangle - last edge is redundant
    result = find_redundant_connection([[1, 2], [1, 3], [2, 3]])
    assert result == [2, 3], f"Expected [2, 3], got {result}"

    # Test 2: Larger cycle
    result = find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
    assert result == [1, 4], f"Expected [1, 4], got {result}"

    # Test 3: Minimum graph (3 nodes, triangle)
    result = find_redundant_connection([[1, 2], [2, 3], [1, 3]])
    assert result == [1, 3], f"Expected [1, 3], got {result}"

    # Test 4: Chain with extra edge at the end
    result = find_redundant_connection([[1, 2], [2, 3], [3, 4], [4, 5], [3, 5]])
    assert result == [3, 5], f"Expected [3, 5], got {result}"

    print("All tests passed!")
