"""
Sort a Nearly Sorted (K-Sorted) Array

Day: 28
Difficulty: Medium
Topic: Heap
Link: https://leetcode.com/problems/find-k-closest-elements/ (variant)
Pattern: Heap Sort with Window of Size K

Description:
    Given an array of n elements where each element is at most k positions
    away from its sorted position, sort the array efficiently.

    A k-sorted array means that for every element at index i in the sorted
    array, it was originally at an index j such that |i - j| <= k.

Examples:
    Input: arr = [6, 5, 3, 2, 8, 10, 9], k = 3
    Output: [2, 3, 5, 6, 8, 9, 10]
    Explanation: Each element is at most 3 positions from its sorted position.

    Input: arr = [3, 1, 2], k = 1
    Output: [1, 2, 3]
    Explanation: Each element is at most 1 position from its sorted position.

Constraints:
    - 1 <= n <= 10^5
    - 0 <= k <= n - 1
    - 1 <= arr[i] <= 10^6

Hint:
    Use a min-heap of size k+1. The key insight is: the correct element for
    position i must be among the first k+1 unsorted elements (since each
    element is at most k positions away).

    1. Build a min-heap from the first k+1 elements.
    2. For each remaining element, pop the min (it goes to the next sorted
       position) and push the new element.
    3. Pop remaining elements from the heap.

    Time: O(n log k) instead of O(n log n) for regular sorting.

Pattern:
    Heap Sort - Use a sliding window min-heap of size k+1. Since each element
    is at most k positions away, a window of k+1 guarantees the minimum in
    the window is the correct next element.
"""

import heapq
from typing import List


def sort_nearly_sorted(arr: List[int], k: int) -> List[int]:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: Standard case
    assert sort_nearly_sorted([6, 5, 3, 2, 8, 10, 9], 3) == [
        2, 3, 5, 6, 8, 9, 10
    ], "Test 1 Failed"

    # Test 2: k = 1
    assert sort_nearly_sorted([3, 1, 2], 1) == [1, 2, 3], "Test 2 Failed"

    # Test 3: Already sorted (k = 0)
    assert sort_nearly_sorted([1, 2, 3, 4, 5], 0) == [
        1, 2, 3, 4, 5
    ], "Test 3 Failed"

    # Test 4: Reverse sorted (k = n-1)
    assert sort_nearly_sorted([5, 4, 3, 2, 1], 4) == [
        1, 2, 3, 4, 5
    ], "Test 4 Failed"

    # Test 5: Single element
    assert sort_nearly_sorted([1], 0) == [1], "Test 5 Failed"

    # Test 6: Two elements swapped
    assert sort_nearly_sorted([2, 1], 1) == [1, 2], "Test 6 Failed"

    # Test 7: Larger k-sorted array
    assert sort_nearly_sorted([2, 1, 4, 3, 6, 5], 1) == [
        1, 2, 3, 4, 5, 6
    ], "Test 7 Failed"

    print("All test cases passed!")
