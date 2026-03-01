"""
Problem: Remove Duplicates from Unsorted Linked List (GFG) | Day 18 | Medium
Topic: Linked List

Given an unsorted linked list, remove all duplicate nodes (keep first occurrence).

Example 1:
  Input: 5 -> 2 -> 2 -> 4 -> 5
  Output: 5 -> 2 -> 4

Constraints:
  - 1 <= n <= 10^5
  - 1 <= node.val <= 10^4

Hint: Use a hash set to track seen values.
Pattern: Hashing
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


def remove_duplicates_unsorted(head: ListNode) -> ListNode:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert to_list(remove_duplicates_unsorted(build([5, 2, 2, 4, 5]))) == [5, 2, 4]
    assert to_list(remove_duplicates_unsorted(build([1, 1, 1]))) == [1]
    assert to_list(remove_duplicates_unsorted(build([1, 2, 3]))) == [1, 2, 3]
    print("All tests passed!")
