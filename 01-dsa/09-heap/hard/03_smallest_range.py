"""
Smallest Range Covering Elements from K Lists

Day: 28
Difficulty: Hard
Topic: Heap + Sliding Window
Link: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
Pattern: Heap with Tracking Max (Merge K Sorted variant)

Description:
    You have k lists of sorted integers in non-decreasing order. Find the
    smallest range [a, b] that includes at least one number from each of
    the k lists.

    We define the range [a, b] is smaller than range [c, d] if:
        b - a < d - c, or
        a < c if b - a == d - c.

Examples:
    Input: nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    Output: [20, 24]
    Explanation:
        List 1: [4, 10, 15, 24, 26], 24 is in range [20, 24].
        List 2: [0, 9, 12, 20], 20 is in range [20, 24].
        List 3: [5, 18, 22, 30], 22 is in range [20, 24].

    Input: nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    Output: [1, 1]

Constraints:
    - nums.length == k
    - 1 <= k <= 3500
    - 1 <= nums[i].length <= 50
    - -10^5 <= nums[i][j] <= 10^5
    - nums[i] is sorted in non-decreasing order.

Hint:
    Think of this as a variation of "Merge K Sorted Lists".

    1. Initialize a min-heap with the first element from each list.
       Track the current maximum across all elements in the heap.
    2. The range is [heap_min, current_max].
    3. Pop the minimum element, advance in that list, push the next element.
       Update current_max if needed.
    4. The range shrinks when we advance the minimum. Track the best range.
    5. Stop when any list is exhausted (we can no longer cover all lists).

    Time: O(N log K) where N = total elements across all lists.
    Space: O(K) for the heap.

Pattern:
    Heap + Tracking Max - Similar to Merge K Sorted, but instead of building
    a merged list, we track the range [min, max] of current elements in the
    heap and try to minimize it by advancing the minimum pointer.
"""

import heapq
from typing import List


def smallest_range(nums: List[List[int]]) -> List[int]:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: Standard case
    assert smallest_range(
        [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    ) == [20, 24], "Test 1 Failed"

    # Test 2: All lists have same elements
    assert smallest_range(
        [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    ) == [1, 1], "Test 2 Failed"

    # Test 3: Single list
    assert smallest_range([[1, 2, 3]]) == [1, 1], "Test 3 Failed"

    # Test 4: Two lists, no overlap
    assert smallest_range([[1, 2], [3, 4]]) == [2, 3], "Test 4 Failed"

    # Test 5: Two lists with overlap
    assert smallest_range([[1, 5, 8], [4, 12]]) == [4, 5], "Test 5 Failed"

    # Test 6: Negative numbers
    assert smallest_range(
        [[-5, -3, -1], [-4, -2, 0]]
    ) == [-3, -2], "Test 6 Failed"

    # Test 7: Single element in each list
    assert smallest_range([[1], [2], [3]]) == [1, 3], "Test 7 Failed"

    print("All test cases passed!")
