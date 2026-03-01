"""
Problem: Interleave First & Second Half of Queue (GFG) | Optional | Medium
Topic: Stacks and Queues

Given a queue of even length, interleave the first half with the second half.

Example 1:
  Input: [1, 2, 3, 4, 5, 6, 7, 8]
  Output: [1, 5, 2, 6, 3, 7, 4, 8]

Constraints:
  - Queue has even number of elements

Hint: Push first half into stack, interleave with remaining queue elements.
Pattern: Stack + Queue
"""
from collections import deque


def interleave_queue(q: deque) -> deque:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert list(interleave_queue(deque([1, 2, 3, 4, 5, 6, 7, 8]))) == [1, 5, 2, 6, 3, 7, 4, 8]
    print("All tests passed!")
