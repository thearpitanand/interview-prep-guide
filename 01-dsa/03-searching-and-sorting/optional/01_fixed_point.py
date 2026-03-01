"""
Problem: Find Fixed Point (Value = Index) (GFG) | Optional | Easy
Topic: Searching and Sorting

Given a sorted array of distinct integers, find an index i such that arr[i] == i.
Return -1 if no such index exists.

Example 1:
  Input: arr = [-10, -5, 0, 3, 7]
  Output: 3

Constraints:
  - Array is sorted with distinct elements

Hint: Binary search — if arr[mid] == mid, found. If arr[mid] < mid, go right.
Pattern: Binary Search
"""


def fixed_point(arr: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert fixed_point([-10, -5, 0, 3, 7]) == 3
    assert fixed_point([0, 2, 5, 8, 17]) == 0
    assert fixed_point([-10, -5, 3, 4, 7, 9]) == -1
    print("All tests passed!")
