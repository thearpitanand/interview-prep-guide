"""
Problem: Longest Valid Parentheses (LC 32) | Smart-DSA Day 51 | Hard
Pattern: Stack (index tracking) or DP (left/right pass)
Time target: 35 minutes

Given a string containing just '(' and ')', return the length of the longest
valid (well-formed) parentheses substring.

Example 1:
  Input: s = "(()"
  Output: 2  (the last "()" is valid)

Example 2:
  Input: s = ")()())"
  Output: 4  ("()()" in the middle)

Example 3:
  Input: s = ""
  Output: 0

Constraints:
  - 0 <= s.length <= 3 * 10^4
  - s consists of '(' and ')' only.

Hint (⚠ read only after time budget is blown):
  Stack approach: push -1 as a base. For '(' push index. For ')': pop top;
  if stack empty push current index as new base; else result = max(result,
  i - stack[-1]). Left/right pass approach: scan left→right counting
  left/right; when equal update max; when right > left reset both. Then
  scan right→left with same logic to catch unmatched '(' prefixes.
"""


def longest_valid_parentheses(s: str) -> int:
    pass


if __name__ == "__main__":
    assert longest_valid_parentheses("(()") == 2
    assert longest_valid_parentheses(")()())") == 4
    assert longest_valid_parentheses("") == 0
    assert longest_valid_parentheses("()") == 2
    assert longest_valid_parentheses("()(()") == 2
    assert longest_valid_parentheses("(()()") == 4
    print("All tests passed!")
