"""
Problem: Merge Sorted Array (LC 88) | Day 12 | Easy
Topic: Searching and Sorting

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2
respectively.

Merge nums2 into nums1 as one sorted array. The final sorted array should be
stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
where the last n elements are set to 0 and should be ignored.

Example 1:
  Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
  Output: [1,2,2,3,5,6]

Example 2:
  Input: nums1 = [1], m = 1, nums2 = [], n = 0
  Output: [1]

Constraints:
  - nums1.length == m + n
  - nums2.length == n
  - 0 <= m, n <= 200
  - -10^9 <= nums1[i], nums2[j] <= 10^9

Hint: Merge from the END of both arrays to avoid overwriting elements.
      Use three pointers: p1 at m-1, p2 at n-1, write pointer at m+n-1.
Pattern: Two Pointers (Merge from Back)
"""

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # Write your solution here (modify nums1 in-place)
    pass


# --- Tests ---
if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    merge(nums1, 1, [], 0)
    assert nums1 == [1]

    nums1 = [0]
    merge(nums1, 0, [1], 1)
    assert nums1 == [1]

    nums1 = [4, 5, 6, 0, 0, 0]
    merge(nums1, 3, [1, 2, 3], 3)
    assert nums1 == [1, 2, 3, 4, 5, 6]

    print("All tests passed!")
