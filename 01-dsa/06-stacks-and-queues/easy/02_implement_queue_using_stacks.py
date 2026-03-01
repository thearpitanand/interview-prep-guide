"""
Implement Queue using Stacks

Day: 20 | Difficulty: Easy | Pattern: Stack
LeetCode 232: https://leetcode.com/problems/implement-queue-using-stacks/

Problem:
    Implement a first-in-first-out (FIFO) queue using only two stacks.
    The implemented queue should support all the functions of a normal queue
    (push, peek, pop, and empty).

    Implement the MyQueue class:
    - void push(int x) -- Pushes element x to the back of the queue.
    - int pop() -- Removes the element from the front of the queue and returns it.
    - int peek() -- Returns the element at the front of the queue.
    - boolean empty() -- Returns true if the queue is empty, false otherwise.

Examples:
    Input:
        myQueue = MyQueue()
        myQueue.push(1)   # queue is: [1]
        myQueue.push(2)   # queue is: [1, 2]
        myQueue.peek()    # return 1
        myQueue.pop()     # return 1, queue is [2]
        myQueue.empty()   # return False

Constraints:
    - 1 <= x <= 9
    - At most 100 calls will be made to push, pop, peek, and empty
    - All the calls to pop and peek are valid

Hint:
    Use two stacks: one for pushing (input stack) and one for popping (output stack).
    When the output stack is empty, transfer all elements from the input stack
    to the output stack. This reverses the order, giving FIFO behavior.

Pattern:
    Two Stack Queue
    - Push: always push to input stack
    - Pop/Peek: if output stack is empty, transfer all from input to output
    - Amortized O(1) for all operations
"""


class MyQueue:
    def __init__(self):
        pass

    def push(self, x: int) -> None:
        pass

    def pop(self) -> int:
        pass

    def peek(self) -> int:
        pass

    def empty(self) -> bool:
        pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Basic operations
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1, "Test 1a Failed"
    assert q.pop() == 1, "Test 1b Failed"
    assert q.empty() == False, "Test 1c Failed"

    # Test 2: Empty after all pops
    q2 = MyQueue()
    q2.push(1)
    q2.pop()
    assert q2.empty() == True, "Test 2 Failed"

    # Test 3: Interleaved push and pop
    q3 = MyQueue()
    q3.push(1)
    q3.push(2)
    q3.push(3)
    assert q3.pop() == 1, "Test 3a Failed"
    q3.push(4)
    assert q3.pop() == 2, "Test 3b Failed"
    assert q3.pop() == 3, "Test 3c Failed"
    assert q3.pop() == 4, "Test 3d Failed"
    assert q3.empty() == True, "Test 3e Failed"

    # Test 4: Peek doesn't remove
    q4 = MyQueue()
    q4.push(10)
    assert q4.peek() == 10, "Test 4a Failed"
    assert q4.peek() == 10, "Test 4b Failed"
    assert q4.empty() == False, "Test 4c Failed"

    print("All test cases passed!")
