"""
Problem: Count of Smaller Numbers After Self (LC 315) | Day 14 | Hard
Topic: Searching and Sorting

Given an integer array nums, return an integer array counts where counts[i]
is the number of smaller elements to the right of nums[i].

Example 1:
  Input: nums = [5,2,6,1]
  Output: [2,1,1,0]
  Explanation:
    To the right of 5 there are 2 smaller elements (2 and 1).
    To the right of 2 there is 1 smaller element (1).
    To the right of 6 there is 1 smaller element (1).
    To the right of 1 there are 0 smaller elements.

Example 2:
  Input: nums = [-1]
  Output: [0]

Example 3:
  Input: nums = [-1,-1]
  Output: [0,0]

Constraints:
  - 1 <= nums.length <= 10^5
  - -10^4 <= nums[i] <= 10^4

Hint: Use merge sort on index-value pairs. During the merge step, when an element
      from the right half is placed before elements in the left half, update the
      count for those left-half elements.
      Alternative: Use a Binary Indexed Tree (BIT / Fenwick Tree) with coordinate
      compression.
Pattern: Merge Sort / Binary Indexed Tree
"""

from typing import List


def count_smaller(nums: List[int]) -> List[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert count_smaller([5, 2, 6, 1]) == [2, 1, 1, 0]
    assert count_smaller([-1]) == [0]
    assert count_smaller([-1, -1]) == [0, 0]
    assert count_smaller([2, 0, 1]) == [2, 0, 0]
    assert count_smaller([1, 2, 3, 4]) == [0, 0, 0, 0]
    assert count_smaller([4, 3, 2, 1]) == [3, 2, 1, 0]
    print("All tests passed!")
