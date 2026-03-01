"""
Implement Stack using Queues

Day: 20 | Difficulty: Easy | Pattern: Queue
LeetCode 225: https://leetcode.com/problems/implement-stack-using-queues/

Problem:
    Implement a last-in-first-out (LIFO) stack using only two queues.
    The implemented stack should support all the functions of a normal stack
    (push, top, pop, and empty).

    Implement the MyStack class:
    - void push(int x) -- Pushes element x to the top of the stack.
    - int pop() -- Removes the element on the top of the stack and returns it.
    - int top() -- Returns the element on the top of the stack.
    - boolean empty() -- Returns true if the stack is empty, false otherwise.

Examples:
    Input:
        myStack = MyStack()
        myStack.push(1)
        myStack.push(2)
        myStack.top()    # return 2
        myStack.pop()    # return 2
        myStack.empty()  # return False

Constraints:
    - 1 <= x <= 9
    - At most 100 calls will be made to push, pop, top, and empty
    - All the calls to pop and top are valid

Hint:
    Use a single queue. After each push, rotate the queue so the most recently
    pushed element is at the front. To rotate: pop from front and push to back
    (n-1) times.

Pattern:
    Queue Rotation
    - Push x, then rotate queue (n-1) times so x is at front
    - This makes pop() and top() O(1), push() is O(n)
    - Alternative: use two queues and swap after transferring
"""

from collections import deque


class MyStack:
    def __init__(self):
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def top(self) -> int:
        pass

    def empty(self) -> bool:
        pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Basic operations
    s = MyStack()
    s.push(1)
    s.push(2)
    assert s.top() == 2, "Test 1a Failed"
    assert s.pop() == 2, "Test 1b Failed"
    assert s.empty() == False, "Test 1c Failed"

    # Test 2: Pop all elements
    s2 = MyStack()
    s2.push(1)
    s2.push(2)
    assert s2.pop() == 2, "Test 2a Failed"
    assert s2.pop() == 1, "Test 2b Failed"
    assert s2.empty() == True, "Test 2c Failed"

    # Test 3: Push after pop
    s3 = MyStack()
    s3.push(1)
    s3.push(2)
    s3.pop()
    s3.push(3)
    assert s3.top() == 3, "Test 3a Failed"
    assert s3.pop() == 3, "Test 3b Failed"
    assert s3.pop() == 1, "Test 3c Failed"

    # Test 4: Single element
    s4 = MyStack()
    s4.push(42)
    assert s4.top() == 42, "Test 4a Failed"
    assert s4.pop() == 42, "Test 4b Failed"
    assert s4.empty() == True, "Test 4c Failed"

    print("All test cases passed!")
