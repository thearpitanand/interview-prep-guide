"""
Problem: Print All Subsequences of a String (GFG) | Optional | Easy
Topic: Strings

Given a string, return all possible subsequences (power set of characters
maintaining order).

Example 1:
  Input: s = "abc"
  Output: ["", "a", "b", "c", "ab", "ac", "bc", "abc"]

Constraints:
  - 1 <= len(s) <= 20

Hint: Use recursion/backtracking: include or exclude each character.
Pattern: Recursion / Power Set
"""


def all_subsequences(s: str) -> list[str]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = all_subsequences("abc")
    assert set(result) == {"", "a", "b", "c", "ab", "ac", "bc", "abc"}
    assert len(all_subsequences("ab")) == 4
    print("All tests passed!")
