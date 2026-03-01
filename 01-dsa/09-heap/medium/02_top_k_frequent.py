"""
Top K Frequent Elements

Day: 28
Difficulty: Medium
Topic: Heap
Link: https://leetcode.com/problems/top-k-frequent-elements/
Pattern: Top-K Elements (Heap + Frequency Count)

Description:
    Given an integer array nums and an integer k, return the k most frequent
    elements. You may return the answer in any order.

Examples:
    Input: nums = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]
    Explanation: 1 appears 3 times, 2 appears 2 times. Top 2 frequent = [1, 2].

    Input: nums = [1], k = 1
    Output: [1]

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - k is in the range [1, the number of unique elements in the array].
    - It is guaranteed that the answer is unique.

Hint:
    1. Count frequencies using a dictionary or Counter.
    2. Use a min-heap of size k: push (frequency, element) tuples.
       If heap size > k, pop the smallest frequency.
    3. At the end, the heap contains the k most frequent elements.

    Alternative: Use bucket sort with frequency as index for O(n) solution.

Pattern:
    Top-K Elements - First count frequencies, then use a min-heap of size K
    to find the K elements with highest frequency. Time: O(n log k).
"""

import heapq
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: Standard case
    result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    assert sorted(result) == [1, 2], "Test 1 Failed"

    # Test 2: Single element
    assert top_k_frequent([1], 1) == [1], "Test 2 Failed"

    # Test 3: All same frequency, k equals unique count
    result = top_k_frequent([1, 2, 3], 3)
    assert sorted(result) == [1, 2, 3], "Test 3 Failed"

    # Test 4: Negative numbers
    result = top_k_frequent([-1, -1, -2, -2, -2, 3], 2)
    assert sorted(result) == [-2, -1], "Test 4 Failed"

    # Test 5: k = 1
    result = top_k_frequent([4, 4, 4, 1, 1, 2, 2, 2, 2], 1)
    assert result == [2], "Test 5 Failed"

    # Test 6: Large input with clear winners
    result = top_k_frequent([1] * 100 + [2] * 50 + [3] * 25 + [4] * 10, 2)
    assert sorted(result) == [1, 2], "Test 6 Failed"

    print("All test cases passed!")
