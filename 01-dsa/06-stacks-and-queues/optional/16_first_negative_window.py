"""
Problem: First Negative Integer in Window K (GFG) | Optional | Medium
Topic: Stacks and Queues

Given an array and window size k, find the first negative integer in each window.

Example 1:
  Input: arr = [-8, 2, 3, -6, 10], k = 2
  Output: [-8, 0, -6, -6]

Constraints:
  - 1 <= n <= 10^5

Hint: Use deque to store indices of negative numbers.
Pattern: Sliding Window + Deque
"""


def first_negative_window(arr: list[int], k: int) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert first_negative_window([-8, 2, 3, -6, 10], 2) == [-8, 0, -6, -6]
    assert first_negative_window([12, -1, -7, 8, -15, 30, 16, 28], 3) == [-1, -1, -7, -15, -15, 0]
    print("All tests passed!")
