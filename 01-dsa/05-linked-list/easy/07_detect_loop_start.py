"""
Problem: Detect Start of Loop (LC 142) | Day 17 | Easy
Topic: Linked List

Given a linked list, return the node where the cycle begins. If there is no cycle, return None.

Example 1:
  Input: 3 -> 2 -> 0 -> -4 -> (back to 2)
  Output: node with value 2

Constraints:
  - 0 <= n <= 10^4
  - -10^5 <= Node.val <= 10^5

Hint: Floyd's cycle detection. After fast and slow meet, move one pointer to head. Advance both by 1 — they meet at cycle start.
Pattern: Floyd's Cycle Detection
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detect_cycle(head: ListNode) -> ListNode:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    # Test 1: cycle at node 2
    n1, n2, n3, n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n2
    assert detect_cycle(n1) == n2

    # Test 2: no cycle
    a = ListNode(1, ListNode(2))
    assert detect_cycle(a) is None

    print("All tests passed!")
