"""
Problem: Valid Anagram (LC 242) | Smart-DSA Day 1 | Easy
Pattern: Arrays & Hashing
Time target: 15 minutes

Given two strings s and t, return True if t is an anagram of s, False otherwise.
An anagram uses all the original letters exactly once.

Example 1:
  Input: s = "anagram", t = "nagaram"
  Output: True

Example 2:
  Input: s = "rat", t = "car"
  Output: False

Constraints:
  - 1 <= s.length, t.length <= 5 * 10^4
  - s and t consist of lowercase English letters.

Hint (⚠ read only after time budget is blown):
  Count character frequencies with a hash map (or Counter). If both maps are
  equal, the strings are anagrams.
"""


def is_anagram(s: str, t: str) -> bool:
    pass


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("a", "a") is True
    assert is_anagram("ab", "a") is False
    print("All tests passed!")
