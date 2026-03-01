"""
Problem: Euler Path / 7 Bridges of Konigsberg (GFG) | Optional | Hard
Topic: Graphs

Given a graph, check if an Eulerian path/circuit exists and find it.
Eulerian Circuit: visit every edge exactly once and return to start.
Eulerian Path: visit every edge exactly once (start and end may differ).

Example 1:
  Input: V = 5, edges = [[0,1],[1,2],[2,0],[0,3],[3,4]]
  Output: "Eulerian Path" (vertices 3,4 have odd degree)

Constraints:
  - 1 <= V <= 10^5

Hint: Count odd-degree vertices: 0 = circuit, 2 = path, else = none.
Pattern: Graph Properties
"""


def euler_type(V: int, edges: list[list[int]]) -> str:
    # Returns "Eulerian Circuit", "Eulerian Path", or "Not Eulerian"
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert euler_type(5, [[0,1],[1,2],[2,0],[0,3],[3,4]]) == "Eulerian Path"
    assert euler_type(3, [[0,1],[1,2],[2,0]]) == "Eulerian Circuit"
    assert euler_type(4, [[0,1],[0,2],[0,3],[1,2]]) == "Not Eulerian"
    print("All tests passed!")
