"""
Problem: Bellman-Ford Algorithm (GFG) | Day 35 | Medium
Topic: Graphs

Given a weighted directed graph with V vertices and E edges, and a source
vertex, find the shortest distances from source to all vertices. Handle
negative weights (detect negative cycles).

Example 1:
  Input: V = 5, edges = [(0,1,-1),(0,2,4),(1,2,3),(1,3,2),(1,4,2),(3,2,5),(3,1,1),(4,3,-3)], src = 0
  Output: [0, -1, 2, -2, 1]

Constraints:
  - 1 <= V <= 10^3
  - 1 <= E <= V*(V-1)

Hint: Relax all edges V-1 times. If any edge can still be relaxed, there's a negative cycle.
Pattern: Bellman-Ford Algorithm
"""


def bellman_ford(V: int, edges: list[tuple[int, int, int]], src: int) -> list[float]:
    # edges = list of (u, v, weight)
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    edges = [(0,1,-1),(0,2,4),(1,2,3),(1,3,2),(1,4,2),(3,2,5),(3,1,1),(4,3,-3)]
    assert bellman_ford(5, edges, 0) == [0, -1, 2, -2, 1]
    print("All tests passed!")
