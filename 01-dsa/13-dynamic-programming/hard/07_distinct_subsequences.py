"""
Problem: Distinct Subsequences
Day: 39 | Difficulty: Hard | Topic: String DP
Link: https://leetcode.com/problems/distinct-subsequences/

Description:
    Given two strings s and t, return the number of distinct subsequences
    of s which equals t. The answer is guaranteed to fit on a 32-bit
    signed integer.

Examples:
    Input: s = "rabbbit", t = "rabbit"
    Output: 3
    Explanation: There are 3 ways to choose "rabbit" from "rabbbit":
    ra_bbit, rab_bit, rabb_it (underscores mark the skipped 'b').

    Input: s = "babgbag", t = "bag"
    Output: 5

Constraints:
    - 1 <= s.length, t.length <= 1000
    - s and t consist of English letters

Hint:
    dp[i][j] = number of distinct subsequences of s[0..i-1] that equal t[0..j-1].
    Base cases: dp[i][0] = 1 (empty t matches any prefix), dp[0][j] = 0 for j > 0.
    If s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        (use this char OR skip it)
    Else: dp[i][j] = dp[i-1][j] (must skip this char)

Pattern: 2D string DP. When characters match, we can either use the match
    (diagonal) or skip it (above). When they don't match, we must skip (above).
    Can be space-optimized to O(t.length).
"""


def num_distinct(s: str, t: str) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"s": "rabbbit", "t": "rabbit", "expected": 3},
        {"s": "babgbag", "t": "bag", "expected": 5},
        {"s": "a", "t": "a", "expected": 1},
        {"s": "a", "t": "b", "expected": 0},
        {"s": "aaa", "t": "a", "expected": 3},
        {"s": "aaa", "t": "aa", "expected": 3},
        {"s": "abc", "t": "abc", "expected": 1},
        {"s": "abc", "t": "abcd", "expected": 0},
    ]

    for i, t_case in enumerate(tests):
        result = num_distinct(t_case["s"], t_case["t"])
        status = "PASS" if result == t_case["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t_case['expected']}, Got: {result}")
