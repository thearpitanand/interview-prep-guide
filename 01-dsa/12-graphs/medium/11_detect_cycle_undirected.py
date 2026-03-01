"""
Problem: Detect Cycle in Undirected Graph (GFG) | Day 33 | Medium
Topic: Graphs

Given an undirected graph with V vertices and E edges, check if it contains a cycle.

Example 1:
  Input: V = 5, edges = [[0,1],[1,2],[2,0],[3,4]]
  Output: True  # 0-1-2-0 is a cycle

Constraints:
  - 1 <= V <= 10^5
  - 0 <= E <= 10^5

Hint: BFS/DFS — if you visit an already-visited node that isn't the parent, there's a cycle. Or use Union-Find.
Pattern: DFS / Union-Find
"""


def has_cycle_undirected(V: int, edges: list[list[int]]) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert has_cycle_undirected(5, [[0,1],[1,2],[2,0],[3,4]]) == True
    assert has_cycle_undirected(4, [[0,1],[1,2],[2,3]]) == False
    assert has_cycle_undirected(3, [[0,1],[1,2],[2,0]]) == True
    print("All tests passed!")
