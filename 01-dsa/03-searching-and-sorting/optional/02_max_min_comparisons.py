"""
Problem: Max/Min Using Minimum Comparisons (GFG) | Optional | Easy
Topic: Searching and Sorting

Find both max and min of an array using minimum number of comparisons.

Example 1:
  Input: arr = [1000, 11, 445, 1, 330, 3000]
  Output: (1, 3000)

Constraints:
  - 1 <= n <= 10^5

Hint: Process elements in pairs — compare pair first, then compare with min/max.
Pattern: Tournament / Pair Comparison
"""


def max_min(arr: list[int]) -> tuple[int, int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_min([1000, 11, 445, 1, 330, 3000]) == (1, 3000)
    assert max_min([5]) == (5, 5)
    assert max_min([3, 1]) == (1, 3)
    print("All tests passed!")
