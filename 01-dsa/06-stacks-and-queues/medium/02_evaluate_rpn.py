"""
Evaluate Reverse Polish Notation

Day: 21 | Difficulty: Medium | Pattern: Stack
LeetCode 150: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Problem:
    You are given an array of strings tokens that represents an arithmetic
    expression in Reverse Polish Notation (postfix notation).

    Evaluate the expression. Return an integer that represents the value
    of the expression.

    Note:
    - The valid operators are '+', '-', '*', and '/'.
    - Each operand may be an integer or another expression.
    - The division between two integers always truncates toward zero.
    - There will not be any division by zero.
    - The input represents a valid arithmetic expression in RPN.

Examples:
    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9

    Input: tokens = ["4","13","5","/","+"]
    Output: 6
    Explanation: (4 + (13 / 5)) = 6

    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22

Constraints:
    - 1 <= tokens.length <= 10^4
    - tokens[i] is either an operator or an integer in range [-200, 200]

Hint:
    Use a stack. If the token is a number, push it. If it's an operator, pop
    two numbers, apply the operation (second_popped OP first_popped), push result.
    Be careful: for subtraction and division, order matters!

Pattern:
    Stack-based Expression Evaluation
    - Number -> push to stack
    - Operator -> pop two operands, compute, push result
    - Note: first popped is the RIGHT operand, second is LEFT
    - Division truncates toward zero: use int(a / b), not a // b
"""

from typing import List


def eval_rpn(tokens: List[str]) -> int:
    pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Simple expression
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9, "Test 1 Failed"

    # Test 2: Division
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6, "Test 2 Failed"

    # Test 3: Complex expression
    assert eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22, "Test 3 Failed"

    # Test 4: Single number
    assert eval_rpn(["42"]) == 42, "Test 4 Failed"

    # Test 5: Negative result
    assert eval_rpn(["3", "4", "-"]) == -1, "Test 5 Failed"

    # Test 6: Division truncates toward zero
    assert eval_rpn(["7", "2", "/"]) == 3, "Test 6 Failed"
    assert eval_rpn(["-7", "2", "/"]) == -3, "Test 7 Failed"

    print("All test cases passed!")
