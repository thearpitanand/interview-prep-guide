"""
Problem: Recursively Remove Adjacent Duplicates (GFG) | Optional | Easy
Topic: Strings

Given a string, recursively remove adjacent duplicates until no more can be removed.

Example 1:
  Input: s = "azxxzy"
  Output: "ay"  # azxxzy -> azzy -> ay

Constraints:
  - 1 <= len(s) <= 10^3

Hint: Use a stack or repeat passes until stable.
Pattern: Stack
"""


def remove_adjacent_dups(s: str) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert remove_adjacent_dups("azxxzy") == "ay"
    assert remove_adjacent_dups("geeksforgeek") == "gksforgg" or remove_adjacent_dups("geeksforgeek") == "gksforgeek"  # depends on interpretation
    assert remove_adjacent_dups("abc") == "abc"
    print("All tests passed!")
