"""
Problem: Implement 2 Stacks in Array (GFG) | Optional | Easy
Topic: Stacks and Queues

Implement two stacks using a single array efficiently.

Example 1:
  Input: push1(1), push2(2), pop1() -> 1, pop2() -> 2

Constraints:
  - Maximize space utilization

Hint: Stack1 grows from left, Stack2 grows from right.
Pattern: Two Pointers
"""


class TwoStacks:
    def __init__(self, n: int):
        # Write your solution here
        pass

    def push1(self, x: int) -> None:
        pass

    def push2(self, x: int) -> None:
        pass

    def pop1(self) -> int:
        pass

    def pop2(self) -> int:
        pass


# --- Tests ---
if __name__ == "__main__":
    ts = TwoStacks(5)
    ts.push1(1)
    ts.push2(2)
    ts.push1(3)
    assert ts.pop1() == 3
    assert ts.pop2() == 2
    assert ts.pop1() == 1
    print("All tests passed!")
