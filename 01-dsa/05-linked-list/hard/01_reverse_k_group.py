"""
Reverse Nodes in k-Group - Day 19 | Hard | LC 25
https://leetcode.com/problems/reverse-nodes-in-k-group/

Pattern: Reversal + Pointer Reconnection

Given the head of a linked list, reverse the nodes of the list k at a
time, and return the modified list. Nodes left out (less than k) at the
end stay in original order.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5, k = 2
    Output: 2 -> 1 -> 4 -> 3 -> 5

    Input:  1 -> 2 -> 3 -> 4 -> 5, k = 3
    Output: 3 -> 2 -> 1 -> 4 -> 5

Approach:
    1. Use a dummy node before head
    2. For each group of k nodes:
       a. Check if there are k nodes remaining
       b. Reverse those k nodes
       c. Reconnect the reversed group to the previous part
       d. Move the pointer to the end of the reversed group
    3. If fewer than k nodes remain, leave them as-is

Time:  O(n) - each node is visited at most twice (check + reverse)
Space: O(1) - only pointer manipulation
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


def reverse_k_group(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy  # node before the current group

    while True:
        # Check if there are k nodes remaining
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next  # fewer than k nodes left, done

        group_next = kth.next  # node after the current group

        # Reverse k nodes: group_prev -> [n1 -> n2 -> ... -> nk] -> group_next
        prev = group_next
        curr = group_prev.next
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Reconnect: group_prev should point to the new first (was kth)
        # The old first node (group_prev.next) is now the last of the group
        old_first = group_prev.next
        group_prev.next = kth  # kth is now the first of reversed group
        group_prev = old_first  # move to end of reversed group for next iteration


if __name__ == "__main__":
    # Test 1: k = 2
    head = build([1, 2, 3, 4, 5])
    result = reverse_k_group(head, 2)
    assert to_list(result) == [2, 1, 4, 3, 5], f"Expected [2,1,4,3,5], got {to_list(result)}"

    # Test 2: k = 3
    head = build([1, 2, 3, 4, 5])
    result = reverse_k_group(head, 3)
    assert to_list(result) == [3, 2, 1, 4, 5], f"Expected [3,2,1,4,5], got {to_list(result)}"

    # Test 3: k = 1 (no change)
    head = build([1, 2, 3])
    result = reverse_k_group(head, 1)
    assert to_list(result) == [1, 2, 3], f"Expected [1,2,3], got {to_list(result)}"

    # Test 4: k = length (reverse entire list)
    head = build([1, 2, 3])
    result = reverse_k_group(head, 3)
    assert to_list(result) == [3, 2, 1], f"Expected [3,2,1], got {to_list(result)}"

    # Test 5: k > length (no change)
    head = build([1, 2])
    result = reverse_k_group(head, 3)
    assert to_list(result) == [1, 2], f"Expected [1,2], got {to_list(result)}"

    # Test 6: Even split
    head = build([1, 2, 3, 4])
    result = reverse_k_group(head, 2)
    assert to_list(result) == [2, 1, 4, 3], f"Expected [2,1,4,3], got {to_list(result)}"

    print("All tests passed!")
