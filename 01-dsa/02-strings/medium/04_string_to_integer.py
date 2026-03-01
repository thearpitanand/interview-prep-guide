"""
Problem: String to Integer - atoi (LC 8) | Day 10 | Medium
Topic: Strings

Implement the myAtoi(string s) function, which converts a string to a
32-bit signed integer.

The algorithm:
1. Read in and ignore any leading whitespace.
2. Check if the next character is '-' or '+'. Read this character in if
   it is either. This determines if the final result is negative or
   positive respectively. Assume the result is positive if neither is present.
3. Read in the next characters until the next non-digit character or the
   end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer. If no digits were read, the
   integer is 0.
5. Clamp the integer to the 32-bit signed integer range:
   [-2^31, 2^31 - 1]. If the integer is less than -2^31, return -2^31.
   If the integer is greater than 2^31 - 1, return 2^31 - 1.

Example 1:
  Input: s = "42"
  Output: 42

Example 2:
  Input: s = "   -42"
  Output: -42

Example 3:
  Input: s = "4193 with words"
  Output: 4193

Example 4:
  Input: s = "words and 987"
  Output: 0

Constraints:
  - 0 <= len(s) <= 200
  - s consists of English letters, digits, ' ', '+', '-', '.'

Hint: Process the string character by character. Handle whitespace, then
      sign, then digits. Clamp to INT_MIN/INT_MAX at the end.
Pattern: String Parsing
"""


def my_atoi(s: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert my_atoi("42") == 42
    assert my_atoi("   -42") == -42
    assert my_atoi("4193 with words") == 4193
    assert my_atoi("words and 987") == 0
    assert my_atoi("-91283472332") == -2147483648
    assert my_atoi("") == 0
    assert my_atoi("+1") == 1
    assert my_atoi("21474836460") == 2147483647
    print("All tests passed!")
