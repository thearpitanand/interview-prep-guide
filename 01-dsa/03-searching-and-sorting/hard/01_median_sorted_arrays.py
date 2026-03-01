"""
Problem: Median of Two Sorted Arrays (LC 4) | Day 14 | Hard
Topic: Searching and Sorting

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log(min(m,n))).

Example 1:
  Input: nums1 = [1,3], nums2 = [2]
  Output: 2.0
  Explanation: Merged = [1,2,3]. Median = 2.0.

Example 2:
  Input: nums1 = [1,2], nums2 = [3,4]
  Output: 2.5
  Explanation: Merged = [1,2,3,4]. Median = (2+3)/2 = 2.5.

Constraints:
  - nums1.length == m
  - nums2.length == n
  - 0 <= m <= 1000
  - 0 <= n <= 1000
  - 1 <= m + n <= 2000
  - -10^6 <= nums1[i], nums2[i] <= 10^6

Hint: Binary search on the partition of the shorter array. For a partition i in
      nums1, the corresponding partition in nums2 is (m+n+1)//2 - i.
      The correct partition satisfies: nums1[i-1] <= nums2[j] and
      nums2[j-1] <= nums1[i].
Pattern: Binary Search on Partition
"""

from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
    assert find_median_sorted_arrays([], [1]) == 1.0
    assert find_median_sorted_arrays([2], []) == 2.0
    assert find_median_sorted_arrays([1, 3], [2, 7]) == 2.5
    assert find_median_sorted_arrays([0, 0], [0, 0]) == 0.0
    print("All tests passed!")
