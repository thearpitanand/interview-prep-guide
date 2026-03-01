"""
Problem: Kth Max/Min Element (GFG) | Day 5 | Easy
Topic: Arrays

Given an array arr[] and a number K, find the Kth smallest and Kth largest
element in the array.

Example 1:
  Input: arr = [7, 10, 4, 3, 20, 15], k = 3
  Output: (7, 10)  # 3rd smallest = 7, 3rd largest = 10

Constraints:
  - 1 <= n <= 10^5
  - 1 <= arr[i] <= 10^5
  - 1 <= k <= n

Hint: Use a heap or quickselect for O(n) average.
Pattern: Heap / Quickselect
"""


def kth_max_min(arr: list[int], k: int) -> tuple[int, int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert kth_max_min([7, 10, 4, 3, 20, 15], 3) == (7, 10)
    assert kth_max_min([1, 2, 3, 4, 5], 1) == (1, 5)
    assert kth_max_min([5], 1) == (5, 5)
    print("All tests passed!")
