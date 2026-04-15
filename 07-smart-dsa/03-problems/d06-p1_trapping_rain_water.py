"""
Problem: Trapping Rain Water (LC 42) | Smart-DSA Day 6 | Medium
Pattern: Two Pointers
Time target: 35 minutes

Given n non-negative integers representing an elevation map where each bar
has width 1, compute how much water it can trap after raining.

Example 1:
  Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
  Output: 6

Example 2:
  Input: height = [4, 2, 0, 3, 2, 5]
  Output: 9

Constraints:
  - n == height.length
  - 1 <= n <= 2 * 10^4
  - 0 <= height[i] <= 10^5

Hint (⚠ read only after time budget is blown):
  Two-pointer approach: maintain left_max and right_max. Water at position i
  is min(left_max, right_max) - height[i]. Process the side with the smaller
  max — you already know the bottleneck there.
"""


def trap(height: list[int]) -> int:
    pass


if __name__ == "__main__":
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    assert trap([3, 0, 2, 0, 4]) == 7
    assert trap([1]) == 0
    print("All tests passed!")
