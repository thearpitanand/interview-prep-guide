"""
Problem: Reverse Words in a String (LC 151) | Day 9 | Easy
Topic: Strings

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s
will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note: s may contain leading or trailing spaces or multiple spaces between
two words. The returned string should only have a single space separating
the words. Do not include any extra spaces.

Example 1:
  Input: s = "the sky is blue"
  Output: "blue is sky the"

Example 2:
  Input: s = "  hello world  "
  Output: "world hello"

Example 3:
  Input: s = "a good   example"
  Output: "example good a"

Constraints:
  - 1 <= len(s) <= 10^4
  - s contains English letters (upper and lower case), digits, and spaces ' '
  - There is at least one word in s

Hint: split() without arguments splits on any whitespace and removes empty strings.
      Then reverse the list and join with a single space.
Pattern: String Manipulation
"""


def reverse_words(s: str) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words("  hello world  ") == "world hello"
    assert reverse_words("a good   example") == "example good a"
    assert reverse_words("word") == "word"
    print("All tests passed!")
