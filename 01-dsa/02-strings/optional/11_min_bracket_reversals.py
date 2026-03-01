"""
Problem: Min Bracket Reversals for Balanced (GFG) | Optional | Medium
Topic: Strings

Given a string of only '{' and '}', find the minimum number of bracket
reversals needed to make it balanced. Return -1 if not possible (odd length).

Example 1:
  Input: s = "}}{{"
  Output: 2

Constraints:
  - 1 <= len(s) <= 10^5

Hint: Remove matched pairs, then count remaining open/close.
Pattern: Stack
"""


def min_bracket_reversals(s: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert min_bracket_reversals("}}{{") == 2
    assert min_bracket_reversals("}{") == 2
    assert min_bracket_reversals("{}}") == -1  # odd length
    assert min_bracket_reversals("{}") == 0
    print("All tests passed!")
