"""
Problem: Zigzag Conversion (LC 6) | Day 11 | Medium
Topic: Strings

The string "PAYPALISHIRING" is written in a zigzag pattern on a given
number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given
a number of rows.

Example 1:
  Input: s = "PAYPALISHIRING", numRows = 3
  Output: "PAHNAPLSIIGYIR"

Example 2:
  Input: s = "PAYPALISHIRING", numRows = 4
  Output: "PINALSIGYAHRPI"
  Explanation:
    P     I     N
    A   L S   I G
    Y A   H R
    P     I

Example 3:
  Input: s = "A", numRows = 1
  Output: "A"

Constraints:
  - 1 <= len(s) <= 1000
  - 1 <= numRows <= 1000

Hint: Create numRows lists (one per row). Iterate through the string,
      placing characters into the appropriate row. Use a direction flag
      that flips when you reach row 0 or row numRows-1. Finally, join
      all rows together.
Pattern: Simulation
"""


def convert(s: str, num_rows: int) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert convert("A", 1) == "A"
    assert convert("AB", 1) == "AB"
    assert convert("ABC", 2) == "ACB"
    print("All tests passed!")
