"""
Problem: Vertex Cover Problem (GFG) | Optional | Hard
Topic: Graphs

Find the minimum vertex cover of a graph (smallest set of vertices such
that every edge has at least one endpoint in the set).

Example 1:
  Input: V = 4, edges = [[0,1],[0,2],[1,3],[2,3]]
  Output: 2  # vertices {0, 3} cover all edges

Constraints:
  - 1 <= V <= 20

Hint: NP-hard in general. For small V, use bitmask DP. For trees, use tree DP.
Pattern: Bitmask / Tree DP
"""


def min_vertex_cover(V: int, edges: list[list[int]]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert min_vertex_cover(4, [[0,1],[0,2],[1,3],[2,3]]) == 2
    assert min_vertex_cover(3, [[0,1],[1,2]]) == 1
    print("All tests passed!")
