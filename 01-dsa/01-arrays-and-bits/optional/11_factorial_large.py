"""
Problem: Factorial of Large Number (GFG) | Optional | Medium
Topic: Arrays

Given an integer N, find its factorial. The result can be very large, so
return it as a list of digits.

Example 1:
  Input: n = 10
  Output: [3, 6, 2, 8, 8, 0, 0]  # 10! = 3628800

Constraints:
  - 1 <= n <= 1000

Hint: Use array to store digits, multiply digit by digit.
Pattern: Array Multiplication
"""


def factorial_large(n: int) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert factorial_large(10) == [3, 6, 2, 8, 8, 0, 0]
    assert factorial_large(5) == [1, 2, 0]
    assert factorial_large(1) == [1]
    print("All tests passed!")
