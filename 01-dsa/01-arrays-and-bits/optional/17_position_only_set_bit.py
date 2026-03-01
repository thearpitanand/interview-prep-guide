"""
Problem: Find Position of Only Set Bit (GFG) | Optional | Easy
Topic: Bit Manipulation

Given a number having only one bit set in its binary representation, find
the position of that set bit (1-indexed from right).

Example 1:
  Input: n = 16
  Output: 5  # 16 = 10000, set bit at position 5

Constraints:
  - n is a power of 2
  - 1 <= n <= 2^30

Hint: If n is power of 2, log2(n) + 1 gives the position.
Pattern: Bit Manipulation
"""


def position_only_set_bit(n: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert position_only_set_bit(16) == 5
    assert position_only_set_bit(1) == 1
    assert position_only_set_bit(2) == 2
    assert position_only_set_bit(64) == 7
    print("All tests passed!")
