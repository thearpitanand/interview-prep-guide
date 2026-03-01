"""
Problem: Word Break Using Backtracking (GFG) | Optional | Medium
Topic: Backtracking

Given a string and a dictionary, determine if the string can be segmented
into space-separated dictionary words. Print all possible segmentations.

Example 1:
  Input: s = "catsanddog", dict = ["cat", "cats", "and", "sand", "dog"]
  Output: ["cat sand dog", "cats and dog"]

Constraints:
  - 1 <= len(s) <= 100

Hint: Backtrack: try all prefixes that are in dictionary, recurse on suffix.
Pattern: Backtracking
"""


def word_break(s: str, word_dict: list[str]) -> list[str]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"])
    assert set(result) == {"cat sand dog", "cats and dog"}
    assert word_break("abc", ["a", "b"]) == []
    print("All tests passed!")
