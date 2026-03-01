"""
Problem: Implement Stack Using Deque (GFG) | Optional | Easy
Topic: Stacks and Queues

Implement a stack using a deque (double-ended queue).

Example 1:
  Input: push(1), push(2), pop() -> 2, top() -> 1

Constraints:
  - All operations O(1)

Hint: Use deque's append/pop from the same end.
Pattern: Deque
"""
from collections import deque


class StackUsingDeque:
    def __init__(self):
        # Write your solution here
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def top(self) -> int:
        pass

    def is_empty(self) -> bool:
        pass


# --- Tests ---
if __name__ == "__main__":
    s = StackUsingDeque()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.top() == 1
    assert not s.is_empty()
    print("All tests passed!")
