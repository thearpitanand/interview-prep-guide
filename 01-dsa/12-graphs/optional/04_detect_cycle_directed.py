"""
Problem: Detect Cycle in Directed Graph (GFG) | Optional | Medium
Topic: Graphs

Given a directed graph, check if it contains a cycle.

Example 1:
  Input: V = 4, edges = [[0,1],[1,2],[2,3],[3,1]]
  Output: True

Constraints:
  - 1 <= V <= 10^5

Hint: DFS with 3 colors: white (unvisited), gray (in current DFS path), black (done). Cycle if gray→gray.
Pattern: DFS / Three-Color
"""


def has_cycle_directed(V: int, edges: list[list[int]]) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert has_cycle_directed(4, [[0,1],[1,2],[2,3],[3,1]]) == True
    assert has_cycle_directed(4, [[0,1],[1,2],[2,3]]) == False
    print("All tests passed!")
