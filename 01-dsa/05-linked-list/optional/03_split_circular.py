"""
Problem: Split Circular LL into Two Halves (GFG) | Optional | Easy
Topic: Linked List

Split a circular linked list into two halves. If odd, first list gets extra node.

Example 1:
  Input: circular: 1 -> 2 -> 3 -> 4 -> (back to 1)
  Output: circular1: 1 -> 2, circular2: 3 -> 4

Constraints:
  - 1 <= n <= 10^5

Hint: Use slow/fast pointer to find middle, then split.
Pattern: Slow-Fast Pointer
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def split_circular(head: ListNode) -> tuple:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    # Build circular: 1->2->3->4->1
    n1, n2, n3, n4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n1
    h1, h2 = split_circular(n1)
    assert h1 is not None and h2 is not None
    print("All tests passed!")
