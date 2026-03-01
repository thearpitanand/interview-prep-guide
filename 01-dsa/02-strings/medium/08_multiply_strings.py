"""
Problem: Multiply Strings (LC 43) | Day 11 | Medium
Topic: Strings

Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the
inputs to integer directly.

Example 1:
  Input: num1 = "2", num2 = "3"
  Output: "6"

Example 2:
  Input: num1 = "123", num2 = "456"
  Output: "56088"

Constraints:
  - 1 <= len(num1), len(num2) <= 200
  - num1 and num2 consist of digits only
  - num1 and num2 do not contain any leading zero, except the number 0 itself

Hint: Simulate grade-school multiplication. If num1 has m digits and num2
      has n digits, the result has at most m + n digits. For digits at
      positions i and j (from the right), their product contributes to
      result positions i + j and i + j + 1.
Pattern: Math/String
"""


def multiply(num1: str, num2: str) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert multiply("2", "3") == "6"
    assert multiply("123", "456") == "56088"
    assert multiply("0", "0") == "0"
    assert multiply("999", "999") == "998001"
    assert multiply("1", "1") == "1"
    print("All tests passed!")
