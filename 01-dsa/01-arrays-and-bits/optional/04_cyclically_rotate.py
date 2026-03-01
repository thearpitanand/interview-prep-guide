"""
Problem: Cyclically Rotate Array by One (GFG) | Optional | Easy
Topic: Arrays

Rotate the array by one position in clockwise direction.

Example 1:
  Input: arr = [1, 2, 3, 4, 5]
  Output: [5, 1, 2, 3, 4]

Constraints:
  - 1 <= n <= 10^5

Hint: Store last element, shift all right by one, place last at beginning.
Pattern: Array Manipulation
"""


def cyclically_rotate(arr: list[int]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert cyclically_rotate([1, 2, 3, 4, 5]) == [5, 1, 2, 3, 4]
    assert cyclically_rotate([1]) == [1]
    assert cyclically_rotate([9, 8, 7]) == [7, 9, 8]
    print("All tests passed!")
