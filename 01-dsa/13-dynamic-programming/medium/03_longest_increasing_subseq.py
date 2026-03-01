"""
Problem: Longest Increasing Subsequence
Day: 37 | Difficulty: Medium | Topic: LIS / DP
Link: https://leetcode.com/problems/longest-increasing-subsequence/

Description:
    Given an integer array nums, return the length of the longest strictly
    increasing subsequence. A subsequence is derived from the array by
    deleting some or no elements without changing the order of remaining
    elements.

Examples:
    Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
    Output: 4
    Explanation: The longest increasing subsequence is [2, 3, 7, 101].

    Input: nums = [0, 1, 0, 3, 2, 3]
    Output: 4

    Input: nums = [7, 7, 7, 7, 7, 7, 7]
    Output: 1

Constraints:
    - 1 <= nums.length <= 2500
    - -10^4 <= nums[i] <= 10^4

Hint:
    O(n^2) DP: dp[i] = length of LIS ending at index i. For each i, check
    all j < i: if nums[j] < nums[i], then dp[i] = max(dp[i], dp[j] + 1).
    Initialize all dp[i] = 1. Answer is max(dp).

    O(n log n) optimization: maintain a "tails" array where tails[k] is the
    smallest tail element of all increasing subsequences of length k+1.
    Use binary search to find where to place each number.

Pattern: Classic LIS. O(n^2) DP approach: for each element, check all previous
    elements to extend the longest subsequence. Can be optimized to O(n log n)
    with patience sorting (binary search on tails array).
"""

from typing import List


def length_of_lis(nums: List[int]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"nums": [10, 9, 2, 5, 3, 7, 101, 18], "expected": 4},
        {"nums": [0, 1, 0, 3, 2, 3], "expected": 4},
        {"nums": [7, 7, 7, 7, 7, 7, 7], "expected": 1},
        {"nums": [1], "expected": 1},
        {"nums": [1, 2, 3, 4, 5], "expected": 5},
        {"nums": [5, 4, 3, 2, 1], "expected": 1},
        {"nums": [3, 1, 4, 1, 5, 9, 2, 6], "expected": 4},
    ]

    for i, t in enumerate(tests):
        result = length_of_lis(t["nums"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
