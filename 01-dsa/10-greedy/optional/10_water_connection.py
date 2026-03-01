"""
Problem: Water Connection Problem (GFG) | Optional | Medium
Topic: Greedy

Given N houses with P pipes connecting them (each with diameter), find all
source-sink paths and the minimum pipe diameter along each path.

Example 1:
  Input: n = 9, pipes = [(7,4,98),(5,9,72),(4,6,10),(2,8,22),(9,7,17),(3,1,66)]
  Output: [(2,6,10), (3,1,66), (5,6,10)]  # source → sink, min diameter

Constraints:
  - 1 <= n <= 10^4

Hint: Build graph, find nodes with in-degree 0 (sources) and out-degree 0 (sinks). Traverse.
Pattern: Graph Traversal
"""


def water_connection(n: int, pipes: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = water_connection(9, [(7,4,98),(5,9,72),(4,6,10),(2,8,22),(9,7,17),(3,1,66)])
    assert len(result) >= 1
    print("All tests passed!")
