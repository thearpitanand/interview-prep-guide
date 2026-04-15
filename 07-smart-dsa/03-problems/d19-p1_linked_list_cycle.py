"""
Problem: Linked List Cycle (LC 141) | Smart-DSA Day 19 | Medium
Pattern: Linked List — Fast/Slow Pointers
Time target: 20 minutes

Given the head of a linked list, determine if the linked list has a cycle.
Return True if there is a cycle, otherwise return False.

Example 1:
  Input: head = [3,2,0,-4], pos = 1  (tail connects to node at index 1)
  Output: True

Example 2:
  Input: head = [1,2], pos = 0  (tail connects to node at index 0)
  Output: True

Example 3:
  Input: head = [1], pos = -1  (no cycle)
  Output: False

Constraints:
  - The number of nodes in the list is in [0, 10^4].
  - -10^5 <= Node.val <= 10^5
  - pos is -1 or a valid index in the linked list.

Hint (⚠ read only after time budget is blown):
  Floyd's tortoise and hare: slow moves 1 step, fast moves 2 steps. If they
  ever point to the same node there is a cycle. If fast reaches None, no cycle.
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    pass


if __name__ == "__main__":
    # Build [3 -> 2 -> 0 -> -4 -> (back to 2)]
    n1, n2, n3, n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2
    assert has_cycle(n1) is True

    # Build [1 -> 2 -> (back to 1)]
    a, b = ListNode(1), ListNode(2)
    a.next = b; b.next = a
    assert has_cycle(a) is True

    # Single node, no cycle
    assert has_cycle(ListNode(1)) is False

    # Empty
    assert has_cycle(None) is False

    # [1 -> 2 -> 3], no cycle
    x, y, z = ListNode(1), ListNode(2), ListNode(3)
    x.next = y; y.next = z
    assert has_cycle(x) is False

    print("All tests passed!")
