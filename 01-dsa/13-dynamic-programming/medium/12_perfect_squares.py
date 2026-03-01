"""
Problem: Perfect Squares
Day: 38 | Difficulty: Medium | Topic: Unbounded Knapsack / DP
Link: https://leetcode.com/problems/perfect-squares/

Description:
    Given an integer n, return the least number of perfect square numbers
    that sum to n. A perfect square is an integer that is the square of an
    integer (e.g., 1, 4, 9, 16, ...).

Examples:
    Input: n = 12
    Output: 3
    Explanation: 12 = 4 + 4 + 4

    Input: n = 13
    Output: 2
    Explanation: 13 = 4 + 9

Constraints:
    - 1 <= n <= 10^4

Hint:
    Think of this as a coin change problem where the "coins" are perfect
    squares (1, 4, 9, 16, ...). dp[i] = minimum number of perfect squares
    that sum to i. dp[0] = 0. For each i, try all perfect squares j*j <= i:
    dp[i] = min(dp[i], dp[i - j*j] + 1).

Pattern: Unbounded knapsack variant. The "coins" are 1, 4, 9, 16, ...
    Each square can be used unlimited times. Same structure as Coin Change.
"""


def num_squares(n: int) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"n": 12, "expected": 3},
        {"n": 13, "expected": 2},
        {"n": 1, "expected": 1},
        {"n": 4, "expected": 1},
        {"n": 7, "expected": 4},
        {"n": 100, "expected": 1},
        {"n": 48, "expected": 3},
    ]

    for i, t in enumerate(tests):
        result = num_squares(t["n"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
