"""
Linked List Cycle - Day 17 | Easy | LC 141
https://leetcode.com/problems/linked-list-cycle/

Pattern: Fast & Slow Pointers (Floyd's Cycle Detection)

Given head, determine if the linked list has a cycle in it.
A cycle exists if some node's next pointer points back to a
previously visited node.

Example:
    3 -> 2 -> 0 -> -4
         ^          |
         |__________|    --> True (cycle at node 2)

Approach (Floyd's Tortoise and Hare):
    - Slow pointer moves 1 step, fast moves 2 steps
    - If there is a cycle, fast will eventually catch up to slow
    - If fast reaches None, there is no cycle

Why it works:
    - In a cycle, fast closes the gap by 1 node per step
    - They must meet within one full loop of the cycle

Time:  O(n) - at most 2 full traversals
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


def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    # Test 1: List with cycle
    # 3 -> 2 -> 0 -> -4 -> (back to 2)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # creates cycle
    assert has_cycle(node1) == True, "Expected True for cyclic list"

    # Test 2: List without cycle
    head = build([1, 2, 3, 4, 5])
    assert has_cycle(head) == False, "Expected False for non-cyclic list"

    # Test 3: Single node, no cycle
    head = build([1])
    assert has_cycle(head) == False, "Expected False for single node"

    # Test 4: Single node with self-cycle
    node = ListNode(1)
    node.next = node
    assert has_cycle(node) == True, "Expected True for self-cycle"

    # Test 5: Empty list
    assert has_cycle(None) == False, "Expected False for empty list"

    print("All tests passed!")
