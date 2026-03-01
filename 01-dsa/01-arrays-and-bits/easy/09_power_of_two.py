"""
Problem: Power of Two (LC 231) | Day 7 | Easy
Topic: Bit Manipulation

Given an integer n, return true if it is a power of two.

Example 1:
  Input: n = 16
  Output: True (2^4)

Example 2:
  Input: n = 3
  Output: False

Hint: A power of 2 has exactly one set bit: n & (n-1) == 0.
Pattern: Bit Manipulation
"""


def is_power_of_two(n: int) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert is_power_of_two(1) == True
    assert is_power_of_two(16) == True
    assert is_power_of_two(3) == False
    assert is_power_of_two(0) == False
    print("All tests passed!")
