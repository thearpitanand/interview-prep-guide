"""
Problem: Largest Rectangle in Histogram (LC 84) | Smart-DSA Day 17 | Hard
Pattern: Monotonic Stack
Time target: 40 minutes

Given an array of integers heights representing the histogram's bar heights
where the width of each bar is 1, return the area of the largest rectangle
in the histogram.

Example 1:
  Input: heights = [2,1,5,6,2,3]
  Output: 10
  Explanation: The rectangle spans bars 2 and 3 (heights 5 and 6), width 2.

Example 2:
  Input: heights = [2,4]
  Output: 4

Constraints:
  - 1 <= heights.length <= 10^5
  - 0 <= heights[i] <= 10^4

Hint (⚠ read only after time budget is blown):
  Use a monotonic increasing stack of (index, height) pairs. When a shorter
  bar breaks the invariant, pop and compute width extending back to the popped
  bar's stored index. Push (start_index, current_height) for each bar.
"""


def largest_rectangle_area(heights: list[int]) -> int:
    pass


if __name__ == "__main__":
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
    assert largest_rectangle_area([2, 4]) == 4
    assert largest_rectangle_area([1]) == 1
    assert largest_rectangle_area([5, 5, 5, 5]) == 20
    assert largest_rectangle_area([6, 2, 5, 4, 5, 1, 6]) == 12
    print("All tests passed!")
