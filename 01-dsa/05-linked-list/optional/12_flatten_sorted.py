"""
Problem: Flatten LL (Sorted Multi-level) (GFG) | Optional | Medium
Topic: Linked List

Given a linked list where each node has a next and down pointer, and each
down list is sorted. Flatten the list into a single sorted list using down pointers.

Example 1:
  Input: 5->10->19->28 (each with down lists)
  Output: single sorted list via down pointers

Constraints:
  - 1 <= n <= 100

Hint: Merge down lists one by one (merge sort style).
Pattern: Merge Sort
"""


class Node:
    def __init__(self, val=0, next=None, down=None):
        self.val = val
        self.next = next
        self.down = down


def flatten(head: Node) -> Node:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    # Simple test: single node
    n = Node(5)
    result = flatten(n)
    assert result.val == 5
    print("All tests passed!")
