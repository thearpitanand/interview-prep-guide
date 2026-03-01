"""
Remove Duplicates from Sorted List - Day 18 | Medium | LC 83
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Pattern: Traversal

Given the head of a sorted linked list, delete all duplicates such
that each element appears only once. Return the sorted list.

Example:
    Input:  1 -> 1 -> 2 -> 3 -> 3
    Output: 1 -> 2 -> 3

Approach:
    - Since the list is sorted, duplicates are adjacent
    - Traverse with a pointer; if curr.val == curr.next.val, skip next
    - Otherwise, move curr forward
    - No dummy node needed since head never changes

Time:  O(n) - single pass
Space: O(1) - in-place modification
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


def delete_duplicates(head: ListNode) -> ListNode:
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next  # skip the duplicate
        else:
            curr = curr.next            # move forward
    return head


if __name__ == "__main__":
    # Test 1: Multiple duplicates
    head = build([1, 1, 2, 3, 3])
    result = delete_duplicates(head)
    assert to_list(result) == [1, 2, 3], f"Expected [1,2,3], got {to_list(result)}"

    # Test 2: All same
    head = build([1, 1, 1])
    result = delete_duplicates(head)
    assert to_list(result) == [1], f"Expected [1], got {to_list(result)}"

    # Test 3: No duplicates
    head = build([1, 2, 3])
    result = delete_duplicates(head)
    assert to_list(result) == [1, 2, 3], f"Expected [1,2,3], got {to_list(result)}"

    # Test 4: Empty list
    result = delete_duplicates(None)
    assert to_list(result) == [], f"Expected [], got {to_list(result)}"

    # Test 5: Single element
    head = build([1])
    result = delete_duplicates(head)
    assert to_list(result) == [1], f"Expected [1], got {to_list(result)}"

    print("All tests passed!")
