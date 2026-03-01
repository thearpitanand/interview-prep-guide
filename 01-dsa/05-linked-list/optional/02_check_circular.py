"""
Problem: Check if LL is Circular (GFG) | Optional | Easy
Topic: Linked List

Check if a linked list is circular (last node points back to head).

Example 1:
  Input: 1 -> 2 -> 3 -> (back to 1)
  Output: True

Constraints:
  - 1 <= n <= 10^5

Hint: Traverse and check if any node's next is head.
Pattern: Linked List Traversal
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_circular(head: ListNode) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    n1, n2, n3 = ListNode(1), ListNode(2), ListNode(3)
    n1.next, n2.next, n3.next = n2, n3, n1
    assert is_circular(n1) == True

    a = ListNode(1, ListNode(2, ListNode(3)))
    assert is_circular(a) == False
    print("All tests passed!")
