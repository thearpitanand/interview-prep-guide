"""
Problem: Quicksort for Linked List (GFG) | Optional | Hard
Topic: Linked List

Implement quicksort for a singly linked list.

Example 1:
  Input: 5 -> 3 -> 8 -> 1 -> 2
  Output: 1 -> 2 -> 3 -> 5 -> 8

Constraints:
  - 1 <= n <= 10^5

Hint: Partition around pivot (last element), recurse on sublists.
Pattern: Quicksort / Partition
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


def quicksort_ll(head: ListNode) -> ListNode:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert to_list(quicksort_ll(build([5, 3, 8, 1, 2]))) == [1, 2, 3, 5, 8]
    assert to_list(quicksort_ll(build([1]))) == [1]
    print("All tests passed!")
