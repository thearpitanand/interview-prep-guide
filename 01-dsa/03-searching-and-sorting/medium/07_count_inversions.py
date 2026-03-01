"""
Problem: Count Inversions | Day 14 | Medium
Topic: Searching and Sorting

Given an array of integers, count the number of inversions. An inversion is
a pair (i, j) where i < j but arr[i] > arr[j].

This is a classic problem solved efficiently using merge sort.

Example 1:
  Input: arr = [2, 4, 1, 3, 5]
  Output: 3
  Explanation: Inversions are (2,1), (4,1), (4,3)

Example 2:
  Input: arr = [1, 2, 3, 4, 5]
  Output: 0 (already sorted, no inversions)

Example 3:
  Input: arr = [5, 4, 3, 2, 1]
  Output: 10 (reverse sorted, maximum inversions = n*(n-1)/2)

Constraints:
  - 1 <= arr.length <= 10^5
  - -10^9 <= arr[i] <= 10^9

Hint: During merge sort, when you pick an element from the right half over
      the left half, ALL remaining elements in the left half form inversions
      with that right element. Count inversions += len(left) - i.
Pattern: Merge Sort Application
"""

from typing import List


def count_inversions(arr: List[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert count_inversions([2, 4, 1, 3, 5]) == 3
    assert count_inversions([1, 2, 3, 4, 5]) == 0
    assert count_inversions([5, 4, 3, 2, 1]) == 10
    assert count_inversions([1]) == 0
    assert count_inversions([2, 1]) == 1
    assert count_inversions([1, 20, 6, 4, 5]) == 5
    print("All tests passed!")
