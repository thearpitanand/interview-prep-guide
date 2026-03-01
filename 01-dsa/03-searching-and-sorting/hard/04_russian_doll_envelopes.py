"""
Problem: Russian Doll Envelopes (LC 354) | Day 14 | Hard
Topic: Searching and Sorting

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height
of one envelope are strictly greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one
inside the other).

Note: You cannot rotate an envelope.

Example 1:
  Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
  Output: 3
  Explanation: The maximum envelopes you can fit is 3: [2,3] => [5,4] => [6,7].

Example 2:
  Input: envelopes = [[1,1],[1,1],[1,1]]
  Output: 1

Constraints:
  - 1 <= envelopes.length <= 10^5
  - envelopes[i].length == 2
  - 1 <= wi, hi <= 10^5

Hint: Sort by width ascending, then by height DESCENDING (for same width).
      This reduces the problem to finding the Longest Increasing Subsequence (LIS)
      on the heights. Use binary search (bisect) for O(n log n) LIS.
      Sorting height descending for same width prevents selecting two envelopes
      with equal width.
Pattern: Sort + Longest Increasing Subsequence (Binary Search)
"""

from typing import List


def max_envelopes(envelopes: List[List[int]]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_envelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3
    assert max_envelopes([[1, 1], [1, 1], [1, 1]]) == 1
    assert max_envelopes([[1, 1]]) == 1
    assert max_envelopes([[1, 2], [2, 3], [3, 4], [4, 5]]) == 4
    assert max_envelopes([[2, 100], [3, 200], [4, 300], [5, 500], [5, 400],
                          [5, 250], [6, 370], [6, 360], [7, 380]]) == 5
    print("All tests passed!")
