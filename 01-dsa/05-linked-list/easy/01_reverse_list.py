"""
Reverse Linked List - Day 17 | Easy | LC 206
https://leetcode.com/problems/reverse-linked-list/

Pattern: Reversal

Given the head of a singly linked list, reverse the list, and return
the reversed list.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1

Approach:
    - Use three pointers: prev, curr, next_node
    - At each step, save next, reverse the pointer, advance prev and curr
    - When curr is None, prev is the new head

Time:  O(n) - single pass through the list
Space: O(1) - only pointer variables
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


def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # save next before we break the link
        curr.next = prev       # reverse the pointer
        prev = curr            # advance prev
        curr = next_node       # advance curr
    return prev                # prev is the new head


if __name__ == "__main__":
    # Test 1: Normal list
    head = build([1, 2, 3, 4, 5])
    result = reverse_list(head)
    assert to_list(result) == [5, 4, 3, 2, 1], f"Expected [5,4,3,2,1], got {to_list(result)}"

    # Test 2: Empty list
    head = build([])
    result = reverse_list(head)
    assert to_list(result) == [], f"Expected [], got {to_list(result)}"

    # Test 3: Single element
    head = build([1])
    result = reverse_list(head)
    assert to_list(result) == [1], f"Expected [1], got {to_list(result)}"

    # Test 4: Two elements
    head = build([1, 2])
    result = reverse_list(head)
    assert to_list(result) == [2, 1], f"Expected [2,1], got {to_list(result)}"

    print("All tests passed!")
