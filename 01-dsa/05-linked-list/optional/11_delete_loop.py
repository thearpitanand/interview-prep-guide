"""
Problem: Delete Loop in Linked List (GFG) | Optional | Medium
Topic: Linked List

Detect and remove the loop in a linked list.

Example 1:
  Input: 1 -> 2 -> 3 -> 4 -> 5 -> (back to 3)
  Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

Constraints:
  - 1 <= n <= 10^4

Hint: Floyd's detection + fix: find meeting point, then find loop start, remove link.
Pattern: Floyd's Cycle Detection
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_list(head, limit=10):
    result = []
    while head and len(result) < limit:
        result.append(head.val)
        head = head.next
    return result


def delete_loop(head: ListNode) -> None:
    # Write your solution here (modify in-place)
    pass


# --- Tests ---
if __name__ == "__main__":
    n1, n2, n3, n4, n5 = [ListNode(i) for i in range(1, 6)]
    n1.next, n2.next, n3.next, n4.next, n5.next = n2, n3, n4, n5, n3
    delete_loop(n1)
    assert to_list(n1) == [1, 2, 3, 4, 5]
    print("All tests passed!")
