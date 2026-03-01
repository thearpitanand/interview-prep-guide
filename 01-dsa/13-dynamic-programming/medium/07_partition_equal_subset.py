"""
Problem: Partition Equal Subset Sum
Day: 38 | Difficulty: Medium | Topic: 0/1 Knapsack / Subset Sum
Link: https://leetcode.com/problems/partition-equal-subset-sum/

Description:
    Given an integer array nums, return True if you can partition the array
    into two subsets such that the sum of the elements in both subsets is equal.

Examples:
    Input: nums = [1, 5, 11, 5]
    Output: True
    Explanation: [1, 5, 5] and [11] both sum to 11.

    Input: nums = [1, 2, 3, 5]
    Output: False
    Explanation: Cannot partition into equal sum subsets.

Constraints:
    - 1 <= nums.length <= 200
    - 1 <= nums[i] <= 100

Hint:
    If total sum is odd, return False immediately. Otherwise, target = sum/2.
    Reduce to: "can we find a subset that sums to target?"
    This is a 0/1 knapsack / subset sum problem.
    dp[s] = True if we can form sum s using some subset of elements.
    dp[0] = True. For each num, iterate s from target down to num:
    dp[s] = dp[s] or dp[s - num].

Pattern: 0/1 Knapsack where capacity = total_sum / 2. Each number is used
    at most once, so iterate backwards in the 1D optimization.
"""

from typing import List


def can_partition(nums: List[int]) -> bool:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"nums": [1, 5, 11, 5], "expected": True},
        {"nums": [1, 2, 3, 5], "expected": False},
        {"nums": [1, 1], "expected": True},
        {"nums": [1, 2, 3], "expected": True},
        {"nums": [1], "expected": False},
        {"nums": [2, 2, 1, 1], "expected": True},
        {"nums": [1, 2, 5], "expected": False},
        {"nums": [100, 100, 100, 100, 100, 100, 100, 100], "expected": True},
    ]

    for i, t in enumerate(tests):
        result = can_partition(t["nums"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
