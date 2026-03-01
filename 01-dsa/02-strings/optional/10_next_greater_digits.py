"""
Problem: Next Greater Number with Same Digits (LC 556) | Optional | Medium
Topic: Strings

Given a positive integer n, find the smallest integer which has exactly the
same digits and is greater than n. Return -1 if none exists.

Example 1:
  Input: n = 12
  Output: 21

Example 2:
  Input: n = 21
  Output: -1

Constraints:
  - 1 <= n <= 2^31 - 1

Hint: Same as "next permutation" on the digit array.
Pattern: Next Permutation
"""


def next_greater_element(n: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert next_greater_element(12) == 21
    assert next_greater_element(21) == -1
    assert next_greater_element(1234) == 1243
    print("All tests passed!")
