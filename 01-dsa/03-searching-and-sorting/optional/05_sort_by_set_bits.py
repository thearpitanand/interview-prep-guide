"""
Problem: Sort Array by Count of Set Bits (GFG) | Optional | Easy
Topic: Searching and Sorting

Sort array in decreasing order of count of set bits. If two elements have
same number of set bits, maintain their relative order.

Example 1:
  Input: arr = [5, 2, 3, 9, 4, 6, 7, 15, 32]
  Output: [15, 7, 5, 3, 6, 9, 2, 4, 32]

Constraints:
  - 1 <= n <= 10^5

Hint: Stable sort with key = -bin(x).count('1').
Pattern: Custom Sort
"""


def sort_by_set_bits(arr: list[int]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = sort_by_set_bits([5, 2, 3, 9, 4, 6, 7, 15, 32])
    # Check that set bit counts are non-increasing
    bits = [bin(x).count('1') for x in result]
    assert bits == sorted(bits, reverse=True)
    print("All tests passed!")
