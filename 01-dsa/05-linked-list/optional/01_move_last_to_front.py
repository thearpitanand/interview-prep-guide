"""
Problem: Move Last Element to Front (GFG) | Optional | Easy
Topic: Linked List

Move the last element of linked list to the front.

Example 1:
  Input: 1 -> 2 -> 3 -> 4 -> 5
  Output: 5 -> 1 -> 2 -> 3 -> 4

Constraints:
  - 1 <= n <= 10^5

Hint: Traverse to second last, detach last, make it head.
Pattern: Linked List Traversal
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


def move_last_to_front(head: ListNode) -> ListNode:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert to_list(move_last_to_front(build([1, 2, 3, 4, 5]))) == [5, 1, 2, 3, 4]
    assert to_list(move_last_to_front(build([1]))) == [1]
    print("All tests passed!")
