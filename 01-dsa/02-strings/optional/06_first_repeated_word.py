"""
Problem: First Repeated Word in String (GFG) | Optional | Easy
Topic: Strings

Given a string of words separated by spaces, find the first word that repeats.

Example 1:
  Input: s = "he had had quite enough of this"
  Output: "had"

Constraints:
  - 1 <= number of words <= 10^4

Hint: Use a set to track seen words.
Pattern: Hashing
"""


def first_repeated_word(s: str) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert first_repeated_word("he had had quite enough of this") == "had"
    assert first_repeated_word("ab ca bc ab") == "ab"
    assert first_repeated_word("ab ca bc") is None
    print("All tests passed!")
