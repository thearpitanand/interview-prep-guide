"""
Problem: Multiply 2 Numbers as Linked Lists (GFG) | Optional | Easy
Topic: Linked List

Given two linked lists representing two numbers, multiply them and return result as integer.

Example 1:
  Input: 3 -> 2, 2 -> 1
  Output: 672  # 32 * 21 = 672

Constraints:
  - 1 <= n, m <= 10

Hint: Convert each list to number, multiply.
Pattern: Linked List to Number
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


def multiply_ll(l1: ListNode, l2: ListNode) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert multiply_ll(build([3, 2]), build([2, 1])) == 672
    assert multiply_ll(build([1, 0, 0]), build([1, 0])) == 1000
    print("All tests passed!")
