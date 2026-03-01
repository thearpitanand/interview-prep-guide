"""
Problem: Minimum Window Substring (LC 76) | Day 11 | Hard
Topic: Strings

Given two strings s and t of lengths m and n respectively, return the
minimum window substring of s such that every character in t (including
duplicates) is included in the window. If there is no such substring,
return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
  Input: s = "ADOBECODEBANC", t = "ABC"
  Output: "BANC"
  Explanation: The minimum window substring "BANC" includes 'A', 'B',
  and 'C' from string t.

Example 2:
  Input: s = "a", t = "a"
  Output: "a"

Example 3:
  Input: s = "a", t = "aa"
  Output: ""
  Explanation: Both 'a's from t must be included, but s only has one 'a'.

Constraints:
  - m == len(s), n == len(t)
  - 1 <= m, n <= 10^5
  - s and t consist of uppercase and lowercase English letters

Hint: Use a sliding window with two pointers. Maintain a frequency map of
      characters in t. Expand right to include characters; once all chars
      in t are covered, shrink from left to find the minimum window.
      Track how many unique characters have been fully satisfied.
Pattern: Sliding Window
"""
from collections import Counter


def min_window(s: str, t: str) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("aa", "aa") == "aa"
    assert min_window("cabwefgewcwaefgcf", "cae") == "cwae"
    print("All tests passed!")
