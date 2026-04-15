"""
Problem: Merge Two Sorted Lists (LC 21) | Smart-DSA Day 18 | Easy
Pattern: Linked List
Time target: 15 minutes

You are given the heads of two sorted linked lists list1 and list2. Merge
the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists. Return the head of the merged list.

Example 1:
  Input: list1 = [1,2,4], list2 = [1,3,4]
  Output: [1,1,2,3,4,4]

Example 2:
  Input: list1 = [], list2 = []
  Output: []

Example 3:
  Input: list1 = [], list2 = [0]
  Output: [0]

Constraints:
  - The number of nodes in both lists is in [0, 50].
  - -100 <= Node.val <= 100
  - Both lists are sorted in non-decreasing order.

Hint (⚠ read only after time budget is blown):
  Use a dummy head to avoid special-casing the first node. Compare list1.val
  and list2.val, attach the smaller node to the result, advance that pointer.
  Attach the remaining non-empty list at the end.
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


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    pass


if __name__ == "__main__":
    assert _to_list(merge_two_lists(_from_list([1, 2, 4]), _from_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert _to_list(merge_two_lists(_from_list([]), _from_list([]))) == []
    assert _to_list(merge_two_lists(_from_list([]), _from_list([0]))) == [0]
    assert _to_list(merge_two_lists(_from_list([5]), _from_list([1, 2, 3]))) == [1, 2, 3, 5]
    print("All tests passed!")
