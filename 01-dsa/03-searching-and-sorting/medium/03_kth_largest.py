"""
Problem: Kth Largest Element in an Array (LC 215) | Day 13 | Medium
Topic: Searching and Sorting

Given an integer array nums and an integer k, return the kth largest element
in the array.

Note that it is the kth largest element in the sorted order, not the kth
distinct element.

Can you solve it without sorting?

Example 1:
  Input: nums = [3,2,1,5,6,4], k = 2
  Output: 5

Example 2:
  Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
  Output: 4

Constraints:
  - 1 <= k <= nums.length <= 10^5
  - -10^4 <= nums[i] <= 10^4

Hint: Quick Select: partition around a random pivot. If pivot lands at index
      n-k, that's the answer. Otherwise recurse on the correct half.
      Alternative: Use a min-heap of size k.
Pattern: Quick Select / Heap
"""

from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest([1], 1) == 1
    assert find_kth_largest([7, 6, 5, 4, 3, 2, 1], 5) == 3
    print("All tests passed!")
