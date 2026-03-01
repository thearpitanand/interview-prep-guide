"""
Problem: Two Clique Problem (GFG) | Optional | Hard
Topic: Graphs

Check if the vertices of a graph can be partitioned into two cliques.

Example 1:
  Input: V = 5, edges forming two cliques
  Output: True/False

Constraints:
  - 1 <= V <= 100

Hint: Two cliques in G ↔ complement graph is bipartite. Build complement and check bipartiteness.
Pattern: Graph Complement + Bipartite Check
"""


def can_two_clique(V: int, edges: list[list[int]]) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    # Complete graph on 4 vertices minus one edge → can split into two cliques
    edges = [[0,1],[0,2],[0,3],[1,2],[2,3]]  # missing 1-3
    assert can_two_clique(4, edges) == True
    print("All tests passed!")
