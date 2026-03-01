"""
Problem: Counting Bits
Day: 36 | Difficulty: Easy | Topic: DP + Bit Manipulation
Link: https://leetcode.com/problems/counting-bits/

Description:
    Given an integer n, return an array ans of length n + 1 such that for
    each i (0 <= i <= n), ans[i] is the number of 1's in the binary
    representation of i.

Examples:
    Input: n = 2
    Output: [0, 1, 1]
    Explanation: 0 -> 0, 1 -> 1, 2 -> 10

    Input: n = 5
    Output: [0, 1, 1, 2, 1, 2]
    Explanation: 0->0, 1->1, 2->10, 3->11, 4->100, 5->101

Constraints:
    - 0 <= n <= 10^5

Hint:
    Use the relation: dp[i] = dp[i >> 1] + (i & 1).
    Right-shifting i by 1 gives a number we already computed, and (i & 1)
    tells us if the last bit is 1. Alternatively: dp[i] = dp[i & (i-1)] + 1
    where i & (i-1) drops the lowest set bit.

Pattern: DP where each state depends on a previously computed state derived
    from bit manipulation. O(n) time, O(n) space for the result.
"""

from typing import List


def count_bits(n: int) -> List[int]:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"n": 2, "expected": [0, 1, 1]},
        {"n": 5, "expected": [0, 1, 1, 2, 1, 2]},
        {"n": 0, "expected": [0]},
        {"n": 1, "expected": [0, 1]},
        {"n": 8, "expected": [0, 1, 1, 2, 1, 2, 2, 3, 1]},
    ]

    for i, t in enumerate(tests):
        result = count_bits(t["n"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
