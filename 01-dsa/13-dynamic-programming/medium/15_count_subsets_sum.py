"""
Problem: Count Subsets with Given Sum
Day: 39 | Difficulty: Medium | Topic: 0/1 Knapsack
Link: Classic DP problem

Description:
    Given an array of positive integers and a target sum, count the number
    of subsets of the array that sum to exactly the target.

Examples:
    Input: nums = [2, 3, 5, 6, 8, 10], target = 10
    Output: 3
    Explanation: Subsets: {2,8}, {2,3,5}, {10}. Three subsets sum to 10.

    Input: nums = [1, 2, 3], target = 3
    Output: 2
    Explanation: Subsets: {3}, {1,2}. Two subsets sum to 3.

Constraints:
    - 1 <= nums.length <= 20
    - 1 <= nums[i] <= 100
    - 0 <= target <= 1000

Hint:
    dp[s] = number of subsets that sum to s.
    dp[0] = 1 (empty subset). For each number, iterate s from target down
    to num: dp[s] += dp[s - num]. This is the 0/1 knapsack counting variant.

Pattern: 0/1 Knapsack counting. Each element is used at most once (iterate
    backwards). Instead of max, we sum the count of ways.
"""

from typing import List


def count_subsets(nums: List[int], target: int) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"nums": [2, 3, 5, 6, 8, 10], "target": 10, "expected": 3},
        {"nums": [1, 2, 3], "target": 3, "expected": 2},
        {"nums": [1, 1, 1, 1], "target": 2, "expected": 6},
        {"nums": [5], "target": 5, "expected": 1},
        {"nums": [5], "target": 3, "expected": 0},
        {"nums": [1, 2, 3, 4, 5], "target": 10, "expected": 3},
    ]

    for i, t in enumerate(tests):
        result = count_subsets(t["nums"], t["target"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
