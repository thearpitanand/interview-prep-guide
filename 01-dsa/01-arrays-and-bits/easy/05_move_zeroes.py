"""
Problem: Move Zeroes (LC 283) | Day 4 | Easy
Topic: Arrays

Move all 0's to the end while maintaining relative order
of non-zero elements. Do it in-place.

Example:
  Input: nums = [0,1,0,3,12]
  Output: [1,3,12,0,0]

Constraints:
  - 1 <= nums.length <= 10^4

Hint: Use a write pointer for non-zero elements.
Pattern: Two Pointers
"""


def move_zeroes(nums: list[int]) -> None:
    # Write your solution here (modify in-place)
    pass


# --- Tests ---
if __name__ == "__main__":
    n1 = [0, 1, 0, 3, 12]
    move_zeroes(n1)
    assert n1 == [1, 3, 12, 0, 0]

    n2 = [0]
    move_zeroes(n2)
    assert n2 == [0]
    print("All tests passed!")
