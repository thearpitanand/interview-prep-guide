"""
Problem: Travelling Salesman Problem (GFG) | Optional | Hard
Topic: Graphs

Given a set of cities and distances, find the shortest route visiting all
cities exactly once and returning to origin.

Example 1:
  Input: dist = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
  Output: 80

Constraints:
  - 1 <= n <= 20

Hint: DP with bitmask: dp[mask][i] = min cost to visit cities in mask, ending at i.
Pattern: DP + Bitmask
"""


def tsp(dist: list[list[int]]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert tsp([[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]) == 80
    assert tsp([[0,5],[5,0]]) == 10
    print("All tests passed!")
