"""
Problem: Floyd-Warshall All-Pairs Shortest Path (GFG) | Day 35 | Medium
Topic: Graphs

Given a weighted directed graph represented as an adjacency matrix, find
shortest distances between every pair of vertices.

Example 1:
  Input: graph = [[0,5,INF,10],[INF,0,3,INF],[INF,INF,0,1],[INF,INF,INF,0]]
  Output: [[0,5,8,9],[INF,0,3,4],[INF,INF,0,1],[INF,INF,INF,0]]

Constraints:
  - 1 <= V <= 500
  - -10^3 <= weight <= 10^3

Hint: For each intermediate vertex k, try to improve dist[i][j] via dist[i][k] + dist[k][j].
Pattern: Floyd-Warshall Algorithm
"""


def floyd_warshall(graph: list[list[float]]) -> list[list[float]]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    INF = float('inf')
    graph = [[0,5,INF,10],[INF,0,3,INF],[INF,INF,0,1],[INF,INF,INF,0]]
    result = floyd_warshall(graph)
    assert result[0] == [0, 5, 8, 9]
    assert result[1] == [INF, 0, 3, 4]
    print("All tests passed!")
