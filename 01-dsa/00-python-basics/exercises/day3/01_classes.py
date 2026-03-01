"""
Exercise: Classes | Day 3
Topic: Python OOP

Practice creating classes, magic methods, and inheritance.

Instructions: Implement each class below.
"""


class Stack:
    """Implement a stack using a list.

    Methods: push(val), pop(), peek(), is_empty(), size()
    pop() and peek() should return None if stack is empty.
    """

    def __init__(self):
        pass

    def push(self, val):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def is_empty(self) -> bool:
        pass

    def size(self) -> int:
        pass

    def __str__(self) -> str:
        """Return string representation: 'Stack([1, 2, 3])'"""
        pass


class Queue:
    """Implement a queue using a list.

    Methods: enqueue(val), dequeue(), front(), is_empty(), size()
    dequeue() and front() should return None if queue is empty.
    """

    def __init__(self):
        pass

    def enqueue(self, val):
        pass

    def dequeue(self):
        pass

    def front(self):
        pass

    def is_empty(self) -> bool:
        pass

    def size(self) -> int:
        pass


class ListNode:
    """A node in a singly linked list."""

    def __init__(self, val=0, next=None):
        pass

    def __str__(self) -> str:
        """Return string like '1 -> 2 -> 3 -> None'"""
        pass


# --- Tests ---
if __name__ == "__main__":
    s = Stack()
    assert s.is_empty() == True
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.peek() == 3
    assert s.pop() == 3
    assert s.size() == 2

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.front() == 1
    assert q.dequeue() == 1
    assert q.size() == 1

    node = ListNode(1, ListNode(2, ListNode(3)))
    assert str(node) == "1 -> 2 -> 3 -> None"
    print("All tests passed!")
