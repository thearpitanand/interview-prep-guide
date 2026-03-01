"""
Problem: Count Bits to Flip A to B (GFG) | Optional | Easy
Topic: Bit Manipulation

Given two numbers A and B, count the number of bits that need to be flipped
to convert A to B.

Example 1:
  Input: a = 10, b = 20
  Output: 4  # 10 = 01010, 20 = 10100, XOR = 11110, count = 4

Constraints:
  - 1 <= a, b <= 10^6

Hint: XOR the two numbers, then count set bits.
Pattern: XOR + Bit Count
"""


def count_bits_flip(a: int, b: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert count_bits_flip(10, 20) == 4
    assert count_bits_flip(7, 10) == 3
    assert count_bits_flip(0, 0) == 0
    print("All tests passed!")
