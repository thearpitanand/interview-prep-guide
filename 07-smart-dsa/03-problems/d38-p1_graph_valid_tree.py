"""
Problem: Graph Valid Tree (LC 261) | Smart-DSA Day 38 | Medium
Pattern: Union-Find
Time target: 30 minutes

Given n nodes labeled 0 to n-1 and a list of undirected edges, determine
whether these edges form a valid tree. A valid tree has no cycles and all
nodes are connected.

Example 1:
  Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
  Output: True

Example 2:
  Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
  Output: False

Constraints:
  - 1 <= n <= 2000
  - 0 <= edges.length <= 5000
  - edges[i].length == 2
  - 0 <= edges[i][0], edges[i][1] < n
  - No self-loops or repeated edges.

Hint (⚠ read only after time budget is blown):
  A tree on n nodes has exactly n-1 edges. Use Union-Find: if union(u, v)
  returns False (both already in the same component), a cycle exists. After
  processing all edges, confirm len(edges) == n - 1.
"""


def valid_tree(n: int, edges: list[list[int]]) -> bool:
    pass


if __name__ == "__main__":
    assert valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True
    assert valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False
    assert valid_tree(1, []) is True
    assert valid_tree(2, [[0, 1]]) is True
    assert valid_tree(2, []) is False
    print("All tests passed!")
