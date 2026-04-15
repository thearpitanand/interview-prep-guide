"""
Problem: Min Stack (LC 155) | Smart-DSA Day 15 | Medium
Pattern: Stack
Time target: 20 minutes

Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

Implement the MinStack class:
  - MinStack() — initializes the stack object.
  - push(val) — pushes val onto the stack.
  - pop() — removes the element on top.
  - top() — returns the top element.
  - getMin() — returns the minimum element in the stack.

Example 1:
  Input:  ["MinStack","push","push","push","getMin","pop","top","getMin"]
          [[],[-2],[0],[-3],[],[],[],[]]
  Output: [null,null,null,null,-3,null,0,-2]

Constraints:
  - -2^31 <= val <= 2^31 - 1
  - pop, top, getMin are always called on non-empty stacks.
  - At most 3 * 10^4 calls to each method.

Hint (⚠ read only after time budget is blown):
  Maintain a parallel "min stack" alongside the main stack. Each push records
  the current minimum (min of new value and current top of min stack). Pop
  both stacks together. getMin peeks the min stack top.
"""


class MinStack:
    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.getMin() == -2

    ms2 = MinStack()
    ms2.push(5)
    ms2.push(3)
    ms2.push(7)
    assert ms2.getMin() == 3
    ms2.pop()
    assert ms2.getMin() == 3
    ms2.pop()
    assert ms2.getMin() == 5
    print("All tests passed!")
