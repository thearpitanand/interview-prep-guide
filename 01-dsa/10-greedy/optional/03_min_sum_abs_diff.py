"""
Problem: Min Sum Absolute Difference of Pairs (GFG) | Optional | Easy
Topic: Greedy

Given two arrays of equal length, pair them to minimize the sum of absolute
differences of pairs.

Example 1:
  Input: a = [4, 1, 8, 7], b = [2, 3, 6, 5]
  Output: 6

Constraints:
  - 1 <= n <= 10^5

Hint: Sort both arrays. Pair corresponding elements.
Pattern: Greedy / Sorting
"""


def min_sum_abs_diff(a: list[int], b: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert min_sum_abs_diff([4, 1, 8, 7], [2, 3, 6, 5]) == 6
    assert min_sum_abs_diff([1, 2], [3, 4]) == 4
    print("All tests passed!")
