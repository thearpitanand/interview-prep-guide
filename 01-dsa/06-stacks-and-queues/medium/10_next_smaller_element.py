"""
Problem: Next Smaller Element (GFG) | Day 21 | Medium
Topic: Stacks and Queues

Given an array, find the next smaller element for every element.
If no smaller element exists to the right, output -1.

Example 1:
  Input: arr = [4, 8, 5, 2, 25]
  Output: [2, 5, 2, -1, -1]

Constraints:
  - 1 <= n <= 10^5

Hint: Use a stack (similar to Next Greater Element but look for smaller).
Pattern: Monotonic Stack
"""


def next_smaller_element(arr: list[int]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert next_smaller_element([4, 8, 5, 2, 25]) == [2, 5, 2, -1, -1]
    assert next_smaller_element([13, 7, 6, 12]) == [7, 6, -1, -1]
    assert next_smaller_element([1, 2, 3]) == [-1, -1, -1]
    print("All tests passed!")
