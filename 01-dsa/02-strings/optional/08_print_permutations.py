"""
Problem: Print All Permutations of String (GFG) | Optional | Medium
Topic: Strings

Given a string, return all its permutations (no duplicates if string has unique chars).

Example 1:
  Input: s = "abc"
  Output: ["abc", "acb", "bac", "bca", "cab", "cba"]

Constraints:
  - 1 <= len(s) <= 8

Hint: Backtracking: fix each character at current position, recurse on rest.
Pattern: Backtracking
"""


def string_permutations(s: str) -> list[str]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = string_permutations("abc")
    assert set(result) == {"abc", "acb", "bac", "bca", "cab", "cba"}
    assert len(string_permutations("ab")) == 2
    print("All tests passed!")
