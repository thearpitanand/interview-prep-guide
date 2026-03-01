"""
Problem: Isomorphic Strings (LC 205) | Day 9 | Easy
Topic: Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced
to get t, with the following rules:
  - Each character in s maps to exactly one character in t.
  - No two characters in s map to the same character in t.
  - The mapping must preserve the order of characters.

Example 1:
  Input: s = "egg", t = "add"
  Output: True
  Explanation: e->a, g->d. Mapping is consistent and one-to-one.

Example 2:
  Input: s = "foo", t = "bar"
  Output: False
  Explanation: o cannot map to both 'a' and 'r'.

Example 3:
  Input: s = "paper", t = "title"
  Output: True

Constraints:
  - 1 <= len(s) <= 5 * 10^4
  - len(s) == len(t)
  - s and t consist of any valid ASCII character

Hint: Use two hash maps for bidirectional mapping (s->t and t->s). If any
      character already has a conflicting mapping, return False.
Pattern: Hash Map
"""


def is_isomorphic(s: str, t: str) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert is_isomorphic("egg", "add") == True
    assert is_isomorphic("foo", "bar") == False
    assert is_isomorphic("paper", "title") == True
    assert is_isomorphic("badc", "baba") == False
    assert is_isomorphic("a", "b") == True
    print("All tests passed!")
