"""
Problem: Reverse a Doubly Linked List (GFG) | Optional | Easy
Topic: Linked List

Reverse a doubly linked list.

Example 1:
  Input: 1 <-> 2 <-> 3 <-> 4
  Output: 4 <-> 3 <-> 2 <-> 1

Constraints:
  - 1 <= n <= 10^4

Hint: Swap prev and next pointers for every node.
Pattern: Pointer Manipulation
"""


class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def reverse_dll(head: DLLNode) -> DLLNode:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    n1, n2, n3 = DLLNode(1), DLLNode(2), DLLNode(3)
    n1.next, n2.prev = n2, n1
    n2.next, n3.prev = n3, n2
    head = reverse_dll(n1)
    assert head.val == 3
    assert head.next.val == 2
    assert head.next.next.val == 1
    print("All tests passed!")
