"""
Problem: Add 1 to Number as Linked List (GFG) | Optional | Medium
Topic: Linked List

Given a number represented as a linked list (head is MSB), add 1 to it.

Example 1:
  Input: 1 -> 9 -> 9
  Output: 2 -> 0 -> 0  (199 + 1 = 200)

Constraints:
  - 1 <= n <= 10^4

Hint: Reverse, add 1 with carry, reverse back. Or use recursion.
Pattern: Reverse and Add / Recursion
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


def add_one(head: ListNode) -> ListNode:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert to_list(add_one(build([1, 9, 9]))) == [2, 0, 0]
    assert to_list(add_one(build([9, 9, 9]))) == [1, 0, 0, 0]
    assert to_list(add_one(build([1, 2, 3]))) == [1, 2, 4]
    print("All tests passed!")
