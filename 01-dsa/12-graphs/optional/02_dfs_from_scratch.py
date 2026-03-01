"""
Problem: DFS Implementation from Scratch (GFG) | Optional | Easy
Topic: Graphs

Implement Depth-First Search traversal from a given source vertex.

Example 1:
  Input: V = 5, edges = [[0,1],[0,2],[1,3],[1,4]], src = 0
  Output: [0, 1, 3, 4, 2]

Constraints:
  - 1 <= V <= 10^5

Hint: Use recursion or explicit stack.
Pattern: DFS
"""


def dfs(V: int, edges: list[list[int]], src: int) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = dfs(5, [[0,1],[0,2],[1,3],[1,4]], 0)
    assert result[0] == 0
    assert len(result) == 5
    print("All tests passed!")
