"""
Largest Rectangle in Histogram

Day: 22 | Difficulty: Hard | Pattern: Monotonic Stack
LeetCode 84: https://leetcode.com/problems/largest-rectangle-in-histogram/

Problem:
    Given an array of integers heights representing the histogram's bar height
    where the width of each bar is 1, return the area of the largest rectangle
    in the histogram.

Examples:
    Input: heights = [2,1,5,6,2,3]
    Output: 10
    Explanation: The largest rectangle has an area of 10 units (bars at index 2
    and 3, height 5, width 2).

    Input: heights = [2,4]
    Output: 4

Constraints:
    - 1 <= heights.length <= 10^5
    - 0 <= heights[i] <= 10^4

Hint:
    Use a monotonic increasing stack of indices. When a bar shorter than the
    stack top is encountered, pop and calculate the area using the popped bar's
    height. The width extends from the current index back to the new stack top.

    For each popped bar with height h:
    - Width = i - stack[-1] - 1 (if stack not empty) or i (if stack empty)
    - Area = h * width

    Process remaining bars in the stack after the loop.

Pattern:
    Monotonic Stack (Increasing)
    - Stack maintains bars in increasing height order (by index)
    - When a shorter bar arrives, pop taller bars and compute their max rectangles
    - The shorter bar acts as the right boundary
    - The bar below in the stack (after pop) is the left boundary
    - Classic problem: understanding this unlocks many monotonic stack problems
    - Time: O(n), Space: O(n)
"""

from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Mixed heights
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10, "Test 1 Failed"

    # Test 2: Two bars
    assert largest_rectangle_area([2, 4]) == 4, "Test 2 Failed"

    # Test 3: Single bar
    assert largest_rectangle_area([5]) == 5, "Test 3 Failed"

    # Test 4: All same height
    assert largest_rectangle_area([3, 3, 3, 3]) == 12, "Test 4 Failed"

    # Test 5: Increasing
    assert largest_rectangle_area([1, 2, 3, 4, 5]) == 9, "Test 5 Failed"

    # Test 6: Decreasing
    assert largest_rectangle_area([5, 4, 3, 2, 1]) == 9, "Test 6 Failed"

    # Test 7: Valley shape
    assert largest_rectangle_area([4, 2, 0, 3, 2, 5]) == 6, "Test 7 Failed"

    # Test 8: All zeros except one
    assert largest_rectangle_area([0, 0, 5, 0, 0]) == 5, "Test 8 Failed"

    print("All test cases passed!")
