"""
Problem: Hamming Distance (LC 461) | Day 7 | Easy
Topic: Bit Manipulation

Return the number of positions where the corresponding
bits of two integers differ.

Example:
  Input: x = 1 (0001), y = 4 (0100)
  Output: 2

Hint: XOR gives 1 where bits differ. Count the 1s.
Pattern: XOR + Count Bits
"""


def hamming_distance(x: int, y: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert hamming_distance(1, 4) == 2
    assert hamming_distance(3, 1) == 1
    assert hamming_distance(0, 0) == 0
    print("All tests passed!")
