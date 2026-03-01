"""
Problem: Count Total Set Bits 1 to N (GFG) | Optional | Medium
Topic: Bit Manipulation

Given a positive integer N, find the total count of set bits for all numbers
from 1 to N.

Example 1:
  Input: n = 4
  Output: 5  # 1(1) + 1(1) + 2(10) + 1(11) = wait, 1=1, 2=1, 3=2, 4=1 => 5

Constraints:
  - 1 <= n <= 10^8

Hint: Use pattern: every bit position contributes in groups of 2^(i+1).
Pattern: Bit Manipulation / Math
"""


def count_total_set_bits(n: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert count_total_set_bits(4) == 5
    assert count_total_set_bits(7) == 12
    assert count_total_set_bits(1) == 1
    print("All tests passed!")
