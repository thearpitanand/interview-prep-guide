"""
Problem: Remove Invalid Parentheses (LC 301) | Day 32 | Hard
Topic: Backtracking

Given a string with parentheses and letters, remove the minimum number of
invalid parentheses to make it valid. Return all unique results.

Example 1:
  Input: s = "()())()"
  Output: ["(())()", "()()()"]

Example 2:
  Input: s = "(a)())()"
  Output: ["(a())()", "(a)()()"]

Constraints:
  - 1 <= s.length <= 25
  - s consists of '(', ')' and lowercase English letters

Hint: BFS level by level (remove one paren at a time) or count mismatched parens and backtrack.
Pattern: BFS / Backtracking
"""


def remove_invalid_parentheses(s: str) -> list[str]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert set(remove_invalid_parentheses("()())()")) == {"(())()", "()()()"}
    assert set(remove_invalid_parentheses("(a)())()")) == {"(a())()", "(a)()()"}
    assert remove_invalid_parentheses(")(") == [""]
    print("All tests passed!")
