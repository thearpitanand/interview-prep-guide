"""
Problem: Move All Negatives to One Side (GFG) | Optional | Easy
Topic: Arrays

Given an array of positive and negative numbers, move all negative numbers
to the left and all positive numbers to the right. Order doesn't matter.

Example 1:
  Input: arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
  Output: all negatives on left, positives on right

Constraints:
  - 1 <= n <= 10^6
  - -10^9 <= arr[i] <= 10^9

Hint: Use Dutch National Flag partitioning or two pointers.
Pattern: Two Pointers / Partitioning
"""


def move_negatives(arr: list[int]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = move_negatives([-1, 2, -3, 4, 5, 6, -7, 8, 9])
    negs = [x for x in result if x < 0]
    poss = [x for x in result if x >= 0]
    assert result == negs + poss
    print("All tests passed!")
