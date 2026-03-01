"""
Problem: Prim's MST (GFG) | Day 35 | Medium
Topic: Graphs

Given a weighted undirected graph, find the Minimum Spanning Tree using
Prim's algorithm. Return the total weight of the MST.

Example 1:
  Input: V = 4, edges = [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
  Output: 19

Constraints:
  - 2 <= V <= 10^5
  - 1 <= E <= 10^5

Hint: Use min-heap. Start from vertex 0. Greedily pick minimum weight edge connecting MST to non-MST vertex.
Pattern: Min-Heap / Prim's Algorithm
"""
import heapq


def prims_mst(V: int, edges: list[tuple[int, int, int]]) -> int:
    # edges = list of (u, v, weight)
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert prims_mst(4, [(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]) == 19
    assert prims_mst(3, [(0,1,1),(1,2,2),(0,2,3)]) == 3
    print("All tests passed!")
