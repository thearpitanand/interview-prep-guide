"""
Problem: Minimum Window Substring (LC 76) | Smart-DSA Day 10 | Hard
Pattern: Sliding Window
Time target: 40 minutes

Given two strings s and t, return the minimum window substring of s such that
every character in t (including duplicates) is included in the window.
Return "" if no valid window exists.

Example 1:
  Input: s = "ADOBECODEBANC", t = "ABC"
  Output: "BANC"

Example 2:
  Input: s = "a", t = "a"
  Output: "a"

Example 3:
  Input: s = "a", t = "aa"
  Output: ""

Constraints:
  - 1 <= s.length, t.length <= 10^5
  - s and t consist of uppercase and lowercase English letters.

Hint (⚠ read only after time budget is blown):
  Track a need count (chars still required) and have count. Expand right to
  satisfy all needs; once satisfied, shrink left to minimize the window.
  Record the minimum valid window each time all chars are covered.
"""


def min_window(s: str, t: str) -> str:
    pass


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("aa", "aa") == "aa"
    print("All tests passed!")
