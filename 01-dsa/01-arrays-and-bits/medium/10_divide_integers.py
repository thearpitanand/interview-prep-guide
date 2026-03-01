"""
Problem: Divide Two Integers (LC 29) | Day 7 | Medium
Topic: Bit Manipulation

Divide two integers without using *, /, or %.
Return the quotient truncated toward zero.

Example 1:
  Input: dividend = 10, divisor = 3
  Output: 3

Example 2:
  Input: dividend = 7, divisor = -2
  Output: -3

Hint: Use bit shifting. Double the divisor until it exceeds dividend.
Pattern: Bit Manipulation
"""


def divide(dividend: int, divisor: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert divide(10, 3) == 3
    assert divide(7, -2) == -3
    assert divide(0, 1) == 0
    assert divide(-2147483648, -1) == 2147483647  # overflow case
    print("All tests passed!")
