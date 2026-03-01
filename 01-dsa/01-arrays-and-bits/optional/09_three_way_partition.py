"""
Problem: Three Way Partitioning (GFG) | Optional | Easy
Topic: Arrays

Given an array and a range [a, b], partition the array such that elements < a
come first, then elements in range [a, b], then elements > b.

Example 1:
  Input: arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32], a = 14, b = 20
  Output: elements < 14, then 14-20, then > 20

Constraints:
  - 1 <= n <= 10^6

Hint: Dutch National Flag-style three-way partitioning.
Pattern: Dutch National Flag
"""


def three_way_partition(arr: list[int], a: int, b: int) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = three_way_partition([1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32], 14, 20)
    low = [x for x in result if x < 14]
    mid = [x for x in result if 14 <= x <= 20]
    high = [x for x in result if x > 20]
    assert result == low + mid + high
    print("All tests passed!")
