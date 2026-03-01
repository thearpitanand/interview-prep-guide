"""
Basic Calculator II

Day: 22 | Difficulty: Medium | Pattern: Stack
LeetCode 227: https://leetcode.com/problems/basic-calculator-ii/

Problem:
    Given a string s which represents an expression, evaluate this expression
    and return its value.

    The integer division should truncate toward zero.

    You may assume that the given expression is always valid. All intermediate
    results will be in the range of [-2^31, 2^31 - 1].

    Note: You are not allowed to use any built-in function which evaluates
    strings as mathematical expressions, such as eval().

Examples:
    Input: s = "3+2*2"
    Output: 7

    Input: s = " 3/2 "
    Output: 1

    Input: s = " 3+5 / 2 "
    Output: 5

Constraints:
    - 1 <= s.length <= 3 * 10^5
    - s consists of integers and operators ('+', '-', '*', '/') separated
      by some number of spaces
    - s represents a valid expression
    - All the integers in the expression are non-negative and fit in a 32-bit integer

Hint:
    Track the last operator and current number. When you encounter a new operator
    (or reach the end), apply the PREVIOUS operator:
    - '+': push current number
    - '-': push -current number
    - '*': pop, multiply, push result
    - '/': pop, divide (truncate toward zero), push result
    At the end, sum everything in the stack.

Pattern:
    Stack-based Expression Evaluation
    - Process left to right, track previous operator
    - + and - defer computation (push to stack)
    - * and / compute immediately (pop, compute, push)
    - Final answer = sum of stack
    - Use int(a / b) for truncation toward zero, NOT a // b
"""


def calculate(s: str) -> int:
    pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Multiplication with addition
    assert calculate("3+2*2") == 7, "Test 1 Failed"

    # Test 2: Division
    assert calculate(" 3/2 ") == 1, "Test 2 Failed"

    # Test 3: Mixed
    assert calculate(" 3+5 / 2 ") == 5, "Test 3 Failed"

    # Test 4: Just a number
    assert calculate("42") == 42, "Test 4 Failed"

    # Test 5: Subtraction
    assert calculate("10-3") == 7, "Test 5 Failed"

    # Test 6: Multiple operations
    assert calculate("1+2*3-4/2") == 5, "Test 6 Failed"

    # Test 7: Large numbers
    assert calculate("100*2+12") == 212, "Test 7 Failed"

    # Test 8: Division truncation toward zero
    assert calculate("14-3/2") == 13, "Test 8 Failed"

    print("All test cases passed!")
