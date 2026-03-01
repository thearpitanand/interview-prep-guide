"""
Problem: Common Elements in 3 Sorted Arrays (GFG) | Optional | Easy
Topic: Arrays

Given three sorted arrays, find the common elements.

Example 1:
  Input: a = [1, 5, 10, 20, 40, 80], b = [6, 7, 20, 80, 100], c = [3, 4, 15, 20, 30, 70, 80, 120]
  Output: [20, 80]

Constraints:
  - Arrays are sorted

Hint: Three pointers — advance the smallest.
Pattern: Three Pointers
"""


def common_in_3_sorted(a: list[int], b: list[int], c: list[int]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert common_in_3_sorted([1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120]) == [20, 80]
    assert common_in_3_sorted([1, 2, 3], [4, 5, 6], [7, 8, 9]) == []
    print("All tests passed!")
