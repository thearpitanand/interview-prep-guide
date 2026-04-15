"""
Problem: Longest Palindromic Substring (LC 5) | Smart-DSA Day 46 | Medium
Pattern: Expand-Around-Center (or 2D DP)
Time target: 30 minutes

Given a string s, return the longest palindromic substring in s.
A palindrome reads the same forwards and backwards.

Example 1:
  Input: s = "babad"
  Output: "bab"  ("aba" is also valid)

Example 2:
  Input: s = "cbbd"
  Output: "bb"

Constraints:
  - 1 <= s.length <= 1000
  - s consists of digits and lowercase English letters.

Hint (⚠ read only after time budget is blown):
  For each center (treat both odd and even length centers), expand outward
  while characters match. Track the longest seen. Two centers per index:
  s[i] alone (odd-length) and s[i], s[i+1] together (even-length).
  O(n²) time, O(1) space — preferred over 2D DP for interviews.
"""


def longest_palindrome(s: str) -> str:
    pass


if __name__ == "__main__":
    # Multiple valid answers possible; check palindrome property and length
    result1 = longest_palindrome("babad")
    assert result1 in ("bab", "aba"), f"Expected 'bab' or 'aba', got {result1}"

    result2 = longest_palindrome("cbbd")
    assert result2 == "bb", f"Expected 'bb', got {result2}"

    result3 = longest_palindrome("a")
    assert result3 == "a"

    result4 = longest_palindrome("racecar")
    assert result4 == "racecar"

    result5 = longest_palindrome("ac")
    assert result5 in ("a", "c")

    print("All tests passed!")
