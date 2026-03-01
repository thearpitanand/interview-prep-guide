"""
Problem: Deletion from Circular LL (GFG) | Optional | Easy
Topic: Linked List

Delete a given node from a circular linked list.

Example 1:
  Input: circular: 1 -> 2 -> 3 -> 4, delete 3
  Output: circular: 1 -> 2 -> 4

Constraints:
  - 1 <= n <= 10^5

Hint: Find the node before target, update its next pointer.
Pattern: Linked List Traversal
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_from_circular(head: ListNode, key: int) -> ListNode:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    n1, n2, n3, n4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n1
    head = delete_from_circular(n1, 3)
    # Verify 3 is removed
    vals = []
    curr = head
    for _ in range(3):
        vals.append(curr.val)
        curr = curr.next
    assert 3 not in vals
    print("All tests passed!")
