"""
Problem: Reverse Stack Using Recursion (GFG) | Optional | Medium
Topic: Stacks and Queues

Reverse a stack using recursion. No extra data structures.

Example 1:
  Input: [1, 2, 3, 4] (top=4)
  Output: [4, 3, 2, 1] (top=1)

Constraints:
  - 1 <= n <= 10^4

Hint: Pop top, reverse remaining, insert popped element at bottom using recursion.
Pattern: Recursion
"""


def reverse_stack(stack: list[int]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert reverse_stack([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert reverse_stack([1]) == [1]
    print("All tests passed!")
