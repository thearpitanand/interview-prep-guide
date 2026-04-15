"""
Problem: Longest Repeating Character Replacement (LC 424) | Smart-DSA Day 9 | Medium
Pattern: Sliding Window
Time target: 30 minutes

You are given a string s and an integer k. You can choose any character of the
string and change it to any other uppercase English character up to k times.
Return the length of the longest substring containing only one distinct character
after performing at most k such replacements.

Example 1:
  Input: s = "ABAB", k = 2
  Output: 4

Example 2:
  Input: s = "AABABBA", k = 1
  Output: 4

Constraints:
  - 1 <= s.length <= 10^5
  - s consists of only uppercase English letters.
  - 0 <= k <= s.length

Hint (⚠ read only after time budget is blown):
  Maintain a frequency map of the window. The window is valid if
  (window_size - max_freq_in_window) <= k. Expand right; if invalid, slide
  left by 1. Track the maximum valid window size.
"""


def character_replacement(s: str, k: int) -> int:
    pass


if __name__ == "__main__":
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
    assert character_replacement("AAAA", 0) == 4
    assert character_replacement("AB", 0) == 1
    print("All tests passed!")
