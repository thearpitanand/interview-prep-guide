"""
Problem: Maximum Subarray
Day: 36 | Difficulty: Easy | Topic: Kadane's Algorithm / DP
Link: https://leetcode.com/problems/maximum-subarray/

Description:
    Given an integer array nums, find the subarray with the largest sum
    and return its sum. A subarray is a contiguous non-empty sequence of
    elements within an array.

Examples:
    Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6
    Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6.

    Input: nums = [1]
    Output: 1

    Input: nums = [5, 4, -1, 7, 8]
    Output: 23

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4

Hint:
    Kadane's algorithm: at each index, either extend the current subarray
    or start a new one. dp[i] = max(nums[i], dp[i-1] + nums[i]).
    The answer is max(dp[0], dp[1], ..., dp[n-1]).
    You only need one variable for the current sum.

Pattern: Kadane's algorithm is a special form of 1D DP. Track current_sum
    and max_sum. If current_sum drops below 0, reset it to the current element.
"""

from typing import List


def max_subarray(nums: List[int]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4], "expected": 6},
        {"nums": [1], "expected": 1},
        {"nums": [5, 4, -1, 7, 8], "expected": 23},
        {"nums": [-1], "expected": -1},
        {"nums": [-2, -1], "expected": -1},
        {"nums": [1, 2, 3, 4], "expected": 10},
        {"nums": [-1, -2, -3, -4], "expected": -1},
    ]

    for i, t in enumerate(tests):
        result = max_subarray(t["nums"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
