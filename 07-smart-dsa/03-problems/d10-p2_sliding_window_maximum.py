"""
Problem: Sliding Window Maximum (LC 239) | Smart-DSA Day 10 | Hard→Medium
Pattern: Sliding Window + Monotonic Deque
Time target: 30 minutes

Given an integer array nums and a window size k, return the max value in each
window as it slides from left to right.

Example 1:
  Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
  Output: [3, 3, 5, 5, 6, 7]

Example 2:
  Input: nums = [1], k = 1
  Output: [1]

Constraints:
  - 1 <= nums.length <= 10^5
  - -10^4 <= nums[i] <= 10^4
  - 1 <= k <= nums.length

Hint (⚠ read only after time budget is blown):
  Use a monotonic deque of indices (decreasing by value). Add new index to
  back, popping smaller elements first. Pop front if out of window. Front is
  always the current window max.
"""

from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    pass


if __name__ == "__main__":
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert max_sliding_window([1], 1) == [1]
    assert max_sliding_window([1, -1], 1) == [1, -1]
    assert max_sliding_window([9, 11], 2) == [11]
    print("All tests passed!")
