"""
Problem: Subset Sums (GFG) | Optional | Easy
Topic: Searching and Sorting

Given an array, return all possible subset sums in sorted order.

Example 1:
  Input: arr = [2, 3]
  Output: [0, 2, 3, 5]

Constraints:
  - 1 <= n <= 15

Hint: Generate all subsets using bit manipulation or recursion.
Pattern: Power Set
"""


def subset_sums(arr: list[int]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert subset_sums([2, 3]) == [0, 2, 3, 5]
    assert subset_sums([1]) == [0, 1]
    print("All tests passed!")
