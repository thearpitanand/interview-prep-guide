"""
Problem: Segregate Even and Odd Nodes (GFG) | Optional | Easy
Topic: Linked List

Given a linked list, segregate even and odd nodes. Even nodes first, then odd.

Example 1:
  Input: 17 -> 15 -> 8 -> 12 -> 10 -> 5 -> 4
  Output: 8 -> 12 -> 10 -> 4 -> 17 -> 15 -> 5

Constraints:
  - 1 <= n <= 10^5

Hint: Maintain two separate lists (even and odd), merge them.
Pattern: Two Lists Merge
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


def segregate_even_odd(head: ListNode) -> ListNode:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = to_list(segregate_even_odd(build([17, 15, 8, 12, 10, 5, 4])))
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds
    print("All tests passed!")
