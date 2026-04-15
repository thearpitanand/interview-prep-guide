"""
Problem: Koko Eating Bananas (LC 875) | Smart-DSA Day 13 | Medium
Pattern: Binary Search on Answer
Time target: 30 minutes

Koko can eat k bananas per hour. Given piles of bananas and h hours to eat all
of them, find the minimum integer k such that she can finish within h hours.
Each hour she picks one pile and eats up to k bananas from it.

Example 1:
  Input: piles = [3, 6, 7, 11], h = 8
  Output: 4

Example 2:
  Input: piles = [30, 11, 23, 4, 20], h = 5
  Output: 30

Example 3:
  Input: piles = [30, 11, 23, 4, 20], h = 6
  Output: 23

Constraints:
  - 1 <= piles.length <= 10^4
  - piles.length <= h <= 10^9
  - 1 <= piles[i] <= 10^9

Hint (⚠ read only after time budget is blown):
  Binary search on k in range [1, max(piles)]. For a given k, hours needed =
  sum(ceil(pile/k) for pile in piles). If hours <= h, k might work — try
  smaller. If hours > h, need larger k.
"""

import math


def min_eating_speed(piles: list[int], h: int) -> int:
    pass


if __name__ == "__main__":
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
    assert min_eating_speed([1000000000], 2) == 500000000
    print("All tests passed!")
