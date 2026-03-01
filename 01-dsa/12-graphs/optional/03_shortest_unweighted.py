"""
Problem: Shortest Path in Unweighted Graph (GFG) | Optional | Easy
Topic: Graphs

Find shortest path from source to all vertices in an unweighted graph.

Example 1:
  Input: V = 6, edges = [[0,1],[0,2],[1,3],[2,3],[3,4],[4,5]], src = 0
  Output: [0, 1, 1, 2, 3, 4]

Constraints:
  - 1 <= V <= 10^5

Hint: BFS from source. Distance = level in BFS tree.
Pattern: BFS
"""


def shortest_path_unweighted(V: int, edges: list[list[int]], src: int) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert shortest_path_unweighted(6, [[0,1],[0,2],[1,3],[2,3],[3,4],[4,5]], 0) == [0, 1, 1, 2, 3, 4]
    print("All tests passed!")
