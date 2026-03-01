"""
Valid Parentheses

Day: 20 | Difficulty: Easy | Pattern: Stack / Parentheses Matching
LeetCode 20: https://leetcode.com/problems/valid-parentheses/

Problem:
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

Examples:
    Input: s = "()"
    Output: True

    Input: s = "(]"
    Output: False

    Input: s = "([{}])"
    Output: True

Constraints:
    - 1 <= s.length <= 10^4
    - s consists of parentheses only '()[]{}'

Hint:
    Use a stack. Push opening brackets. For closing brackets, check if the top
    of the stack is the matching opening bracket. If not, it's invalid.

Pattern:
    Stack - Parentheses Matching
    - Opening bracket -> push onto stack
    - Closing bracket -> pop from stack and verify match
    - At the end, stack must be empty for a valid string
"""


def is_valid(s: str) -> bool:
    pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Simple valid
    assert is_valid("()") == True, "Test 1 Failed"

    # Test 2: Mismatched types
    assert is_valid("(]") == False, "Test 2 Failed"

    # Test 3: Nested valid
    assert is_valid("([{}])") == True, "Test 3 Failed"

    # Test 4: Multiple pairs
    assert is_valid("()[]{}") == True, "Test 4 Failed"

    # Test 5: Single opening bracket
    assert is_valid("(") == False, "Test 5 Failed"

    # Test 6: Single closing bracket
    assert is_valid(")") == False, "Test 6 Failed"

    # Test 7: Wrong nesting order
    assert is_valid("([)]") == False, "Test 7 Failed"

    # Test 8: Empty string
    assert is_valid("") == True, "Test 8 Failed"

    print("All test cases passed!")
