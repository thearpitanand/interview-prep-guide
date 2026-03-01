"""
Problem: Longest Common Subsequence
Day: 37 | Difficulty: Medium | Topic: LCS / 2D DP
Link: https://leetcode.com/problems/longest-common-subsequence/

Description:
    Given two strings text1 and text2, return the length of their longest
    common subsequence. A subsequence is a sequence that can be derived
    from another sequence by deleting some or no elements without changing
    the order of the remaining elements.

Examples:
    Input: text1 = "abcde", text2 = "ace"
    Output: 3
    Explanation: The longest common subsequence is "ace".

    Input: text1 = "abc", text2 = "abc"
    Output: 3

    Input: text1 = "abc", text2 = "def"
    Output: 0

Constraints:
    - 1 <= text1.length, text2.length <= 1000
    - text1 and text2 consist of only lowercase English characters

Hint:
    dp[i][j] = length of LCS of text1[0..i-1] and text2[0..j-1].
    If text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
    Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    Base case: dp[0][j] = dp[i][0] = 0 (empty string).

Pattern: Classic 2D DP on two strings. Build an (m+1) x (n+1) table.
    Can be space-optimized to O(min(m, n)) using two rows.
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"text1": "abcde", "text2": "ace", "expected": 3},
        {"text1": "abc", "text2": "abc", "expected": 3},
        {"text1": "abc", "text2": "def", "expected": 0},
        {"text1": "a", "text2": "a", "expected": 1},
        {"text1": "a", "text2": "b", "expected": 0},
        {"text1": "bsbininm", "text2": "jmjkbkjkv", "expected": 1},
        {"text1": "oxcpqrsvwf", "text2": "shmtulqrypy", "expected": 2},
    ]

    for i, t in enumerate(tests):
        result = longest_common_subsequence(t["text1"], t["text2"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
