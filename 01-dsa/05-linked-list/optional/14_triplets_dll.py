"""
Problem: Count Triplets in Sorted DLL (GFG) | Optional | Medium
Topic: Linked List

Given a sorted doubly linked list and a value x, count triplets with sum = x.

Example 1:
  Input: 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9, x = 17
  Output: 2  # (2,6,9) and (4,5,8)

Constraints:
  - 1 <= n <= 10^3

Hint: Fix one node, use two-pointer (head/tail) for remaining pair.
Pattern: Two Pointers
"""


class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def count_triplets_dll(head: DLLNode, x: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    nodes = [DLLNode(v) for v in [1, 2, 4, 5, 6, 8, 9]]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
        nodes[i+1].prev = nodes[i]
    assert count_triplets_dll(nodes[0], 17) == 2
    print("All tests passed!")
