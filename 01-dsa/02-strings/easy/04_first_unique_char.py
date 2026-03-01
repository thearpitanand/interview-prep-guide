"""
Problem: First Unique Character in a String (LC 387) | Day 9 | Easy
Topic: Strings

Given a string s, find the first non-repeating character in it and return
its index. If it does not exist, return -1.

Example 1:
  Input: s = "leetcode"
  Output: 0
  Explanation: 'l' appears once and is the first character.

Example 2:
  Input: s = "loveleetcode"
  Output: 2
  Explanation: 'v' appears once at index 2 (the first unique).

Example 3:
  Input: s = "aabb"
  Output: -1
  Explanation: No unique character exists.

Constraints:
  - 1 <= len(s) <= 10^5
  - s consists of only lowercase English letters

Hint: First pass: build a frequency map. Second pass: find the first char
      with frequency 1. Total O(n) time.
Pattern: Hash Map
"""


def first_uniq_char(s: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert first_uniq_char("leetcode") == 0
    assert first_uniq_char("loveleetcode") == 2
    assert first_uniq_char("aabb") == -1
    assert first_uniq_char("a") == 0
    assert first_uniq_char("aadadaad") == -1
    print("All tests passed!")
