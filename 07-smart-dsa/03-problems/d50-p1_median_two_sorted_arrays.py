"""
Problem: Median of Two Sorted Arrays (LC 4) | Smart-DSA Day 50 | Hard
Pattern: Binary Search — partition on shorter array
Time target: 40 minutes

Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays. The overall run time complexity must be
O(log(m + n)).

Example 1:
  Input: nums1 = [1, 3], nums2 = [2]
  Output: 2.0  (merged: [1,2,3])

Example 2:
  Input: nums1 = [1, 2], nums2 = [3, 4]
  Output: 2.5  (merged: [1,2,3,4], median = (2+3)/2)

Constraints:
  - nums1.length == m, nums2.length == n
  - 0 <= m, n <= 1000
  - 1 <= m + n <= 2000
  - -10^6 <= nums1[i], nums2[i] <= 10^6

Hint (⚠ read only after time budget is blown):
  Binary search on the partition index of the shorter array.
  Partition both arrays such that left halves together form the smaller half
  of the merged array. Valid partition: max(left1, left2) <= min(right1, right2).
  Adjust partition using binary search. Handle odd/even total length differently.
  Always binary search on the shorter array to keep O(log(min(m,n))).
"""


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    pass


if __name__ == "__main__":
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
    assert find_median_sorted_arrays([0, 0], [0, 0]) == 0.0
    assert find_median_sorted_arrays([], [1]) == 1.0
    assert find_median_sorted_arrays([2], []) == 2.0
    assert find_median_sorted_arrays([1, 3], [2, 4]) == 2.5
    print("All tests passed!")
