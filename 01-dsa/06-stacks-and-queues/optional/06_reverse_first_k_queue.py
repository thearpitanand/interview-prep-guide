"""
Problem: Reverse First K Elements of Queue (GFG) | Optional | Easy
Topic: Stacks and Queues

Given a queue and integer k, reverse the order of first k elements.

Example 1:
  Input: queue = [1, 2, 3, 4, 5], k = 3
  Output: [3, 2, 1, 4, 5]

Constraints:
  - 1 <= k <= n

Hint: Push first k into stack, pop back to queue, then rotate remaining n-k elements.
Pattern: Stack + Queue
"""
from collections import deque


def reverse_first_k(queue: deque, k: int) -> deque:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    q = deque([1, 2, 3, 4, 5])
    assert list(reverse_first_k(q, 3)) == [3, 2, 1, 4, 5]
    print("All tests passed!")
