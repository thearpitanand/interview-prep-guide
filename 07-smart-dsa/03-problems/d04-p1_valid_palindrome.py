"""
Problem: Valid Palindrome (LC 125) | Smart-DSA Day 4 | Easy
Pattern: Two Pointers
Time target: 15 minutes

A phrase is a palindrome if, after converting all uppercase letters to lowercase
and removing all non-alphanumeric characters, it reads the same forward and
backward. Given a string s, return True if it is a palindrome, False otherwise.

Example 1:
  Input: s = "A man, a plan, a canal: Panama"
  Output: True

Example 2:
  Input: s = "race a car"
  Output: False

Example 3:
  Input: s = " "
  Output: True

Constraints:
  - 1 <= s.length <= 2 * 10^5
  - s consists only of printable ASCII characters.

Hint (⚠ read only after time budget is blown):
  Use two pointers: left starts at 0, right starts at end. Skip non-alphanumeric
  characters. Compare lowercased chars; if mismatch return False.
"""


def is_palindrome(s: str) -> bool:
    pass


if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("0P") is False
    print("All tests passed!")
