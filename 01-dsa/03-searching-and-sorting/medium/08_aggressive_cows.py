"""
Problem: Aggressive Cows (SPOJ Classic) | Day 14 | Medium
Topic: Searching and Sorting

You are given n stalls located at certain positions along a straight line.
You need to place c cows in these stalls such that the minimum distance
between any two cows is maximized. Find this maximum possible minimum distance.

Example 1:
  Input: stalls = [1, 2, 4, 8, 9], cows = 3
  Output: 3
  Explanation: Place cows at positions 1, 4, 9. Minimum distance = 3.

Example 2:
  Input: stalls = [1, 2, 3], cows = 2
  Output: 2
  Explanation: Place cows at positions 1, 3. Minimum distance = 2.

Constraints:
  - 2 <= n <= 10^5
  - 2 <= c <= n
  - 0 <= stall positions <= 10^9

Hint: Binary search on the answer (minimum distance).
      For a given distance d, greedily check if you can place all c cows
      such that each pair is at least d apart. Sort stalls first.
      Search space: lo=0, hi=max(stalls)-min(stalls).
Pattern: Binary Search on Answer
"""

from typing import List


def aggressive_cows(stalls: List[int], cows: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert aggressive_cows([1, 2, 4, 8, 9], 3) == 3
    assert aggressive_cows([1, 2, 3], 2) == 2
    assert aggressive_cows([1, 5, 9, 13], 4) == 4
    assert aggressive_cows([1, 2, 8, 4, 9], 3) == 3  # unsorted input
    assert aggressive_cows([0, 1000000000], 2) == 1000000000
    print("All tests passed!")
