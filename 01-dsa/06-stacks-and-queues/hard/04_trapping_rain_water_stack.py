"""
Trapping Rain Water (Stack Approach)

Day: 22 | Difficulty: Hard | Pattern: Stack
LeetCode 42: https://leetcode.com/problems/trapping-rain-water/

Problem:
    Given n non-negative integers representing an elevation map where the width
    of each bar is 1, compute how much water it can trap after raining.

Examples:
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The elevation map can trap 6 units of rain water.

    Input: height = [4,2,0,3,2,5]
    Output: 9

Constraints:
    - n == height.length
    - 1 <= n <= 2 * 10^4
    - 0 <= height[i] <= 10^5

Hint:
    Use a monotonic decreasing stack. When a bar taller than the stack top is
    found, it means water can be trapped. Pop the top (this is the bottom of
    the "pool"). The bounded height is min(current bar, new stack top) minus
    the popped bar's height. The width is the distance between current index
    and new stack top.

    water += (min(left_boundary, right_boundary) - bottom) * width

    Note: This problem can also be solved with two pointers or DP (prefix max),
    but the stack approach is great practice for monotonic stack patterns.

Pattern:
    Monotonic Stack (Decreasing)
    - Stack stores indices in decreasing order of height
    - When height[i] > height[stack top], water is trapped between boundaries
    - Pop the "bottom" bar, then compute trapped water:
      - bottom = height[popped]
      - bounded_height = min(height[i], height[new_stack_top]) - bottom
      - width = i - new_stack_top - 1
      - water += bounded_height * width
    - Process layer by layer (horizontal slicing), unlike the DP approach
      which works column by column (vertical slicing)
    - Time: O(n), Space: O(n)
"""

from typing import List


def trap(height: List[int]) -> int:
    pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Classic example
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "Test 1 Failed"

    # Test 2: V-shape
    assert trap([4, 2, 0, 3, 2, 5]) == 9, "Test 2 Failed"

    # Test 3: No water (increasing)
    assert trap([1, 2, 3, 4, 5]) == 0, "Test 3 Failed"

    # Test 4: No water (decreasing)
    assert trap([5, 4, 3, 2, 1]) == 0, "Test 4 Failed"

    # Test 5: Single element
    assert trap([5]) == 0, "Test 5 Failed"

    # Test 6: Two elements
    assert trap([3, 2]) == 0, "Test 6 Failed"

    # Test 7: Simple pool
    assert trap([3, 0, 3]) == 3, "Test 7 Failed"

    # Test 8: All zeros
    assert trap([0, 0, 0, 0]) == 0, "Test 8 Failed"

    # Test 9: Multiple pools
    assert trap([5, 2, 1, 2, 1, 5]) == 14, "Test 9 Failed"

    print("All test cases passed!")
