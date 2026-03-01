"""
Problem: Strongly Connected Components (Kosaraju's) (GFG) | Optional | Hard
Topic: Graphs

Find all strongly connected components in a directed graph.

Example 1:
  Input: V = 5, edges = [[0,2],[2,1],[1,0],[0,3],[3,4]]
  Output: [[0,1,2],[3],[4]]

Constraints:
  - 1 <= V <= 10^5

Hint: Kosaraju's: 1) Fill stack by finish time (DFS). 2) Transpose graph. 3) DFS on transpose in stack order.
Pattern: Kosaraju's Algorithm
"""


def kosaraju_scc(V: int, edges: list[list[int]]) -> list[list[int]]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = kosaraju_scc(5, [[0,2],[2,1],[1,0],[0,3],[3,4]])
    # Check that we have 3 SCCs
    assert len(result) == 3
    # The SCC containing 0 should also have 1 and 2
    scc_with_0 = [s for s in result if 0 in s][0]
    assert set(scc_with_0) == {0, 1, 2}
    print("All tests passed!")
