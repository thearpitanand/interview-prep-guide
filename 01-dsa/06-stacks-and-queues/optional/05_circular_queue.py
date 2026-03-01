"""
Problem: Implement Circular Queue (GFG) | Optional | Easy
Topic: Stacks and Queues

Implement a circular queue with fixed size using an array.

Example 1:
  Input: enqueue(1), enqueue(2), dequeue() -> 1, enqueue(3)

Constraints:
  - Fixed size k

Hint: Use front and rear pointers with modular arithmetic.
Pattern: Circular Array
"""


class CircularQueue:
    def __init__(self, k: int):
        # Write your solution here
        pass

    def enqueue(self, val: int) -> bool:
        pass

    def dequeue(self) -> int:
        pass

    def front(self) -> int:
        pass

    def is_empty(self) -> bool:
        pass

    def is_full(self) -> bool:
        pass


# --- Tests ---
if __name__ == "__main__":
    cq = CircularQueue(3)
    assert cq.enqueue(1) == True
    assert cq.enqueue(2) == True
    assert cq.enqueue(3) == True
    assert cq.enqueue(4) == False  # full
    assert cq.dequeue() == 1
    assert cq.enqueue(4) == True
    print("All tests passed!")
