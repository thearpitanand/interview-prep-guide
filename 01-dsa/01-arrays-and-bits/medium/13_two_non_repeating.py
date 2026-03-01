"""
Problem: Two Non-Repeating Elements (GFG) | Day 7 | Medium
Topic: Bit Manipulation

Given an array where every element occurs twice except two elements which
occur only once. Find those two non-repeating elements.

Example 1:
  Input: arr = [2, 4, 7, 9, 2, 4]
  Output: {7, 9}

Constraints:
  - 2 <= n <= 10^6
  - 1 <= arr[i] <= 5 * 10^6

Hint: XOR all — result is xor of the two unique nums. Use rightmost set bit to partition.
Pattern: XOR Bit Manipulation
"""


def two_non_repeating(arr: list[int]) -> set[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert two_non_repeating([2, 4, 7, 9, 2, 4]) == {7, 9}
    assert two_non_repeating([1, 2]) == {1, 2}
    assert two_non_repeating([1, 1, 3, 5, 5, 7]) == {3, 7}
    print("All tests passed!")
