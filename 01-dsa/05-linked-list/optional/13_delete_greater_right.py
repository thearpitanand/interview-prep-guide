"""
Problem: Delete Nodes with Greater on Right (GFG) | Optional | Medium
Topic: Linked List

Given a linked list, delete all nodes that have a greater value node on their right.

Example 1:
  Input: 12 -> 15 -> 10 -> 11 -> 5 -> 6 -> 2 -> 3
  Output: 15 -> 11 -> 6 -> 3

Constraints:
  - 1 <= n <= 10^5

Hint: Reverse list, keep running max, remove nodes less than max, reverse back.
Pattern: Reverse and Track Max
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


def delete_greater_right(head: ListNode) -> ListNode:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert to_list(delete_greater_right(build([12, 15, 10, 11, 5, 6, 2, 3]))) == [15, 11, 6, 3]
    assert to_list(delete_greater_right(build([10, 20, 30]))) == [30]
    print("All tests passed!")
