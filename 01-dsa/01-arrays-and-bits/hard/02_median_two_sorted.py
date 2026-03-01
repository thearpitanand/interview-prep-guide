"""
Problem: Median of Two Sorted Arrays (LC 4) | Day 6 | Hard
Topic: Arrays

Find the median of two sorted arrays in O(log(m+n)) time.

Example 1:
  Input: nums1 = [1,3], nums2 = [2]
  Output: 2.0

Example 2:
  Input: nums1 = [1,2], nums2 = [3,4]
  Output: 2.5

Hint: Binary search on the shorter array to find correct partition.
Pattern: Binary Search
"""


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
    assert find_median_sorted_arrays([], [1]) == 1.0
    print("All tests passed!")
