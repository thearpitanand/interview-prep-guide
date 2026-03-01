"""
Problem: Number of 1 Bits (LC 191) | Day 7 | Easy
Topic: Bit Manipulation

Return the number of '1' bits (Hamming weight).

Example 1:
  Input: n = 11 (binary: 1011)
  Output: 3

Example 2:
  Input: n = 128 (binary: 10000000)
  Output: 1

Hint: n & (n-1) removes the lowest set bit.
Pattern: Bit Manipulation
"""


def hamming_weight(n: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert hamming_weight(11) == 3
    assert hamming_weight(128) == 1
    assert hamming_weight(0) == 0
    assert hamming_weight(0xFFFFFFFF) == 32
    print("All tests passed!")
