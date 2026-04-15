"""
Problem: Permutation in String (LC 567) | Smart-DSA Day 9 | Medium
Pattern: Sliding Window (Fixed size)
Time target: 25 minutes

Given two strings s1 and s2, return True if s2 contains a permutation of s1,
or False otherwise. In other words, return True if one of s1's permutations is
a substring of s2.

Example 1:
  Input: s1 = "ab", s2 = "eidbaooo"
  Output: True  ("ba" is at index 3)

Example 2:
  Input: s1 = "ab", s2 = "eidboaoo"
  Output: False

Constraints:
  - 1 <= s1.length, s2.length <= 10^4
  - s1 and s2 consist of lowercase English letters.

Hint (⚠ read only after time budget is blown):
  Use a fixed-size window of length len(s1) over s2. Compare frequency maps
  (or use a difference counter that tracks how many chars are "balanced").
"""


def check_inclusion(s1: str, s2: str) -> bool:
    pass


if __name__ == "__main__":
    assert check_inclusion("ab", "eidbaooo") is True
    assert check_inclusion("ab", "eidboaoo") is False
    assert check_inclusion("adc", "dcda") is True
    assert check_inclusion("hello", "ooolleoooleh") is False
    print("All tests passed!")
