"""
Problem: Graph Coloring Problem (GFG) | Optional | Medium
Topic: Graphs

Find the chromatic number (minimum colors needed) to color a graph such that
no two adjacent vertices share a same color.

Example 1:
  Input: V = 4, edges = [[0,1],[1,2],[2,3],[3,0],[0,2]]
  Output: 3

Constraints:
  - 1 <= V <= 20

Hint: Greedy coloring with ordering. For exact chromatic number, try backtracking.
Pattern: Greedy / Backtracking
"""


def chromatic_number(V: int, edges: list[list[int]]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert chromatic_number(4, [[0,1],[1,2],[2,3],[3,0],[0,2]]) == 3
    assert chromatic_number(3, [[0,1],[1,2]]) == 2
    print("All tests passed!")
