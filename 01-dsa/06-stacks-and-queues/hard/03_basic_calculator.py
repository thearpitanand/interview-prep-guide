"""
Basic Calculator

Day: 22 | Difficulty: Hard | Pattern: Stack
LeetCode 224: https://leetcode.com/problems/basic-calculator/

Problem:
    Given a string s representing a valid expression, implement a basic
    calculator to evaluate it, and return the result of the evaluation.

    Note: You are not allowed to use any built-in function which evaluates
    strings as mathematical expressions, such as eval().

Examples:
    Input: s = "1 + 1"
    Output: 2

    Input: s = " 2-1 + 2 "
    Output: 3

    Input: s = "(1+(4+5+2)-3)+(6+8)"
    Output: 23

Constraints:
    - 1 <= s.length <= 3 * 10^5
    - s consists of digits, '+', '-', '(', ')', and ' '
    - s represents a valid expression
    - '+' is not used as a unary operation (i.e., "+1" and "+(2+3)" is invalid)
    - '-' could be used as a unary operation (i.e., "-1" and "-(2+3)" is valid)
    - There will be no two consecutive operators in the input
    - Every number and running calculation will fit in a signed 32-bit integer

Hint:
    Use a stack to handle parentheses. Track the current result and current sign.
    When you see '(', push the current result and sign onto the stack, then reset.
    When you see ')', pop the sign and previous result, and combine.

    Think of it as: result_before_paren + sign * result_inside_paren

Pattern:
    Stack for Parentheses
    - Maintain running result and current sign (+1 or -1)
    - '(' -> push (result, sign), reset result=0, sign=1
    - ')' -> pop (prev_result, prev_sign), result = prev_result + prev_sign * result
    - Digit -> build multi-digit number, add to result with current sign
    - '+' -> sign = 1
    - '-' -> sign = -1
    - Time: O(n), Space: O(n) for nested parens
"""


def calculate(s: str) -> int:
    pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Simple addition
    assert calculate("1 + 1") == 2, "Test 1 Failed"

    # Test 2: Mixed operations
    assert calculate(" 2-1 + 2 ") == 3, "Test 2 Failed"

    # Test 3: Nested parentheses
    assert calculate("(1+(4+5+2)-3)+(6+8)") == 23, "Test 3 Failed"

    # Test 4: Single number
    assert calculate("42") == 42, "Test 4 Failed"

    # Test 5: Subtraction
    assert calculate("10 - 3 - 2") == 5, "Test 5 Failed"

    # Test 6: Nested negation
    assert calculate("1-(2+3)") == -4, "Test 6 Failed"

    # Test 7: Deeply nested
    assert calculate("((1+2)+(3+4))") == 10, "Test 7 Failed"

    # Test 8: Leading negative (unary minus)
    assert calculate("-1 + 2") == 1, "Test 8 Failed"

    # Test 9: Complex
    assert calculate("1-(5)") == -4, "Test 9 Failed"

    print("All test cases passed!")
