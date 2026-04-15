"""
Problem: Valid Parentheses (LC 20) | Smart-DSA Day 15 | Easy
Pattern: Stack
Time target: 15 minutes

Given a string s containing only the characters '(', ')', '{', '}', '[', ']',
determine if the input string is valid. A string is valid if every open bracket
is closed by the same type of bracket and in the correct order.

Example 1:
  Input: s = "()"
  Output: True

Example 2:
  Input: s = "()[]{}"
  Output: True

Example 3:
  Input: s = "(]"
  Output: False

Constraints:
  - 1 <= s.length <= 10^4
  - s consists of parentheses only '()[]{}'

Hint (⚠ read only after time budget is blown):
  Use a stack. Push open brackets. For each close bracket check that the top
  of the stack is the matching open bracket; if not (or stack empty) return
  False. At the end the stack must be empty.
"""


def is_valid(s: str) -> bool:
    pass


if __name__ == "__main__":
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("") is True
    print("All tests passed!")
