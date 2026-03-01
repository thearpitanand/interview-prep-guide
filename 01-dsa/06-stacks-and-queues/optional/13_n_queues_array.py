"""
Problem: Implement N Queues in Array (GFG) | Optional | Medium
Topic: Stacks and Queues

Implement N queues using a single array of size S.

Example 1:
  Input: enqueue(0, 10), enqueue(1, 20), dequeue(0) -> 10

Constraints:
  - Space efficient

Hint: Similar to N stacks — use free list + front/rear arrays + next array.
Pattern: Array with Free List
"""


class NQueues:
    def __init__(self, n: int, s: int):
        # Write your solution here
        pass

    def enqueue(self, queue_num: int, val: int) -> None:
        pass

    def dequeue(self, queue_num: int) -> int:
        pass


# --- Tests ---
if __name__ == "__main__":
    nq = NQueues(3, 6)
    nq.enqueue(0, 10)
    nq.enqueue(0, 20)
    nq.enqueue(1, 30)
    assert nq.dequeue(0) == 10
    assert nq.dequeue(1) == 30
    print("All tests passed!")
