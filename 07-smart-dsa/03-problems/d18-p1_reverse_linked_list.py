"""
Problem: Reverse Linked List (LC 206) | Smart-DSA Day 18 | Easy
Pattern: Linked List
Time target: 15 minutes

Given the head of a singly linked list, reverse the list and return the
reversed list's head.

Example 1:
  Input: head = [1,2,3,4,5]
  Output: [5,4,3,2,1]

Example 2:
  Input: head = [1,2]
  Output: [2,1]

Example 3:
  Input: head = []
  Output: []

Constraints:
  - The number of nodes is in the range [0, 5000].
  - -5000 <= Node.val <= 5000

Hint (⚠ read only after time budget is blown):
  Three pointers: prev=None, curr=head. Each iteration: save curr.next, point
  curr.next to prev, advance both pointers. Return prev when curr is None.
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def _to_list(head: ListNode | None) -> list[int]:
    result: list[int] = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def _from_list(values: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def reverse_list(head: ListNode | None) -> ListNode | None:
    pass


if __name__ == "__main__":
    assert _to_list(reverse_list(_from_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert _to_list(reverse_list(_from_list([1, 2]))) == [2, 1]
    assert _to_list(reverse_list(_from_list([]))) == []
    assert _to_list(reverse_list(_from_list([1]))) == [1]
    print("All tests passed!")
