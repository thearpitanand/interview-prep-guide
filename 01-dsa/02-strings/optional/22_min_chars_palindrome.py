"""
Problem: Min Chars to Add at Front for Palindrome (GFG) | Optional | Hard
Topic: Strings

Given a string, find the minimum number of characters to add at the front
to make it a palindrome.

Example 1:
  Input: s = "abc"
  Output: 2  # add "cb" -> "cbabc"

Constraints:
  - 1 <= len(s) <= 10^6

Hint: Use KMP failure function on s + "$" + reverse(s).
Pattern: KMP / String Matching
"""


def min_chars_palindrome(s: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert min_chars_palindrome("abc") == 2
    assert min_chars_palindrome("aacecaaa") == 1
    assert min_chars_palindrome("abcd") == 3
    print("All tests passed!")
