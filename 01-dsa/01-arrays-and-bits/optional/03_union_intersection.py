"""
Problem: Union & Intersection of Two Sorted Arrays (GFG) | Optional | Easy
Topic: Arrays

Given two sorted arrays, find their union and intersection.

Example 1:
  Input: arr1 = [1, 2, 3, 4, 5], arr2 = [1, 2, 3]
  Output: union = [1, 2, 3, 4, 5], intersection = [1, 2, 3]

Constraints:
  - 1 <= n, m <= 10^5
  - Arrays are sorted

Hint: Two pointer merge-like approach.
Pattern: Two Pointers
"""


def union_sorted(arr1: list[int], arr2: list[int]) -> list[int]:
    # Write your solution here
    pass


def intersection_sorted(arr1: list[int], arr2: list[int]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert union_sorted([1, 2, 3, 4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
    assert intersection_sorted([1, 2, 3, 4, 5], [1, 2, 3]) == [1, 2, 3]
    assert union_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert intersection_sorted([1, 3, 5], [2, 4, 6]) == []
    print("All tests passed!")
