"""
Problem: Climbing Stairs
Day: 36 | Difficulty: Easy | Topic: 1D DP (Fibonacci-style)
Link: https://leetcode.com/problems/climbing-stairs/

Description:
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps.
    In how many distinct ways can you climb to the top?

Examples:
    Input: n = 2
    Output: 2
    Explanation: (1+1) or (2). Two ways.

    Input: n = 3
    Output: 3
    Explanation: (1+1+1), (1+2), (2+1). Three ways.

    Input: n = 5
    Output: 8

Constraints:
    - 1 <= n <= 45

Hint:
    The number of ways to reach step i is the sum of ways to reach step i-1
    (take 1 step) and step i-2 (take 2 steps). This is exactly the Fibonacci
    sequence: dp[i] = dp[i-1] + dp[i-2].

Pattern: Fibonacci-style 1D DP. Only need the previous two values, so you
    can optimize to O(1) space.
"""


def climb_stairs(n: int) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"n": 1, "expected": 1},
        {"n": 2, "expected": 2},
        {"n": 3, "expected": 3},
        {"n": 5, "expected": 8},
        {"n": 10, "expected": 89},
        {"n": 45, "expected": 1836311903},
    ]

    for i, t in enumerate(tests):
        result = climb_stairs(t["n"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
