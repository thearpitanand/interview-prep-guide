"""
Sliding Window Maximum

Day: 22 | Difficulty: Hard | Pattern: Monotonic Deque
LeetCode 239: https://leetcode.com/problems/sliding-window-maximum/

Problem:
    You are given an array of integers nums, there is a sliding window of size k
    which is moving from the very left of the array to the very right. You can
    only see the k numbers in the window. Each time the sliding window moves
    right by one position.

    Return the max sliding window.

Examples:
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    Explanation:
        Window position                Max
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       3
         1 [3  -1  -3] 5  3  6  7       3
         1  3 [-1  -3  5] 3  6  7       5
         1  3  -1 [-3  5  3] 6  7       5
         1  3  -1  -3 [5  3  6] 7       6
         1  3  -1  -3  5 [3  6  7]      7

    Input: nums = [1], k = 1
    Output: [1]

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - 1 <= k <= nums.length

Hint:
    Use a monotonic decreasing deque that stores indices. The front of the
    deque is always the index of the maximum element in the current window.

    For each element:
    1. Remove indices from the front that are out of the window
    2. Remove indices from the back that have values smaller than current
    3. Add current index to the back
    4. If window is full (i >= k-1), record deque front as the max

Pattern:
    Monotonic Deque (Decreasing)
    - Deque stores indices in decreasing order of their values
    - Front of deque = index of current window's maximum
    - Remove from back: smaller values that will never be the max
    - Remove from front: indices that fall outside the window
    - Time: O(n), Space: O(k)
    - Each element is added and removed from the deque at most once
"""

from typing import List
from collections import deque


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Standard case
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7], "Test 1 Failed"

    # Test 2: Single element
    assert max_sliding_window([1], 1) == [1], "Test 2 Failed"

    # Test 3: Window size equals array
    assert max_sliding_window([1, 3, 2], 3) == [3], "Test 3 Failed"

    # Test 4: All same elements
    assert max_sliding_window([5, 5, 5, 5], 2) == [5, 5, 5], "Test 4 Failed"

    # Test 5: Decreasing array
    assert max_sliding_window([5, 4, 3, 2, 1], 3) == [5, 4, 3], "Test 5 Failed"

    # Test 6: Increasing array
    assert max_sliding_window([1, 2, 3, 4, 5], 3) == [3, 4, 5], "Test 6 Failed"

    # Test 7: Window size 1
    assert max_sliding_window([3, 1, 4, 1, 5], 1) == [3, 1, 4, 1, 5], "Test 7 Failed"

    # Test 8: Negative numbers
    assert max_sliding_window([-1, -3, -5, -2, -4], 2) == [-1, -3, -2, -2], "Test 8 Failed"

    print("All test cases passed!")
