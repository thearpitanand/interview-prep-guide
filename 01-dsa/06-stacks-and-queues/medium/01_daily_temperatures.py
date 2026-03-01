"""
Daily Temperatures

Day: 21 | Difficulty: Medium | Pattern: Monotonic Stack
LeetCode 739: https://leetcode.com/problems/daily-temperatures/

Problem:
    Given an array of integers temperatures represents the daily temperatures,
    return an array answer such that answer[i] is the number of days you have
    to wait after the ith day to get a warmer temperature. If there is no
    future day for which this is possible, keep answer[i] == 0 instead.

Examples:
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]

    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]

    Input: temperatures = [30,60,90]
    Output: [1,1,0]

Constraints:
    - 1 <= temperatures.length <= 10^5
    - 30 <= temperatures[i] <= 100

Hint:
    Use a monotonic decreasing stack of indices. For each new temperature,
    pop indices from the stack while the current temperature is warmer than
    the temperature at the stack's top index. The difference in indices gives
    the number of days to wait.

Pattern:
    Monotonic Stack (Decreasing)
    - Stack stores indices of temperatures in decreasing order
    - When current temp > temp at stack top: pop and compute difference
    - This finds the "next greater element" (next warmer day)
    - Time: O(n), Space: O(n)
"""

from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Mixed temperatures
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0], "Test 1 Failed"

    # Test 2: Strictly increasing
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0], "Test 2 Failed"

    # Test 3: Short increasing
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0], "Test 3 Failed"

    # Test 4: Strictly decreasing
    assert daily_temperatures([90, 80, 70, 60]) == [0, 0, 0, 0], "Test 4 Failed"

    # Test 5: Single element
    assert daily_temperatures([50]) == [0], "Test 5 Failed"

    # Test 6: All same
    assert daily_temperatures([70, 70, 70]) == [0, 0, 0], "Test 6 Failed"

    print("All test cases passed!")
