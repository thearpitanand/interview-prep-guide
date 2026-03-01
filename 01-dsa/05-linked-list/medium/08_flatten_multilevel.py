"""
Flatten a Multilevel Doubly Linked List - Day 19 | Medium | LC 430
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

Pattern: DFS (Depth-First Search)

A multilevel doubly linked list has nodes that may have a child pointer
pointing to a separate doubly linked list. Flatten all levels into a
single-level doubly linked list.

Simplified version: We represent the multilevel structure using nested
lists and flatten them into a single linked list.

Example:
    Input:  1 -- 2 -- 3 -- 4 -- 5 -- 6
                      |
                      7 -- 8 -- 9 -- 10
                           |
                           11 -- 12
    Output: 1 - 2 - 3 - 7 - 8 - 11 - 12 - 9 - 10 - 4 - 5 - 6

Approach:
    - Use DFS / stack-based approach
    - When encountering a child, push next onto stack, process child
    - When reaching end of a level, pop from stack to continue

Time:  O(n) - visit each node once
Space: O(n) - stack for nested levels
"""


class ListNode:
    """Simplified node with val, next, and child pointers."""
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child


def build(arr):
    """Build a flat linked list from array."""
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


def build_multilevel(data):
    """
    Build a multilevel list from nested structure.
    data is a list where sublists represent child levels.

    Example: [1, 2, [3, 4, [5, 6]], 7]
    Creates: 1 - 2 - 7
                 |
                 3 - 4
                     |
                     5 - 6
    Convention: a sublist after a value becomes the child of that value's node.
    """
    if not data:
        return None

    dummy = ListNode(0)
    curr = dummy
    i = 0

    while i < len(data):
        if isinstance(data[i], list):
            # This sublist is the child of the previous node
            curr.child = build_multilevel(data[i])
            i += 1
        else:
            curr.next = ListNode(data[i])
            curr = curr.next
            i += 1

    return dummy.next


def flatten(head: ListNode) -> ListNode:
    if not head:
        return None

    curr = head
    stack = []

    while curr:
        # If current node has a child, handle it
        if curr.child:
            # Save next for later (if exists)
            if curr.next:
                stack.append(curr.next)
            # Child becomes the next node
            curr.next = curr.child
            curr.child = None

        # If we reached the end of current level, check stack
        if not curr.next and stack:
            curr.next = stack.pop()

        curr = curr.next

    return head


if __name__ == "__main__":
    # Test 1: Multilevel list
    # Level 1: 1 - 2 - 3 - 4
    # Level 2 (child of 2): 5 - 6
    head = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    head.next = n2
    n2.next = n3
    n3.next = n4
    n2.child = n5
    n5.next = n6
    result = flatten(head)
    assert to_list(result) == [1, 2, 5, 6, 3, 4], f"Expected [1,2,5,6,3,4], got {to_list(result)}"

    # Test 2: Three levels
    # Level 1: 1 - 2 - 3
    # Level 2 (child of 1): 4 - 5
    # Level 3 (child of 4): 6
    head = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    head.next = n2
    n2.next = n3
    head.child = n4
    n4.next = n5
    n4.child = n6
    result = flatten(head)
    assert to_list(result) == [1, 4, 6, 5, 2, 3], f"Expected [1,4,6,5,2,3], got {to_list(result)}"

    # Test 3: No children (flat list)
    head = build([1, 2, 3])
    result = flatten(head)
    assert to_list(result) == [1, 2, 3], f"Expected [1,2,3], got {to_list(result)}"

    # Test 4: Empty list
    result = flatten(None)
    assert to_list(result) == [], f"Expected [], got {to_list(result)}"

    # Test 5: Single node with child
    head = ListNode(1)
    head.child = ListNode(2)
    result = flatten(head)
    assert to_list(result) == [1, 2], f"Expected [1,2], got {to_list(result)}"

    print("All tests passed!")
