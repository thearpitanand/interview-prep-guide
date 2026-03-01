"""
Problem: Longest Valid Parentheses (LC 32) | Day 22 | Hard
Topic: Stacks and Queues

Given a string containing just '(' and ')', find the length of the longest
valid (well-formed) parentheses substring.

Example 1:
  Input: s = "(()"
  Output: 2

Example 2:
  Input: s = ")()())"
  Output: 4

Constraints:
  - 0 <= s.length <= 3 * 10^4
  - s[i] is '(' or ')'

Hint: Use stack storing indices. Push -1 as base. On ')', pop; if stack empty push current index as new base.
Pattern: Stack with Indices
"""


def longest_valid_parentheses(s: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert longest_valid_parentheses("(()") == 2
    assert longest_valid_parentheses(")()())") == 4
    assert longest_valid_parentheses("") == 0
    assert longest_valid_parentheses("()(()") == 2
    print("All tests passed!")
