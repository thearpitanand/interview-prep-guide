"""
Problem: Number of Connected Components in an Undirected Graph (LC 323) | Smart-DSA Day 38 | Medium
Pattern: Union-Find
Time target: 25 minutes

Given n nodes labeled 0 to n-1 and a list of undirected edges, return the
number of connected components in the graph.

Example 1:
  Input: n = 5, edges = [[0,1],[1,2],[3,4]]
  Output: 2

Example 2:
  Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
  Output: 1

Constraints:
  - 1 <= n <= 2000
  - 0 <= edges.length <= 5000
  - edges[i].length == 2
  - 0 <= edges[i][0], edges[i][1] < n
  - No repeated edges or self-loops.

Hint (⚠ read only after time budget is blown):
  Initialize count = n (each node is its own component). For each edge,
  union(u, v): if they were in different components, decrement count. Return
  count at the end.
"""


def count_components(n: int, edges: list[list[int]]) -> int:
    pass


if __name__ == "__main__":
    assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
    assert count_components(4, []) == 4
    assert count_components(1, []) == 1
    print("All tests passed!")
