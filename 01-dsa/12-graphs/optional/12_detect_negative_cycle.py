"""
Problem: Detect Negative Cycle (GFG) | Optional | Medium
Topic: Graphs

Given a weighted directed graph, detect if it contains a negative weight cycle.

Example 1:
  Input: V = 4, edges = [(0,1,1),(1,2,-1),(2,3,-1),(3,0,-1)]
  Output: True

Constraints:
  - 1 <= V <= 10^3

Hint: Run Bellman-Ford. After V-1 relaxations, if any edge can still be relaxed → negative cycle.
Pattern: Bellman-Ford
"""


def has_negative_cycle(V: int, edges: list[tuple[int, int, int]]) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert has_negative_cycle(4, [(0,1,1),(1,2,-1),(2,3,-1),(3,0,-1)]) == True
    assert has_negative_cycle(3, [(0,1,1),(1,2,2),(0,2,4)]) == False
    print("All tests passed!")
