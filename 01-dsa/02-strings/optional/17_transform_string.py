"""
Problem: Transform One String to Another (GFG) | Optional | Medium
Topic: Strings

Given two strings A and B of same length, check if A can be transformed to B
using operations: remove a character from end and insert it at front.
If possible, return the minimum number of operations.

Example 1:
  Input: a = "ABD", b = "BAD"
  Output: 1

Constraints:
  - 1 <= len(A) <= 10^4

Hint: Both must have same character frequencies. Count from right, matching chars.
Pattern: Greedy
"""


def transform_string(a: str, b: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert transform_string("ABD", "BAD") == 1
    assert transform_string("ABC", "BCA") == 2
    assert transform_string("ABC", "DEF") == -1  # impossible
    print("All tests passed!")
