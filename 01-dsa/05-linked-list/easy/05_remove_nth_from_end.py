"""
Remove Nth Node From End of List - Day 17 | Easy | LC 19
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Pattern: Two Pointers (Gap Technique)

Given the head of a linked list, remove the nth node from the end
and return the head.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5, n = 2
    Output: 1 -> 2 -> 3 -> 5

Approach:
    - Use a dummy node to handle edge case of removing the head
    - Move fast pointer n+1 steps ahead (so there is an n-node gap)
    - Move both pointers until fast reaches None
    - slow is now just before the node to remove
    - Skip over the target node: slow.next = slow.next.next

Time:  O(n) - single pass
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


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    # Move fast n+1 steps ahead so the gap between fast and slow is n
    for _ in range(n + 1):
        fast = fast.next

    # Move both until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next

    # slow is now right before the node to remove
    slow.next = slow.next.next

    return dummy.next


if __name__ == "__main__":
    # Test 1: Remove 2nd from end
    head = build([1, 2, 3, 4, 5])
    result = remove_nth_from_end(head, 2)
    assert to_list(result) == [1, 2, 3, 5], f"Expected [1,2,3,5], got {to_list(result)}"

    # Test 2: Remove the only element
    head = build([1])
    result = remove_nth_from_end(head, 1)
    assert to_list(result) == [], f"Expected [], got {to_list(result)}"

    # Test 3: Remove head (last from end = length)
    head = build([1, 2])
    result = remove_nth_from_end(head, 2)
    assert to_list(result) == [2], f"Expected [2], got {to_list(result)}"

    # Test 4: Remove tail
    head = build([1, 2, 3])
    result = remove_nth_from_end(head, 1)
    assert to_list(result) == [1, 2], f"Expected [1,2], got {to_list(result)}"

    print("All tests passed!")
