"""
Min Stack

Day: 20 | Difficulty: Easy | Pattern: Stack
LeetCode 155: https://leetcode.com/problems/min-stack/

Problem:
    Design a stack that supports push, pop, top, and retrieving the minimum
    element in constant time.

    Implement the MinStack class:
    - MinStack() initializes the stack object.
    - void push(int val) pushes the element val onto the stack.
    - void pop() removes the element on the top of the stack.
    - int top() gets the top element of the stack.
    - int getMin() retrieves the minimum element in the stack.

    You must implement a solution with O(1) time complexity for each function.

Examples:
    Input:
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        minStack.getMin()   # return -3
        minStack.pop()
        minStack.getMin()   # return -2

Constraints:
    - -2^31 <= val <= 2^31 - 1
    - Methods pop, top and getMin operations will always be called on non-empty stacks
    - At most 3 * 10^4 calls will be made to push, pop, top, and getMin

Hint:
    Keep a second stack (min_stack) that tracks the minimum at each level.
    Every time you push a value, also push the current minimum onto min_stack.
    When you pop, pop from both stacks.

Pattern:
    Parallel Min Stack
    - Main stack stores actual values
    - Min stack stores the minimum value at each level
    - Both stacks grow and shrink together
    - getMin() just peeks at the min stack -> O(1)
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


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Basic min tracking
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3, "Test 1a Failed"
    ms.pop()
    assert ms.top() == 0, "Test 1b Failed"
    assert ms.getMin() == -2, "Test 1c Failed"

    # Test 2: All same values
    ms2 = MinStack()
    ms2.push(5)
    ms2.push(5)
    ms2.push(5)
    assert ms2.getMin() == 5, "Test 2a Failed"
    ms2.pop()
    assert ms2.getMin() == 5, "Test 2b Failed"

    # Test 3: Increasing then decreasing
    ms3 = MinStack()
    ms3.push(1)
    ms3.push(2)
    ms3.push(3)
    assert ms3.getMin() == 1, "Test 3a Failed"
    ms3.pop()
    ms3.pop()
    assert ms3.getMin() == 1, "Test 3b Failed"

    # Test 4: Min changes on pop
    ms4 = MinStack()
    ms4.push(2)
    ms4.push(0)
    ms4.push(3)
    ms4.push(0)
    assert ms4.getMin() == 0, "Test 4a Failed"
    ms4.pop()
    assert ms4.getMin() == 0, "Test 4b Failed"
    ms4.pop()
    assert ms4.getMin() == 0, "Test 4c Failed"
    ms4.pop()
    assert ms4.getMin() == 2, "Test 4d Failed"

    print("All test cases passed!")
