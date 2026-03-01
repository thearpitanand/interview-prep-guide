"""
Problem: Sort Stack Using Recursion (GFG) | Optional | Medium
Topic: Stacks and Queues

Sort a stack using recursion. No loops allowed.

Example 1:
  Input: [3, 2, 1, 4]
  Output: [1, 2, 3, 4] (bottom to top)

Constraints:
  - 1 <= n <= 10^3

Hint: Pop top, sort remaining, insert top at correct position recursively.
Pattern: Recursion
"""


def sort_stack(stack: list[int]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert sort_stack([3, 2, 1, 4]) == [1, 2, 3, 4]
    assert sort_stack([5, 1, 3]) == [1, 3, 5]
    print("All tests passed!")
