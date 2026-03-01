"""
Problem: Chocolate Distribution Problem (GFG) | Optional | Easy
Topic: Arrays

Given an array of n integers where each value represents number of chocolates
in a packet. Distribute m packets among m students such that the difference
between max and min chocolates given is minimized.

Example 1:
  Input: arr = [7, 3, 2, 4, 9, 12, 56], m = 3
  Output: 2  # packets [3, 4, 2] -> sorted window [2, 3, 4], diff = 4-2 = 2

Constraints:
  - 1 <= n <= 10^5
  - 1 <= m <= n

Hint: Sort the array, then find the minimum difference in a window of size m.
Pattern: Sliding Window
"""


def chocolate_distribution(arr: list[int], m: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert chocolate_distribution([7, 3, 2, 4, 9, 12, 56], 3) == 2
    assert chocolate_distribution([3, 4, 1, 9, 56, 7, 9, 12], 5) == 6
    print("All tests passed!")
