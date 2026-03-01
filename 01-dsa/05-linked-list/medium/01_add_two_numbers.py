"""
Add Two Numbers - Day 18 | Medium | LC 2
https://leetcode.com/problems/add-two-numbers/

Pattern: Traversal + Dummy Node

Two non-empty linked lists represent two non-negative integers.
Digits are stored in reverse order, each node contains a single digit.
Add the two numbers and return the sum as a linked list.

Example:
    Input:  2 -> 4 -> 3  (342)
            5 -> 6 -> 4  (465)
    Output: 7 -> 0 -> 8  (807)
    Because 342 + 465 = 807

Approach:
    - Traverse both lists simultaneously, adding corresponding digits
    - Track carry from each addition
    - Create new nodes for each digit of the result
    - Use dummy node to simplify list construction
    - Don't forget the final carry!

Time:  O(max(n, m)) - traverse the longer list
Space: O(max(n, m)) - new list for the result
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


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        curr.next = ListNode(digit)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


if __name__ == "__main__":
    # Test 1: 342 + 465 = 807
    l1 = build([2, 4, 3])
    l2 = build([5, 6, 4])
    result = add_two_numbers(l1, l2)
    assert to_list(result) == [7, 0, 8], f"Expected [7,0,8], got {to_list(result)}"

    # Test 2: 0 + 0 = 0
    l1 = build([0])
    l2 = build([0])
    result = add_two_numbers(l1, l2)
    assert to_list(result) == [0], f"Expected [0], got {to_list(result)}"

    # Test 3: Different lengths with carry: 99 + 1 = 100
    l1 = build([9, 9])
    l2 = build([1])
    result = add_two_numbers(l1, l2)
    assert to_list(result) == [0, 0, 1], f"Expected [0,0,1], got {to_list(result)}"

    # Test 4: 999 + 999 = 1998
    l1 = build([9, 9, 9])
    l2 = build([9, 9, 9])
    result = add_two_numbers(l1, l2)
    assert to_list(result) == [8, 9, 9, 1], f"Expected [8,9,9,1], got {to_list(result)}"

    print("All tests passed!")
