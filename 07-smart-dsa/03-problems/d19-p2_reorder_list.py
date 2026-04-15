"""
Problem: Reorder List (LC 143) | Smart-DSA Day 19 | Medium
Pattern: Linked List — Fast/Slow Pointers
Time target: 30 minutes

Given the head of a singly linked list L0 -> L1 -> ... -> Ln, reorder it to:
L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
Modify the list in-place; do not return a new list.

Example 1:
  Input: head = [1,2,3,4]
  Output: [1,4,2,3]

Example 2:
  Input: head = [1,2,3,4,5]
  Output: [1,5,2,4,3]

Constraints:
  - The number of nodes is in [1, 5 * 10^4].
  - 1 <= Node.val <= 1000

Hint (⚠ read only after time budget is blown):
  Three steps: (1) find the midpoint with fast/slow pointers, (2) reverse the
  second half in place, (3) merge the first half and the reversed second half
  by interleaving — each step is a problem you already know.
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


def reorder_list(head: ListNode | None) -> None:
    pass


if __name__ == "__main__":
    h1 = _from_list([1, 2, 3, 4])
    reorder_list(h1)
    assert _to_list(h1) == [1, 4, 2, 3]

    h2 = _from_list([1, 2, 3, 4, 5])
    reorder_list(h2)
    assert _to_list(h2) == [1, 5, 2, 4, 3]

    h3 = _from_list([1])
    reorder_list(h3)
    assert _to_list(h3) == [1]

    h4 = _from_list([1, 2])
    reorder_list(h4)
    assert _to_list(h4) == [1, 2]

    print("All tests passed!")
