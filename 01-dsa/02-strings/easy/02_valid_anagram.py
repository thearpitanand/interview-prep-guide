"""
Problem: Valid Anagram (LC 242) | Day 9 | Easy
Topic: Strings

Given two strings s and t, return True if t is an anagram of s,
and False otherwise.

An anagram is a word or phrase formed by rearranging the letters of
a different word or phrase, using all the original letters exactly once.

Example 1:
  Input: s = "anagram", t = "nagaram"
  Output: True

Example 2:
  Input: s = "rat", t = "car"
  Output: False

Constraints:
  - 1 <= len(s), len(t) <= 5 * 10^4
  - s and t consist of lowercase English letters

Hint: Count character frequencies with a hash map or Counter. Two strings
      are anagrams if and only if their character frequency maps are identical.
Pattern: Hash Map
"""


def is_anagram(s: str, t: str) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
    assert is_anagram("a", "a") == True
    assert is_anagram("ab", "a") == False
    assert is_anagram("", "") == True
    print("All tests passed!")
