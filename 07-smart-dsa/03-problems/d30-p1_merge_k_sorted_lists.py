"""
Problem: Merge K Sorted Lists (LC 23) | Smart-DSA Day 30 | Hard
Pattern: Heap / Top-K
Time target: 35 minutes

Merge k sorted linked lists into one sorted linked list and return it.

Example 1:
  Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
  Output: [1, 1, 2, 3, 4, 4, 5, 6]

Example 2:
  Input: lists = []
  Output: []

Constraints:
  - k == lists.length
  - 0 <= k <= 10^4
  - 0 <= lists[i].length <= 500
  - -10^4 <= lists[i][j] <= 10^4
  - lists[i] is sorted in ascending order.

Hint (⚠ read only after time budget is blown):
  Push (node.val, list_index, node) into a min-heap. Pop the smallest, append
  to result, then push that node's next (if any). Use list_index as a
  tiebreaker so ListNode objects are never compared directly.
"""
import heapq
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def build_list(values: list[int]) -> Optional[ListNode]:
    """Helper: build a linked list from a Python list."""
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def list_to_array(head: Optional[ListNode]) -> list[int]:
    """Helper: convert linked list back to a Python list for assertions."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    pass


if __name__ == "__main__":
    lists1 = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    assert list_to_array(merge_k_lists(lists1)) == [1, 1, 2, 3, 4, 4, 5, 6]

    assert list_to_array(merge_k_lists([])) == []

    lists3 = [build_list([])]
    assert list_to_array(merge_k_lists(lists3)) == []

    lists4 = [build_list([1]), build_list([0])]
    assert list_to_array(merge_k_lists(lists4)) == [0, 1]
    print("All tests passed!")
