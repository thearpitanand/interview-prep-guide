"""
Problem: Nth Node from End (GFG) | Optional | Easy
Topic: Linked List

Find the nth node from the end of linked list.

Example 1:
  Input: 1 -> 2 -> 3 -> 4 -> 5, n = 2
  Output: 4

Constraints:
  - 1 <= n <= length of list

Hint: Two pointers — advance first pointer n steps, then move both until first reaches end.
Pattern: Two Pointers
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


def nth_from_end(head: ListNode, n: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert nth_from_end(build([1, 2, 3, 4, 5]), 2) == 4
    assert nth_from_end(build([10, 20, 30]), 3) == 10
    print("All tests passed!")
