"""
Odd Even Linked List - Day 18 | Medium | LC 328
https://leetcode.com/problems/odd-even-linked-list/

Pattern: Pointer Manipulation

Group all odd-indexed nodes together followed by even-indexed nodes.
The first node is considered odd (index 1), second is even, etc.
Maintain the relative order within each group.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: 1 -> 3 -> 5 -> 2 -> 4
    (odd positions: 1,3,5 then even positions: 2,4)

Approach:
    - Maintain two separate chains: odd and even
    - odd pointer collects nodes at odd positions
    - even pointer collects nodes at even positions
    - Connect end of odd chain to head of even chain

Time:  O(n) - single pass
Space: O(1) - rearranging existing nodes
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


def odd_even_list(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even  # save to connect later

    while even and even.next:
        odd.next = even.next    # odd points to next odd
        odd = odd.next
        even.next = odd.next    # even points to next even
        even = even.next

    odd.next = even_head  # connect odd chain to even chain
    return head


if __name__ == "__main__":
    # Test 1: Odd length
    head = build([1, 2, 3, 4, 5])
    result = odd_even_list(head)
    assert to_list(result) == [1, 3, 5, 2, 4], f"Expected [1,3,5,2,4], got {to_list(result)}"

    # Test 2: Even length
    head = build([2, 1, 3, 5, 6, 4, 7])
    result = odd_even_list(head)
    assert to_list(result) == [2, 3, 6, 7, 1, 5, 4], f"Expected [2,3,6,7,1,5,4], got {to_list(result)}"

    # Test 3: Two elements
    head = build([1, 2])
    result = odd_even_list(head)
    assert to_list(result) == [1, 2], f"Expected [1,2], got {to_list(result)}"

    # Test 4: Single element
    head = build([1])
    result = odd_even_list(head)
    assert to_list(result) == [1], f"Expected [1], got {to_list(result)}"

    # Test 5: Empty
    result = odd_even_list(None)
    assert to_list(result) == [], f"Expected [], got {to_list(result)}"

    print("All tests passed!")
