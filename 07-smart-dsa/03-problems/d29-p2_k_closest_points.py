"""
Problem: K Closest Points to Origin (LC 973) | Smart-DSA Day 29 | Medium
Pattern: Heap / Top-K
Time target: 25 minutes

Given an array of points on a 2D plane, return the k closest points to the
origin (0, 0). Distance is Euclidean. The answer may be in any order.

Example 1:
  Input: points = [[1, 3], [-2, 2]], k = 1
  Output: [[-2, 2]]

Example 2:
  Input: points = [[3, 3], [5, -1], [-2, 4]], k = 2
  Output: [[3, 3], [-2, 4]]

Constraints:
  - 1 <= k <= points.length <= 10^4
  - -10^4 <= points[i][0], points[i][1] <= 10^4

Hint (⚠ read only after time budget is blown):
  Compare squared distances to avoid sqrt. Use a max-heap of size k (negate
  distances), or sort by distance and slice the first k elements.
"""
import heapq


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    pass


if __name__ == "__main__":
    result1 = k_closest([[1, 3], [-2, 2]], 1)
    assert result1 == [[-2, 2]]

    result2 = k_closest([[3, 3], [5, -1], [-2, 4]], 2)
    assert sorted(result2) == sorted([[3, 3], [-2, 4]])

    result3 = k_closest([[0, 1], [1, 0]], 2)
    assert sorted(result3) == sorted([[0, 1], [1, 0]])
    print("All tests passed!")
