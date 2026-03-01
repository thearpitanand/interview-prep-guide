"""
Problem: Count Triplets with Sum < X (LC 259) | Optional | Medium
Topic: Searching and Sorting

Given an array and a value X, count the number of triplets with sum less than X.

Example 1:
  Input: arr = [-2, 0, 1, 3], x = 2
  Output: 2  # (-2,0,1) and (-2,0,3)

Constraints:
  - 3 <= n <= 10^3

Hint: Sort, fix one element, use two pointers for remaining.
Pattern: Two Pointers
"""


def count_triplets_smaller(arr: list[int], x: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert count_triplets_smaller([-2, 0, 1, 3], 2) == 2
    assert count_triplets_smaller([5, 1, 3, 4, 7], 12) == 4
    print("All tests passed!")
