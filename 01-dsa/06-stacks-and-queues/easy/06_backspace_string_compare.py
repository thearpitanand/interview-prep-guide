"""
Backspace String Compare

Day: 20 | Difficulty: Easy | Pattern: Stack
LeetCode 844: https://leetcode.com/problems/backspace-string-compare/

Problem:
    Given two strings s and t, return true if they are equal when both are
    typed into empty text editors. '#' means a backspace character.

    Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    Explanation: Both s and t become "ac".

    Input: s = "ab##", t = "c#d#"
    Output: True
    Explanation: Both s and t become "".

    Input: s = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

Constraints:
    - 1 <= s.length, t.length <= 200
    - s and t only contain lowercase letters and '#' characters

Hint:
    Build the final string using a stack. For each character: if it's '#', pop
    from the stack (if non-empty). Otherwise, push onto the stack. Compare
    the two resulting stacks.

    Follow-up: Can you solve it in O(1) space? (Use two pointers from the end.)

Pattern:
    Stack Simulation
    - Process each string through a stack
    - '#' = pop (backspace), other chars = push
    - Compare final stacks
"""


def backspace_compare(s: str, t: str) -> bool:
    pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Basic backspace
    assert backspace_compare("ab#c", "ad#c") == True, "Test 1 Failed"

    # Test 2: Multiple backspaces
    assert backspace_compare("ab##", "c#d#") == True, "Test 2 Failed"

    # Test 3: Different results
    assert backspace_compare("a#c", "b") == False, "Test 3 Failed"

    # Test 4: No backspaces
    assert backspace_compare("abc", "abc") == True, "Test 4 Failed"

    # Test 5: All backspaced
    assert backspace_compare("a##", "b##") == True, "Test 5 Failed"

    # Test 6: Backspace on empty
    assert backspace_compare("#a", "a") == True, "Test 6 Failed"

    # Test 7: Longer strings
    assert backspace_compare("bxj##tw", "bxo#j##tw") == True, "Test 7 Failed"

    print("All test cases passed!")
