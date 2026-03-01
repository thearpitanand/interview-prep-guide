"""
Problem: Expression Contains Redundant Bracket (GFG) | Optional | Easy
Topic: Stacks and Queues

Given a string of balanced expression with operators +, -, *, / and parentheses,
check if it contains redundant brackets.

Example 1:
  Input: s = "((a+b))"
  Output: True  # outer brackets are redundant

Example 2:
  Input: s = "(a+b)"
  Output: False

Constraints:
  - 1 <= len(s) <= 10^4

Hint: Use stack. On ')', pop until '('. If no operator found between, it's redundant.
Pattern: Stack
"""


def has_redundant_brackets(s: str) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert has_redundant_brackets("((a+b))") == True
    assert has_redundant_brackets("(a+b)") == False
    assert has_redundant_brackets("(a+(b)/c)") == True
    print("All tests passed!")
