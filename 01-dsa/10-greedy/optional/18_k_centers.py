"""
Problem: K Centers Problem (GFG) | Optional | Hard
Topic: Greedy

Given N cities and distances between them, select K cities as centers to
minimize the maximum distance of any city to its nearest center.

Example 1:
  Input: dist matrix, k = 2
  Output: minimum possible maximum distance

Constraints:
  - 1 <= k <= n <= 100

Hint: Greedy: pick first center arbitrarily, then always pick the farthest city from current centers.
Pattern: Greedy
"""


def k_centers(dist: list[list[int]], k: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    dist = [[0,4,8,5],[4,0,10,7],[8,10,0,9],[5,7,9,0]]
    result = k_centers(dist, 2)
    assert isinstance(result, int)
    print("All tests passed!")
