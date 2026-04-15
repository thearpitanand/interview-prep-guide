"""
Problem: Longest Common Subsequence (LC 1143) | Smart-DSA Day 44 | Medium
Pattern: Dynamic Programming — 2D String DP
Time target: 30 minutes

Given two strings text1 and text2, return the length of their longest common
subsequence. A subsequence is a sequence derived by deleting some (or no)
characters without changing the relative order of remaining characters.
If there is no common subsequence, return 0.

Example 1:
  Input: text1 = "abcde", text2 = "ace"
  Output: 3  (subsequence "ace")

Example 2:
  Input: text1 = "abc", text2 = "abc"
  Output: 3

Example 3:
  Input: text1 = "abc", text2 = "def"
  Output: 0

Constraints:
  - 1 <= text1.length, text2.length <= 1000
  - text1 and text2 consist of lowercase English letters only.

Hint (⚠ read only after time budget is blown):
  dp[i][j] = LCS length for text1[:i] and text2[:j].
  If text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1.
  Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1]).
  Base case: first row and column are all 0. Answer is dp[m][n].
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    pass


if __name__ == "__main__":
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("bl", "yby") == 1
    assert longest_common_subsequence("oxcpqrsvwf", "shmtulqrypy") == 2
    print("All tests passed!")
