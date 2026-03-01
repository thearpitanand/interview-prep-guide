"""
Problem: Kth Element of Two Sorted Arrays (GFG) | Optional | Medium
Topic: Searching and Sorting

Given two sorted arrays of sizes m and n, find the element that would be at
the kth position of the combined sorted array.

Example 1:
  Input: arr1 = [2, 3, 6, 7, 9], arr2 = [1, 4, 8, 10], k = 5
  Output: 6

Constraints:
  - 1 <= m, n <= 10^6
  - 1 <= k <= m + n

Hint: Binary search on partition similar to median of two sorted arrays.
Pattern: Binary Search
"""


def kth_element(arr1: list[int], arr2: list[int], k: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert kth_element([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
    assert kth_element([1, 2], [3, 4], 3) == 3
    print("All tests passed!")
