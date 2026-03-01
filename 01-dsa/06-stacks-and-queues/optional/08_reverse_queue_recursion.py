"""
Problem: Reverse Queue Using Recursion (GFG) | Optional | Easy
Topic: Stacks and Queues

Reverse a queue using recursion (no extra data structure).

Example 1:
  Input: [1, 2, 3, 4, 5]
  Output: [5, 4, 3, 2, 1]

Constraints:
  - 1 <= n <= 10^4

Hint: Dequeue front, reverse remaining, enqueue front at back.
Pattern: Recursion
"""
from collections import deque


def reverse_queue(q: deque) -> deque:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert list(reverse_queue(deque([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert list(reverse_queue(deque([1]))) == [1]
    print("All tests passed!")
