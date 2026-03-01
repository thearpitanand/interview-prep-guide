"""
Reorder List - Day 18 | Medium | LC 143
https://leetcode.com/problems/reorder-list/

Pattern: Fast & Slow + Reversal + Merge

Reorder the list: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
Do it in-place without modifying node values.

Example:
    Input:  1 -> 2 -> 3 -> 4
    Output: 1 -> 4 -> 2 -> 3

    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: 1 -> 5 -> 2 -> 4 -> 3

Approach (3 classic steps combined):
    1. Find middle using fast/slow pointers
    2. Reverse the second half
    3. Merge the two halves by alternating nodes

Time:  O(n) - three O(n) passes
Space: O(1) - in-place
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


def reorder_list(head: ListNode) -> None:
    if not head or not head.next:
        return

    # Step 1: Find the middle
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half
    prev = None
    curr = slow.next
    slow.next = None  # cut the list
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    # prev is now the head of the reversed second half

    # Step 3: Merge two halves alternately
    first = head
    second = prev
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2


if __name__ == "__main__":
    # Test 1: Even length
    head = build([1, 2, 3, 4])
    reorder_list(head)
    assert to_list(head) == [1, 4, 2, 3], f"Expected [1,4,2,3], got {to_list(head)}"

    # Test 2: Odd length
    head = build([1, 2, 3, 4, 5])
    reorder_list(head)
    assert to_list(head) == [1, 5, 2, 4, 3], f"Expected [1,5,2,4,3], got {to_list(head)}"

    # Test 3: Two elements
    head = build([1, 2])
    reorder_list(head)
    assert to_list(head) == [1, 2], f"Expected [1,2], got {to_list(head)}"

    # Test 4: Single element
    head = build([1])
    reorder_list(head)
    assert to_list(head) == [1], f"Expected [1], got {to_list(head)}"

    # Test 5: Longer list
    head = build([1, 2, 3, 4, 5, 6])
    reorder_list(head)
    assert to_list(head) == [1, 6, 2, 5, 3, 4], f"Expected [1,6,2,5,3,4], got {to_list(head)}"

    print("All tests passed!")
