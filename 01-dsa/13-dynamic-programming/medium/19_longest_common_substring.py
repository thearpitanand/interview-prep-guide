"""
Problem: Longest Common Substring (GFG) | Day 38 | Medium
Topic: Dynamic Programming

Given two strings, find the length of their longest common substring.

Example 1:
  Input: s1 = "ABCDGH", s2 = "ACDGHR"
  Output: 4  # "CDGH"

Constraints:
  - 1 <= len(s1), len(s2) <= 1000

Hint: dp[i][j] = length of common substring ending at s1[i-1] and s2[j-1]. If match, dp[i][j] = dp[i-1][j-1]+1.
Pattern: 2D DP
"""


def longest_common_substring(s1: str, s2: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert longest_common_substring("ABCDGH", "ACDGHR") == 4
    assert longest_common_substring("ABC", "ACB") == 1
    assert longest_common_substring("", "ABC") == 0
    print("All tests passed!")
