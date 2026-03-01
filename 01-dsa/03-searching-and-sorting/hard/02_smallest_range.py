"""
Problem: Smallest Range Covering Elements from K Lists (LC 632) | Day 14 | Hard
Topic: Searching and Sorting

You have k lists of sorted integers in non-decreasing order. Find the smallest
range [a, b] that includes at least one number from each of the k lists.

Range [a, b] is smaller than range [c, d] if b - a < d - c, or if
b - a == d - c and a < c.

Example 1:
  Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
  Output: [20,24]
  Explanation:
    List 1: [4,10,15,24,26], 24 is in range [20,24].
    List 2: [0,9,12,20], 20 is in range [20,24].
    List 3: [5,18,22,30], 22 is in range [20,24].

Example 2:
  Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
  Output: [1,1]

Constraints:
  - nums.length == k
  - 1 <= k <= 3500
  - 1 <= nums[i].length <= 50
  - -10^5 <= nums[i][j] <= 10^5
  - nums[i] is sorted in non-decreasing order

Hint: Use a min-heap containing one element from each list. Track the current
      maximum. The range is [heap_min, current_max]. Pop the minimum and push
      the next element from that same list. Update the best range as you go.
Pattern: Heap + Tracking Min/Max
"""

from typing import List


def smallest_range(nums: List[List[int]]) -> List[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert smallest_range([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]) == [20, 24]
    assert smallest_range([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) == [1, 1]
    assert smallest_range([[10, 10], [11, 11]]) == [10, 11]
    assert smallest_range([[1], [2], [3]]) == [1, 3]
    print("All tests passed!")
