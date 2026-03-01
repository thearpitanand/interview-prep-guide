"""
Problem: M-Coloring Problem (GFG) | Day 32 | Medium
Topic: Backtracking

Given an undirected graph and M colors, determine if the graph can be colored
with at most M colors such that no two adjacent vertices share the same color.

Example 1:
  Input: graph = [[1,2],[0,2],[0,1]], m = 3
  Output: True  # 3 vertices, all connected — need 3 colors

Constraints:
  - 1 <= n <= 20
  - 1 <= m <= n

Hint: Try coloring each vertex 1..m, backtrack if any neighbor has same color.
Pattern: Backtracking
"""


def m_coloring(graph: list[list[int]], m: int) -> bool:
    # graph[i] = list of neighbors of vertex i
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert m_coloring([[1, 2], [0, 2], [0, 1]], 3) == True
    assert m_coloring([[1, 2], [0, 2], [0, 1]], 2) == False
    assert m_coloring([[1], [0]], 2) == True
    print("All tests passed!")
