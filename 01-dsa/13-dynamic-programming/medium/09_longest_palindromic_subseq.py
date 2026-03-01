"""
Problem: Longest Palindromic Subsequence
Day: 38 | Difficulty: Medium | Topic: String DP
Link: https://leetcode.com/problems/longest-palindromic-subsequence/

Description:
    Given a string s, find the longest palindromic subsequence's length in s.
    A subsequence is a sequence that can be derived from another sequence by
    deleting some or no elements without changing the order of the remaining
    elements.

Examples:
    Input: s = "bbbab"
    Output: 4
    Explanation: One possible longest palindromic subsequence is "bbbb".

    Input: s = "cbbd"
    Output: 2
    Explanation: One possible longest palindromic subsequence is "bb".

Constraints:
    - 1 <= s.length <= 1000
    - s consists only of lowercase English letters

Hint:
    This is equivalent to finding the LCS of s and reverse(s).
    Alternatively, use interval DP: dp[i][j] = length of longest palindromic
    subsequence in s[i..j].
    If s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
    Else: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    Base case: dp[i][i] = 1.

Pattern: String DP / Interval DP. Can also be reduced to LCS(s, reverse(s)).
    Fill the table by increasing interval length.
"""


def longest_palindrome_subseq(s: str) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"s": "bbbab", "expected": 4},
        {"s": "cbbd", "expected": 2},
        {"s": "a", "expected": 1},
        {"s": "abcba", "expected": 5},
        {"s": "abcd", "expected": 1},
        {"s": "aab", "expected": 2},
        {"s": "euazbipzncptldueebcbtszigatconspoapottpomnipattyiqaeyuvhwas", "expected": 15},
    ]

    for i, t in enumerate(tests):
        result = longest_palindrome_subseq(t["s"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
