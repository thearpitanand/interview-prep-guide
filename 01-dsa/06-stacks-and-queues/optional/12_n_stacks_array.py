"""
Problem: Implement N Stacks in Array (GFG) | Optional | Medium
Topic: Stacks and Queues

Implement N stacks using a single array of size S.

Example 1:
  Input: push(0, 10), push(1, 20), pop(0) -> 10

Constraints:
  - Space efficient — use all S slots across N stacks

Hint: Use free list + top array + next array.
Pattern: Array with Free List
"""


class NStacks:
    def __init__(self, n: int, s: int):
        # Write your solution here
        pass

    def push(self, stack_num: int, val: int) -> None:
        pass

    def pop(self, stack_num: int) -> int:
        pass


# --- Tests ---
if __name__ == "__main__":
    ns = NStacks(3, 6)
    ns.push(0, 10)
    ns.push(1, 20)
    ns.push(2, 30)
    assert ns.pop(0) == 10
    assert ns.pop(1) == 20
    print("All tests passed!")
