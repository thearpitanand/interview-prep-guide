"""
Problem: Longest Path in DAG (GFG) | Optional | Medium
Topic: Graphs

Given a weighted DAG, find the longest path from source to all vertices.

Example 1:
  Input: V = 6, edges = [(0,1,5),(0,2,3),(1,3,6),(1,2,2),(2,4,4),(2,5,2),(2,3,7),(3,5,1),(3,4,-1),(4,5,-2)], src = 1
  Output: [-inf, 0, 2, 9, 8, 10]  (from vertex 1)

Constraints:
  - 1 <= V <= 10^4

Hint: Topological sort, then relax edges in topo order (negate for longest).
Pattern: Topological Sort + DP
"""


def longest_path_dag(V: int, edges: list[tuple[int, int, int]], src: int) -> list[float]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    edges = [(0,1,5),(0,2,3),(1,3,6),(1,2,2),(2,4,4),(2,5,2),(2,3,7),(3,5,1),(3,4,-1),(4,5,-2)]
    result = longest_path_dag(6, edges, 1)
    assert result[1] == 0
    assert result[3] == 9
    print("All tests passed!")
