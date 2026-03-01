"""
Problem: Insert at Bottom of Stack (GFG) | Optional | Easy
Topic: Stacks and Queues

Insert an element at the bottom of a stack using recursion.

Example 1:
  Input: stack = [1, 2, 3, 4] (top=4), x = 0
  Output: [0, 1, 2, 3, 4]

Constraints:
  - 1 <= n <= 10^5

Hint: Recursively pop all elements, push x, push all back.
Pattern: Recursion
"""


def insert_at_bottom(stack: list[int], x: int) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert insert_at_bottom([1, 2, 3, 4], 0) == [0, 1, 2, 3, 4]
    assert insert_at_bottom([], 5) == [5]
    print("All tests passed!")
