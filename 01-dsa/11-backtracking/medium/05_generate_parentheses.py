"""
Generate Parentheses (LC 22)

Day: 32 | Difficulty: Medium | Pattern: Backtracking - Constraint-based Generation

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

Examples:
    Input: n = 3
    Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

    Input: n = 1
    Output: ["()"]

    Input: n = 2
    Output: ["(())", "()()"]

Constraints:
    - 1 <= n <= 8

Hint:
    Track the count of open and close parentheses used so far. You can add an
    open paren if open_count < n. You can add a close paren if close_count <
    open_count (ensures validity). The base case is when the string length
    reaches 2*n.

Pattern: Backtracking with constraints. Two choices at each step (open or close
paren), but pruned by: (1) can't exceed n opens, (2) closes can't exceed opens.
"""

from typing import List


def generate_parenthesis(n: int) -> List[str]:
    """Generate all valid parentheses combinations using backtracking."""
    pass


def generate_parenthesis_string(n: int) -> List[str]:
    """Alternative: build string instead of list (slightly different style)."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: n = 3
    result = sorted(generate_parenthesis(3))
    expected = sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 2: n = 1
    result = generate_parenthesis(1)
    assert result == ["()"], f"Expected ['()'], got {result}"

    # Test 3: n = 2
    result = sorted(generate_parenthesis(2))
    expected = sorted(["(())", "()()"])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 4: n = 4 - verify count (Catalan number C4 = 14)
    result = generate_parenthesis(4)
    assert len(result) == 14, f"Expected 14 combinations, got {len(result)}"

    # Test 5: All results are valid
    for combo in generate_parenthesis(3):
        count = 0
        for c in combo:
            count += 1 if c == "(" else -1
            assert count >= 0, f"Invalid parentheses: {combo}"
        assert count == 0, f"Unbalanced parentheses: {combo}"

    # Test 6: No duplicates
    result = generate_parenthesis(4)
    assert len(result) == len(set(result)), "Found duplicates in result"

    # Test 7: String-based approach
    result = sorted(generate_parenthesis_string(3))
    expected = sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert result == expected, f"Expected {expected}, got {result}"

    print("All tests passed!")
