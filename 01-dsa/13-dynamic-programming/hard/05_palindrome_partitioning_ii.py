"""
Problem: Palindrome Partitioning II
Day: 39 | Difficulty: Hard | Topic: String DP
Link: https://leetcode.com/problems/palindrome-partitioning-ii/

Description:
    Given a string s, partition s such that every substring of the partition
    is a palindrome. Return the minimum number of cuts needed for a
    palindrome partitioning of s.

Examples:
    Input: s = "aab"
    Output: 1
    Explanation: The palindrome partitioning ["aa", "b"] could be produced
    using 1 cut.

    Input: s = "a"
    Output: 0

    Input: s = "ab"
    Output: 1

Constraints:
    - 1 <= s.length <= 2000
    - s consists of lowercase English letters only

Hint:
    Two-step approach:
    1. Precompute is_palindrome[i][j] for all substrings using DP.
    2. dp[i] = min cuts for s[0..i]. For each j from 0 to i, if s[j..i] is
       a palindrome, then dp[i] = min(dp[i], dp[j-1] + 1). If s[0..i]
       itself is a palindrome, dp[i] = 0.

Pattern: String DP. First precompute palindrome table (expand-around-center
    or DP), then use 1D DP for minimum cuts.
"""


def min_cut(s: str) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"s": "aab", "expected": 1},
        {"s": "a", "expected": 0},
        {"s": "ab", "expected": 1},
        {"s": "aba", "expected": 0},
        {"s": "aabb", "expected": 1},
        {"s": "abcba", "expected": 0},
        {"s": "abcdef", "expected": 5},
        {"s": "aaabaa", "expected": 1},
    ]

    for i, t in enumerate(tests):
        result = min_cut(t["s"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
