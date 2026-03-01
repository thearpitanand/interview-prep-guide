"""
Middle of the Linked List - Day 17 | Easy | LC 876
https://leetcode.com/problems/middle-of-the-linked-list/

Pattern: Fast & Slow Pointers

Given the head of a singly linked list, return the middle node.
If there are two middle nodes, return the second middle node.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: Node with value 3

    Input:  1 -> 2 -> 3 -> 4 -> 5 -> 6
    Output: Node with value 4 (second middle)

Approach:
    - Use slow pointer (1 step) and fast pointer (2 steps)
    - When fast reaches the end, slow is at the middle
    - For even length, slow lands on the second middle naturally

Time:  O(n) - single pass (fast traverses full list)
Space: O(1) - two pointers
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


def middle_node(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    # Test 1: Odd length - exact middle
    head = build([1, 2, 3, 4, 5])
    result = middle_node(head)
    assert result.val == 3, f"Expected 3, got {result.val}"

    # Test 2: Even length - second middle
    head = build([1, 2, 3, 4, 5, 6])
    result = middle_node(head)
    assert result.val == 4, f"Expected 4, got {result.val}"

    # Test 3: Single element
    head = build([1])
    result = middle_node(head)
    assert result.val == 1, f"Expected 1, got {result.val}"

    # Test 4: Two elements
    head = build([1, 2])
    result = middle_node(head)
    assert result.val == 2, f"Expected 2, got {result.val}"

    print("All tests passed!")
