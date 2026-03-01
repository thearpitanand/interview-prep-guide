"""
Problem: Valid Palindrome (LC 125) | Day 9 | Easy
Topic: Strings

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward. Alphanumeric characters include letters
and numbers.

Given a string s, return True if it is a palindrome, or False otherwise.

Example 1:
  Input: s = "A man, a plan, a canal: Panama"
  Output: True
  Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
  Input: s = "race a car"
  Output: False
  Explanation: "raceacar" is not a palindrome.

Constraints:
  - 1 <= len(s) <= 2 * 10^5
  - s consists only of printable ASCII characters

Hint: Use two pointers from both ends. Skip non-alphanumeric characters.
Pattern: Two Pointers
"""


def is_palindrome(s: str) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome(" ") == True
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("ab") == False
    print("All tests passed!")
