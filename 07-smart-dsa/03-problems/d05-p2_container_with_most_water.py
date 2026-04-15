"""
Problem: Container With Most Water (LC 11) | Smart-DSA Day 5 | Medium
Pattern: Two Pointers
Time target: 25 minutes

You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).
Find two lines that form a container holding the most water. Return the max area.

Example 1:
  Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
  Output: 49

Example 2:
  Input: height = [1, 1]
  Output: 1

Constraints:
  - 2 <= height.length <= 10^5
  - 0 <= height[i] <= 10^4

Hint (⚠ read only after time budget is blown):
  Start with the widest container (left=0, right=n-1). Move the pointer with
  the shorter height inward — moving the taller one can only decrease area.
"""


def max_area(height: list[int]) -> int:
    pass


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    print("All tests passed!")
