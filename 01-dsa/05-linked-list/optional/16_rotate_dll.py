"""
Problem: Rotate DLL by N Nodes (GFG) | Optional | Medium
Topic: Linked List

Rotate a doubly linked list counter-clockwise by N nodes.

Example 1:
  Input: 1 <-> 2 <-> 3 <-> 4 <-> 5, n = 2
  Output: 3 <-> 4 <-> 5 <-> 1 <-> 2

Constraints:
  - 1 <= n < length of list

Hint: Find the nth node, make it new head, update prev/next pointers.
Pattern: Pointer Manipulation
"""


class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def rotate_dll(head: DLLNode, n: int) -> DLLNode:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    nodes = [DLLNode(v) for v in [1, 2, 3, 4, 5]]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
        nodes[i+1].prev = nodes[i]
    result = rotate_dll(nodes[0], 2)
    vals = []
    curr = result
    for _ in range(5):
        vals.append(curr.val)
        curr = curr.next
    assert vals == [3, 4, 5, 1, 2]
    print("All tests passed!")
