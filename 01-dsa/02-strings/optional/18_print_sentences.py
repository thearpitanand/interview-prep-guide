"""
Problem: Print All Sentences from Word Lists (GFG) | Optional | Medium
Topic: Strings

Given a list of word lists, print all possible sentences by picking one word
from each list.

Example 1:
  Input: [["you", "we"], ["have", "are"], ["fun"]]
  Output: ["you have fun", "you are fun", "we have fun", "we are fun"]

Constraints:
  - 1 <= number of lists <= 10
  - 1 <= words per list <= 10

Hint: Backtracking / Cartesian product.
Pattern: Backtracking
"""


def all_sentences(word_lists: list[list[str]]) -> list[str]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = all_sentences([["you", "we"], ["have", "are"], ["fun"]])
    assert set(result) == {"you have fun", "you are fun", "we have fun", "we are fun"}
    print("All tests passed!")
