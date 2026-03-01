"""
Problem: Jump Game
Day: 29 | Difficulty: Medium | Topic: Greedy
Link: https://leetcode.com/problems/jump-game/

Description:
    You are given an integer array nums. You are initially positioned at the
    array's first index, and each element in the array represents your maximum
    jump length at that position.
    Return True if you can reach the last index, or False otherwise.

Examples:
    Input: nums = [2, 3, 1, 1, 4]
    Output: True
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

    Input: nums = [3, 2, 1, 0, 4]
    Output: False
    Explanation: You will always arrive at index 3, where the value is 0.
                 You can never reach the last index.

Constraints:
    - 1 <= nums.length <= 10^4
    - 0 <= nums[i] <= 10^5

Hint:
    Track the farthest index you can reach. At each position, update the
    farthest reachable index. If you ever find yourself at a position beyond
    the farthest reachable, return False.

Pattern: Greedy - maintain the farthest reachable position. At each step,
    update farthest = max(farthest, i + nums[i]). If i > farthest, stuck.
"""

from typing import List


def can_jump(nums: List[int]) -> bool:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"nums": [2, 3, 1, 1, 4], "expected": True},
        {"nums": [3, 2, 1, 0, 4], "expected": False},
        {"nums": [0], "expected": True},
        {"nums": [1, 0], "expected": True},
        {"nums": [0, 1], "expected": False},
        {"nums": [2, 0, 0], "expected": True},
        {"nums": [1, 1, 1, 1, 1], "expected": True},
        {"nums": [5, 0, 0, 0, 0, 0], "expected": True},
    ]

    for i, t in enumerate(tests):
        result = can_jump(t["nums"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
