"""
Problem: Find Middle Element of Stack (GFG) | Optional | Medium
Topic: Stacks and Queues

Design a stack that supports findMiddle() in O(1) time.

Example 1:
  Input: push(1), push(2), push(3), findMiddle() -> 2

Constraints:
  - All operations in O(1)

Hint: Use a DLL with a mid pointer. Update mid on push/pop.
Pattern: Doubly Linked List
"""


class MiddleStack:
    def __init__(self):
        # Write your solution here
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def find_middle(self) -> int:
        pass


# --- Tests ---
if __name__ == "__main__":
    ms = MiddleStack()
    ms.push(1)
    ms.push(2)
    ms.push(3)
    assert ms.find_middle() == 2
    ms.push(4)
    assert ms.find_middle() == 2  # or 3, depends on convention
    print("All tests passed!")
