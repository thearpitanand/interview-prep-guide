"""
Problem: Wildcard Matching (LC 44) | Day 11 | Hard
Topic: Strings

Given an input string s and a pattern p, implement wildcard pattern
matching with support for '?' and '*' where:
  - '?' matches any single character
  - '*' matches any sequence of characters (including the empty sequence)

The matching should cover the entire input string (not partial).

Example 1:
  Input: s = "aa", p = "a"
  Output: False
  Explanation: "a" does not match the entire string "aa".

Example 2:
  Input: s = "aa", p = "*"
  Output: True
  Explanation: '*' matches any sequence.

Example 3:
  Input: s = "cb", p = "?a"
  Output: False
  Explanation: '?' matches 'c', but 'a' does not match 'b'.

Example 4:
  Input: s = "adceb", p = "*a*b"
  Output: True
  Explanation: '*' matches "", 'a' matches 'a', '*' matches "dce", 'b' matches 'b'.

Constraints:
  - 0 <= len(s), len(p) <= 2000
  - s contains only lowercase English letters
  - p contains only lowercase English letters, '?' or '*'

Hint: Use a 2D DP table where dp[i][j] = True if s[:i] matches p[:j].
      - If p[j-1] == '*': dp[i][j] = dp[i-1][j] (star matches one more char)
                           OR dp[i][j-1] (star matches empty sequence)
      - If p[j-1] == '?' or p[j-1] == s[i-1]: dp[i][j] = dp[i-1][j-1]
      - Base case: dp[0][0] = True. dp[0][j] = True only if p[:j] is all '*'.
Pattern: Dynamic Programming
"""


def is_match(s: str, p: str) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert is_match("aa", "a") == False
    assert is_match("aa", "*") == True
    assert is_match("cb", "?a") == False
    assert is_match("adceb", "*a*b") == True
    assert is_match("acdcb", "a*c?b") == False
    assert is_match("", "") == True
    assert is_match("", "*") == True
    assert is_match("abc", "abc") == True
    assert is_match("abc", "a?c") == True
    assert is_match("abc", "a*c") == True
    print("All tests passed!")
