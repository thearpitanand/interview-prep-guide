"""
Problem: Check if Binary Tree is Heap (GFG) | Optional | Medium
Topic: Heap

Given a binary tree, check if it has max-heap properties:
1. Complete binary tree
2. Every node >= its children

Example 1:
  Input:     10
           /    \\
          9      8
         / \\
        7   6
  Output: True

Constraints:
  - 1 <= n <= 10^5

Hint: BFS — check completeness (no node after a non-full node) and max property.
Pattern: BFS
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_heap(root: TreeNode) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    root = TreeNode(10, TreeNode(9, TreeNode(7), TreeNode(6)), TreeNode(8))
    assert is_heap(root) == True
    root2 = TreeNode(5, TreeNode(10), TreeNode(3))
    assert is_heap(root2) == False  # 5 < 10 violates max-heap
    print("All tests passed!")
