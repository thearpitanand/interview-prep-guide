"""
Problem: Roman to Integer (LC 13) | Day 9 | Easy
Topic: Strings

Convert a Roman numeral string to an integer.
Roman numerals: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.
Subtractive forms: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900.

Example 1:
  Input: s = "MCMXCIV"
  Output: 1994

Constraints:
  - 1 <= s.length <= 15
  - s only contains 'I', 'V', 'X', 'L', 'C', 'D', 'M'
  - 1 <= answer <= 3999

Hint: If current value < next value, subtract; otherwise add.
Pattern: Greedy / HashMap
"""


def roman_to_int(s: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert roman_to_int("III") == 3
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994
    assert roman_to_int("IV") == 4
    print("All tests passed!")
