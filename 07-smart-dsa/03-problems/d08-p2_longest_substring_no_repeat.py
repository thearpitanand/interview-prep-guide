"""
Problem: Longest Substring Without Repeating Characters (LC 3) | Smart-DSA Day 8 | Medium
Pattern: Sliding Window
Time target: 25 minutes

Given a string s, find the length of the longest substring without repeating
characters.

Example 1:
  Input: s = "abcabcbb"
  Output: 3  (substring "abc")

Example 2:
  Input: s = "bbbbb"
  Output: 1

Example 3:
  Input: s = "pwwkew"
  Output: 3  (substring "wke")

Constraints:
  - 0 <= s.length <= 5 * 10^4
  - s consists of English letters, digits, symbols, and spaces.

Hint (⚠ read only after time budget is blown):
  Expand right pointer and add each char to a set. When a duplicate is found,
  shrink from the left until the duplicate is removed. Track max window size.
"""


def length_of_longest_substring(s: str) -> int:
    pass


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    print("All tests passed!")
