"""
Problem: Sort K-Sorted DLL (GFG) | Optional | Medium
Topic: Linked List

Given a doubly linked list where each node is at most k positions away from
its target position, sort it efficiently.

Example 1:
  Input: 3 <-> 6 <-> 2 <-> 12 <-> 56 <-> 8, k = 2
  Output: 2 <-> 3 <-> 6 <-> 8 <-> 12 <-> 56

Constraints:
  - 1 <= n <= 10^5
  - 1 <= k <= n

Hint: Use min-heap of size k+1.
Pattern: Min-Heap
"""


class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def sort_k_sorted_dll(head: DLLNode, k: int) -> DLLNode:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    nodes = [DLLNode(v) for v in [3, 6, 2, 12, 56, 8]]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
        nodes[i+1].prev = nodes[i]
    result = sort_k_sorted_dll(nodes[0], 2)
    vals = []
    while result:
        vals.append(result.val)
        result = result.next
    assert vals == [2, 3, 6, 8, 12, 56]
    print("All tests passed!")
