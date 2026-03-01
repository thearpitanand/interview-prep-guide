"""
Merge Two Sorted Lists - Day 17 | Easy | LC 21
https://leetcode.com/problems/merge-two-sorted-lists/

Pattern: Merge / Dummy Node

Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the two lists.

Example:
    Input:  1 -> 2 -> 4,  1 -> 3 -> 4
    Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4

Approach:
    - Create a dummy head node to simplify edge cases
    - Compare nodes from both lists, attach the smaller one
    - When one list is exhausted, attach the remaining of the other
    - Return dummy.next

Time:  O(n + m) - visit each node once
Space: O(1) - only rearranging pointers, no new nodes created
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


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    # Attach whichever list still has nodes
    curr.next = list1 or list2

    return dummy.next


if __name__ == "__main__":
    # Test 1: Normal merge
    l1 = build([1, 2, 4])
    l2 = build([1, 3, 4])
    result = merge_two_lists(l1, l2)
    assert to_list(result) == [1, 1, 2, 3, 4, 4], f"Expected [1,1,2,3,4,4], got {to_list(result)}"

    # Test 2: Both empty
    result = merge_two_lists(None, None)
    assert to_list(result) == [], f"Expected [], got {to_list(result)}"

    # Test 3: One empty
    l1 = build([1, 2, 3])
    result = merge_two_lists(l1, None)
    assert to_list(result) == [1, 2, 3], f"Expected [1,2,3], got {to_list(result)}"

    # Test 4: Different lengths
    l1 = build([1])
    l2 = build([2, 3, 4])
    result = merge_two_lists(l1, l2)
    assert to_list(result) == [1, 2, 3, 4], f"Expected [1,2,3,4], got {to_list(result)}"

    print("All tests passed!")
