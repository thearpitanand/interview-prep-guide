"""
Problem: Evaluate Reverse Polish Notation (LC 150) | Smart-DSA Day 16 | Medium
Pattern: Stack
Time target: 25 minutes

Evaluate an arithmetic expression in Reverse Polish Notation. Valid operators
are '+', '-', '*', '/'. Each operand may be an integer or another expression.
Division truncates toward zero.

Example 1:
  Input: tokens = ["2","1","+","3","*"]
  Output: 9
  Explanation: ((2 + 1) * 3) = 9

Example 2:
  Input: tokens = ["4","13","5","/","+"]
  Output: 6
  Explanation: (4 + (13 / 5)) = 6

Example 3:
  Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
  Output: 22

Constraints:
  - 1 <= tokens.length <= 10^4
  - tokens[i] is an integer in [-200, 200] or one of '+', '-', '*', '/'.

Hint (⚠ read only after time budget is blown):
  Push numbers; when you see an operator pop two numbers (b then a), apply
  the operator (a op b), and push the result. Use int() to truncate division.
"""


def eval_rpn(tokens: list[str]) -> int:
    pass


if __name__ == "__main__":
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
    assert eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    assert eval_rpn(["3", "11", "5", "+", "-"]) == -13
    assert eval_rpn(["7", "2", "/"]) == 3   # truncates toward zero
    print("All tests passed!")
