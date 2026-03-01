"""
Kth Largest Element in an Array

Day: 28
Difficulty: Medium
Topic: Min Heap
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
Pattern: Top-K Elements (Min Heap of size K)

Description:
    Given an integer array nums and an integer k, return the kth largest
    element in the array.

    Note that it is the kth largest element in the sorted order, not the
    kth distinct element.

    Can you solve it without sorting?

Examples:
    Input: nums = [3, 2, 1, 5, 6, 4], k = 2
    Output: 5
    Explanation: The 2nd largest element is 5.

    Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
    Output: 4
    Explanation: The 4th largest element is 4.

Constraints:
    - 1 <= k <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4

Hint:
    Maintain a min-heap of size k. Iterate through all elements: push each
    element, and if the heap size exceeds k, pop the smallest. After
    processing all elements, the heap root is the kth largest.

Pattern:
    Top-K Elements - Use a min-heap of size K. After processing all elements,
    the root of the heap is the Kth largest element. This avoids full sorting
    and runs in O(n log k).
"""

import heapq
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: Standard case
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5, "Test 1 Failed"

    # Test 2: Duplicates present
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4, "Test 2 Failed"

    # Test 3: k = 1 (find maximum)
    assert find_kth_largest([7, 3, 1, 9, 2], 1) == 9, "Test 3 Failed"

    # Test 4: k = len(nums) (find minimum)
    assert find_kth_largest([7, 3, 1, 9, 2], 5) == 1, "Test 4 Failed"

    # Test 5: Single element
    assert find_kth_largest([42], 1) == 42, "Test 5 Failed"

    # Test 6: All same elements
    assert find_kth_largest([5, 5, 5, 5], 2) == 5, "Test 6 Failed"

    # Test 7: Negative numbers
    assert find_kth_largest([-1, -2, -3, -4], 2) == -2, "Test 7 Failed"

    print("All test cases passed!")
