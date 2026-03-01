"""
Problem: Find Peak Element (LC 162) | Day 13 | Medium
Topic: Searching and Sorting

A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -infinity. In other words, an element
is always considered to be strictly greater than a neighbor that is outside the
array.

You must write an algorithm that runs in O(log n) time.

Example 1:
  Input: nums = [1,2,3,1]
  Output: 2
  Explanation: 3 is a peak element (index 2).

Example 2:
  Input: nums = [1,2,1,3,5,6,4]
  Output: 5 (or 1, either is valid)

Constraints:
  - 1 <= nums.length <= 1000
  - -2^31 <= nums[i] <= 2^31 - 1
  - nums[i] != nums[i + 1] for all valid i

Hint: If nums[mid] < nums[mid+1], a peak must exist on the right side.
      If nums[mid] > nums[mid+1], a peak must exist on the left side (including mid).
      Use binary search with left < right variant.
Pattern: Binary Search on Unsorted Array
"""

from typing import List


def find_peak_element(nums: List[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert find_peak_element([1, 2, 3, 1]) == 2
    result = find_peak_element([1, 2, 1, 3, 5, 6, 4])
    assert result in [1, 5]  # either peak is valid
    assert find_peak_element([1]) == 0
    assert find_peak_element([1, 2]) == 1
    assert find_peak_element([2, 1]) == 0
    print("All tests passed!")
