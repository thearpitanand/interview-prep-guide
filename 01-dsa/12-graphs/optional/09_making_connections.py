"""
Problem: Making Wired Connections (LC 1319) | Optional | Medium
Topic: Graphs

Given n computers and connections between them, find the minimum number of
cable changes needed to connect all computers. Each connection can be
reassigned.

Example 1:
  Input: n = 4, connections = [[0,1],[0,2],[1,2]]
  Output: 1

Constraints:
  - 1 <= n <= 10^5

Hint: Need at least n-1 edges. Count connected components using Union-Find. Answer = components - 1 (if enough edges).
Pattern: Union-Find
"""


def make_connected(n: int, connections: list[list[int]]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert make_connected(4, [[0,1],[0,2],[1,2]]) == 1
    assert make_connected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]) == 2
    assert make_connected(6, [[0,1],[0,2],[0,3],[1,2]]) == -1
    print("All tests passed!")
