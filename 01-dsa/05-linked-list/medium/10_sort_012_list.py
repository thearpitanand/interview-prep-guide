"""
Problem: Sort Linked List of 0s, 1s, 2s (GFG) | Day 18 | Medium
Topic: Linked List

Given a linked list of 0s, 1s, and 2s, sort it in a single traversal.

Example 1:
  Input: 1 -> 2 -> 0 -> 1
  Output: 0 -> 1 -> 1 -> 2

Constraints:
  - 1 <= n <= 10^6
  - 0 <= node.val <= 2

Hint: Use three dummy heads for 0s, 1s, 2s — connect them at the end.
Pattern: Dutch National Flag / Three-Way Partition
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(arr):
    dummy = ListNode(0)
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def sort_012_list(head: ListNode) -> ListNode:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert to_list(sort_012_list(build([1, 2, 0, 1]))) == [0, 1, 1, 2]
    assert to_list(sort_012_list(build([2, 1, 0]))) == [0, 1, 2]
    assert to_list(sort_012_list(build([0, 0, 0]))) == [0, 0, 0]
    print("All tests passed!")
