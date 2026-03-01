"""
Problem: Longest Palindromic Substring (LC 5) | Day 10 | Medium
Topic: Strings

Given a string s, return the longest palindromic substring in s.

Example 1:
  Input: s = "babad"
  Output: "bab"
  Explanation: "aba" is also a valid answer.

Example 2:
  Input: s = "cbbd"
  Output: "bb"

Constraints:
  - 1 <= len(s) <= 1000
  - s consists of only digits and English letters

Hint: For each character (and each pair of adjacent characters), expand
      outward while the characters on both sides match. This handles both
      odd-length and even-length palindromes. Time: O(n^2), Space: O(1).
Pattern: Expand Around Center
"""


def longest_palindrome(s: str) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("ac") in ("a", "c")
    assert longest_palindrome("racecar") == "racecar"
    print("All tests passed!")
