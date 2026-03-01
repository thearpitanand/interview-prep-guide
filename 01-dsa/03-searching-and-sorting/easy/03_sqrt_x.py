"""
Problem: Sqrt(x) (LC 69) | Day 12 | Easy
Topic: Searching and Sorting

Given a non-negative integer x, return the square root of x rounded down
to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator (like pow(x, 0.5)
or x ** 0.5).

Example 1:
  Input: x = 4
  Output: 2

Example 2:
  Input: x = 8
  Output: 2
  Explanation: The square root of 8 is 2.828..., rounded down to 2.

Constraints:
  - 0 <= x <= 2^31 - 1

Hint: Binary search in range [0, x]. For mid, check if mid*mid <= x.
      Find the largest mid such that mid*mid <= x.
Pattern: Binary Search on Answer
"""


def my_sqrt(x: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert my_sqrt(4) == 2
    assert my_sqrt(8) == 2
    assert my_sqrt(0) == 0
    assert my_sqrt(1) == 1
    assert my_sqrt(16) == 4
    assert my_sqrt(2147395599) == 46339
    print("All tests passed!")
