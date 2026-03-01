"""
Problem: Topological Sort (standalone) (GFG) | Optional | Medium
Topic: Graphs

Given a DAG with V vertices, return a topological ordering.

Example 1:
  Input: V = 6, edges = [[5,0],[5,2],[4,0],[4,1],[2,3],[3,1]]
  Output: [5, 4, 2, 3, 1, 0] (one valid ordering)

Constraints:
  - 1 <= V <= 10^4

Hint: Kahn's algorithm (BFS with in-degree) or DFS + stack.
Pattern: Topological Sort
"""


def topological_sort(V: int, edges: list[list[int]]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = topological_sort(6, [[5,0],[5,2],[4,0],[4,1],[2,3],[3,1]])
    # Verify topological order: for each edge (u,v), u appears before v
    pos = {v: i for i, v in enumerate(result)}
    for u, v in [[5,0],[5,2],[4,0],[4,1],[2,3],[3,1]]:
        assert pos[u] < pos[v]
    print("All tests passed!")
