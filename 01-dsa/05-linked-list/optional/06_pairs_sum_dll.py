"""
Problem: Find Pairs with Sum in DLL (GFG) | Optional | Easy
Topic: Linked List

Given a sorted doubly linked list and a value x, find pairs with sum equal to x.

Example 1:
  Input: 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9, x = 7
  Output: [(1,6), (2,5)]

Constraints:
  - 1 <= n <= 10^4

Hint: Two pointers from head and tail (last node), move inward.
Pattern: Two Pointers
"""


class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def pairs_sum_dll(head: DLLNode, x: int) -> list[tuple[int, int]]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    nodes = [DLLNode(v) for v in [1, 2, 4, 5, 6, 8, 9]]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
        nodes[i+1].prev = nodes[i]
    assert pairs_sum_dll(nodes[0], 7) == [(1, 6), (2, 5)]
    print("All tests passed!")
